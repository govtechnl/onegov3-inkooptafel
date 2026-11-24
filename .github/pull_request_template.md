## Summary

<!-- One paragraph: what does this PR add or change? -->

## Type of contribution

- [ ] **Hackathon team submission** (one PR per team, fork, PR into `main`)
- [ ] Starter-repo improvement (docs, data, tooling, CI)
- [ ] Bug fix
- [ ] Other (describe)

---

## For hackathon team submissions

### Team

- **Team name:**
- **Members:**
- **Folder:** `submissions/<team-name>/`
- **Angle:** [ ] Rules first [ ] User first [ ] Bonus (open-source viability / maturity model)

### ✅ Must checklist (jury blocking)

- [ ] **M1** Working tool that classifies a system on business criticality and data sensitivity, based on the supplied model.
- [ ] **M2** Per pattern, an advised sovereignty level with a justification traceable to the model and sources.
- [ ] **M3** The tool produces requirements or award criteria a buyer can use in tender documents.
- [ ] **M4** Decision rules are explicit in code or configuration (rules-as-code), not hidden in a prompt.
- [ ] **M5** Code and rules open source under an OSI-approved licence; rules and docs under CC BY 4.0 or CC0. See [`CONTRIBUTING.md`](../CONTRIBUTING.md#licensing-of-contributions).

### ⭐ Should evidence (linked in the PR body)

- [ ] **S1** Traceability: user sees why a system falls in a pattern and which source each requirement comes from.
- [ ] **S2** Question flow usable by a non-technical user in about five minutes.
- [ ] **S3** Demonstrated on a supplied procurement case (worked example included).
- [ ] **S4** Requirements align with existing frameworks and respect minimum requirements from law and regulation.
- [ ] **S5** Rules maintainable separately from the interface.

### Hygiene

- [ ] Tests for the decision rules are included and pass.
- [ ] No confidential tender documents, prices or supplier information.
- [ ] No judgements about named suppliers or products.
- [ ] If an LLM is used: where, why, and which model is described below.

### Sources used

<!-- One bullet per source id from data/sources.yaml, plus any you added with origin: team -->

### Reproduction

```bash
# Single command (or short sequence) that runs your tool from a clean checkout:
```

### Pitch artefacts

- [ ] Pitch deck (max. 10 slides), link or attachment
- [ ] Worked procurement case, file in the PR

---

## For starter-repo improvements

- [ ] Data, docs and README updated together.
- [ ] `ruff check .` and `pytest -v` pass locally (`tooling/`).
- [ ] CI ([`.github/workflows/validate.yml`](workflows/validate.yml)) is green.
- [ ] Related issue: #
