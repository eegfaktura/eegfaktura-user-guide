# Einrichtung & Hilfe

## Anbindung an die Netzbetreiber

eegFaktura tauscht die Nachrichten mit den Netzbetreibern über die österreichische Marktkommunikation (EDA) aus. Dafür
gibt es zwei Wege:

| Weg | Was er bedeutet |
|-----|-----------------|
| **Online-Anbindung** über den Kommunikationsdienstleister (KEP) des VFEEG | eegFaktura meldet Zählpunkte selbst an und ab, fordert Daten nach und bekommt die Energiedaten automatisch. **Empfohlen.** |
| **EDA-Anwenderportal** (ohne Online-Anbindung) | Anmeldungen und Datenfreigaben laufen im Portal; Energiedaten importierst du in eegFaktura selbst (siehe [Energiedaten importieren](06-energiedaten.md#energiedaten-importieren)) |

### Online-Anbindung einrichten

1. Melde die Gemeinschaft bei der EDA für die Anbindung über einen KEP an (Anleitung der EDA:
   <https://www.eda.at/e-mail-anbindung>). Als KEP gibst du den **VFEEG** an, als Backend-System **EEG Faktura**.
2. Die Zugangsdaten, die du von der EDA bekommst, schickst du als Ticket an den Support (siehe unten).
3. Sobald die Anbindung aktiv ist, erscheint in eegFaktura der Menüpunkt **Prozesse**.

**Wechsel vom EDA-Anwenderportal:** Ein Abmelden im Portal vorab ist nicht nötig. Lege die Mitglieder in eegFaktura an
oder importiere sie (siehe [Stammdaten importieren](02-mitglieder-zaehlpunkte.md#stammdaten-aus-excel-importieren)).
Zählpunkte, die beim Netzbetreiber schon aktiv sind, importierst du als **aktiv** — sonst würden sie neu angemeldet.
Danach forderst du die Energiedaten rückwirkend an
([Zählpunktdaten nachfordern](08-prozesse.md#zahlpunktdaten-nachfordern)).

## Datenfreigabe der Mitglieder

Damit der Netzbetreiber Daten an die Gemeinschaft schickt, muss jedes Mitglied die **Datenfreigabe** bestätigen —
meist im Smart-Meter-Portal seines Netzbetreibers. Wie das je Netzbetreiber geht (Registrierung im Portal,
Datenfreigabe, Viertelstundenwerte einschalten), steht in den Anleitungen der bisherigen Doku:
<https://docs.eegfaktura.at/shelves/netz-betreiber-infos>.

> Diese Anleitungen beschreiben die Portale der Netzbetreiber. Die Portale ändern sich ohne unser Zutun; wenn etwas
> nicht mehr passt, hilft der Netzbetreiber weiter.

## Datenschutz

Bevor du ein Mitglied aufnimmst, sollte eine unterschriebene **Beitrittserklärung mit Vereinbarung zur
Auftragsverarbeitung** vorliegen. Halte im Bezugs- bzw. Einspeisevertrag fest, dass die Daten auf den Servern des
VFEEG (eegFaktura) gespeichert und für die Verrechnung verarbeitet werden. Für die rechtliche Gestaltung wende dich an
eure Rechtsberatung.

## Hilfe und Support

| Wo | Wofür |
|----|-------|
| **Support-Portal** <https://support.vfeeg.org> | Tickets, z. B. Zugangsdaten der EDA übermitteln, einen weiteren **EEG-Admin** anlegen (mit Vor- und Nachname und E-Mail-Adresse der Person) oder Änderungen, die nur der Betrieb machen kann. Anmeldung mit denselben Zugangsdaten wie eegFaktura |
| **Forum** <https://www.eeg-grossraming.at/Forum/index.php> | Fragen an andere Gemeinschaften; Ideen für neue Funktionen im Bereich **Feature Requests** |
| dieses Handbuch | Bedienung von eegFaktura |

Der Support wird **ehrenamtlich** betrieben. Eine Antwort kann einige Tage bis mehrere Wochen dauern; einfache Fragen
sind im Forum oft schneller beantwortet.
