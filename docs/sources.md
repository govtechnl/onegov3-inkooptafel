# Sources

Laws, frameworks and guidance that may contain **minimum requirements for suppliers or data storage**, depending on what is being procured. They form the floor of your advice. Machine-readable version: [`data/sources.yaml`](../data/sources.yaml). Use the ids from that file in your rules.

This is a **first pass** compiled by the challenge owners from the VNG *Uitvoeringsstrategie Cloud* work. It is not exhaustive. Sources without a link are still waiting for the canonical public link; pull requests with verified links are welcome.

## Dutch law

| Id | Source |
|---|---|
| `avg` | [Algemene verordening gegevensbescherming (AVG / GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) |
| `woo` | [Wet open overheid (Woo)](https://wetten.overheid.nl/BWBR0045754) |
| `archiefwet` | [Archiefwet](https://zoek.officielebekendmakingen.nl/stb-2026-149.html) (Archiefwet 2026, replacing the [Archiefwet 1995](https://wetten.overheid.nl/BWBR0007376)) |
| `wwke` | [Wet weerbaarheid kritieke entiteiten (Wwke, Dutch implementation of the EU CER directive)](https://zoek.officielebekendmakingen.nl/kst-36765-3.html) |
| `cbw` | [Cyberbeveiligingswet (Cbw, Dutch implementation of NIS2)](https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet) |

## EU law and frameworks

| Id | Source |
|---|---|
| `data-act` | [Data Act (EU)](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) |
| `ai-act` | [AI Act (EU)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| `dora` | [Digital Operational Resilience Act (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) |
| `cra` | [Cyber Resilience Act (EU)](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| `ecsf` | [European Cloud Sovereignty Framework (SEAL levels) (see [sovereignty-levels.md](sovereignty-levels.md))](https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en?filename=Cloud-Sovereignty-Framework.pdf) |
| `cada` | [Cloud and AI Development Act (CADA, EU proposal)](https://digital-strategy.ec.europa.eu/en/library/proposal-cloud-and-ai-development-act-cada) |

## Architecture, standards and policy

| Id | Source |
|---|---|
| `gemma` | [GEMMA (Gemeentelijke Model Architectuur)](https://www.gemmaonline.nl) |
| `nora` | [NORA (Nederlandse Overheid Referentie Architectuur)](https://www.noraonline.nl) |
| `bio2` | [Baseline Informatiebeveiliging Overheid 2 (BIO2)](https://www.bio-overheid.nl) |
| `rijks-cloudbeleid` | [Rijksbreed cloudbeleid (revision of 3 July 2026)](https://www.tweedekamer.nl/downloads/document?id=2026D35295) |
| `dpia-framework` | DPIA framework |
| `ibd-plc` | [Proportioneel Leveranciers- en Contractmanagement (PLC), IBD](https://www.informatiebeveiligingsdienst.nl/plc-proportioneel-leveranciers-en-contractmanagement/) |

## Guidance

| Id | Source |
|---|---|
| `handreiking-cloud` | [Handreiking Cloud](https://vng.nl/sites/default/files/2026-07/handreiking-cloud-voor-gemeenten.pdf) |
| `handreikingen-ict-sourcing` | [Rijksbrede handreiking IT-sourcing (BZK)](https://www.digitaleoverheid.nl/wp-content/uploads/sites/8/2026/02/85096-BZK-Rijksbrede-Handreiking-IT-sourcing-TG.pdf) |
| `handreiking-exit` | Handreiking exitstrategie en tijdlijnen / technologierisico's |

## Practice

| Id | Source |
|---|---|
| `hent-amsterdam` | [HenT tender (Hosting en Technisch applicatiebeheer), gemeente Amsterdam](https://www.tenderned.nl/aankondigingen/overzicht/391737) |

## Additional resources from the challenge brief

| Id | Source |
|---|---|
| `ibd-bio2-kritieke-processen` | [BIO2 kritieke processen gemeenten (IBD)](https://www.informatiebeveiligingsdienst.nl/product/bio2-kritieke-processen-gemeenten/) |
| `gibit` | [GIBIT (Gemeentelijke Inkoopvoorwaarden bij IT)](https://vng.nl/artikelen/gebruik-vng-model-algemene-inkoopvoorwaarden-of-gibit) |
| `vng-bestek-cloud` | [VNG handreiking Eisen aan gemeentelijke cloudvoorzieningen (with PvE and award criteria, incl. PaaS / IaaS)](https://vng.nl/sites/default/files/2026-07/handreiking-cloud-voor-gemeenten.pdf) |
| `dacc-volwassenheidsmodel` | [Volwassenheidsmodel Digitale Autonomie (DACC)](https://vng.nl/nieuws/nieuw-model-geeft-gemeenten-meer-grip-op-digitale-autonomie) |
| `toezichthouders-digitale-autonomie` | [De route naar digitale autonomie (position paper ACM, AFM, AP, DNB and RDI)](https://www.acm.nl/system/files/documents/de-route-naar-digitale-autonomie.pdf) |
| `quickscan-soevereiniteit` | [Quick scan soevereiniteit (Gemeente Venlo / VNG)](https://vng.nl/artikelen/digitale-autonomie-wat-kunnen-gemeenten-nu-al-doen) |
| `bzk-referentiekader` | Referentiekader digitale autonomie (BZK) |
| `ams-inkooptool-lijst` | List from the prototype procurement tool (AMS Institute / Amsterdam) |

## How to work with these sources

- **Do not let an LLM decide what a law requires.** Read the relevant article or ask a mentor, then encode the requirement as an explicit rule with its `source`. An LLM may help you *find* candidate passages; a person checks them.
- **Cite precisely where you can.** A requirement that points to an article or section is stronger than one that points to a whole law. Use the optional `notes` field.
- **Add what is missing.** Found a source that sets a minimum requirement? Add it to `data/sources.yaml` with `origin: team`.
