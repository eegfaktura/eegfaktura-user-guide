"""Screenshot generator for the user guide.

Takes the screenshots in docs/images/ from a LOCAL eegFaktura stack with fixture data (never production or pilot:
the guide is public, so no real names, addresses or IBANs). The local stack is the eegfaktura-dev workspace
(web on http://localhost:8090, Keycloak on http://localhost:8180, fixture users from its realm supplement).

Usage:
    SCREENSHOT_PASSWORD=<fixture password> python scripts/screenshots.py            # all screenshots
    SCREENSHOT_PASSWORD=<fixture password> python scripts/screenshots.py email-texte  # only names containing this

Env (optional): BASE_URL (default http://localhost:8090), SCREENSHOT_USER (default rc100100-admin, an EEG_ADMIN of
one community), SCREENSHOT_MULTI_USER (default multi-admin, an EEG_ADMIN of two communities, for the switcher).

Nothing is saved in the app — except by the billing chapter (screens_more.py), which creates a billing preview and,
once, a final billing run in the local stack; run scripts/prepare-local-stack.sql before. Edits made for a dialog are
discarded. A screenshot that fails is reported and the script exits with 1 (the others are still taken).
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

import screens_more

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8090").rstrip("/")
USER = os.environ.get("SCREENSHOT_USER", "rc100100-admin")
MULTI_USER = os.environ.get("SCREENSHOT_MULTI_USER", "multi-admin")
PASSWORD = os.environ.get("SCREENSHOT_PASSWORD")
OUT = Path(__file__).resolve().parent.parent / "docs" / "images"
VIEWPORT = {"width": 1440, "height": 900}
MAX_HEIGHT = 2400  # a page taller than its content area is shot in full, up to this height
DEBUG_DIR = Path(__file__).resolve().parent.parent / ".cache"  # failed steps leave an image here (gitignored)

# height of the visible page content: Ionic scrolls inside ion-content, so a plain full-page shot would cut it off
CONTENT_HEIGHT_JS = """async () => {
  let bottom = 0
  for (const c of document.querySelectorAll('ion-content')) {
    const r = c.getBoundingClientRect()
    if (r.width === 0 || r.height === 0) continue
    const el = await c.getScrollElement()
    bottom = Math.max(bottom, r.top + el.scrollHeight)
  }
  return Math.ceil(bottom)
}"""
OVERLAYS = "ion-alert, ion-modal, ion-popover, ion-picker"
ONLY = sys.argv[1] if len(sys.argv) > 1 else ""
# the community with online connection of SCREENSHOT_MULTI_USER (only there the menu has "Prozesse")
ONLINE_COMMUNITY = os.environ.get("SCREENSHOT_ONLINE_COMMUNITY", "GC106668")

failed: list[str] = []
written: list[str] = []
CURRENT_PAGE: list[Page] = []  # the page of the running user, for the debug image of a failed step


def shot(name: str, page: Page, locator=None, fit: bool = True) -> None:
    """Saves docs/images/<name>.png: the whole page (fit: window grown to the content), or only the given element."""
    if ONLY and ONLY not in name:
        return
    path = OUT / f"{name}.png"
    page.wait_for_timeout(400)  # Ionic transitions
    wait_toasts_gone(page)
    overlay = any(o.is_visible() for o in page.locator(OVERLAYS).all())
    if locator or overlay or not fit:  # an element, a dialog, or a long list in the normal window
        (locator or page).screenshot(path=str(path))
    else:  # the whole page: let the window grow to the content, then back
        height = min(max(page.evaluate(CONTENT_HEIGHT_JS), VIEWPORT["height"]), MAX_HEIGHT)
        page.set_viewport_size({"width": VIEWPORT["width"], "height": height})
        try:
            page.wait_for_timeout(600)
            page.screenshot(path=str(path))
        finally:
            page.set_viewport_size(VIEWPORT)
    written.append(name)
    print(f"ok    {name}")


def wait_toasts_gone(page: Page) -> None:
    """Notices disappear on their own; one that stays (an error with a button) fails the screenshot."""
    for _ in range(40):
        if not any(t.is_visible() for t in page.locator("ion-toast").all()):
            return
        page.wait_for_timeout(250)
    raise RuntimeError("a notice (ion-toast) is still shown: " + page.locator("ion-toast").first.inner_text()[:120])


def scroll_to(locator) -> None:
    locator.evaluate("e => e.scrollIntoView({block: 'start'})")


def step(name: str, fn) -> None:
    """Runs one screenshot step; a failure is recorded, the run goes on. Every step runs, also with a name filter,
    because later steps build on the page state of earlier ones; the filter only decides which images are saved."""
    try:
        fn()
    except Exception as e:  # noqa: BLE001 — report every failing step, then exit 1
        failed.append(name)
        lines = str(e).splitlines() or [type(e).__name__]
        print(f"FAIL  {name}: {lines[0]}" + (f"  | {lines[2].strip()}" if len(lines) > 2 else ""))
        if CURRENT_PAGE:
            try:
                DEBUG_DIR.mkdir(exist_ok=True)
                CURRENT_PAGE[0].screenshot(path=str(DEBUG_DIR / f"failed-{name}.png"))
            except Exception:  # noqa: BLE001 — the debug image is optional, the run goes on
                pass


def login(page: Page, user: str, capture: bool = False) -> None:
    page.goto(BASE_URL + "/")
    page.locator("#username, input[name=username]").first.wait_for(timeout=30000)
    if capture:
        shot("anmeldung-keycloak", page)
    page.locator("#username, input[name=username]").first.fill(user)
    page.locator("#password, input[name=password]").first.fill(PASSWORD)
    page.locator("#kc-login, [type=submit]").first.click()
    page.wait_for_url("**/page/participants", timeout=30000)
    page.locator("ion-menu ion-header ion-chip").wait_for(timeout=30000)
    page.wait_for_load_state("networkidle")


def goto(page: Page, route: str, ready_text: str) -> None:
    page.goto(BASE_URL + route)
    page.get_by_text(ready_text, exact=True).first.wait_for(timeout=30000)
    page.wait_for_load_state("networkidle")


def close_overlays(page: Page) -> None:
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)


def chapter_overview(page: Page) -> None:
    def shell():
        shot("oberflaeche-start", page)

    def user_menu():
        page.locator("ion-menu ion-header ion-chip").click()
        page.locator("ion-popover ion-item", has_text="Abmelden").wait_for()
        shot("oberflaeche-benutzermenue", page)
        close_overlays(page)

    step("oberflaeche-start", shell)
    step("oberflaeche-benutzermenue", user_menu)
    step("dashboard", lambda: (goto(page, "/page/dashboard", "Übersicht EEG"), page.wait_for_timeout(1500),
                               shot("dashboard", page)))
    step("eeg-seite", lambda: (goto(page, "/page/eeg", "Allgemeines"), shot("eeg-seite", page)))


def chapter_switch_community(page: Page) -> None:
    def switcher():
        page.locator("ion-menu ion-header ion-chip").click()
        page.locator('ion-popover ion-select[label="Auswahl Gemeinschaft"]').click()
        page.locator("ion-alert").wait_for()
        shot("oberflaeche-gemeinschaft-wechseln", page)
        # switch to the online community explicitly: the "Prozesse" screenshot needs its menu entry
        page.locator("ion-alert button[role=radio]", has_text=ONLINE_COMMUNITY).click()
        page.locator("ion-alert button", has_text="OK").click()
        page.locator("ion-menu ion-item", has_text="Prozesse").wait_for()
        close_overlays(page)

    step("oberflaeche-gemeinschaft-wechseln", switcher)
    # "Prozesse" is only in the menu of an online community (GC106668 of the second user)
    step("prozesse", lambda: (goto(page, "/page/processes", "Zählpunktdaten nachfordern"), shot("prozesse", page)))


def chapter_members(page: Page) -> None:
    def member_meter():
        goto(page, "/page/participants", "Periode")
        page.locator("div.participant").first.click()  # opens the member with its first metering point
        page.locator("ion-item.eeg-item-box", has_text="Details und Adresse").wait_for()
        shot("mitglied-zaehlpunkt", page)

    def member_details():
        page.locator("ion-item.eeg-item-box", has_text="Details").first.click()
        page.wait_for_load_state("networkidle")
        shot("mitglied-details", page)

    def sort_dialog():
        page.locator(".period-filter-menu .sort").first.click()
        page.locator("ion-alert").wait_for()
        shot("mitglieder-sortierung", page)
        close_overlays(page)

    def filter_dialog():
        tab = page.locator(".period-filter-menu > div.item").nth(1)
        tab.locator("ion-icon").first.click()
        page.locator("ion-alert", has_text="Filteroptionen").wait_for()
        shot("mitglieder-filter", page)
        close_overlays(page)

    def add_member():
        goto(page, "/page/addParticipant", "Allgemeines")
        shot("mitglied-anlegen", page)
        page.get_by_text("Zählpunkt hinzufügen", exact=True).first.click()
        page.get_by_text("Teilnahmefaktor in %").first.wait_for()
        shot("mitglied-anlegen-zaehlpunkt", page)

    for name, fn in (("mitglied-zaehlpunkt", member_meter), ("mitglied-details", member_details),
                     ("mitglieder-sortierung", sort_dialog), ("mitglieder-filter", filter_dialog),
                     ("mitglied-anlegen", add_member)):
        step(name, fn)


def chapter_mail_texts(page: Page) -> None:
    card = page.locator(".eeg-property-card", has=page.locator(".header", has_text="E-Mail-Texte"))
    toggle = page.locator("ion-toggle", has_text="Eigenen Text verwenden")
    # the mail must be on the standard text: with a saved own text, switching off would offer to delete it
    standard_box = page.locator(".mail-template-status-box.standard")

    def card_shot():
        goto(page, "/page/eeg", "Allgemeines")
        card.scroll_into_view_if_needed()
        shot("email-texte-karte", page, card)

    def mail_list():
        goto(page, "/page/mailtemplates", "Zählpunkt aktiv")
        page.locator("ion-badge").first.wait_for()
        shot("email-texte-liste", page)

    def editor_standard():
        page.locator("ion-item", has=page.locator("h2", has_text="Zählpunkt aktiv")).click()
        toggle.wait_for()
        page.wait_for_load_state("networkidle")
        if not standard_box.is_visible():
            raise RuntimeError("'Zählpunkt aktiv' has a saved own text in this stack — reset it first")
        shot("email-texte-standard", page)

    def preview():
        page.locator(".mail-template-actions ion-button", has_text="Vorschau").click()
        preview_card = page.locator("ion-card", has_text="Vorschau mit Beispieldaten").last
        preview_card.wait_for()
        page.wait_for_timeout(1000)
        scroll_to(preview_card)
        shot("email-texte-vorschau", page, preview_card)
        page.get_by_text("Vorschau schließen").click()

    def own_text():
        if not standard_box.is_visible():
            raise RuntimeError("not on the standard text")
        toggle.click()
        page.get_by_text("Noch nicht gespeichert", exact=False).first.wait_for()
        scroll_to(page.locator(".mail-template-editor"))
        shot("email-texte-eigener-text", page)

    def switch_off():
        # an unsaved edit makes switching off ask first; the edit is discarded with "Ja" (nothing is saved)
        page.locator(".mail-editor .ProseMirror").click()
        page.keyboard.press("End")
        page.keyboard.type(" Beispiel")
        toggle.click()
        page.locator("ion-alert").wait_for()
        scroll_to(page.locator(".mail-template-editor"))
        shot("email-texte-ausschalten", page)
        page.locator("ion-alert button", has_text="Ja").click()

    for name, fn in (("email-texte-karte", card_shot), ("email-texte-liste", mail_list),
                     ("email-texte-standard", editor_standard), ("email-texte-vorschau", preview),
                     ("email-texte-eigener-text", own_text), ("email-texte-ausschalten", switch_off)):
        step(name, fn)


def main() -> int:
    if not PASSWORD:
        print("SCREENSHOT_PASSWORD is not set (fixture password of the local stack)")
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    if not ONLY:  # a full run starts empty, so an image of a failed step cannot survive from an older run
        for old in OUT.glob("*.png"):
            old.unlink()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        more = [lambda pg, f=f: f(pg, shot, step, goto) for f in (
            screens_more.chapter_tariffs, screens_more.chapter_billing, screens_more.chapter_energy,
            screens_more.chapter_messages_documents)]
        processes = lambda pg: screens_more.chapter_processes(pg, shot, step, goto)  # noqa: E731
        for user, chapters, capture in ((USER, (chapter_overview, chapter_members, chapter_mail_texts, *more), True),
                                        (MULTI_USER, (chapter_switch_community, processes), False)):
            ctx = browser.new_context(viewport=VIEWPORT, locale="de-AT", timezone_id="Europe/Vienna")
            page = ctx.new_page()
            CURRENT_PAGE[:] = [page]
            try:
                login(page, user, capture)
            except Exception as e:  # noqa: BLE001
                failed.append(f"login {user}")
                print(f"FAIL  login {user}: {str(e).splitlines()[0]}")
                ctx.close()
                continue
            for chapter in chapters:
                chapter(page)
            ctx.close()
        browser.close()
    if ONLY and not written:
        failed.append(f"no screenshot name contains {ONLY!r}")
    if failed:
        print(f"{len(failed)} screenshot(s) failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
