# Scenarios

> **Why this file exists.** These scenarios turn the brief into concrete, demo-able user stories. Each is small enough to prototype in a few hours; together they cover the Must and Should criteria.
>
> **How to use.** Pick one or two as your demo spine. You are not required to implement them. The systems are generic examples; your rules decide the outcome, not this file.

---

## 1. Five-minute classification

**Persona:** Sanne.
**Goal:** Sanne answers a handful of plain-language questions about the *zaaksysteem* she is tendering and gets a profile, an advised level and a short justification.
**Covers:** M1, M2, S1, S2.
**Bonus:** questions Sanne cannot answer herself can be forwarded to Ahmed with one click.

## 2. From profile to PvE fragment

**Persona:** Sanne.
**Goal:** Export the requirements and award criteria for the classified system as a document she can paste into the tender, each with its source and type (requirement or award criterion).
**Covers:** M3, S1, S4.
**Starter:** `python -m inkooptafel.advies <assessment> --rules <your-rules>`.

## 3. Same answers, same outcome

**Persona:** Ahmed, with the CISO looking over his shoulder.
**Goal:** Show that two people classifying the same system get the same profile and level, and that the tool can explain every step.
**Covers:** M4, S1.
**Demo trick:** run your rule tests live.

## 4. A public website versus a youth-care file

**Persona:** Ahmed.
**Goal:** Classify two very different systems, for example the CMS of the municipal website and a youth-care case file, and show that the advised levels and requirements differ in a proportionate, explainable way.
**Covers:** M2, S1; shows the "not everything has to be sovereign" point.

## 5. Classifying the landscape

**Persona:** Ahmed.
**Goal:** Upload a simple list of systems (name, process, data types) and get a profile per process, with the ones that need attention first.
**Covers:** S2, S5; useful for the joint-procurement bonus.

## 6. Policy changes, the tool does not break

**Persona:** whoever maintains the rules after the hackathon.
**Goal:** A new law adds a minimum requirement for one kind of outcome. Show that you change one data file, the tests tell you what changed, and the tool picks it up without code changes.
**Covers:** S5.

## 7. Worked case

**Persona:** Sanne.
**Goal:** Run one of the supplied cases in [`cases/`](../cases/) end-to-end: classification, advised level, requirements, and a comparison with what was actually asked in the original tender.
**Covers:** S3.

## 8. Is this open-source alternative viable? (bonus)

**Persona:** Ahmed.
**Goal:** For an open-source alternative to a system, show indicators of viability: number of active contributors, spread across organisations and countries, activity over time.
**Covers:** Could, open-source viability.
**Note:** use public data (for example a repository's public contribution history) and be careful with conclusions; do not present it as a verdict.

## 9. Process level meets system level (bonus)

**Persona:** Ahmed.
**Goal:** Link the outcome of the DACC *Volwassenheidsmodel Digitale Autonomie* for a primary process to the systems that support it.
**Covers:** Could, maturity model link.
