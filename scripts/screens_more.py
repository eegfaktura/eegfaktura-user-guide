"""Screenshot steps of the chapters Tarife, Abrechnung, Energiedaten, Nachrichten, Prozesse and Dokumente.

Used by screenshots.py (shot/step/goto come from there). Unlike the other chapters, the billing steps WRITE to the
local stack: they create a preview for the current period and, once, a final billing run for FINAL_PERIOD (a final
run cannot be undone; on a fresh stack it is created again). Run scripts/prepare-local-stack.sql first.
"""
import re

from playwright.sync_api import Page

FINAL_PERIOD = "Jul-Sep 2026"  # the period that gets a final billing run in the local stack
FINAL_RANGE = "01.07.2026 – 30.09.2026"  # as the check dialog shows it: the final run is confirmed only for this
CHECK_TITLE = "Prüfung vor der Abrechnung"
METER_WITH_DATA = "0000143001"  # shown shortened in the list ("AT008000...0000143001")


def chapter_tariffs(page: Page, shot, step, goto) -> None:
    def tariff_list():
        goto(page, "/page/rates", "Bezug Standard")
        page.get_by_text("Bezug Standard", exact=True).first.click()
        page.get_by_role("button", name="Änderungen speichern").wait_for()
        shot("tarife-liste", page)

    def new_time_tariff():
        # the new-tariff form with a time-based consumer tariff; nothing is saved
        page.locator(".ratePane ion-toolbar ion-button").first.click()
        page.get_by_text("Verbraucher", exact=True).first.click()
        page.get_by_text("Zeitbasiert", exact=True).first.click()
        page.get_by_text("Zeitraum 1 aktiv", exact=False).first.wait_for()
        shot("tarife-neu-zeitbasiert", page)
        page.get_by_role("button", name="Zurück").click()

    def delete_blocked():
        goto(page, "/page/rates", "Bezug Standard")
        page.get_by_text("Bezug Standard", exact=True).first.click()
        page.get_by_text("Tarif löschen", exact=True).first.click()
        page.locator("ion-alert", has_text="Tarif löschen nicht möglich").wait_for()
        shot("tarife-loeschen-gesperrt", page)
        page.locator("ion-alert button", has_text="Abbrechen").click()

    for name, fn in (("tarife-liste", tariff_list), ("tarife-neu-zeitbasiert", new_time_tariff),
                     ("tarife-loeschen-gesperrt", delete_blocked)):
        step(name, fn)


def _billing_mode(page: Page, goto, period: str | None = None) -> None:
    goto(page, "/page/participants", "Periode")
    if period:
        select = page.locator("ion-select.select-box").first
        select.click()
        page.locator("ion-popover ion-item, ion-popover button", has_text=period).first.click()
        page.wait_for_function("([el, p]) => el.textContent.includes(p) || (el.value || '').includes(p)",
                               arg=[select.element_handle(), period], timeout=10000)
        page.wait_for_timeout(1500)  # the billing run of the new period is loaded after the selection
    page.locator("ion-checkbox").first.click()  # all members
    page.locator("label.eeg-sliding-box").first.click()


def chapter_billing(page: Page, shot, step, goto) -> None:
    def mode_alert():
        _billing_mode(page, goto)
        page.locator("ion-alert", has_text="Abrechnungsmodus").wait_for()
        shot("abrechnung-modus", page)
        page.locator("ion-alert button", has_text="OK").click()

    def check_and_preview():
        # first preview of the period, or a refresh of an existing one ("Vorschau Akt.")
        page.get_by_role("button", name=re.compile(r"^(VORSCHAU ERSTELLEN|VORSCHAU AKT)", re.I)).first.click()
        page.get_by_text(CHECK_TITLE, exact=False).first.wait_for()
        page.get_by_text("Prüfung läuft", exact=False).first.wait_for(state="hidden", timeout=60000)
        shot("abrechnung-pruefung", page)
        page.locator("ion-modal ion-button").filter(has_text="Vorschau erstellen").last.click()
        page.get_by_role("button", name="ABRECHNUNG DURCHFÜHREN", exact=False).wait_for(timeout=120000)
        page.get_by_text("Saldo Zahlungen", exact=False).first.wait_for()
        shot("abrechnung-vorschau", page)
        # the confirmation of a final run, cancelled: nothing is billed for the current period
        page.get_by_role("button", name="ABRECHNUNG DURCHFÜHREN", exact=False).click()
        page.get_by_text(CHECK_TITLE, exact=False).first.wait_for()
        page.get_by_text("Prüfung läuft", exact=False).first.wait_for(state="hidden", timeout=60000)
        shot("abrechnung-durchfuehren", page)
        page.locator("ion-modal ion-button").filter(has_text="Abbrechen").last.click()

    def final_run():
        # once per local stack: a final run for FINAL_PERIOD (skipped when it exists already)
        _billing_mode(page, goto, FINAL_PERIOD)
        page.wait_for_timeout(800)
        ok = page.locator("ion-alert button", has_text="OK")  # the hint comes only once per session
        if ok.count() and ok.first.is_visible():
            ok.first.click()
        sepa_button = page.get_by_role("button", name="SEPA")
        new_preview = page.get_by_role("button", name="VORSCHAU ERSTELLEN")
        run_button = page.get_by_role("button", name="ABRECHNUNG DURCHFÜHREN", exact=False)
        sepa_button.or_(new_preview).or_(run_button).first.wait_for(timeout=60000)  # footer loaded
        if not sepa_button.is_visible():
            if new_preview.is_visible():
                new_preview.click()
                page.get_by_text("Prüfung läuft", exact=False).first.wait_for(state="hidden", timeout=60000)
                page.locator("ion-modal ion-button").filter(has_text="Vorschau erstellen").last.click()
            run_button.click(timeout=120000)
            page.get_by_text(CHECK_TITLE, exact=False).first.wait_for()
            page.get_by_text("Prüfung läuft", exact=False).first.wait_for(state="hidden", timeout=60000)
            # irreversible: confirm only when the dialog is about FINAL_PERIOD (warnings are accepted on purpose)
            if page.get_by_text(f"{CHECK_TITLE} ({FINAL_RANGE})", exact=False).count() == 0:
                page.locator("ion-modal ion-button").filter(has_text="Abbrechen").last.click()
                raise RuntimeError(f"the check dialog is not about {FINAL_RANGE} — final run not started")
            page.locator("ion-modal ion-button").filter(has_text=re.compile(r"Abrechnung durchführen$")).last.click()
        page.get_by_role("button", name="SEPA").wait_for(timeout=120000)
        shot("abrechnung-abgerechnet", page)

    def sepa():
        page.get_by_role("button", name="SEPA").click()
        page.get_by_text("SEPA Dateien", exact=False).first.wait_for()
        page.get_by_role("button", name="Generieren").click()
        page.get_by_role("button", name="Herunterladen").first.wait_for(timeout=60000)
        shot("abrechnung-sepa", page)
        page.get_by_role("button", name="Schließen").click()

    def invoices_of_member():
        goto(page, "/page/participants", "Periode")
        page.locator("div.participant").first.click()
        page.locator("ion-item.eeg-item-box", has_text="Meine Rechnungen").click()
        page.get_by_text("Rechnungen", exact=True).first.wait_for()
        page.get_by_text(".pdf", exact=False).first.wait_for()  # the list of documents has loaded
        shot("abrechnung-meine-rechnungen", page)

    def settings():
        goto(page, "/page/eeg", "Allgemeines")
        card = page.locator(".eeg-property-card", has=page.locator(".header", has_text="Abrechnungseinstellungen"))
        card.evaluate("e => e.scrollIntoView({block: 'start'})")
        shot("abrechnung-einstellungen", page, card)

    for name, fn in (("abrechnung-modus", mode_alert), ("abrechnung-pruefung", check_and_preview),
                     ("abrechnung-abgerechnet", final_run), ("abrechnung-sepa", sepa),
                     ("abrechnung-meine-rechnungen", invoices_of_member), ("abrechnung-einstellungen", settings)):
        step(name, fn)


def chapter_energy(page: Page, shot, step, goto) -> None:
    def meter_chart():
        goto(page, "/page/participants", "Periode")
        # an active consumer with data (the fixture's first metering point has a warning and no chart)
        page.locator("div.participant ion-card", has_text=METER_WITH_DATA).first.click()
        page.get_by_text("Energiedaten", exact=True).first.wait_for()
        page.get_by_text("YM", exact=True).first.click()
        page.locator(".recharts-bar-rectangle").first.wait_for()  # bars of the month view drawn
        shot("energiedaten-diagramm", page)

    def day_view():
        page.get_by_text("D", exact=True).first.click()
        page.get_by_label("Vorheriger Tag").first.wait_for()  # the day view is active (fails if "D" hit something else)
        page.locator(".recharts-line").first.wait_for()
        shot("energiedaten-tag", page)

    def export_popover():
        page.locator("ion-button.header-fav-button").nth(2).click()
        page.get_by_text("Download Daten für", exact=False).first.wait_for()
        shot("energiedaten-export", page)
        page.keyboard.press("Escape")

    for name, fn in (("energiedaten-diagramm", meter_chart), ("energiedaten-tag", day_view),
                     ("energiedaten-export", export_popover)):
        step(name, fn)


def chapter_messages_documents(page: Page, shot, step, goto) -> None:
    def messages():
        goto(page, "/page/notifications", "Nachrichten")
        shot("nachrichten", page, fit=False)  # a long list: the first messages are enough

    def documents():
        goto(page, "/page/participants", "Periode")
        page.locator("div.participant").first.click()
        page.locator("ion-item.eeg-item-box", has_text="Dokumente").click()
        page.get_by_role("button", name="Hochladen").first.click()
        page.get_by_text("Bitte lade die Anmeldedokumente", exact=False).first.wait_for()
        shot("dokumente-hochladen", page)
        page.get_by_role("button", name="Abbrechen").last.click()

    step("nachrichten", messages)
    step("dokumente-hochladen", documents)


def chapter_processes(page: Page, shot, step, goto) -> None:
    """Runs as the user of the online community (only there the menu has "Prozesse"); nothing is sent."""
    def card(title: str, name: str, ready: str):
        def run():
            goto(page, "/page/processes", "Zählpunktdaten nachfordern")
            page.locator("ion-card", has=page.locator("h2", has_text=title)).click()
            page.get_by_text(ready, exact=False).first.wait_for()
            shot(name, page)
        step(name, run)

    card("Zählpunkt abmelden", "prozesse-abmelden", "Begründung")
    card("Teilnahmefaktor ändern", "prozesse-teilnahmefaktor", "Teilnahmefaktor in %")
    card("Prozess History", "prozesse-history", "Anmeldung Teilnahme Online")
