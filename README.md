# OneGov #3: Van classificatie naar inkooptafel

Startrepository voor challenge 2 van de OneGov AI Hackathon Series, editie #3 (9-10 december 2026, The Hague Tech, Den Haag).

Challenge owners: Jacco Brouwer (VNG Realisatie) en Thijs Turel (DACC, Digitale Autonomie Competentiecentrum).

## De opgave in het kort

Is dit systeem bedrijfskritiek? Welke data zit erin? En wat moet je dan eisen van je leverancier? Teams bouwen een tool die een systeem classificeert, een onderbouwd soevereiniteitsniveau adviseert en eisen oplevert die een inkoper zo in het bestek kan zetten. De beslisregels staan expliciet in code of configuratie (rules-as-code).

De volledige challenge brief staat op Alkemio.

## Wat staat hier

| Map / bestand | Inhoud | Status |
| --- | --- | --- |
| `docs/classificatieschema.md` | Het classificatieschema: kritikaliteit x gegevensclassificatie, 10 patronen | Beschikbaar |
| `docs/bronnen.md` | Wet- en regelgeving, kaders en handreikingen die mogelijk minimumeisen bevatten | Beschikbaar (eerste lezing) |
| `data/patronen.yaml` | De 10 patronen als startbestand voor je beslisregels | Beschikbaar |
| `data/README.md` | Overige datasets, zoals de IBD-lijst met kritieke processen van gemeenten | In voorbereiding |
| `casussen/` | Geanonimiseerde inkoopcasussen om je tool op te demonstreren | In voorbereiding |

## Belangrijk om te weten

- Het classificatiemodel bepaalt nog geen soevereiniteitsniveau. Die vertaling is aan jullie: adviseer per patroon een niveau en onderbouw het. De SEAL-schaal uit het EU Cloud Sovereignty Framework kan als referentie dienen.
- Minimumeisen uit wet- en regelgeving (zie `docs/bronnen.md`) vormen de ondergrens.
- Gebruik AI gerust voor uitleg of de vragenflow, maar laat de classificatie niet door een taalmodel bepalen. De regels moeten te lezen en te testen zijn.

## Open source

Alle code, regels en documentatie die tijdens de hackathon ontstaan, worden open source gepubliceerd.

## Vragen

hack@govtechnl.nl
