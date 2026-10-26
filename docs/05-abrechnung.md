# Abrechnung

Am Ende jedes Abrechnungszeitraums erstellt eegFaktura für deine Mitglieder **Rechnungen** (Strombezug,
Mitgliedsbeitrag) und **Gutschriften** (Einspeisung). Abrechnen können nur EEG-Admins.

Der Ablauf in Kurzform:

1. [Abrechnungseinstellungen](#abrechnungseinstellungen) einmalig anlegen.
2. In der Mitgliederliste den **Abrechnungsmodus** einschalten und den Zeitraum wählen.
3. Eine **Vorschau** erstellen und prüfen — so oft du willst.
4. **Abrechnung durchführen** — endgültig, mit fortlaufenden Nummern.
5. Belege **senden**, als ZIP oder Excel herunterladen, **SEPA**-Dateien erzeugen.

## Abrechnungseinstellungen

Auf der **EEG-Seite** in der Karte **Abrechnungseinstellungen** (beim ersten Mal **Abrechnungseinstellungen
hinzufügen**):

![Abrechnungseinstellungen](images/abrechnung-einstellungen.png)

| Feld | Wofür |
|------|-------|
| **Rechnungen: Text vor / nach Positionen, Abschlusstext** | Texte auf jeder Rechnung, z. B. Zahlungsbedingungen |
| **Präfix / Startwert für Rechnungsnummern** | Die Nummer setzt sich aus Präfix, Jahr des Belegdatums und laufender Nummer zusammen, z. B. `RE20260004`; die laufende Nummer beginnt je Jahr beim Startwert |
| **Gutschriften für Mitgliedstyp Privat: Texte** | Texte auf Gutschriften an Privatpersonen |
| **Präfix / Startwert für Gutschriftennummern** | wie bei den Rechnungen, z. B. `GS20260001` |
| **Gutschriften für Mitgliedstyp Firma: Texte** | Texte auf Gutschriften an Firmen (mit UID: Reverse Charge) |
| **Text für Fußzeile** | steht unten auf jedem Beleg |
| **Dokumentennummer: Anzahl Stellen** | Länge der laufenden Nummer (1–6, mit führenden Nullen) |
| **Bild für Logo** | das Logo oben auf den Belegen |

Änderungen werden gespeichert, sobald du ein Feld verlässt.

## Abrechnungsmodus

1. Öffne **Mitglieder** und wähle oben den **Zeitraum** (z. B. „Jul-Sep 2026“). Jeder Zeitraum hat seinen eigenen
   Abrechnungslauf.
2. Hake die Mitglieder an, die abgerechnet werden sollen — der Haken ganz oben wählt alle aktiven Mitglieder mit
   Tarif.

    > **Wichtig:** Hake **alle** Mitglieder an, die in diesem Zeitraum abgerechnet werden sollen. Ein Zeitraum lässt
    > sich nur **einmal** endgültig abrechnen; Mitglieder, die dabei nicht angehakt waren, kannst du für diesen Zeitraum
    > nicht nachträglich abrechnen.
3. Schalte unten links den Schalter **€** ein. eegFaktura erklärt den Ablauf; bestätige mit **OK**.

![Hinweis zum Abrechnungsmodus](images/abrechnung-modus.png)

Im Abrechnungsmodus zeigen die Zählpunkt-Karten Beträge in € statt kWh.

## Vorschau erstellen

Wähle das **Rechnungsdatum** und klicke auf **Vorschau erstellen**. Vorher prüft eegFaktura die Daten des Zeitraums:

![Prüfung vor der Abrechnung](images/abrechnung-pruefung.png)

| Prüfung | Was sie zeigt |
|---------|---------------|
| **Tarif** | Zählpunkte ohne Tarif (für sie entsteht keine Position) |
| **L3-Werte** | Zählpunkte mit vorläufigen Werten des Netzbetreibers |
| **Energiebilanz** | ob Produktion, Verbrauch und Verteilung zusammenpassen |
| **Vollständigkeit** | Zählpunkte mit fehlenden Viertelstunden |

Die Prüfung umfasst alle aktiven Zählpunkte der Gemeinschaft, nicht nur die angehakten Mitglieder. Die Pfeile klappen
die Details auf. Warnungen halten dich nicht auf (**Trotzdem Vorschau erstellen**), sie zeigen
aber, wo die Abrechnung noch unvollständig ist. Fehlende Daten forderst du unter
[Prozesse → Zählpunktdaten nachfordern](08-prozesse.md#zahlpunktdaten-nachfordern) an.

Die Vorschau erstellt Belege mit dem Zusatz „Vorschau“ und ohne Nummern:

![Vorschau](images/abrechnung-vorschau.png)

- Die Tabelle zeigt Rechnungen und Gutschriften netto, USt und brutto; **Saldo Zahlungen (brutto)** ist die zu
  erwartende Kontobewegung.
- **Marge bei Regelbesteuerung (netto)** ist ein rechnerischer Wert zur Orientierung, kein Buchungsbetrag und keine
  steuerliche Beratung.
- Den **Mitgliedsbeitrag** bekommt ein Mitglied nur, wenn es im Zeitraum mindestens einen Zählpunkt mit Energiedaten
  hat.
- **ZIP** lädt alle Vorschau-Belege als PDF herunter, **EXCEL** eine Aufstellung aller Positionen.
- **Vorschau Akt.** rechnet die Vorschau neu, z. B. nachdem du einen Tarif geändert oder Daten nachgefordert hast.

## Abrechnung durchführen

Passt die Vorschau, klicke auf **Abrechnung durchführen**. Die endgültigen Belege werden dabei **neu berechnet** — mit
den Tarifen, Stammdaten und Energiedaten im Moment des Klicks und mit den gerade angehakten Mitgliedern. Hat sich seit
der Vorschau etwas geändert, erstelle sie mit **Vorschau Akt.** direkt davor neu. eegFaktura prüft noch einmal und
warnt ausdrücklich:

![Abrechnung durchführen](images/abrechnung-durchfuehren.png)

> **Die Abrechnung ist endgültig.** Die Belege bekommen fortlaufende Nummern und lassen sich danach nicht mehr ändern
> oder löschen. Ein Belegdatum in der Zukunft ist nicht erlaubt.

Belege mit dem Betrag 0 werden nicht erstellt. Erzeuger ohne UID bekommen eine **Gutschrift**. Erzeuger mit UID
bekommen — je nach Einstellung der Gemeinschaft — eine **Gutschrift im Reverse-Charge-Verfahren** oder eine
**Information** (ohne Nummer, mit den Texten „Gutschriften für Mitgliedstyp Firma“); dann stellt der Erzeuger der
Gemeinschaft selbst eine Rechnung. Welche Variante deine Gemeinschaft hat, siehst du an den Belegen der Vorschau.

## Nach der Abrechnung

![Abgerechneter Zeitraum](images/abrechnung-abgerechnet.png)

| Knopf | Was er tut |
|-------|------------|
| **SENDEN** | schickt jedem Mitglied mit E-Mail-Adresse seinen Beleg als PDF, mit der Gemeinschaft in Kopie. Text und Betreff kommen aus den [E-Mail-Texten](03-email-texte.md) („Rechnung / Gutschrift“) |
| **DOWNLOAD** | alle Belege als ZIP |
| **EXCEL** | Aufstellung aller Belege und Positionen, z. B. für die Buchhaltung |
| **SEPA** | Dateien für die Bank (siehe unten) |

> **Vor dem Senden:** **SENDEN** geht pro Lauf nur **einmal**. Einzelne Mails, die nicht zugestellt werden können
> (fehlende oder ungültige Adresse), zeigt eegFaktura nicht an, und der Versand lässt sich nicht wiederholen. Prüfe die
> E-Mail-Adressen deshalb vorher und gib Mitgliedern ohne Mail ihren Beleg aus dem **DOWNLOAD** (ZIP).

### SEPA-Dateien

**SEPA** öffnet den Dialog **SEPA Dateien**:

![SEPA Dateien](images/abrechnung-sepa.png)

1. Wähle **Einzug am** (für die Lastschriften, voreingestellt heute) und **Überweisung am** (für die Gutschriften,
   voreingestellt fünf Tage später, nicht am Wochenende). Liegt die Überweisung vor dem Einzug, warnt eegFaktura.
   Passe das Einzugsdatum an das an, was eure Rechnungstexte versprechen.
2. Mit **SEPA Sammelbuchung** bucht die Bank die Datei als eine Sammelbuchung.
3. **Mitglieder zusammenfassen** **verrechnet** Rechnungen und Gutschriften je Konto (IBAN, Einzugsart, Mandat):
   Ist die Summe positiv, wird sie eingezogen, ist sie negativ, überwiesen, bei 0 gibt es keine Buchung. Beispiel:
   Rechnung 50 €, Gutschrift 20 € → Einzug 30 €. Ohne den Haken wird jeder Beleg einzeln gebucht. Beides ist
   voreingestellt.
4. Klicke auf **Generieren** und lade die Dateien mit **Herunterladen** herunter. Sie werden im Browser erstellt und
   nicht auf dem Server gespeichert.

Die Hinweise darunter nennen, was nicht in den Dateien ist, z. B.:

- keine Lastschrift-Datei, weil die Gemeinschaft keine **Creditor-ID** hat (EEG-Seite → Bankdaten),
- Mitglieder mit Einzugsart „Kein SEPA“ oder ohne Einzugsart,
- Mitglieder ohne IBAN — diese bitte händisch abwickeln.

> Prüfe die Überweisungsdatei vor dem Hochladen zur Bank gegen die Gutschriften. Belege der Art **Information**
> werden derzeit ebenfalls als Überweisung aufgenommen, obwohl dort der Erzeuger der Gemeinschaft eine Rechnung stellt.

## Belege eines Mitglieds

Beim Mitglied unter **Meine Rechnungen** stehen seine Belege, mit den Reitern Alle, Rechnungen, Gutschriften und
Information. Ein Klick öffnet das PDF:

![Belege eines Mitglieds](images/abrechnung-meine-rechnungen.png)

Belege mit „Vorschau“ im Namen stammen aus einer Vorschau und sind nicht gültig. Der Reiter **Information** zeigt
Info-Belege für Erzeuger mit UID (siehe oben).
