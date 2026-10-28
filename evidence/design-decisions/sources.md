# Sources: the pool, the flow and the scores

This file lists every source in the design-decisions review: how the pool narrowed, and one row per source with its kind, how it was found, its quality and where it is used. Method and strings are in [protocol](protocol.md). Architecture terms (viewpoint, architectural knowledge) are defined in [architecture-descriptions](../architecture-descriptions/frame.md).

## Flow

| Stage | Formal | Grey |
|---|---|---|
| Records returned by the strings | 2,267 (Semantic Scholar 2,092; arXiv 175) | about 75 results, plus 5 producer visits |
| Screened by title or snippet | 231 (with repeats across strings) | 80 |
| Already in the narrative review | about 14 | 19 |
| New and included | 15, plus 1 thesis counted as grey | 11 |
| Excluded | about 200, reasons below | about 69, reasons below |

- Formal exclusions, counted by title and rounded to tens:
  - repeats across strings: 40;
  - not about software documents (physics, imaging, buildings, networks): 85;
  - LLM generators, mining tools and notation proposals with no bearing on document form: 70;
  - relevant but not read, located only: 6.
    - Two IEEE Software articles by Keeling (2022), a 2018 MADR workshop paper, a 2019 generalised MADR paper.
    - An ADR explainability framework and a 2023 agile ADR study.
- Grey exclusions, rounded:
  - known sources seen again: 12;
  - not software design: 12;
  - vendors of documentation products: 8;
  - project ADR pages that are examples of use, not accounts: 20;
  - pages found but not read: 15;
  - books not read: 2.
- Added by snowballing: none beyond those found by the strings; forward snowballing was one page.
- Existing reviews found: 9, listed in review.md strand 0.

## Formal sources

Grade vocabulary as in the README. "narrative" means found by the earlier reading of the field, before the protocol.

| Key | Kind | Found via | Quality | Used in |
|---|---|---|---|---|
| Lee 1997 | formal | narrative | argument, secondary | review 1 |
| Regli 2000 | formal | narrative | survey, secondary | review 1 |
| Dutoit 2006 | formal | narrative | edited volume | review 1 |
| Shahin 2009 | formal | narrative | comparison, secondary | review 1 |
| Capilla 2016 | formal | narrative | retrospective, secondary | review 1 |
| Conklin 1988 | formal | narrative | tool experiments, secondary | review 2 |
| MacLean 1991 | formal | narrative | method, secondary | review 2 |
| Karsenty 1996 | formal | narrative | evaluation, abstract not read | review 2 |
| Tyree 2005 | formal | narrative | template, secondary | review 2 |
| Jansen 2005 | formal | narrative | position, secondary | review 2 |
| Zdun 2013 | formal | narrative | position | review 2 |
| Tang 2006 | formal | narrative | measured, descriptive, 81 answers, secondary | review 3 |
| Weinreich 2015 | formal | narrative | measured, descriptive, 25 interviews, secondary | review 3 |
| Groher 2015 | formal | narrative | same 25 interviews, secondary | review 3 |
| Borowa 2023 | formal | narrative | 63 answers, 13 interviews, secondary | review 3 |
| Ding 2014b | formal | narrative | exploratory survey, secondary | review 3 |
| Wan 2023 | formal | narrative | 32 interviews, secondary | review 3 |
| Bratthall 2000 | formal | narrative | experiment, result not read | review 4 |
| Falessi 2010 | formal | narrative | measured, experiment, 50 students | review 4 |
| Falessi 2008 | formal | narrative | feasibility study, secondary | review 4 |
| Nogueira 2026 | formal | narrative | measured, crossover, 33 students, preprint | review 4 |
| Buchgeher 2023 | formal | narrative | repository mining, secondary | review 5 |
| Santana 2026 | formal | narrative | repository mining, abstract only | review 5 |
| Ahmeti 2024 | formal | narrative | action research, one company | review 5 |
| Keertipati 2016 | formal | narrative | process mining, secondary | review 5 |
| Sharma 2022 | formal | narrative | process mining, secondary | review 5 |
| Kondo 2025 | formal | narrative | 1,095 classic proposals, preprint | review 5 |
| Viviani 2021 | formal | narrative | classifier, secondary | review 5 |
| Parnas 1987 | formal | narrative | title and venue only | review 6 |
| Basili 1996 | formal | narrative | abstract not read | review 6 |
| Aurum 2002 | formal | narrative | review of inspections | review 6 |
| Zanaty 2018 | formal | narrative | abstract only | review 6 |
| van Heesch 2012 | formal | narrative | viewpoint, title only | frame |
| Tofan 2014 | formal | R1 | systematic mapping, 144 papers, abstract read | review 0 |
| Bhat 2020 | formal | R1 | semi-systematic review, 218 papers, abstract only | review 0 |
| Razavian 2019 | formal | R1 | review of empirical methods, abstract partly read | review 0 |
| Hyun 2023 | formal | R2 | systematic mapping, journal page only | review 0 |
| Tang 2017 | formal | R1 | literature review, title and venue only | review 0 |
| Weinreich 2014 | formal | R1 | systematic review, title and venue only | review 0 |
| Alexeeva 2016 | formal | R1 | literature overview, title and venue only | review 0 |
| Li 2013 | formal | F5 | systematic mapping, title and venue only | review 0 |
| Buckingham Shum 1994 | formal | F1 | title and venue only | review 1 |
| van Heesch 2012b | formal | F6 | framework, title and venue only | review 4 |
| van Heesch 2013 | formal | F6 | measured, multiple-case, 4 student teams, abstract read | review 4 |
| Manteuffel 2014 | formal | F6 | industrial implementation, title and venue only | review 5 |
| Gebreweld 2023 | formal | F2 | descriptive survey, 45 architects, preprint, abstract only | review 3 |
| Nakashima 2026 | formal | F1 | exploratory, preprint, abstract only | review 5 |
| Gupta 2026 | formal | F2 | adjacent, LLM generation, preprint, abstract only | position |

## Grey sources, scored

Subtotals in order: authority (4), methodology (6), objectivity (4), date (1), position (1), novelty (2), impact (1), outlet (1). A source under 10 is an example of practice only.

| Key | Kind | Found via | Quality (total, then subtotals) | Used in |
|---|---|---|---|---|
| Nygard 2011 | grey tier 3 | narrative | 13.5 of 20 (4 / 2.5 / 2.5 / 1 / 0.5 / 2 / 1 / 0) | review 2, 7; baseline |
| ThoughtWorks 2018 | grey tier 1 | narrative | 12.5 of 20 (3.5 / 3 / 1.5 / 1 / 0.5 / 1 / 1 / 1) | review 7; position |
| MADR 2024 | grey tier 2 | narrative; G1 | 12 of 20 (3 / 3 / 2 / 1 / 0.5 / 1 / 1 / 0.5) | review 7; state-of-the-art |
| ADR 2026 | grey tier 2 | narrative | 12 of 20 (3 / 3 / 2.5 / 0 / 1 / 1 / 1 / 0.5) | review 2; frame |
| AWS 2026c | grey tier 1 | narrative | 9.5 of 20 (2.5 / 3 / 1.5 / 0 / 0.5 / 0.5 / 0.5 / 1) | frame; state-of-the-art; position (example only) |
| Microsoft 2026 | grey tier 1 | narrative | 10 of 20 (2.5 / 2.5 / 1.5 / 1 / 0.5 / 0.5 / 0.5 / 1) | state-of-the-art; against |
| GOV.UK 2025 | grey tier 1 | narrative (secondary) | 11.5 of 20 (3 / 2.5 / 2.5 / 1 / 0.5 / 0.5 / 0.5 / 1) | review 7; position |
| Warsaw 2000 | grey tier 2 | narrative | 15 of 20 (3.5 / 5 / 2 / 1 / 0.5 / 1.5 / 1 / 0.5) | baseline; state-of-the-art |
| Goodger 2002 | grey tier 2 | narrative | 12 of 20 (3.5 / 3 / 2 / 1 / 0 / 1 / 1 / 0.5) | baseline; state-of-the-art |
| Rust 2026a | grey tier 2 | narrative | 12.5 of 20 (3.5 / 4 / 2 / 0 / 0.5 / 1 / 1 / 0.5) | state-of-the-art |
| Rust 2026b | grey tier 2 | narrative | 10 of 20 (3.5 / 2.5 / 2 / 0 / 0 / 0.5 / 1 / 0.5) | state-of-the-art |
| Kubernetes 2026 | grey tier 2 | narrative | 11 of 20 (3.5 / 3 / 2 / 0 / 0 / 1 / 1 / 0.5) | state-of-the-art; position |
| Ubl 2020 | grey tier 3 | narrative | 11.5 of 20 (3.5 / 3 / 1.5 / 1 / 0 / 1.5 / 1 / 0) | review 7; position; against |
| Frazelle 2026 | grey tier 2 | narrative | 9.5 of 20 (3 / 3.5 / 1.5 / 0 / 0 / 0.5 / 0.5 / 0.5) | frame; review 7 (example only) |
| HashiCorp 2026 | grey tier 2 | narrative | 9 of 20 (3 / 2.5 / 1.5 / 0.5 / 0 / 0.5 / 0.5 / 0.5) | state-of-the-art (example only) |
| Amazon 2021 | grey tier 2 | narrative (secondary) | 11.5 of 20 (4 / 3 / 1 / 1 / 0 / 1 / 1 / 0.5) | review 7; against |
| IETF 2014 | grey tier 1 | narrative | 17.5 of 20 (4 / 5.5 / 3.5 / 1 / 1 / 0.5 / 1 / 1) | review 7 |
| Attentive 2026 | grey tier 3 | narrative | 9 of 20 (2.5 / 3.5 / 1 / 1 / 0 / 1 / 0 / 0) | against (example only) |
| Pragmatic Engineer 2022 | grey tier 3 | narrative | 14.5 of 20 (3 / 5 / 2.5 / 1 / 1 / 1 / 1 / 0) | against; review 7 |
| Harhio 2022 | grey tier 1 | R2 | 16 of 20 (2 / 6 / 3.5 / 1 / 1 / 1.5 / 0 / 1) | review 0; position |
| Perkins 2020 | grey tier 3 | G4 | 11.5 of 20 (2.5 / 4.5 / 1.5 / 1 / 1 / 0.5 / 0.5 / 0) | review 7 |
| GDS 2026 | grey tier 1 | G6 | 13.5 of 20 (3 / 4 / 2.5 / 1 / 1 / 0.5 / 0.5 / 1) | review 7; state-of-the-art |
| Bitwarden 2026 | grey tier 2 | G4 | 8.5 of 20 (1.5 / 3.5 / 1.5 / 0 / 0.5 / 0.5 / 0.5 / 0.5) | review 7 (example only) |
| Go 2026 | grey tier 2 | P | 13 of 20 (3.5 / 4.5 / 2 / 0 / 0.5 / 1 / 1 / 0.5) | review 5, 7 |
| Swift 2026 | grey tier 2 | P | 12 of 20 (3.5 / 4 / 2 / 0 / 0.5 / 0.5 / 1 / 0.5) | review 7; state-of-the-art |
| Arc42 2026b | grey tier 2 | P | 12 of 20 (3.5 / 3 / 2.5 / 0 / 1 / 0.5 / 1 / 0.5) | review 7; state-of-the-art |
| Google Cloud 2024 | grey tier 1 | P | 9 of 20 (2.5 / 2 / 1.5 / 1 / 0 / 0.5 / 0.5 / 1) | review 7 (example only) |
| Runde 2018 | grey tier 2 | G1 | 12.5 of 20 (4 / 4 / 1.5 / 0.5 / 0.5 / 1 / 0.5 / 0.5) | review 7; position |
| Polishchuk 2026 | grey tier 3 | G1 | 6 of 20 (1 / 2 / 1.5 / 1 / 0 / 0.5 / 0 / 0) | against (example only) |
| Taylor 2025 | grey tier 1 | G1 | 9 of 20 (2 / 2.5 / 1.5 / 1 / 0.5 / 0 / 0.5 / 1) | review 7 (example only) |
| Kashitsyn 2024 | grey tier 3 | G2 | 10.5 of 20 (1.5 / 4 / 2.5 / 1 / 1 / 0.5 / 0 / 0) | review 7; state-of-the-art |

## Result of the scoring

- 31 grey sources scored; 8 fall below 10 of 20: AWS 2026c, Frazelle 2026, HashiCorp 2026, Attentive 2026, Bitwarden 2026, Google Cloud 2024, Polishchuk 2026, Taylor 2025.
- Those 8 appear in the text only as examples of practice.
- Microsoft 2026 and Rust 2026b sit exactly at 10 and stay in.
- GitHub 2026 is the reviewer's own count of public listings, not a source, so it is not scored.
- The highest scores go to a standards document (IETF 2014), a thesis (Harhio 2022) and the Python process (Warsaw 2000).
