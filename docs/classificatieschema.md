# Classificatieschema

Dit schema komt uit het werk aan de gemeentelijke Uitvoeringsstrategie Cloud (VNG). Het doel: bij inkoop en aanbesteding van gemeentelijke software kunnen duiden hoe een systeem zich classificeert en welk patroon met soevereiniteitseisen daarbij hoort. Het bouwt voort op bestaande kaders zoals de BIO en NIS2, en niet op iets nieuws.

## Opbouw

```
Classificatie-object  ->  Classificatiecriteria  ->  Patroon  ->  Maatregelen
   (systeem X)            (2 assen, zie hieronder)    (2 x 5 = 10)   (mitigerende maatregelen,
                                                                      Handreiking Cloud)
```

### As 1: kritikaliteit van het bedrijfsproces

| Waarde | Omschrijving |
| --- | --- |
| Bedrijfskritiek | Het systeem ondersteunt een kritiek bedrijfsproces |
| Niet kritiek | Het systeem ondersteunt geen kritiek bedrijfsproces |

### As 2: gegevensclassificatie

| Waarde |
| --- |
| Openbaar |
| Door wet- en regelgeving gebonden |
| Persoonsgegevens |
| Bijzondere persoonsgegevens |
| Staatsgeheimen |

### Patronen

De combinatie van beide assen levert 2 x 5 = 10 patronen op. Elk patroon hoort op termijn bij een set mitigerende maatregelen (uit de Handreiking Cloud) en soevereiniteitseisen.

## Wat ontbreekt, en waar jullie aan de slag gaan

De koppeling van een patroon aan een **soevereiniteitsniveau** bestaat nog niet. Dat is de kern van de challenge: adviseer per patroon een niveau, onderbouw het met de bronnen in `bronnen.md`, en vertaal het naar eisen die in een programma van eisen (PvE) passen.

Het startbestand `data/patronen.yaml` bevat de 10 patronen met lege velden voor niveau, onderbouwing en eisen.
