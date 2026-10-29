# Against: controversies, null results, where practice contradicts the evidence

This file collects the evidence against the common rules of architecture design. A source under 10 of 20 is an example only.

## Against design patterns as a cure

- Zhang 2012: firm support for the claims made for patterns in general could not be identified, in 11 formal experiments.
- Zhang 2012: some indication that patterns do not help novices learn design.
- Prechelt 2001 (abstract read): in most of nine tasks the pattern design was no worse, so the evidence is mixed rather than against; a few tasks favoured the simpler design.
- Khomh 2008 (technical report abstract, secondary): several quality attributes were affected negatively by patterns.
- Vokac 2004 (secondary): defect rates of pattern classes ranged from 63% to 154% of the average, so no pattern is uniformly safer.
- Prechelt 2002 supports pattern documentation only for pattern-relevant tasks, in small programs of 360 to 560 lines (secondary).

## Against fixed rules of coupling

- SESE 2020d: low coupling is a trade-off; indirection that lowers coupling can break a real-time budget.
- SESE 2012k: the tool metrics give counts, not a verdict on a design.
- No study found tests information hiding as a criterion on a real system; its support is argument and one worked example on an indexing problem (Parnas 1972, abstract read in a summary).
- The measures of dependency structure are observational: Mo 2016 relates decoupling level to proxies from revision history, not to effort (secondary).

## Against microservices as default

- Blinowski 2022: on a single machine the monolith performed better; vertical scaling was more cost-effective in one cloud.
- Mendonca 2021 and Noonan 2018: two companies moved from services to a monolith, each reporting on its own decision.
- SESE 2017h and SESE 2018d: microservices turn software into a distributed system; benefits come from decoupled components, not from the deployment.
- Fowler 2015: monolith first, with the evidence admitted as sparse.
- Taibi 2017 (secondary): splitting the monolith and its data stayed hard for those who migrated.
- For the other side: 92% of the 1,502 respondents report some success (Loukides 2020); the sample is self-selected from mailing lists.

## Against Conway as a design lever

- Mauerer 2022: across 25 open source projects, socio-technical motif congruence was not related to bugs or churn in any temporal scenario.
- Cataldo 2013 (secondary) found congruence tied to fewer failures in two industrial projects, so the effect is not robust across settings.

- Colfer 2016: mirroring is prevalent but not universal in industry and firm studies, not supported in open collaborative projects, and partial mirroring appears in technologically dynamic industries.
- The inverse Conway maneuver reached Trial in 2014 and left the current Radar (ThoughtWorks 2014).
- Team Topologies 2026 (example only) gives anecdotes and no study count.

## Against evaluation and up-front design

- No controlled study shows ATAM or any evaluation improves the system built.
- Boehm 2008 (abstract read): the cost gap between minimal and very thorough architecture work is about 18% for small projects and 92% for very large ones. The case for thorough up-front work is therefore weaker for small projects (the paper's own guidance was not read).
- Waterman 2015: too little up-front design raises risk and too much delays value; teams use forces and strategies, not a rule.

## Where practice contradicts the evidence

- Vendor guides recommend styles by domain type with no study (Microsoft 2025).
- The quality model has nine characteristics, while the cloud framework has six pillars; the two lists are not mapped to each other in the pages read (ISO 2023; AWS 2026d).
- Practice moves on without the evidence: the two Radar entries read are no longer on the current edition.

## Limits of this file

- Eleven formal works were not reached beyond a summary line or the title; no counter-evidence is claimed from them.
- The strongest null result is a mapping (Zhang 2012), not a replication.
