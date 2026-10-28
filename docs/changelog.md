# Was ist neu?

Neue Funktionen von eegFaktura, die du als EEG-Admin bemerkst. Die Kapitel beschreiben jeweils den aktuellen
Stand.

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
Siehe [Mitglieder & Zählpunkte](02-mitglieder-zaehlpunkte.md#zeitraum-filter-und-sortierung).

### Prozesse

Die Zählpunkt-Auswahl zeigt Verbraucher oder Erzeuger und den Anlagennamen; die Prozess History zeigt Datum als
TT.MM.JJJJ und die Uhrzeit. Siehe [Prozesse](08-prozesse.md).

### Abrechnung

- Positionen eines Tarifs ohne „Umsatzsteuer anführen“ stehen auf dem Beleg mit 0 %, ohne eigene USt-Summenzeile.
  Die Beträge bleiben gleich. Siehe [Tarife](04-tarife.md#umsatzsteuer).
- Die Dateien im ZIP-Download heißen wie die Belege, ohne Zahl davor.
  Siehe [Abrechnung](05-abrechnung.md#nach-der-abrechnung).
