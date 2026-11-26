# Start Here (Hackathon Teams)

If you are starting the challenge now, follow this order.

## 1) Understand the scope (10 min)

- Read [CHALLENGE.md](CHALLENGE.md).
- Skim [docs/judging-criteria.md](docs/judging-criteria.md). Every Must is blocking.
- Read [docs/requirements.md](docs/requirements.md): what exists today, what is missing, and the starter format.
- Skim [cases/](cases/): four procurements of different scope.

## 2) Pick your angle (10 min)

Steps 01 (classify) and 02 (SEAL level) exist already; keep them short. The core is step 03: a requirement set that fits the SEAL level and the scope. Choose where you go deepest:

- **Library first:** build a requirement library from public sources, each requirement with its source and the scope conditions under which it applies. Start with [docs/requirements.md](docs/requirements.md) and [docs/sources.md](docs/sources.md).
- **Selection first:** find the facts about a procurement that decide which requirements apply, and explain every requirement left out. Start with the cases in [cases/](cases/).
- **User first:** a question flow a buyer completes in five minutes, and output they can paste into a tender. Start with [docs/personas.md](docs/personas.md) and [docs/scenarios.md](docs/scenarios.md).
- **Bonus:** open-source viability, or linking to the DACC maturity model. See the Could criteria.

Make sure your team has at least one person who knows procurement or information security. Mentors can help.

## 3) Set up (10 min)

Fork this repository, then:

```bash
cd tooling
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest -v
```

Using another language? Fine. Keep the data files in `data/` as your input and make sure your rules are testable.

## 4) Make one profile work end-to-end (first hours)

- Run the selection example: `python -m inkooptafel.selectie examples/scope-example.yaml --library examples/example-requirements.yaml`.
- Write your first library in `submissions/<team-name>/requirements.yaml` and scopes for two cases of different size, in the format of [docs/requirements.md](docs/requirements.md).
- Optional: run the toets example: `python -m inkooptafel.toets examples/assessment-example.yaml`.
- Write your first rules file in `submissions/<team-name>/rules.yaml`, using the format of [tooling/examples/example-rules.yaml](tooling/examples/example-rules.yaml). That file is an illustration, not advice.
- Add a SEAL minimum per objective and two or three requirements, each with a `source` from [data/sources.yaml](data/sources.yaml).
- Render it: `python -m inkooptafel.advies examples/assessment-example.yaml --rules ../submissions/<team-name>/rules.yaml`.

## 5) Scale out and demo

- Cover cases of different scope (licences only, one module, a full application, hosting), or explain in your pitch what is out of scope.
- Build the question flow and the export.
- Run your tool on a case from [cases/](cases/).

## 6) Keep your submission valid

- Selection explicit and testable; no SEAL level, classification or selection by a language model.
- Material shared on Alkemio only stays out of your repository, prompts and pitch deck.
- Every requirement traceable to a source.
- Code and rules open source; put your work in `submissions/<team-name>/`.
- No confidential tender documents or supplier information.
- Keep your repository public with an open source licence, and submit on [Alkemio](https://alkem.io/onegov-hackathon) before **Thursday 10 December, 14:00**. A Pull Request here is optional.
