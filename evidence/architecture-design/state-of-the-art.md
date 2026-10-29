# State of the art, per sub-question

This file keeps two records apart for each sub-question: the **most adopted** practice (what people use) and the **best evidence** (what a study measured). Upper bounds record what has been achieved. Lower bounds would record what is impossible; this topic has none, since no result shows a structure cannot be reached.

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 design method | ADD 3.0 and the SEI texts (Cervantes 2016; Bass 2021); no adoption count found | Hofmeister 2007, a common model from five methods, with a grid to compare them (full text) | descriptive comparison; no controlled study |
| Q2 modularity | information hiding, coupling and cohesion, checked by tools through LCOM4 and instability (SESE 2012k) | Basili 1996b; Briand 2000; Mo 2016 | 8 systems, design metrics against fault-prone classes; 108 open source and 21 industrial projects, decoupling level against change locality (secondary); observational, no intervention |
| Q3 styles and patterns | layered, microservices, event-driven as listed by vendors (Microsoft 2025); Shaw 1996 names the styles | Zhang 2012; Prechelt 2001; Vokac 2004 | mapping, 11 formal experiments; professionals on nine tasks; one product over three years (secondary) |
| Q4 quality attributes | ISO/IEC 25010 with nine characteristics (ISO 2023); six cloud pillars (AWS 2026d) | Bellomo 2015 | ATAM data, 31 projects (secondary) |
| Q5 evaluation | ATAM (Kazman 2000) | none found | no controlled study of evaluation before building |
| Q6 up front | agile teams decide case by case (Waterman 2015) | Boehm 2008; Waterman 2015 | 161 projects, abstract read; grounded theory, 44 participants |
| Q7 organisation | inverse Conway maneuver, team topologies (ThoughtWorks 2014; Skelton 2025) | Colfer 2016; Nagappan 2008; Mauerer 2022 (null) | review of 142 studies; one Windows case; 25 open source projects with no relation of congruence to bugs and churn |
| Q8 erosion and debt | boundary checks in builds (Packwerk, ArchUnit; 1,928 and 3,882 stars) | Li 2022; Ernst 2015; Kazman 2015 | mapping of 73 studies; survey of 1,831 (secondary); one industrial case with an economic model (secondary) |
| Q9 monolith and services | microservices, used by at most 77% of 1,502 respondents (Loukides 2020) | Blinowski 2022; Taibi 2017 | controlled runs of one application; practitioner interviews (secondary) |
| Q10 model as implementer | none | Schmid 2025; Esposito 2025 | systematic review of 18 articles; multivocal review |
| Q11 how architects reason | none | Razavian 2016; Mohanani 2020 | multiple case studies with 12 student groups; mapping of 65 articles |

## Reading the table

- The best-evidence column holds no randomised trial of a design method on a real system.
- The strongest quantitative results are about prediction (metrics, organisation) and about pattern documentation in small tasks.
- The modularity results are correlational: dependency structure predicts defects and change effort across many systems; no intervention study shows that restructuring lowers change cost.
- Practice leads where no study exists: methods, evaluation and the microservices debate.

## Adoption counts

- The counts are in [sources](sources.md), read 2026-10-29: at most 77% of 1,502 respondents use microservices (a mailing-list sample; over 23% do not); ArchUnit has 3,882 stars; 4,221 repositories carry the topic software-architecture.
- Stars show interest, not use; the survey sample is self-selected.

## Where research stopped

- Hofmeister 2007 and Falessi 2011 describe methods; no work found measures a method against another.
- Zhang 2012 recommends case studies on key patterns and their effect on maintenance.
- Li 2022 asks for equal attention to non-technical causes of erosion.
- Esposito 2025 asks for general evaluation methods and architecture-specific datasets.
