# Case: Forensic medicine application, GGD

> Anonymised. Source: a Dutch GGD (municipal public health service), description supplied by the challenge owners (DACC). Year: 2026.
>
> Short on purpose: the challenge owners kept it to the essentials. Where you need more detail, write down your assumption and keep going.

## The system or service

An application for **forensic medicine** at the GGD of a municipality. It supports post-mortem examinations (*lijkschouw*), injury and trace examinations, and medical care for people in police custody (*medische arrestantenzorg*).

The application was built in-house about 15 years ago on a low-code platform and is used by **several GGDs across the country**.

## The data

Highly sensitive: medical data, findings from post-mortem and injury examinations, and data on people in custody. Special categories of personal data are involved. Only a very limited number of users have access to the data in the application.

## Criticality

Not specified by the challenge owners. Work out with the classificatietoets or the DACC matrix what follows for criticality, and write down your assumptions (for example: what happens when the application is unavailable during a post-mortem or in a custody setting?).

## Current situation

- Built in-house on a low-code platform, about 15 years old and no longer up to date. It has to be replaced.
- Coverage problems: there is no mobile reception in cell complexes, so the required data cannot be entered there.
- Several GGDs depend on the same application.

## What is being asked

- The preference is to **buy** the application from a market party, so that management is properly secured. A market exploration (*marktverkenning*) is under way.
- The front-end is a lot of work to reproduce exactly, so it has to be redeveloped in a simpler way. Resistance from users is expected.
- **Open question:** which requirements should be set for the supplier from the perspective of digital autonomy?

## Questions for teams

- Which SEAL level follows for this application, and why?
- This is a full replacement of one application. Which requirements from the full set for that level apply, and which can be left out? Explain each choice.
- What changes when the application has to work offline in a cell complex and synchronise later?
- Several GGDs use the application. What does that mean for exit and for joint procurement?
