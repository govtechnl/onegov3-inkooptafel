# Contributing

Thanks for your interest in the **OneGov #3 | Van beleid naar inkooptafel** challenge repository.

This repo is maintained by **GovTech NL** together with the challenge owners **DACC** and **VNG Realisatie** for the hackathon on **9-10 December 2026** at The Hague Tech. Contributions are welcome from organisers, mentors, participating teams and the wider community.

## Two contribution flows

### 1. Hackathon teams: fork, build, one PR

This is the primary flow during the hackathon.

1. **Fork** this repository to your team's GitHub account and clone the fork.
2. Build your tool and rules in your fork. Put everything team-specific under `submissions/<team-name>/` (see [submissions/README.md](submissions/README.md)).
3. Open **one Pull Request per team** into `main` of `govtechnl/onegov3-inkooptafel`.
4. Use the [pull request template](.github/pull_request_template.md) and tick every Must box.

### 2. Improving the starter repo

- **Add verified links** to [`data/sources.yaml`](data/sources.yaml) (many entries still have `url: null`).
- **Sharpen documentation** under [`docs/`](docs/).
- **Improve the tooling** under [`tooling/`](tooling/).
- **Report issues** using the [issue templates](.github/ISSUE_TEMPLATE/).

## Ground rules

1. **Explicit, testable rules.** The classification and the mapping to a sovereignty level live in code or configuration that can be read and tested without the interface. No decision hidden in a prompt.
2. **Traceable requirements.** Every requirement or award criterion your tool produces points to a source in `data/sources.yaml`. Add sources with `origin: team` if you need more.
3. **No confidential material.** Do not commit non-public tender documents, contracts, supplier quotes, prices or internal documents of any organisation. Cases in this repo are anonymised; keep them that way.
4. **No naming and shaming.** Your tool assesses requirements and patterns, not named suppliers. Example output must not label real companies as compliant or non-compliant.
5. **Open source.** All submitted code and rules are released under the licences below.
6. **Language.** Documentation in this repo is primarily English. Output for buyers (requirements, question flow) may be in Dutch, because that is what goes into Dutch tenders.

## Development workflow

```bash
cd tooling
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
ruff check .
pytest -v
```

CI ([`.github/workflows/validate.yml`](.github/workflows/validate.yml)) runs lint, schema checks and tests on every push and PR. Make sure they pass locally before opening a PR.

## Pull requests

- Keep PRs focused, one logical change per PR (the one-PR-per-team rule is the hackathon exception).
- Update the README, data and docs together when behaviour changes.
- Reference the related issue if there is one.

## Code of Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md) (Contributor Covenant 2.1), including the section on **handling procurement and supplier information**.

## Licensing of contributions

This is the **canonical licensing rule** for the repository. All other documents refer back here.

- This **starter repository** is licensed under **Apache-2.0** for code (see [LICENSE](LICENSE)) and **CC BY 4.0** for data, documentation and challenge text (see [LICENSE-DATA](LICENSE-DATA)).
- **Hackathon team submissions** must be open source under an **OSI-approved licence** for code (Apache-2.0, MIT, EUPL-1.2 or another OSI-approved licence) and an open licence for rules, data and documentation (CC BY 4.0 recommended; CC0 also accepted).
- Code contributed *into this starter repo* is licensed under Apache-2.0; data and documentation under CC BY 4.0.
- Laws, frameworks and guidance referenced in `data/sources.yaml` keep their own terms. Link to them; do not copy protected texts into the repo.

By submitting a contribution you confirm that you have the right to license it under these terms.
