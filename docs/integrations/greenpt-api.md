# GreenPT API (optional)

[GreenPT](https://greenpt.nl/), the tech partner of the OneGov Hackathon Series, provides API access to LLMs hosted on European infrastructure. It is an **optional resource** for teams that want an AI step in their tool.

## Where an LLM call might help

- **Explanation:** turn a profile, level and requirement list into a short plain-language summary for a buyer or a board.
- **Question support:** help a user understand a question ("what counts as special categories of personal data?"), after which the user answers.
- **Finding passages:** suggest where in a law or framework a requirement may come from, for a person to check.

## Where an LLM call should **not** be used

- To decide the profile, the level or a requirement. That violates M4.
- To generate requirement text on the fly that is not stored in your rules.
- To send confidential tender information to any API.

## Practical notes

- **Access.** Ask the organisers at [hack@govtechnl.nl](mailto:hack@govtechnl.nl) for credentials.
- **Reproducibility.** Pin a model version and log prompts and responses where they influence what the user sees.

If your submission uses GreenPT or another LLM, note in the PR description **where** and **why**.
