# Energiedaten

Der Netzbetreiber schickt für jeden aktiven Zählpunkt die Energiedaten in Viertelstundenwerten. eegFaktura speichert
sie und rechnet daraus die Anteile der Gemeinschaft.

## In der Mitgliederliste

Jede Zählpunkt-Karte zeigt die Energiemenge im gewählten Zeitraum:

- bei **Verbrauchern** den Anteil, den sie aus der Gemeinschaft bezogen haben,
- bei **Erzeugern** den Teil ihrer Einspeisung, der nicht in der Gemeinschaft verteilt wurde.

Den Zeitraum wählst du oben in der Liste.

## Diagramm eines Zählpunkts

Ein Klick auf einen aktiven Zählpunkt zeigt unter **Energiedaten** ein Diagramm:

![Energiedaten eines Zählpunkts](images/energiedaten-diagramm.png)

| Knopf | Ansicht |
|-------|---------|
| **Y** | ein Jahr |
| **YH** | ein Halbjahr |
| **YQ** | ein Quartal |
| **YM** | ein Monat |
| **D** | ein Tag in Viertelstunden |

**EEG** (grün) ist der Anteil aus der Gemeinschaft, **EVU** der Rest vom Energieversorger bzw. ins Netz. In der
Tagesansicht blätterst du mit den Pfeilen; sie beginnt beim letzten Tag mit Daten:

![Tagesansicht](images/energiedaten-tag.png)

## Energiedaten exportieren

Der Knopf mit dem Pfeil nach unten oben in der Mitgliederliste öffnet **Download Daten für …**:

![Export](images/energiedaten-export.png)

1. Wähle **Energiedaten** (oder **Stammdaten** für die Mitglieder- und Zählpunktdaten).
2. Bei Energiedaten: Wähle unter **Zeitspanne auswählen** den **Zeitraum**.
3. Klicke auf **Export**. Du bekommst eine Excel-Datei.

Die Excel-Datei hat zwei Blätter:

- **Summary**: Summen der Gemeinschaft (Verbrauch, Erzeugung, Eigendeckung, Überschuss, Mengenbilanz — sie sollte
  nahe 0 sein) und je Zählpunkt, ab wann und bis wann Daten da sind und ob sie **vollständig** sind.
- **Energiedaten**: alle Viertelstundenwerte je Zählpunkt.

Die Farben zeigen die Qualität der Werte:

| Kennung | Bedeutung | Farbe |
|---------|-----------|-------|
| L1 | gemessener Wert | ohne |
| L2 | Ersatzwert des Netzbetreibers (gilt als vollständig) | gelb |
| L3 | vorläufiger oder fehlerhafter Wert | rot |
| L0 | kein Wert | grau |

Werte mit L0 oder L3 machen einen Zählpunkt „nicht vollständig“. Für sie kannst du die Daten unter
[Prozesse → Zählpunktdaten nachfordern](08-prozesse.md#zahlpunktdaten-nachfordern) erneut anfordern — mit „Smart“
nur die fehlenden.

## Energiedaten importieren

Der Knopf mit der Wolke öffnet **Upload Daten für …**. Mit **Stammdaten** liest du Mitglieder und Zählpunkte aus einer
Excel-Datei ein (Blatt „EEG Stammdaten“). Nur bei Gemeinschaften **ohne Online-Anbindung** gibt es zusätzlich
**Energiedaten** (Blatt „Energiedaten“). Wähle die Datei und klicke auf **Import**.
