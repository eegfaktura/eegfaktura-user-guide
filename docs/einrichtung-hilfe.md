# Einrichtung & Hilfe

## Anbindung an die Netzbetreiber

eegFaktura tauscht die Nachrichten mit den Netzbetreibern über die österreichische Marktkommunikation (EDA) aus. Dafür
gibt es zwei Wege:

| Weg | Was er bedeutet |
|-----|-----------------|
| **Online-Anbindung** über den Kommunikationsendpunkt (KEP) des VFEEG | eegFaktura meldet Zählpunkte selbst an und ab, fordert Daten nach und bekommt die Energiedaten automatisch. **Empfohlen.** |
| **EDA-Anwenderportal** (ohne Online-Anbindung) | Anmeldungen und Datenfreigaben laufen im Portal; Energiedaten importierst du in eegFaktura selbst (siehe [Energiedaten importieren](06-energiedaten.md#energiedaten-importieren)) |

### Online-Anbindung einrichten

1. Melde die Gemeinschaft bei der EDA für die Anbindung über einen KEP an (Anleitung der EDA:
   <https://www.eda.at/e-mail-anbindung>). Als KEP-Betreiber gibst du den **VFEEG** an, als Backend-System
   **EEG Faktura**.
2. Die Zugangsdaten, die du von der EDA bekommst, schickst du als Ticket an den Support (siehe unten).
3. Sobald die Anbindung aktiv ist, erscheint in eegFaktura der Menüpunkt **Prozesse**.

**Wechsel vom EDA-Anwenderportal:** Ein Abmelden im Portal vorab ist nicht nötig. Lege die Mitglieder in eegFaktura an
oder importiere sie (siehe [Stammdaten importieren](stammdaten-import.md)).
Zählpunkte, die beim Netzbetreiber schon aktiv sind, importierst du als **aktiv** — sonst würden sie neu angemeldet —
und mit dem tatsächlichen Datum in „registriert seit“. Danach forderst du die Energiedaten rückwirkend an
([Zählpunktdaten nachfordern](08-prozesse.md#zahlpunktdaten-nachfordern)).

## Datenfreigabe der Mitglieder

Damit der Netzbetreiber Daten an die Gemeinschaft schickt, muss jedes Mitglied die **Datenfreigabe** bestätigen —
meist im Smart-Meter-Portal seines Netzbetreibers. Wie das je Netzbetreiber geht (Registrierung im Portal,
Datenfreigabe, Viertelstundenwerte einschalten), steht in den Anleitungen der bisherigen Doku:
<https://docs.eegfaktura.at/shelves/netz-betreiber-infos>.

> Diese Anleitungen beschreiben die Portale der Netzbetreiber. Die Portale ändern sich ohne unser Zutun; wenn etwas
> nicht mehr passt, hilft der Netzbetreiber weiter.

## Datenschutz

eegFaktura speichert die Daten der Mitglieder auf den Servern des VFEEG und verarbeitet sie für die Verrechnung.
Darauf sollten eure Beitrittserklärung bzw. eure Verträge mit den Mitgliedern hinweisen. Wie ihr Beitrittserklärung und
Datenverarbeitung rechtlich gestaltet, klärt bitte mit eurer Rechtsberatung oder dem VFEEG. Vorlagen für Verträge mit
den Mitgliedern bietet die Österreichische Koordinationsstelle für Energiegemeinschaften in ihrem
[Downloadbereich](https://energiegemeinschaften.gv.at/downloadbereich/).

## Hilfe und Support

| Wo | Wofür |
|----|-------|
| **Support-Portal** <https://support.vfeeg.org> | Tickets (siehe [unten](#dafur-schreibst-du-ein-ticket)). Anmeldung mit denselben Zugangsdaten wie eegFaktura |
| **Forum** <https://www.eeg-grossraming.at/Forum/index.php> | Fragen an andere Gemeinschaften; Ideen für neue Funktionen im Bereich **Feature Requests** |
| dieses Handbuch | Bedienung von eegFaktura |

Der Support wird **ehrenamtlich** betrieben. Eine Antwort kann einige Tage bis mehrere Wochen dauern; einfache Fragen
sind im Forum oft schneller beantwortet.

### Dafür schreibst du ein Ticket

- **Zugangsdaten der EDA** für die Online-Anbindung übermitteln.
- Einen weiteren **EEG-Admin** anlegen lassen (mit Vor- und Nachname und E-Mail-Adresse der Person).
- **Tarif vieler Zählpunkte oder Mitglieder auf einmal ändern** (Massenänderung): Lege den neuen Tarif vorher an und
  nenne ihn im Ticket, dazu für wen er gelten soll — für alle, nur für jene ohne Tarif oder nur für jene mit einem
  bestimmten bisherigen Tarif. Wie jede Tarifänderung gilt er ab der nächsten Abrechnung für deren ganzen Zeitraum;
  lass ihn deshalb erst nach der Abrechnung des alten Zeitraums umstellen.
- **Bankdaten vieler Mitglieder auf einmal setzen** (Massenänderung): Einzugsart, Mandatsreferenz und Mandatsdatum,
  Mandatsreferenz und Mandatsdatum auch aus einer Excel-Liste je Mitgliedsnummer.
- Änderungen, die nur der Betrieb machen kann.
