# Start Here (Hackathon Teams)

If you are starting the challenge now, follow this order.

## 1) Understand the scope (10 min)

- Read [CHALLENGE.md](CHALLENGE.md).
- Skim [docs/judging-criteria.md](docs/judging-criteria.md). Every Must is blocking.
- Read [docs/classification-model.md](docs/classification-model.md): the classificatietoets in five steps, and what is missing.

## 2) Pick your angle (10 min)

All teams cover the three steps (classify, advise a level, produce requirements). Choose where you go deepest:

- **Rules first:** a well-founded level per toets outcome, with traceable minimum requirements from law and regulation. Start with [docs/sovereignty-levels.md](docs/sovereignty-levels.md) and [docs/sources.md](docs/sources.md).
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

- Run the example: `python -m inkooptafel.toets examples/assessment-example.yaml`.
- Write your first rules file in `submissions/<team-name>/rules.yaml`, using the format of [tooling/examples/example-rules.yaml](tooling/examples/example-rules.yaml). That file is an illustration, not advice.
- Add a SEAL minimum per objective and two or three requirements, each with a `source` from [data/sources.yaml](data/sources.yaml).
- Render it: `python -m inkooptafel.advies examples/assessment-example.yaml --rules ../submissions/<team-name>/rules.yaml`.

## 5) Scale out and demo

- Cover the range of outcomes (low and high B, I and V; with and without supplier dependency), or explain in your pitch what is out of scope.
- Build the question flow and the export.
- Run your tool on a case from [cases/](cases/).

## 6) Keep your submission valid

- Rules explicit and testable; no classification by a language model.
- Every requirement traceable to a source.
- Code and rules open source; put your work in `submissions/<team-name>/`.
- No confidential tender documents or supplier information.
- Keep your repository public with an open source licence, and submit on [Alkemio](https://alkem.io/onegov-hackathon) before **Thursday 10 December, 14:00**. A Pull Request here is optional.
