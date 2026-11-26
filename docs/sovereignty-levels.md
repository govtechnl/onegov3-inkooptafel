# Sovereignty levels

The classificatietoets does not assign a sovereignty level. The DACC's procurement-requirements tool gives an indicative SEAL level from a matrix of criticality and data classification; use that as the input to step 03 (see [requirements.md](requirements.md)). This page explains the SEAL scale and what to keep in mind. You may still argue for a different level for a specific case, if you justify it.

## Reference: the EU Cloud Sovereignty Framework (SEAL)

The European Commission's **Cloud Sovereignty Framework** (version 1.2.1, October 2025) is a procurement framework for cloud services. It defines **eight sovereignty objectives** and a scale of **Sovereignty Effectiveness Assurance Levels (SEAL)**.

### Eight objectives

| Id | Objective |
|---|---|
| SOV-1 | Strategic sovereignty |
| SOV-2 | Legal and jurisdictional sovereignty |
| SOV-3 | Data and AI sovereignty |
| SOV-4 | Operational sovereignty |
| SOV-5 | Supply chain sovereignty |
| SOV-6 | Technology sovereignty |
| SOV-7 | Security and compliance sovereignty |
| SOV-8 | Environmental sustainability |

### SEAL levels

| Level | Name | In short |
|---|---|---|
| SEAL-0 | No sovereignty | Service, technology or operations under exclusive control of non-EU parties |
| SEAL-1 | Jurisdictional sovereignty | EU law formally applies, with limited practical enforceability |
| SEAL-2 | Data sovereignty | EU law applies and is enforceable, but material non-EU dependencies remain |
| SEAL-3 | Digital resilience | Meaningful EU influence, with marginal non-EU control |
| SEAL-4 | Full digital sovereignty | Technology and operations under full EU control, subject only to EU law |

### How the framework is used in a tender

- The contracting authority sets a **minimum SEAL per objective**. Offers that do not meet the minimum on every objective are rejected.
- On top of that, a **weighted sovereignty score** can be used as an award criterion to compare offers that pass.

Source: [Cloud Sovereignty Framework (European Commission)](https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en?filename=Cloud-Sovereignty-Framework.pdf).

### A Dutch reference point

The exploration *Verkenning Soevereine Cloud* (Gartner for the Ministry of the Interior, April 2026) sets SEAL-4 as the baseline for the national sovereign-cloud programme, uniformly, for information up to *Departementaal Vertrouwelijk*. That is exactly the kind of one-size-fits-all level this challenge wants to differentiate per pattern. Source: [tweedekamer.nl, 2026D34381](https://www.tweedekamer.nl/downloads/document?id=2026D34381).

## Guidance for your advice

- **BIV is input, not the answer.** The toets tells you what is critical and how sensitive it is. Add what you need to know about the service: where it runs, who operates it, which jurisdiction applies, how exit works.

- **Per objective, not only overall.** An outcome may need a high level on data and legal sovereignty but a lower one on supply chain. The SEAL model allows that; your tool can too.
- **Minimum requirements are the floor.** If a law or framework in [`data/sources.yaml`](../data/sources.yaml) sets a hard requirement for a situation, your level cannot go below it.
- **Proportionate, not maximal.** A higher level narrows the market and raises costs. Explain why a level is needed, not only that it is safer. See [procurement-context.md](procurement-context.md).
- **Make it testable.** Write tests that pin your choices, for example: "a higher V never gives a lower level on SOV-3" or "every outcome with personal data has at least one requirement sourced from `avg`".
- **You may use another scale.** If you think SEAL is the wrong fit for municipal SaaS, propose a better one and justify it.

## Where to record it

In your fork, write your rules under `submissions/<team-name>/` in the format of [`data/schemas/rules.schema.json`](../data/schemas/rules.schema.json): conditions on the profile, a SEAL minimum per objective, a rationale and requirements.
