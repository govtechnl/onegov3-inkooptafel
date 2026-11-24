# Sources

Laws, frameworks and guidance that may contain **minimum requirements for suppliers or data storage**, depending on what is being procured. They form the floor of your advice. Machine-readable version: [`data/sources.yaml`](../data/sources.yaml). Use the ids from that file in your rules.

This is a **first pass** compiled by the challenge owners from the VNG *Uitvoeringsstrategie Cloud* work. It is not exhaustive. Links are being added; pull requests with verified public links are welcome.

## Dutch law

| Id | Source |
|---|---|
| `avg` | Algemene verordening gegevensbescherming (AVG / GDPR) |
| `woo` | Wet open overheid (Woo) |
| `archiefwet` | Archiefwet |
| `wwke` | WWKE |
| `cbw` | Cyberbeveiligingswet (Dutch implementation of NIS2) |

## EU law and frameworks

| Id | Source |
|---|---|
| `data-act` | Data Act |
| `ai-act` | AI Act |
| `dora` | Digital Operational Resilience Act (DORA) |
| `cra` | Cyber Resilience Act |
| `ecsf` | European Cloud Sovereignty Framework (see [sovereignty-levels.md](sovereignty-levels.md)) |
| `cada` | CaDa (in development) |

## Architecture, standards and policy

| Id | Source |
|---|---|
| `gemma` | GEMMA |
| `nora` | NORA |
| `bio2` | BIO2 |
| `rijks-cloudbeleid` | Rijksbreed cloudbeleid (revised) |
| `dpia-framework` | DPIA framework |
| `ibd-plc` | [Proportioneel Leveranciers- en Contractmanagement (IBD)](https://www.informatiebeveiligingsdienst.nl/plc-proportioneel-leveranciers-en-contractmanagement/) |

## Guidance

| Id | Source |
|---|---|
| `handreiking-cloud` | Handreiking Cloud (source of the mitigating measures per pattern) |
| `handreikingen-ict-sourcing` | Handreikingen ICT Sourcing |
| `handreiking-exit` | Handreiking exitstrategie en tijdlijnen / technologierisico's |

## Practice

| Id | Source |
|---|---|
| `hent-amsterdam` | HenT tender (Hosting en Technisch applicatiebeheer), gemeente Amsterdam |

## Other resources from the challenge brief

| Id | Source |
|---|---|
| `ibd-bio2-kritieke-processen` | [BIO2 kritieke processen gemeenten (IBD)](https://www.informatiebeveiligingsdienst.nl/product/bio2-kritieke-processen-gemeenten/) |
| `gibit` | [GIBIT, Gemeentelijke Inkoopvoorwaarden bij IT](https://vng.nl/artikelen/gebruik-vng-model-algemene-inkoopvoorwaarden-of-gibit) |
| `vng-bestek-cloud` | [VNG bestek cloud-inkoop (PaaS / IaaS)](https://vng.nl/artikelen/digitale-autonomie-wat-kunnen-gemeenten-nu-al-doen) |
| `dacc-volwassenheidsmodel` | [Volwassenheidsmodel Digitale Autonomie (DACC)](https://vng.nl/nieuws/nieuw-model-geeft-gemeenten-meer-grip-op-digitale-autonomie) |

## How to work with these sources

- **Do not let an LLM decide what a law requires.** Read the relevant article or ask a mentor, then encode the requirement as an explicit rule with its `source`. An LLM may help you *find* candidate passages; a person checks them.
- **Cite precisely where you can.** A requirement that points to an article or section is stronger than one that points to a whole law. Use the optional `notes` field.
- **Add what is missing.** Found a source that sets a minimum requirement? Add it to `data/sources.yaml` with `origin: team`.
