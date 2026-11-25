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

There is plenty of policy on digital autonomy, but it disappears at the procurement table because nobody can make it concrete. Not every system needs the same level of autonomy. The **classificatietoets**, in use in an Amsterdam pilot, takes a process down to its critical data and scores **process criticality** and **availability, integrity and confidentiality (BIV)**. What is missing is the step from that outcome to a **sovereignty level** and **requirements a buyer can put in the tender**.

**How do we turn that toets into a tool buyers and information managers can use tomorrow: classify a system, advise a well-founded sovereignty level, and get requirements that go straight into the tender documents?**

The full brief is in [CHALLENGE.md](CHALLENGE.md). New teams start with [START_HERE.md](START_HERE.md).

## What's in here

| Path | Purpose | Status |
|---|---|---|
| [CHALLENGE.md](CHALLENGE.md) | Full challenge brief (English working translation of the Dutch original) | Available |
| [START_HERE.md](START_HERE.md) | Step-by-step start for teams | Available |
| [docs/](docs/) | Classificatietoets, sovereignty levels, sources, rules-as-code guidance, procurement context, personas, scenarios, judging criteria, glossary | Available |
| [data/toets.yaml](data/toets.yaml) | The classificatietoets: steps 0-4, process criticality, all BIV questions, scores and decision rules | Available |
| [data/sources.yaml](data/sources.yaml) | Laws, frameworks and guidance with possible minimum requirements | Available (links for most sources; the rest follow) |
| [data/schemas/](data/schemas/) | JSON Schemas for the catalogues, for answers to the toets and for your rules | Available |
| [data/ibd/](data/ibd/) | IBD list of critical processes for municipalities | Being prepared |
| [cases/](cases/) | Procurement cases to demonstrate your tool on | One case available (HenT, Amsterdam); GGD case follows |
| [tooling/](tooling/) | Optional Python starter: the toets as code, a rules engine and PvE renderer, examples, tests | Available |
| [submissions/](submissions/) | Where your team's work goes if you build in a fork of this repository | Empty |
| [resources/](resources/) | Source material as delivered by the challenge owners | Being prepared |

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
```

The tooling is optional. **Teams are free to choose any language and approach**, as long as the decision rules are explicit and testable.

## Important to know

- The toets does **not** give a sovereignty level, and the SEAL level does not follow automatically from BIV: it concerns the concrete service being procured. Designing that step is the core of the challenge.
- Minimum requirements from law and regulation (see [docs/sources.md](docs/sources.md)) form the floor of your advice.
- Use AI for explanation or the question flow if you like, but do not let a language model decide the classification. See [docs/rules-as-code.md](docs/rules-as-code.md).
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
