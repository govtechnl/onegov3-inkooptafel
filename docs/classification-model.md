# Classification model

The classification model comes from the work on the *gemeentelijke Uitvoeringsstrategie Cloud* (VNG), together with the DACC. Its purpose: when a municipality buys software or a digital service, it should be able to say how that system classifies and which pattern of sovereignty requirements belongs to it. The model builds on existing frameworks such as the BIO and NIS2, not on something new.

Machine-readable version: [`data/classification.yaml`](../data/classification.yaml) (axes) and [`data/patterns.yaml`](../data/patterns.yaml) (patterns).

## Structure

```
Object         ->  Criteria (two axes)       ->  Pattern        ->  Measures
(system X)         criticality x data class      2 x 5 = 10         mitigating measures
                                                                     (Handreiking Cloud)
```

### Axis 1: criticality of the business process (`kritikaliteit`)

| Id | Dutch | English |
|---|---|---|
| `bedrijfskritiek` | Bedrijfskritiek | Business-critical |
| `niet-kritiek` | Niet kritiek | Not critical |

Use the IBD list of critical processes for municipalities to decide (see [`data/ibd/`](../data/ibd/)).

### Axis 2: data classification (`gegevensclassificatie`)

| Id | Dutch | English |
|---|---|---|
| `openbaar` | Openbaar | Public |
| `wettelijk-gebonden` | Door wet- en regelgeving gebonden | Bound by law and regulation |
| `persoonsgegevens` | Persoonsgegevens | Personal data |
| `bijzondere-persoonsgegevens` | Bijzondere persoonsgegevens | Special categories of personal data |
| `staatsgeheimen` | Staatsgeheimen | State secrets |

### Patterns

| | openbaar | wettelijk-gebonden | persoonsgegevens | bijzondere-persoonsgegevens | staatsgeheimen |
|---|---|---|---|---|---|
| **bedrijfskritiek** | P01 | P02 | P03 | P04 | P05 |
| **niet-kritiek** | P06 | P07 | P08 | P09 | P10 |

## What is missing, and where you come in

The model classifies. It does **not** yet say which **sovereignty level** belongs to a pattern, or which **requirements** follow from it. That is the core of the challenge:

1. Advise a sovereignty level per pattern and justify it. See [sovereignty-levels.md](sovereignty-levels.md).
2. Use minimum requirements from law and regulation as the floor. See [sources.md](sources.md).
3. Translate the level into requirements and award criteria for the programme of requirements (PvE). See [procurement-context.md](procurement-context.md).

## Design choices you will have to make

- **A system with several data classes.** Does the most sensitive class decide ("highest class wins"), or do you split the system? The example question flow in [`tooling/examples/01_vragenflow.py`](../tooling/examples/01_vragenflow.py) uses "highest class wins". You may choose differently; explain why.
- **Is the matrix monotone?** Should a more sensitive or more critical pattern always get an equal or higher level? A test for that is a good idea.
- **Edge cases.** State secrets are rare for municipalities. Decide whether your tool handles them or refers the user elsewhere.

If you think the model itself is wrong or incomplete, say so in your pitch or open an issue. Do not change `classification.yaml` silently.
