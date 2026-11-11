# Was ist neu?

Neue Funktionen von eegFaktura, die du als EEG-Admin bemerkst. Die Kapitel beschreiben jeweils den aktuellen
Stand.

## In der Pilot-Zone

--8<-- "pilot.md"

### Zählpunkt abmelden: Begründung geht an den Netzbetreiber

Die optionale **Begründung** beim Abmelden eines Zählpunkts wird jetzt an den Netzbetreiber übermittelt und in der
Prozess History gespeichert, höchstens 50 Zeichen. Siehe [Begründung](08-prozesse.md#begrundung).

## Herbst 2026 (seit 11.11.2026)

### Peer-to-Peer und Eigenversorgung: Abrechnung als Vorschau

Bei **P2P** und **EVA** gibt es jetzt alle Funktionen wie bei einer EEG, die Abrechnung aber nur als Vorschau, etwa für
Vorlage-Rechnungen. Eine endgültige Abrechnung und der Mailversand bleiben gesperrt.
Siehe [Peer-to-Peer und Eigenversorgung](01-anmeldung.md#peer-to-peer-und-eigenversorgung).

### EEG-Seite: Abrechnungsintervall unter „Allgemeines“

Die Karte **Einstellungen** auf der EEG-Seite entfällt. Die Gemeinschaft wechselst du nur noch im
[Benutzermenü](01-anmeldung.md#gemeinschaft-wechseln). Das Intervall heißt **Abrechnungsintervall** und steht als erstes
Feld unter **Allgemeines**. Siehe [Abrechnung](05-abrechnung.md#abrechnungszeitraum-wechseln).

### Mitgliederliste: Mitgliedsnummer nach dem Namen

Jedes Mitglied steht mit seiner Mitgliedsnummer in Klammern in der Liste, z. B. „Max Mustermann (001)“.
Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#die-mitgliederliste).

### Suche mit mehreren Begriffen

Die Suche in der Mitgliederliste versteht mehrere Begriffe in beliebiger Reihenfolge, z. B. „huber maria“; gefunden
wird, wer alle Begriffe enthält. Begriffe, die nur bei Zählpunkten vorkommen, grenzen die Zählpunkte ein
(„markt pumpwerk“). Siehe [Suche](02-mitglieder-zaehlpunkte.md#suche).

### Mitglied registrieren: Zählpunkt korrigieren oder entfernen

Ein eingetragener Zählpunkt lässt sich vor dem Registrieren ändern (**Übernehmen**) oder wieder **Entfernen**; jede
Nummer steht nur einmal in der Liste. Der Name der Bank heißt **Bank (optional)** und muss nicht ausgefüllt werden.
Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#zahlpunkt-vor-dem-registrieren-andern-oder-entfernen).

### Beitrittsgebühr nachverrechnen nur für schon abgerechnete Mitglieder

Den Knopf **Beitrittsgebühr nachverrechnen** gibt es nur noch für Mitglieder, die schon mit Energie abgerechnet wurden.
Bei allen anderen kommt die Gebühr ohnehin mit der ersten endgültigen Energieabrechnung.
Siehe [Beitrittsgebühr eines Mitglieds](02-mitglieder-zaehlpunkte.md#beitrittsgebuhr-eines-mitglieds).

### Stammdaten-Export nach Mitgliedsnummer sortiert

Das Blatt „Mitglieder“ im Stammdaten-Export ist nach der Mitgliedsnummer sortiert.
Siehe [Energiedaten exportieren](06-energiedaten.md#energiedaten-exportieren).

### Klarere Meldungen beim Anlegen

Ist ein Zählpunkt schon einem anderen Mitglied zugeordnet, hat das Mitglied ihn schon, oder ist eine E-Mail-Adresse
ungültig, sagt eegFaktura das in einem Satz statt mit einem Fehlercode wie „E_1104_…“. Die Felder TechCode und
FuelCode beim Zählpunkt werden nicht mehr angezeigt. Siehe [Gut zu wissen](02-mitglieder-zaehlpunkte.md#gut-zu-wissen).

### Rechnungen mit Tausenderpunkt

Auf neu erstellten Belegen stehen alle Zahlen mit Tausenderpunkt, z. B. „21.345,00 kWh“.
Siehe [Was auf einem Beleg steht](05-abrechnung.md#was-auf-einem-beleg-steht).

### Gemeinschaft wechseln immer im Benutzermenü

Den Eintrag **Gemeinschaft wechseln** gibt es im Benutzermenü immer, auch wenn du nur eine Gemeinschaft betreust.
Siehe [Gemeinschaft wechseln](01-anmeldung.md#gemeinschaft-wechseln).

## Herbst 2026 (seit 08.11.2026)

### Abrechnungszeitraum wechseln

EEG-Admins wechseln das Abrechnungsintervall (monatlich, vierteljährlich, halbjährlich, jährlich) selbst auf der
EEG-Seite. eegFaktura prüft, ab wann der Wechsel möglich ist, und nennt, was ihn aufhält.
Siehe [Abrechnung](05-abrechnung.md#abrechnungszeitraum-wechseln).

### Zählpunkt abmelden: inaktiv erst nach der Antwort

Ein Zählpunkt wird erst inaktiv, wenn der Netzbetreiber die Abmeldung bestätigt (oder sie ablehnt, weil keine
Datenfreigabe mehr besteht). Eine Ablehnung zeigt den Grund des Netzbetreibers.
Siehe [Prozesse](08-prozesse.md#was-nach-dem-anfordern-passiert).

### Dashboard: Übersicht EEG mit dem Stand heute

Die Kachel **Übersicht EEG** zeigt Mitglieder, Zählpunkte und Tarife einheitlich mit dem Stand von heute; Zählpunkte
in Anmeldung stehen extra, die Tarife sind in Energietarife und Mitgliedsbeitrag getrennt.
Siehe [Dashboard](01-anmeldung.md#ubersicht-eeg).

### EEG-Seite: Modell und Nahebereich

Die EEG-Seite zeigt das **Modell** der Gemeinschaft mit Lang- und Kurzform und den **Nahebereich** mit der amtlichen
Bezeichnung laut ElWG. Für **Peer-to-Peer** und **Eigenversorgung** bietet eegFaktura keine Abrechnung an.
Siehe [EEG-Seite](01-anmeldung.md#modell-und-nahebereich).

### Gemeinschaft wechseln mit Suche

Wer mehrere Gemeinschaften betreut, wechselt über **Gemeinschaft wechseln** im Benutzermenü und findet die Gemeinschaft
über ein Suchfeld. Das Benutzermenü zeigt die aktuelle Gemeinschaft.
Siehe [Gemeinschaft wechseln](01-anmeldung.md#gemeinschaft-wechseln).

## Herbst 2026 (seit 03.11.2026)

### Keine Offline-Registrierung mehr

Die Netzbetreiber unterstützen die Anmeldung mit **Aktivierungs-Code** (Offline-Registrierung) nicht mehr. Beim
Anlegen eines Zählpunkts, beim **Zulassen** und unter **Prozesse → Zählpunkt aktivieren** gibt es die Auswahl
Offline-Registrierung daher nicht mehr. Zählpunkte werden immer online beim Netzbetreiber angemeldet; das Mitglied
bestätigt danach die Datenfreigabe.
Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#neues-mitglied-zulassen).


## Herbst 2026 (seit 29.10.2026)

### Einmalige Beitrittsgebühr

Ein Mitgliedstarif kann eine einmalige **Beitrittsgebühr** haben, mit eigener Umsatzsteuer-Einstellung. eegFaktura
verrechnet sie einmal je Mitglied im ersten endgültigen Lauf mit Energie, auf einer Rechnung. Mitglieder, die schon
abgerechnet waren, bekommen sie nicht automatisch. Beim Mitglied unter **Details** siehst du
den Stand („Beitrittsgebühr: …“) und kannst die Gebühr **nachverrechnen** (für schon abgerechnete Mitglieder) oder
**außerhalb bezahlt** erfassen. Der Stammdaten-Export hat zwei neue Spalten dazu.
Siehe [Tarife](04-tarife.md#beitrittsgebuhr) und
[Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#beitrittsgebuhr-eines-mitglieds).

### Abrechnung ohne Auswahl

Abgerechnet wird immer die ganze Gemeinschaft (alle aktiven Mitglieder mit Tarif); die Haken in der Mitgliederliste
gibt es nicht mehr. Der Schalter **€** zeigt beim Darüberfahren, was er tut, oder warum er gesperrt ist. Ein Zeitraum
ganz ohne Energiedaten wird nicht abgerechnet.
Siehe [Abrechnung](05-abrechnung.md#abrechnungsmodus).

### Mitgliederliste

- Statt der zwei Reiter gibt es eine Auswahl **Anzeige**: **Standard** (die Mitglieder des gewählten Zeitraums, wie
  bisher „Periode“), **Alle**, **Aktive** oder **Inaktive**. Hinweise beim Darüberfahren erklären die Ansicht und die
  Knöpfe unten.
- Beim Import (Wolke) kannst du die Datei in das Fenster ziehen, und der eingetragene **Sheet-Name** wird jetzt
  verwendet.

Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#anzeige-zeitraum-und-sortierung).

### Verträge per Drag & Drop

Dokumente eines Mitglieds (PDF, JPEG, PNG) ziehst du in das Fenster zum Hochladen, mehrere auf einmal, oder direkt auf
den Bereich **Verträge** des Mitglieds.
Siehe [Dokumente eines Mitglieds](02-mitglieder-zaehlpunkte.md#dokumente-eines-mitglieds).

### Tarife

Die Tarifliste ist in Mitgliedstarife, Erzeugertarife und Verbrauchertarife gruppiert, nach Namen sortiert, mit
einklappbaren Gruppen, Suche (Lupe) und kleineren Karten. Die Tarifauswahl bei Mitglied und Zählpunkt ist gleich
sortiert. Siehe [Tarife](04-tarife.md#die-tarifliste).

### E-Mail-Texte

Ein neu eingefügtes Bild ist zunächst klein (200 px). Siehe [E-Mail-Texte](03-email-texte.md#bilder).

## Herbst 2026 (seit 28.10.2026)

### E-Mail-Texte selbst gestalten

Die automatischen Mails an Mitglieder (Freigabe-Aufforderung, Zählpunkt aktiv, Zählpunkt inaktiv,
Rechnung / Gutschrift) lassen sich anpassen: eigener Betreff und Text, Schriftgröße, Bilder (auch per Einfügen oder
Ziehen), Vorschau und Testmail. Ob der Standardtext oder ein eigener Text verschickt wird, wählst du mit dem
Schalter **Eigenen Text verwenden**. Unter jeder Mail steht fest „versandt durch EEG Faktura, ein Service des
VFEEG“. Gegen Spam gelten Regeln für Links (höchstens 3, keine Kurz-Links).
Siehe [E-Mail-Texte](03-email-texte.md).

### Energiedaten smart nachfordern

Beim Nachfordern prüft eegFaktura zuerst, wo Daten fehlen oder nur L3-Werte da sind, und fordert nur diese
Zählpunkte an. Den Fortschritt siehst du unter **Nachrichten**.
Siehe [Prozesse](08-prozesse.md#zahlpunktdaten-nachfordern).

### Dashboard

- Tagesansicht für die ganze Gemeinschaft, Zeitraum in den oberen Kacheln.
- Der **Lastverlauf** zeigt die Bilanzdifferenz (Hinweis auf fehlende Energiedaten) und markiert auffällige
  Zeiträume.
- Unter **Energiemengen** nennt ein Hinweis die Zählpunkte ohne gültigen Tarif, die in „Eingekauft“ und „Verkauft“
  nicht enthalten sind.
- **Tarife** zeigt auch die Mitgliedsbeiträge und wie viele aktive Mitglieder keinen haben.

Siehe [Dashboard](01-anmeldung.md#dashboard).

### Mitgliederliste

Filter **Alle / Aktive / Inaktive** und eine wählbare Sortierung, z. B. nach Ort oder Einzugsart; „Mitglieder mit
nötiger Aktion oben“ lässt sich abschalten.
Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#anzeige-zeitraum-und-sortierung).

### Prozesse

Die Zählpunkt-Auswahl zeigt Verbraucher oder Erzeuger und den Anlagennamen; die Prozess History zeigt Datum als
TT.MM.JJJJ und die Uhrzeit. Siehe [Prozesse](08-prozesse.md).

### Abrechnung

- Positionen eines Tarifs ohne „Umsatzsteuer anführen“ stehen auf dem Beleg mit 0 %, ohne eigene USt-Summenzeile.
  Die Beträge bleiben gleich. Siehe [Tarife](04-tarife.md#umsatzsteuer).
- Die Dateien im ZIP-Download heißen wie die Belege, ohne Zahl davor.
  Siehe [Abrechnung](05-abrechnung.md#nach-der-abrechnung).
