# Rules-as-code: how to approach it

The jury wants decision rules that a buyer, a lawyer and a developer can all read, test and change. This page gives practical guidance. You are free to choose your own stack.

## What "rules-as-code" means here

- The logic that decides the **profile**, the **advised level** and the **requirements** lives in code or configuration, separate from the user interface.
- Every rule is **deterministic**: the same answers always give the same outcome.
- Every rule is **testable** without clicking through the interface.
- Every outcome is **traceable**: the tool can show which question, which rule and which source led to it.

## Three layers that work well

| Layer | Content | In this repo |
|---|---|---|
| 1. Toets | Answers to a profile: proceskritikaliteit, B, I, V | `data/toets.yaml` and `tooling/inkooptafel/toets.py` (done for you) |
| 2. Advice | Profile (plus facts about the service) to an advised sovereignty level, for example a SEAL minimum per objective | **Your rules**, format in `data/schemas/rules.schema.json` |
| 3. Requirements | Advice to requirements and award criteria, each with a source | **Your rules**, rendered by `tooling/inkooptafel/advies.py` |

Keep layers 2 and 3 in data files rather than in code, so they can be updated when policy changes without rebuilding the tool. That is a Should criterion. The example in `tooling/examples/example-rules.yaml` shows the format; it is not advice.

## Encoding the toets correctly

The toets has a few rules that are easy to get wrong:

- **B and I: highest score wins.** Not the sum, not the average.
- **V: decision rules in order.** Geheim if V1, V2, V3 or V7 is "ja"; otherwise Vertrouwelijk if V4, V5 or V6 is "ja"; Openbaar only if V1 to V7 are "nee" and V8 is "ja".
- **"Weet ik niet" is not "nee".** If an unknown answer could change the level, the outcome is unknown until someone finds out.
- **Kern versus Ondersteunend is a judgement.** Let the user record the process owner's choice; do not derive it.

`tooling/inkooptafel/toets.py` implements these rules and `tooling/tests/` tests them.

## Options for a rules engine

You do not need one; plain data files plus a small interpreter are enough. If you want to use an existing approach, decision tables (DMN) or a policy language are common in government rules-as-code work. Choose what your team can explain in a three-minute pitch.

## Where AI fits, and where it does not

**Fine:**

- Explaining an outcome in plain language for a buyer or a board.
- Helping a user answer a question ("does a youth-care system process special categories of personal data?"), as long as the user confirms the answer.
- Suggesting candidate passages in a law for a human to check.

**Not fine:**

- Letting a model decide the profile, the level or a requirement.
- Generating requirement text that is not stored and versioned in your rules.

If you use an LLM, the [GreenPT API](integrations/greenpt-api.md) runs on European infrastructure. Describe in your PR where and why you use it.

## Test ideas

- The toets rules (already in `tooling/tests/`).
- Monotonicity: a higher B, I or V never gives a lower advised level.
- Every profile with V Vertrouwelijk or Geheim gets at least one requirement sourced from `avg` when personal data are involved.
- Every requirement has a source that exists in `data/sources.yaml`.
- A worked case gives the same output twice in a row.
