# Stammdaten aus Excel importieren

Viele Mitglieder auf einmal — z. B. beim Umstieg auf eegFaktura — liest du aus einer Excel-Datei ein:

1. Klicke oben in der [Mitgliederliste](02-mitglieder-zaehlpunkte.md#die-mitgliederliste) auf den Knopf mit der Wolke
   und wähle **Stammdaten**.
2. **Sheet-Name** ist mit „EEG Stammdaten“ voreingestellt; heißt das Blatt in deiner Datei anders, trägst du hier
   seinen Namen ein.
3. Wähle die Datei mit dem Stern oder ziehe sie in das Fenster. Es geht eine Datei je Import.
4. Klicke auf **Import**.

Eine Vorlage mit allen Spalten gibt es hier; Zeile 5 erklärt die wichtigsten Spalten:
[Vorlage Stammdatenimport (Excel)](https://github.com/eegfaktura/eegfaktura-backend/raw/master/tests/261124-vorlage-import-stammdaten.xlsx).
Ältere Vorlagen funktionieren weiter: eegFaktura erkennt die Spalten an ihrer Überschrift, nicht an der Position.

Probiere den Import zuerst mit wenigen Mitgliedern aus (siehe
[Import zuerst mit wenigen Mitgliedern testen](#import-zuerst-mit-wenigen-mitgliedern-testen)).

## Wichtige Spalten

| Spalte | Hinweis |
|--------|---------|
| Gemeinschafts-ID | Pflicht, muss zur Gemeinschaft passen |
| Name 1 / Name 2 | Vorname / Nachname (bei Firmen: Firmenname / Nachname der Kontaktperson). Groß-/Kleinschreibung zählt beim Wiedererkennen. Ist „Name 1“ leer, muss „Name 2“ „Nachname Vorname“ enthalten |
| BusinessRole | `business` für eine Firma, sonst privat |
| Mitglied seit | Excel-Datum oder `TT.MM.JJJJ`; leer = Spalte „Dokument unterschrieben“ (ältere Vorlagen), sonst heute |
| Zählpunkt | genau 33 Zeichen |
| Energierichtung | `CONSUMPTION` (Verbraucher, auch leer) oder `GENERATION` (Erzeuger) |
| Zählpunktstatus | Pflicht. `ACTIVE`, `ACTIVATED` oder `REGISTERED` → wird als **aktiv** übernommen; `NEW` → wird neu angemeldet; andere Werte → Zeile wird nicht importiert |
| registriert seit | ab wann der Zählpunkt aktiv ist (Excel-Datum oder `TT.MM.JJJJ`); **leer = 1. Jänner des laufenden Jahres**. Ältere Energiedaten werden davor weder angefordert noch abgerechnet — beim Umstieg das tatsächliche Datum eintragen |
| Zugeteilte Menge in Prozent | Teilnahmefaktor (1–100); leer oder 0 wird 100 % |
| email | mehrere Adressen mit `;` trennen; ist eine Adresse ungültig, wird das Mitglied ohne E-Mail angelegt (mit Hinweis) |
| Einzugsart | `CORE`, `B2B` oder `Kein SEPA`. Leer: kein Einzug; hat das Mitglied eine IBAN, kommt ein Hinweis |
| MandatRef | Mandatsreferenz für die Lastschrift. Leer: Die Abrechnung nimmt die Mitgliedsnummer. Die Bank nimmt sie nur ohne Leerzeichen und Umlaute an (höchstens 35 Zeichen) – sonst die Mandatsreferenz ausfüllen |
| MandatDat | Datum, an dem das Mitglied das Mandat unterschrieben hat (Excel-Datum oder `TT.MM.JJJJ`); bei `CORE` und `B2B` immer ausfüllen |
| ObjektName | wird als Anlagenname übernommen |
| Mitgliedstarif | Name eines aktiven Mitgliedstarifs eurer Gemeinschaft, so geschrieben wie im Stammdaten-Export (Groß-/Kleinschreibung egal). Leer: kein Tarif. Steht das Mitglied in mehreren Zeilen, zählt die erste ausgefüllte |
| Zp. Tarifname | Name eines aktiven Zählpunkttarifs, passend zur Energierichtung (Verbrauch bzw. Erzeugung). Leer: kein Tarif |

## So verhält sich der Import

!!! warning "Schon aktive Zählpunkte als aktiv importieren"
    Zählpunkte, die beim Netzbetreiber **schon aktiv** sind, importierst du mit dem Status aktiv und dem tatsächlichen
    Datum in „registriert seit“ — mit `NEW` würden sie erneut angemeldet.

- Ein Mitglied mit gleichem Vor- und Nachnamen wie ein vorhandenes gilt als **dasselbe**: Es bekommt die Zählpunkte
  aus der Datei (samt Zählpunkttarif), seine übrigen Daten werden **nicht** geändert — auch nicht durch einen
  erneuten Import; einen Fehler korrigierst du direkt beim Mitglied. Hat es einen dieser Zählpunkte schon, wird für
  dieses Mitglied nichts importiert (Fehler unter Nachrichten) — nimm dann nur die neuen Zählpunkte in die Datei.
- Zählpunkte mit `NEW` bei einem schon zugelassenen Mitglied legt der Import nur an. Melde sie danach unter
  **Prozesse → Zählpunkt aktivieren** an.
- Ein Fehler betrifft nur das jeweilige Mitglied; die übrigen Zeilen werden trotzdem importiert. Hinweise und Fehler
  (z. B. doppelte Mitgliedsnummer, Zählpunkt mit falscher Länge) kommen als Nachricht
  **„Excel Stammdaten importiert — Hinweise: …“** unter [Nachrichten](07-nachrichten.md); ohne Hinweise kommt keine
  Nachricht.
- Bekommt ein neues Mitglied einen Tarif mit [Beitrittsgebühr](04-tarife.md#beitrittsgebuhr), weist die Nachricht
  darauf hin: Die Gebühr wird mit der ersten Energieabrechnung verrechnet, auch wenn das Mitglied sie schon früher
  bezahlt hat (z. B. vor dem Umstieg). Dann beim Mitglied **Außerhalb bezahlt erfassen**, siehe
  [Beitrittsgebühr eines Mitglieds](02-mitglieder-zaehlpunkte.md#beitrittsgebuhr-eines-mitglieds).

??? note "Hinweise des Imports (englisch) und was sie bedeuten"
    Die Hinweise stehen derzeit großteils auf Englisch. Die häufigsten:

    - „Rows skipped: 'Gemeinschafts-ID' …“: Die Gemeinschafts-ID fehlt oder passt nicht zu deiner Gemeinschaft.
    - „Len not equal 33“: Die Zählpunktnummer hat nicht 33 Zeichen.
    - „Participant has wrong status“: Der Zählpunktstatus ist leer oder kein erlaubter Wert.
    - „unknown 'Energierichtung'“: Erlaubt sind `CONSUMPTION` und `GENERATION`.
    - „no active tariff named …“: Einen aktiven Tarif mit diesem Namen (und der passenden Art) gibt es nicht; das
      Mitglied bzw. der Zählpunkt wird ohne Tarif angelegt.
    - „MitgliedsNr … is already assigned …“ oder „… is used by several members“: Die Mitgliedsnummer ist schon
      vergeben oder steht in der Datei bei mehreren Mitgliedern.
    - „… have no direct debit type“: Mitglieder mit IBAN, aber ohne Einzugsart; sie werden nicht eingezogen.

## Import zuerst mit wenigen Mitgliedern testen

Bevor du alle Mitglieder einliest, probiere den Import mit **zwei oder drei Mitgliedern** aus. So siehst du, ob die
Spalten passen, ohne dass sich Fehler in Hunderten Mitgliedern wiederfinden.

> **Wichtig:** Ein Mitglied, dessen Zählpunkte in der Spalte **Zählpunktstatus** als aktiv eingetragen sind
> (`ACTIVE`, `ACTIVATED` oder `REGISTERED`), kannst du nach dem Import **nicht mehr löschen**. Deshalb läuft der Test
> mit dem Status `NEW`: Solche Mitglieder lassen sich wieder löschen.

1. **Testdatei anlegen.** Kopiere deine Importdatei und lass darin nur zwei oder drei Mitglieder stehen, am besten
   verschiedene Fälle: einen Verbraucher, einen Erzeuger, ein Mitglied mit mehreren Zählpunkten, ein Mitglied mit
   Einzugsart **Kein SEPA**. Nimm nur Mitglieder, die **noch nicht** in eegFaktura stehen — sonst gilt ein Mitglied
   mit gleichem Namen als dasselbe, und seine neuen Zählpunkte ließen sich nicht mehr löschen. Setze die Spalte
   **Zählpunktstatus** in **allen** Zeilen auf `NEW`.
2. **Importieren.** Lies die Testdatei ein. Der Import selbst schickt **nichts** an den Netzbetreiber.
3. **Prüfen.** Sieh unter [Nachrichten](07-nachrichten.md) nach der Nachricht
   **„Excel Stammdaten importiert — Hinweise: …“**: Jeder Hinweis nennt ein Mitglied oder einen Zählpunkt, den du
   auch in der großen Datei korrigieren solltest. Öffne dann in der Mitgliederliste jedes Testmitglied und prüfe
   Name, Adresse, E-Mail, Bankverbindung und Einzugsart sowie die Zählpunkte mit Energierichtung, Teilnahmefaktor und
   Anlagenname.
4. **Testmitglieder wieder löschen.** Bei den Testmitgliedern sind die Zählpunkte orange. Öffne jedes; rechts steht
   die Frage „Möchtest du *Nachname* in deine EEG aufnehmen?“ (siehe
   [Neues Mitglied zulassen](02-mitglieder-zaehlpunkte.md#neues-mitglied-zulassen)). Klicke auf **Nein, Löschen** und
   bestätige die Rückfrage mit **Löschen**. Lösche **alle** Testmitglieder.

    !!! danger "Nicht auf „Ja, Zulassen“ klicken"
        Bei Gemeinschaften mit Online-Anbindung meldet eegFaktura die Zählpunkte damit beim Netzbetreiber an. Ohne
        Online-Anbindung werden sie aktiv. In beiden Fällen lässt sich das Mitglied danach nicht mehr löschen.

5. **Korrigieren und wiederholen.** Passe die große Datei an. Wiederhole die Schritte 2 bis 4, bis keine Hinweise
   mehr kommen, und lösche die Testmitglieder jedes Mal wieder.
6. **Alle Mitglieder importieren.** Trage in der großen Datei bei Zählpunkten, die beim Netzbetreiber schon aktiv
   sind, den Status aktiv und unter „registriert seit“ das tatsächliche Datum ein. Importiere dann die vollständige
   Datei.

Gut zu wissen:

- **Aktiven Status mitprüfen:** Den Status aktiv und das Datum „registriert seit“ prüft der Test mit `NEW` nicht.
  Willst du auch das sehen, importiere vor Schritt 6 zuerst **einige echte Mitglieder** mit ihrem richtigen Status
  und prüfe sie. Diese Mitglieder bleiben in eegFaktura. **Nimm sie danach aus der großen Datei heraus**, sonst
  meldet der große Import für jedes von ihnen einen Fehler.
- **Ein Testmitglied wurde nicht gelöscht:** Steht es auch in der großen Datei, meldet der Import für dieses Mitglied
  einen Fehler (unter Nachrichten) und lässt es mit dem Teststatus stehen. Lösche es mit **Nein, Löschen** und
  importiere eine Datei nur mit diesem Mitglied noch einmal.
- Ist beim großen Import etwas schiefgegangen, wende dich an den [Support](einrichtung-hilfe.md#hilfe-und-support).
