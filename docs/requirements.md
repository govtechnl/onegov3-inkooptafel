# Requirement libraries and scope

Step 03 is the core of the challenge: from a SEAL level **and** the scope of the procurement to a focused set of requirements.

## What exists today

The DACC has a procurement-requirements tool. The user determines an indicative SEAL level with a matrix of criticality (K1-K4) and data classification (D1-D4), and the tool then shows **all** requirements for that level. The buyer has to strike out what does not fit their procurement themselves. A demo of that tool, without the requirements, follows in [`resources/`](../resources/).

That works for a large procurement. It does not work for a small one: a tender for one module or for licences only, on a high SEAL level, should not get every requirement for that level.

## The DACC requirement library is not shared

The DACC's own requirement library is not part of this repository and is not shared with teams. It contains strategically sensitive material: suppliers could tune their story to it, which leads to "sovereignty washing". The challenge owners use it as a **checklist for the jury**: they compare the requirement sets teams produce with it.

So you build your own library, from public sources. That is part of the challenge.

## Building a library from public sources

Good starting points, all in [`data/sources.yaml`](../data/sources.yaml):

- `ecsf`: the EU Cloud Sovereignty Framework, with its eight sovereignty objectives and SEAL levels.
- `vng-bestek-cloud`: the VNG guidance for municipal cloud procurement, with a programme of requirements and award criteria.
- `gibit`: the municipal IT purchasing terms.
- `handreiking-exit`, `handreikingen-ict-sourcing`: exit and sourcing guidance.
- `pianoo`: PIANOo, the Dutch public procurement expertise centre.
- `dictu-toetsingsinstrument`: DICTU's assessment instrument for sovereignty of cloud services.
- Laws such as `avg`, `cbw`, `data-act` and `ai-act` for the floor.

You may use a language model to find, extract and group candidate requirements from these sources. Two conditions: every requirement keeps a link to the source it came from, and a language model does not decide the SEAL level or the classification.

## Starter format

The repository ships a starter format. You may extend it or use your own, as long as the selection is explicit and testable.

- **Library:** [`data/schemas/requirements.schema.json`](../data/schemas/requirements.schema.json). Each requirement has the SEAL levels it belongs to, the sovereignty objectives it serves, a type (requirement or award criterion), a text, a source and `applies_when`: the scope conditions under which it applies.
- **Scope:** [`data/schemas/scope.schema.json`](../data/schemas/scope.schema.json). The chosen SEAL level plus yes/no facts about what is being procured, such as `persoonsgegevens`, `hooggerubriceerd`, `leverancier_beheert_dienst`, `cloud` and `ai`. These flag names are a starting vocabulary, not a standard. Finding the right facts to ask is part of the design.
- **Examples:** [`tooling/examples/example-requirements.yaml`](../tooling/examples/example-requirements.yaml) and [`tooling/examples/scope-example.yaml`](../tooling/examples/scope-example.yaml). Illustrative only, marked `VOORBEELD`.

Run the starter selection:

```bash
cd tooling
python -m inkooptafel.selectie examples/scope-example.yaml --library examples/example-requirements.yaml
```

It prints the selected requirements and, for every requirement it leaves out, the reason.

## What makes a good selection

- **Fits the scope.** Two procurements on the same SEAL level can need very different sets. The cases in [`cases/`](../cases/) differ on purpose.
- **Explains what it leaves out.** A buyer must be able to defend in a tender why a requirement is not there.
- **Proportionate.** See [procurement-context.md](procurement-context.md).
- **Traceable.** Every requirement links to its source.
