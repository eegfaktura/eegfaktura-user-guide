# Was ist neu?

Neue Funktionen von eegFaktura, die du als EEG-Admin bemerkst. Die Kapitel beschreiben jeweils den aktuellen
Stand.

## Herbst 2026 (nächste Version)

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
