# Architecture design: how to choose the structure of one software system before it is built

Question: how is the structure of one software system chosen before it is built? The structure should meet its quality goals and stay cheap to change. The review asks what the evidence says about the methods and principles used to choose it.

| Steps | [frame](frame.md) | [review](review.md) | [state of the art](state-of-the-art.md) | [position](position.md) | [against](against.md) | [baseline](baseline.md) | [protocol](protocol.md) | [sources](sources.md) | [bibliography](../bibliography.md) |
|---|---|---|---|---|---|---|---|---|---|

Method: a multivocal literature review (Garousi 2019, [evidence method](../README.md#method)), one reviewer, searched on 2026-10-29.

- Research papers and public practice are both in scope.
- It holds 65 formal sources and 30 grey ones. The grey ones are 13 web sources scored, 11 threads from Q/A sites scored and 6 books not opened. Two of the scored grey sources fall below the threshold of 10 of 20 and are examples only.
- It is no standard, no new result and no claim on the state of the art.
- A number read only in an account of an abstract is marked "(secondary)"; 11 formal works were not reached beyond a summary line or the title ("located only"), and sources.md says which.
- arXiv counts are absent; OpenAlex counts were taken after the search and are in the [protocol](protocol.md).

## Claims

| Claim | Grade | Where |
|---|---|---|
| Of 611 candidate papers on the 23 Gang of Four patterns, 10 report 11 formal experiments; firm support for the claims made for patterns in general was not found | measured, descriptive (systematic mapping to 2009; secondary) | review.md 0, 3 |
| Pattern use has mixed effects: professionals on nine maintenance tasks did no worse with a pattern in most and worse in a few; pattern classes' defect rates ranged from 63% to 154% of the average in one product | measured, mixed (abstracts read; one in a record, secondary) | review.md 3 |
| Documenting patterns helped pattern-relevant maintenance tasks in two experiments, with 74 and 22 students | measured, one study (secondary; draft abstract) | review.md 3 |
| In eight systems from identical requirements, several object-oriented design metrics predicted fault-prone classes better than traditional code metrics | measured, one setting (abstract read) | review.md 2 |
| Organisational metrics predicted failure-proneness in Windows Vista better than traditional code metrics | measured, one company (abstract read) | review.md 6 |
| Mirroring of organisation and technical structure holds in 70% of descriptive industry and firm studies (partly in 22%), and fails in 56% of those on open collaborative projects, over 142 studies | measured, descriptive (review of studies; full text read) | review.md 6 |
| On one machine a monolith beat its microservice counterpart; vertical scaling was more cost-effective in one cloud | measured, one reference application (abstract read) | review.md 8 |
| At most 77% of 1,502 respondents use microservices (over 23% do not); 92% of respondents report some success | measured, descriptive, self-selected sample | review.md 8 |
| Architectural decisions ranked first as a source of technical debt in a survey of 1,831 | measured, descriptive (secondary) | review.md 7 |
| Architecture erosion has non-technical reasons that deserve equal attention, in 73 studies | measured, descriptive (mapping; abstract read) | review.md 7 |
| ATAM data over 31 projects show modifiability, performance, availability, interoperability and deployability dominate | measured, descriptive (secondary) | review.md 4 |
| The cost gap of minimal against very thorough architecture work is about 18% for small and 92% for very large projects | measured, one database (abstract read) | review.md 5 |
| A grounded theory of 44 participants gives six forces and five strategies for how much to design up front | supported with caveat (qualitative; abstract read) | review.md 5 |
| Dependency structure measures (design metrics, decoupling level, hotspots, architecture subspaces) predict defects and change effort in observational studies over many systems | measured, descriptive (observational; no intervention study) | review.md 2 |
| Restructuring toward more modularity lowers the cost of change | supported with caveat (one industrial case with an economic model; no controlled study) | review.md 2, 7 |
| Parnas's criterion itself (decompose by hidden decisions) | convention, untested; one worked example on one small problem | review.md 2 |
| Socio-technical congruence predicts failures in two industrial projects but not bugs or churn in 25 open source projects | measured, contested (abstracts read; one in a summary) | review.md 6 |
| Design decisions are made by satisficing, with few reasons and rarely many options; 65 articles map 37 cognitive biases | measured, descriptive (summary lines, secondary; mapping abstract read) | review.md 12 |
| ADD 3.0 as the method; ATAM as the check; no controlled test of either | convention, untested | review.md 1, 4 |
| Microservices, monolith first, modular monolith, inverse Conway maneuver, fitness functions | convention, untested; adoption shown by a survey and repository counts | review.md 8, 9 |
| A given architecture handed to a model: no study of the architecture quality of the code returned | not found; reviews call it underexplored (abstract read) | review.md 11 |

## Named baseline

- Method: ADD 3.0 (Cervantes 2016).
- Principle: information hiding (Parnas 1972).
- Check: ATAM (Kazman 2000).
- Comparison: a crossover task on a requirements brief, scored on stated scenarios (baseline.md).

## General principles linked, not reviewed again

- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/document/overview-first.md)
- [Define before use](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/document/define-before-use.md)
- [Group by what changes together](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/collection/group-by-what-changes-together.md)
- [Dependencies without cycles](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/collection/dependencies-without-cycles.md)

## Boundaries

- Documenting an architecture: [architecture-descriptions](../architecture-descriptions/README.md).
- Decision records and design docs: [design-decisions](../design-decisions/README.md).
- Running systems across machines, and algorithm design: the system-design and algorithm-design reviews.
