# Data

Machine-readable starter data. YAML is the source of truth; the JSON Schemas in [`schemas/`](schemas/) define the format and CI checks every file against them.

| File | What it holds | Status |
|---|---|---|
| [`classification.yaml`](classification.yaml) | The two axes of the classification model and their values | Available (working version) |
| [`patterns.yaml`](patterns.yaml) | The 10 patterns, with empty fields for advised level, rationale and requirements | Available, to be filled in by teams |
| [`sources.yaml`](sources.yaml) | Laws, frameworks and guidance that may contain minimum requirements | Available (first pass, links being added) |
| [`ibd/`](ibd/) | IBD list of critical processes for municipalities | Being prepared |

## Rules for this folder

1. **Ids are stable.** Rules, requirements and tests refer to pattern ids (`P01` to `P10`), axis value ids and source ids. Do not rename them in your fork; add new ones instead.
2. **Every requirement has a source.** The `source` field of a requirement must be an `id` from `sources.yaml`. If you use a source that is not listed, add it with `origin: team`.
3. **Leave the model alone, extend around it.** If you think the classification model is wrong or incomplete, open an issue or describe it in your pitch. Do not silently change `classification.yaml`.

## Validate locally

```bash
cd tooling
pip install -e .[dev]
pytest -v
```
