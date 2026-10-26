# Prozesse beim Netzbetreiber

Unter **Prozesse** löst du Vorgänge beim Netzbetreiber aus. Den Menüpunkt gibt es nur für EEG-Admins von
Gemeinschaften mit **Online-Anbindung**. eegFaktura verschickt die Anfrage über die Marktkommunikation (EDA); die
Antwort kommt später unter [Nachrichten](07-nachrichten.md).

Jedes Formular zeigt oben die **Gemeinschafts-ID**. Nach **Anfordern** meldet eegFaktura „Die Anforderung wurde an
den Netzbetreiber gesendet.“ oder den Grund, warum es nicht geklappt hat.

![Prozesse](images/prozesse.png)

## Zählpunktdaten nachfordern

Fordert Energiedaten für einen Zeitraum erneut an, z. B. wenn Daten fehlen oder nur vorläufig (L3) sind.

1. Wähle **Mitglied** und **Zählpunkt** (mehrere möglich) — oder hake **Zählpunkte für die gesamte EEG
   nachfordern** an.
2. Wähle den **Zeitraum**.
3. Lass **Nur fehlende Daten oder L3-Werte anfordern (Smart)** angehakt: eegFaktura prüft zuerst, wo wirklich etwas
   fehlt, und schlägt vor, nur diese Zählpunkte anzufordern.
4. Klicke auf **Anfordern**.

Für heute und spätere Tage gibt es noch keine Daten; dieselben Zählpunkte innerhalb einer Stunde erneut anzufordern
ist nicht nötig. Das Ergebnis kommt als **Zusammenfassung Energiedaten-Anforderung** unter Nachrichten.

## Zählpunkt aktivieren

Meldet einen noch nicht aktiven Zählpunkt (erneut) beim Netzbetreiber an, z. B. nach einer Abweisung, wenn der Fehler
behoben ist. Wähle **Mitglied** und **Zählpunkt**. Hast du vom Netzbetreiber einen **Aktivierungs-Code**, hake
**Offline-Registrierung** an und trage ihn ein. Bei der Online-Anmeldung muss das Mitglied die Datenfreigabe danach
bestätigen; es bekommt dazu die Mail „Freigabe-Aufforderung“.

## Zählpunkt abmelden

Hebt die Datenfreigabe eines Zählpunkts beim Netzbetreiber auf — der Zählpunkt verlässt die Gemeinschaft.

![Zählpunkt abmelden](images/prozesse-abmelden.png)

1. Wähle **Mitglied** und **Zählpunkt** (mehrere möglich).
2. Wähle unter **Zeitraum** das Ende der Teilnahme (frühestens morgen).
3. Klicke auf **Anfordern** und bestätige „Datenfreigabe aufheben“ mit **Aufheben**.

Fehlt eegFaktura die Kennung der Datenfreigabe, fordere zuerst die **Teilnehmerliste** an (siehe unten).

## Teilnahmefaktor ändern

Ändert, welchen Anteil ein Zählpunkt an der Gemeinschaft hat.

![Teilnahmefaktor ändern](images/prozesse-teilnahmefaktor.png)

1. Wähle **Mitglied** und **Zählpunkt** (die Auswahl zeigt den aktuellen Faktor).
2. Gib den neuen **Teilnahmefaktor in %** ein (1–100) und klicke auf **Anfordern**.

> Der Netzbetreiber nimmt Änderungen **nur zwischen 9 und 17 Uhr** an, **eine pro Tag** je Zählpunkt; die Änderung
> gilt ab dem nächsten Tag. Außerhalb dieser Zeit warnt eegFaktura, weil der Netzbetreiber sonst mit „Prozessdatum
> falsch“ ablehnt.

## Teilnehmerliste anfordern

Fordert beim Netzbetreiber die Liste aller Zählpunkte der Gemeinschaft an. Die Antwort kommt später; die
verantwortliche Person der EEG bekommt eine E-Mail. Bei Bürgerenergiegemeinschaften wählst du zuerst die
**Netzbetreiber-ID**.

## Prozess History

Zeigt die Kommunikation mit dem Netzbetreiber, standardmäßig der letzten 14 Tage (Zeitraum oben rechts):

![Prozess History](images/prozesse-history.png)

| Bereich | Inhalt |
|---------|--------|
| **Anmeldung Teilnahme Online** | Anmeldungen von Zählpunkten |
| **Datenfreigabe-Aufhebung** | Abmeldungen |
| **Anfordern von Energiedaten** | Nachforderungen |
| **Änderung des Teilnahmefaktors** | Änderungen des Faktors |
| **Versenden der Energiedaten** | Energiedaten, die der Netzbetreiber geschickt hat (von – bis) |

Jeder Bereich lässt sich nach Zählpunkt, Name, Mitgliedsnummer oder Conversation-ID durchsuchen. Je Zählpunkt stehen
die Schritte mit Datum, **Protokoll** und **Status** bzw. **Info**.

**Eine Ablehnung lesen:** In der Spalte Protokoll steht dann ABLEHNUNG, in Status oder Info der Grund, z. B.
„Zählpunkt nicht gefunden“, „Kunde hat Datenfreigabe abgelehnt“ oder „Prozessdatum falsch“.
