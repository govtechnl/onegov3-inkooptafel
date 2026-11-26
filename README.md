# OneGov #3 | Van beleid naar inkooptafel

> *From a classification model to requirements that go straight into the tender.*

This repository hosts the challenge brief, supporting documents, machine-readable starter data and optional tooling for challenge 2 of **OneGov #3**, part of the OneGov Hackathon Series hosted by [GovTechNL](https://govtechnl.nl), with challenge owners **DACC** (Digitale Autonomie Competentiecentrum) and **VNG Realisatie**.

- **Theme:** Digital autonomy and sovereignty
- **Date:** 9-10 December 2026
- **Location:** The Hague Tech, Den Haag
- **Challenge owners:** Jacco Brouwer (VNG Realisatie), Thijs Turèl (DACC / AMS Institute)
- **Tech partner:** [GreenPT](https://greenpt.nl/)
- **Community, teams and submissions:** [alkem.io/onegov-hackathon](https://alkem.io/onegov-hackathon)
- **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)
- **Submission deadline:** Thursday 10 December 2026, 14:00, on [Alkemio](https://alkem.io/onegov-hackathon)
- **Programme, prizes, judging and help:** [EVENT.md](EVENT.md)
- **Organised by:** GovTechNL with Digicampus, The Hague Tech, VNG Realisatie, Provincie Zuid-Holland, Platform AI & Overheid and Gemeente Den Haag

## The challenge in one paragraph

There is plenty of policy on digital autonomy, but it disappears at the procurement table because nobody can make it concrete. Not every system needs the same level of autonomy. The DACC's procurement-requirements tool determines an indicative **SEAL level** from a system's criticality and data classification, and then shows **every** requirement for that level. What is missing is the step after that: a requirement set that also fits **what is actually being procured**. A small procurement for one module, on a high SEAL level, does not need the full list.

**How do we give a buyer the requirements that fit their procurement: matched not only to the SEAL level, but also to what is being bought, with an explanation for every requirement that is left out?**

The full brief is in [CHALLENGE.md](CHALLENGE.md). New teams start with [START_HERE.md](START_HERE.md).

## What's in here

| Path | Purpose | Status |
|---|---|---|
| [CHALLENGE.md](CHALLENGE.md) | Full challenge brief (English working translation of the Dutch original) | Available |
| [START_HERE.md](START_HERE.md) | Step-by-step start for teams | Available |
| [docs/](docs/) | Requirement libraries and scope, classificatietoets, sovereignty levels, sources, rules-as-code guidance, procurement context, personas, scenarios, judging criteria, glossary | Available |
| [data/toets.yaml](data/toets.yaml) | The classificatietoets: steps 0-4, process criticality, all BIV questions, scores and decision rules | Available |
| [data/sources.yaml](data/sources.yaml) | Laws, frameworks and guidance with possible minimum requirements | Available (links for most sources; the rest follow) |
| [data/schemas/](data/schemas/) | JSON Schemas for the catalogues, answers to the toets, your rules, a requirement library and a procurement scope | Available |
| [data/ibd/](data/ibd/) | IBD list of critical processes for municipalities | Being prepared |
| [cases/](cases/) | Four procurement cases of different scope to demonstrate your tool on | Available |
| [tooling/](tooling/) | Optional Python starter: the toets as code, a rules engine, a scope-based requirement selection, examples, tests | Available |
| [submissions/](submissions/) | Where your team's work goes if you build in a fork of this repository | Empty |
| [resources/](resources/) | Source material as delivered by the challenge owners, including a demo of the DACC procurement-requirements tool | Being prepared |

## Quick start

```bash
cd tooling
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest -v

# Steps 0-4: from answers to a profile (process criticality, B, I, V)
python -m inkooptafel.toets examples/assessment-example.yaml

# From profile to sovereignty advice and requirements (illustrative rules, not advice)
python -m inkooptafel.advies examples/assessment-example.yaml --rules examples/example-rules.yaml

# From SEAL level and scope to a focused requirement set (illustrative library, not advice)
python -m inkooptafel.selectie examples/scope-example.yaml --library examples/example-requirements.yaml
```

The tooling is optional. **Teams are free to choose any language and approach**, as long as the decision rules are explicit and testable.

## Important to know

- The core of the challenge is step 03: from a SEAL level **and** the scope of the procurement to a focused requirement set, with a reason for every requirement left out. See [docs/requirements.md](docs/requirements.md).
- The DACC's own requirement library is **not** shared with teams. Build your library from public sources; the jury uses the DACC library as a checklist.
- Material shared on Alkemio only stays out of your repository, prompts and pitch deck.
- Minimum requirements from law and regulation (see [docs/sources.md](docs/sources.md)) form the floor of your advice.
- A language model may help find requirements in public sources, as long as each keeps its source. Do not let it decide the SEAL level, the classification or the selection. See [docs/rules-as-code.md](docs/rules-as-code.md).
- This repository contains no confidential tender documents or supplier information. Keep it that way in your submission.

## Licensing

See [CONTRIBUTING.md](CONTRIBUTING.md#licensing-of-contributions) for the canonical rule. In short:

- This **starter repo** ships under **Apache-2.0** (code, see [LICENSE](LICENSE)) and **CC BY 4.0** (data, docs, challenge text, see [LICENSE-DATA](LICENSE-DATA)).
- **Team submissions** must be open source under an **OSI-approved licence** for code (Apache-2.0, MIT, EUPL-1.2, ...) and an open licence (CC BY 4.0 recommended, CC0 accepted) for rules, data and documentation.
- Laws, frameworks and guidance listed in `data/sources.yaml` keep their own terms. This repo links to them; it does not redistribute them.

## Contributing

Issues and pull requests are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). Team submissions go through [Alkemio](https://alkem.io/onegov-hackathon); a Pull Request from your team is welcome but optional.

## Submission

Submit on [Alkemio](https://alkem.io/onegov-hackathon) before **Thursday 10 December 2026, 14:00**, with a link to your public repository (your fork or your own), a short explanation of your approach, assumptions and limitations, and your pitch deck. A Pull Request into this repository is optional. See [CHALLENGE.md](CHALLENGE.md#submission) and [EVENT.md](EVENT.md#submission).

## Disclaimer

Tools and rules built during the hackathon are prototypes, not legal advice and not ready for use in real tenders without further substantive and legal review by the challenge owners.
