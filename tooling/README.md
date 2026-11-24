# Tooling (optional Python starter)

A small, deterministic starter. Use it, extend it, or ignore it and build in any language you like. The only hard rule is that your decision rules are explicit and testable.

## Install

```bash
cd tooling
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest -v
```

## What is in here

| Path | What it does |
|---|---|
| `inkooptafel/catalog.py` | Loads `data/*.yaml` and validates it against `data/schemas/` |
| `inkooptafel/classify.py` | Maps the two axis values to one of the 10 patterns. No AI, just a lookup |
| `inkooptafel/pve.py` | Renders a programme-of-requirements (PvE) fragment for a pattern, with a source per requirement |
| `examples/01_vragenflow.py` | Minimal yes/no question flow, from answers to pattern to PvE fragment |
| `examples/example-patterns.yaml` | One illustrative filled-in pattern (P03). **Example only, not advice** |
| `tests/` | Schema checks, coverage of all 10 combinations, source references, classifier tests |

## Try it

```bash
python -m inkooptafel.classify --kritikaliteit bedrijfskritiek --gegevens persoonsgegevens
python -m inkooptafel.pve P03 --patterns examples/example-patterns.yaml
python examples/01_vragenflow.py --patterns examples/example-patterns.yaml
```
