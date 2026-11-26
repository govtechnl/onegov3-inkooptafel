# Tooling (optional Python starter)

A small, deterministic starter. Use it, extend it, or ignore it and build in any language. The only hard rule is that your decision rules are explicit and testable.

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
| `inkooptafel/catalog.py` | Loads `data/*.yaml` and team files, validates them against `data/schemas/` |
| `inkooptafel/toets.py` | The classificatietoets as code: answers in, profile out (proceskritikaliteit, B, I, V). Highest score wins for B and I; decision rules for V |
| `inkooptafel/advies.py` | Evaluates **your** rules on a profile: combined SEAL minimum per objective and a PvE fragment with a source per requirement |
| `examples/assessment-example.yaml` | A filled-in toets for a fictional process |
| `examples/example-rules.yaml` | Three illustrative rules in the rules format. **Example only, not advice** |
| `inkooptafel/selectie.py` | Step 03: from a SEAL level and a scope to a focused requirement set, with a reason for every requirement left out |
| `examples/example-requirements.yaml`, `examples/scope-example.yaml` | An illustrative requirement library and scope. **Example only, not the DACC library** |
| `tests/` | Schema checks, BIV rule tests, an end-to-end example |

## Try it

```bash
# Step 0-4: from answers to a profile
python -m inkooptafel.toets examples/assessment-example.yaml

# The part that does not exist yet: from profile to sovereignty advice and requirements
python -m inkooptafel.advies examples/assessment-example.yaml --rules examples/example-rules.yaml
```

## Where the toets needs human judgement

The code only decides what the questionnaire decides. Two places need a person:

- **Kern versus Ondersteunend** (proceskritikaliteit) is a judgement of the process owner. Without an `oordeel`, the outcome is `beoordeling-nodig`.
- **"Weet ik niet"** on a V question that could change the level gives `onbekend`: find out, do not guess.
