# OneGov #3 | Van beleid naar inkooptafel

> *From a classification model to requirements that go straight into the tender.*

This repository hosts the challenge brief, supporting documents, machine-readable starter data and optional tooling for challenge 2 of **OneGov #3**, part of the OneGov Hackathon Series hosted by [GovTech NL](https://govtechnl.nl), with challenge owners **DACC** (Digitale Autonomie Competentiecentrum) and **VNG Realisatie**.

- **Theme:** Digital autonomy and sovereignty
- **Date:** 9-10 December 2026
- **Location:** The Hague Tech, Den Haag
- **Challenge owners:** Jacco Brouwer (VNG Realisatie), Thijs Turel (DACC / AMS Institute)
- **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

## The challenge in one paragraph

There is plenty of policy on digital autonomy, but it disappears at the procurement table because nobody can make it concrete. Not every system needs the same level of autonomy. A classification model combines the **business criticality** of a system with the **sensitivity of its data** into one of ten patterns. What is missing is the step from pattern to **sovereignty level** to **requirements a buyer can put in the tender**.

**How do we turn that model into a tool buyers and information managers can use tomorrow: classify a system, advise a well-founded sovereignty level, and get requirements that go straight into the tender documents?**

The full brief is in [CHALLENGE.md](CHALLENGE.md). New teams start with [START_HERE.md](START_HERE.md).

## What's in here

| Path | Purpose | Status |
|---|---|---|
| [CHALLENGE.md](CHALLENGE.md) | Full challenge brief (English working translation of the Dutch original) | Available |
| [START_HERE.md](START_HERE.md) | Step-by-step start for teams | Available |
| [docs/](docs/) | Classification model, sovereignty levels, sources, rules-as-code guidance, procurement context, personas, scenarios, judging criteria, glossary | Available |
| [data/classification.yaml](data/classification.yaml) | The two axes of the classification model | Available (working version) |
| [data/patterns.yaml](data/patterns.yaml) | The 10 patterns, with empty fields for level, rationale and requirements | Available, to be filled in by teams |
| [data/sources.yaml](data/sources.yaml) | Laws, frameworks and guidance with possible minimum requirements | Available (links being added) |
| [data/schemas/](data/schemas/) | JSON Schemas for all catalogues | Available |
| [data/ibd/](data/ibd/) | IBD list of critical processes for municipalities | Being prepared |
| [cases/](cases/) | Anonymised procurement cases to demonstrate your tool on | Being prepared |
| [tooling/](tooling/) | Optional Python starter: catalogue validation, classifier, PvE renderer, example question flow, tests | Available |
| [submissions/](submissions/) | Where your team's work lands in your Pull Request | Empty |
| [resources/](resources/) | Source material as delivered by the challenge owners | Being prepared |

## Quick start

```bash
cd tooling
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest -v

# Which pattern is a business-critical system with personal data?
python -m inkooptafel.classify --kritikaliteit bedrijfskritiek --gegevens persoonsgegevens

# What does a filled-in PvE fragment look like? (illustrative example, not advice)
python -m inkooptafel.pve P03 --patterns examples/example-patterns.yaml
```

The tooling is optional. **Teams are free to choose any language and approach**, as long as the decision rules are explicit and testable.

## Important to know

- The classification model does **not** yet map patterns to a sovereignty level. That mapping is the core of the challenge.
- Minimum requirements from law and regulation (see [docs/sources.md](docs/sources.md)) form the floor of your advice.
- Use AI for explanation or the question flow if you like, but do not let a language model decide the classification. See [docs/rules-as-code.md](docs/rules-as-code.md).
- This repository contains no confidential tender documents or supplier information. Keep it that way in your submission.

## Licensing

See [CONTRIBUTING.md](CONTRIBUTING.md#licensing-of-contributions) for the canonical rule. In short:

- This **starter repo** ships under **Apache-2.0** (code, see [LICENSE](LICENSE)) and **CC BY 4.0** (data, docs, challenge text, see [LICENSE-DATA](LICENSE-DATA)).
- **Team submissions** must be open source under an **OSI-approved licence** for code (Apache-2.0, MIT, EUPL-1.2, ...) and an open licence (CC BY 4.0 recommended, CC0 accepted) for rules, data and documentation.
- Laws, frameworks and guidance listed in `data/sources.yaml` keep their own terms. This repo links to them; it does not redistribute them.

## Contributing

Issues and pull requests are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). During the hackathon the rule is **one PR per team**.

## Submission

Submissions go through **Alkemio**. Each team submits a link to its Pull Request on this repo, the worked procurement case, and the pitch deck. See [CHALLENGE.md](CHALLENGE.md#submission).

## Disclaimer

Tools and rules built during the hackathon are prototypes, not legal advice and not ready for use in real tenders without further substantive and legal review by the challenge owners.
