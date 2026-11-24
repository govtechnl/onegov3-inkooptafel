# Data

Machine-readable starter data. YAML is the source of truth; the JSON Schemas in [`schemas/`](schemas/) define the format and CI checks every file against them.

| File | What it holds | Status |
|---|---|---|
| [`toets.yaml`](toets.yaml) | The classificatietoets: five steps, proceskritikaliteit, all B, I and V questions with scores and decision rules, follow-up topics | Available (version in use in an Amsterdam pilot) |
| [`sources.yaml`](sources.yaml) | Laws, frameworks and guidance that may contain minimum requirements | Available (links being added) |
| [`ibd/`](ibd/) | IBD list of critical processes for municipalities | Being prepared |

## Schemas for team files

| Schema | Use it for |
|---|---|
| [`schemas/assessment.schema.json`](schemas/assessment.schema.json) | Answers to the toets for one process or data element (see `tooling/examples/assessment-example.yaml`) |
| [`schemas/rules.schema.json`](schemas/rules.schema.json) | Your rules: from a toets profile to SEAL minimums and requirements (see `tooling/examples/example-rules.yaml`) |

## Rules for this folder

1. **Ids are stable.** Rules and tests refer to question ids (`B1` to `B7`, `I1` to `I7`, `V1` to `V8`) and source ids. Do not rename them in your fork.
2. **Every requirement has a source.** The `source` of a requirement must be an `id` from `sources.yaml`. Add missing sources with `origin: team`.
3. **Leave the toets alone, build on it.** If you think the toets is wrong or incomplete, open an issue or describe it in your pitch. Do not silently change `toets.yaml`.

## Validate locally

```bash
cd tooling
pip install -e .[dev]
pytest -v
```
