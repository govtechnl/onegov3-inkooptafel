# Rules-as-code: how to approach it

The jury wants decision rules that a buyer, a lawyer and a developer can all read, test and change. This page gives practical guidance. You are free to choose your own stack.

## What "rules-as-code" means here

- The logic that decides **pattern**, **level** and **requirements** lives in code or configuration, separate from the user interface.
- Every rule is **deterministic**: the same answers always give the same outcome.
- Every rule is **testable** without clicking through the interface.
- Every outcome is **traceable**: the tool can show which rule and which source led to it.

## Three layers that work well

| Layer | Content | Format suggestion |
|---|---|---|
| 1. Classification | Answers to pattern | A lookup table; see `tooling/inkooptafel/classify.py` |
| 2. Level | Pattern to advised sovereignty level (optionally per SEAL objective) | A decision table in YAML or JSON |
| 3. Requirements | Pattern and level to requirements and award criteria, each with a source | A requirements catalogue in YAML or JSON |

Keep layer 2 and 3 in data files rather than in code, so they can be updated when policy changes without rebuilding the tool. That is a Should criterion.

## Options for a rules engine

You do not need one; plain data files plus a small interpreter are enough for ten patterns. If you want to use an existing approach, decision tables (DMN) or a policy language are common in government rules-as-code work. Choose what your team can explain in a three-minute pitch.

## Where AI fits, and where it does not

**Fine:**

- Explaining an outcome in plain language for a buyer or a board.
- Helping a user answer a question ("does a jeugdzorg system process special categories of personal data?"), as long as the user confirms the answer.
- Suggesting candidate passages in a law for a human to check.

**Not fine:**

- Letting a model decide the pattern, the level or a requirement.
- Generating requirement text that is not stored and versioned in your rules.

If you use an LLM, the [GreenPT API](integrations/greenpt-api.md) runs on European infrastructure. Describe in your PR where and why you use it.

## Test ideas

- Every combination of axis values maps to exactly one pattern (already in `tooling/tests/`).
- Monotonicity: a more critical or more sensitive pattern never gets a lower level.
- Every pattern with personal data has at least one requirement sourced from `avg`.
- Every requirement has a source that exists in `data/sources.yaml` (already in `tooling/tests/`).
- A worked case gives the same output twice in a row.
