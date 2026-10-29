# Protocol: how the pool of sources was built

The searches, screening and scoring of the system-design review are set out here so that they can be rerun. The rules that every review shares are in the [evidence method](../README.md#method). All searches of this review ran on 2026-10-29. Its terms of architecture are defined in [architecture-descriptions](../architecture-descriptions/frame.md); module-level design is in [architecture-design](../architecture-design/frame.md).

## 1. Why grey literature

Garousi 2019 Table 4 lists seven questions for grey literature, where a single yes suffices ([the rule](../README.md#method)). For system design every answer is yes.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the main forms (primers, guidelines, postmortems) come from practice |
| 2 | Lack of volume or quality of evidence? | yes: no controlled study found for estimation or for most principles |
| 3 | Context important? | yes: load, failure model and team decide the design |
| 4 | Corroborate research with practice? | yes: failure studies against postmortem practice |
| 5 | Challenge practice with research, or the reverse? | yes: primers state CAP as a binary choice (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 376k stars on one primer (state-of-the-art.md) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | Which principles of computer system design are stated, and which are tested? |
| Q2 | What do consistency and availability trade-offs say, as theory and as practice? |
| Q3 | What do failure studies say designs get wrong? |
| Q4 | How are capacity and load estimated before building? |
| Q5 | How are interfaces between services designed, and what do usability studies show? |
| Q6 | How is a design checked before it is built? |
| Q7 | What do systems engineering standards ask of design? |
| Q8 | What do interview books and primers teach, and how does it compare with research? |

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by relevance searches on Semantic Scholar (four returned listings) and by web searches, on these topics (R1 to R6).
- R1: multivocal or systematic review of site reliability engineering, chaos engineering.
- R2: systematic review of consistency models; of REST and microservice API design rules.
- R3: systematic review of cloud outages, incidents, postmortems.
- R4: systematic mapping of formal methods, TLA+, in distributed design.
- R5: systematic review of capacity planning (junk results, see section 10).
- R6: systematic review of large language models and architecture design.
- Found: 7 reviews; all read at least to the abstract, and Bogli 2024 and Costa 2025 beyond it. They are placed in review.md strand 0.
- Boundary: a review of architecture design with models (Schmid 2025, arXiv 2505.16697) was located and left to architecture-design.

## 4. Formal search

Count source: the Semantic Scholar bulk title-and-abstract search and the arXiv search API (all fields). OpenAlex had no budget left during the search; it counted every string later that day (table below). Semantic Scholar matches words, not phrases, so counts are noisy upper bounds. Semantic Scholar has OR as `|` and AND as `+`.

| Id | String as run (abridged) | Semantic Scholar | arXiv |
|---|---|---|---|
| F1 | "end-to-end argument" OR "computer system design" OR "system design principles" | 2,067 | 49 |
| F2 | "CAP theorem" AND (consistency OR availability) | 198 | 46 |
| F3 | "consistency models" AND "distributed" | 832 | 493 |
| F4 | "cloud outages" OR "outage study" OR "production failures" AND distributed | 36 | 49 |
| F5 | "capacity planning" AND software | 604 | 174 |
| F6 | "API usability" OR "API design" | 2,429 | 81 |
| F7 | "formal methods" AND ("distributed systems" OR "cloud") AND design | 367 | 17 |
| F8 | "site reliability engineering" | 195 | 38 |
| F9 | "systems engineering" AND ("design definition" OR "architecture definition") | 98 | 2 |
| F10 | "large language model" AND "system design" | 1,336 | 534 |
| F11 | "design review" AND (distributed OR "production readiness") | 254 | 374 |
| F12 | "literature review" AND "distributed systems" AND (design OR reliability) | 65 | 13 |
| Total | 12 strings | 8,481 | 1,870 |

- Screened by title: the top 6 of four relevance searches (24 titles), and the arXiv listings of three searches (8 titles). The counts above were not screened one by one.
- Named works: 14 leads from the brief and 11 works known to the reviewer were checked in Crossref (no mailto, no identity): title, year and authors were compared; all matched. The second pass checked 8 more the same way.
- Zero or junk results were treated as a wrong query: "systematic review cloud outages incidents postmortems" returned energy and agriculture papers, and was redone as a web search.
- Snowballing, second pass (2026-10-29), recorded:
  - Backward from Yuan 2014: its related-work section was read; it names Oppenheimer and colleagues (over 100 failure reports from internet services, not located) and Rabkin and Katz (taken as Rabkin 2013).
  - Backward from Alquraan 2018: its references 21 to 24 were read. The network-failure study of Gill and colleagues was taken as Gill 2011. The others (a Google network paper and two network failure reports) were not taken.
  - Backward from Lampson 2020: its reference list was scanned for empirical work; Fonseca 2017 was taken.
  - Forward from Newcombe 2015: the first page of the citation list of Semantic Scholar (100 records) was read by title, and the 25 most cited were screened. Three were taken, as design-to-implementation conformance and industry reviews: ter Beek 2024, Cirstea 2024 and Tang 2024.
  - Backward from Myers 2016: its reference list gave Ellis 2007 (already held) and Stylos 2008.
  - Limits: one page forward only; one level; no chase from the other seminal works.
- Second pass: open copies were sought for every formal source held by title; the author's or an institution's copy, an open publisher page or a republication was read as text and not saved. Routes used need no identity: the Semantic Scholar paper endpoint, Crossref, publisher landing pages, authors' pages.
- Still unreachable after the second pass: Nuseibeh 2001 (the publisher refused the fetch) and Ellis 2007 (no open copy found); they are marked located only in sources.md. Brooker 2025 was read in full later, and Ellis 2007 on 2026-10-29 from its authors' page.
- Four standard or book leads could not be read at all from the open web (ISO 15288, ISO 42020, INCOSE, Kleppmann 2017); they are located, not scored.

### OpenAlex counts (2026-10-29)

Counted as the [method](../README.md#method) describes; exact for each query as written.

| Id | OpenAlex query as run | Count |
|---|---|---|
| F1 | `"end-to-end argument" OR "computer system design" OR "system design principles"` | 1,225 |
| F2 | `"CAP theorem" AND (consistency OR availability)` | 237 |
| F3 | `"consistency models" AND "distributed"` | 827 |
| F4 | `"cloud outages" OR "outage study" OR ("production failures" AND "distributed")` | 190 |
| F5 | `"capacity planning" AND "software"` | 657 |
| F6 | `"API usability" OR "API design"` | 3,134 |
| F7 | `"formal methods" AND ("distributed systems" OR "cloud") AND "design"` | 345 |
| F8 | `"site reliability engineering"` | 402 |
| F9 | `"systems engineering" AND ("design definition" OR "architecture definition")` | 114 |
| F10 | `"large language model" AND "system design"` | 2,062 |
| F11 | `"design review" AND ("distributed" OR "production readiness")` | 273 |
| F12 | `"literature review" AND "distributed systems" AND ("design" OR "reliability")` | 95 |

## 5. Grey search

- Types and producers, chosen because primers, vendor frameworks, company API rule sets, SRE postmortem practice and independent fault testers produce most grey writing on this topic:
  - study guides and primers (Primer 2026);
  - vendor guidance (AWS 2026p, Azure Patterns 2026);
  - company API guidelines (Google AIP 2025, Zalando 2026, Microsoft API 2026);
  - practitioner books (Beyer 2016);
  - independent test reports (Jepsen 2026);
  - keynote slides (Brewer 2000);
  - Q/A sites (section 5.1).
- Engine: a general web search engine for existing reviews and for the benchmark leads; direct visits to named producers for practice. Results personalise and change.
- Practice sources were read on 2026-10-29 by page fetch; star counts were read through the public repository interface without sign-in.
- Several lead pages blocked the fetch (ISO, INCOSE); they are "located only".

| Id | String or visit | Screened | Included |
|---|---|---|---|
| G1 | direct: Primer repository (README and counts) | 1 | 1 |
| G2 | direct: AWS Well-Architected page | 1 | 1 |
| G3 | direct: Azure cloud design patterns page | 1 | 1 |
| G4 | direct: Google AIP-1 page | 1 | 1 |
| G5 | direct: Zalando guidelines page (first 100,000 characters) | 1 | 1 |
| G6 | direct: Microsoft API guidelines repository | 1 | 1 |
| G7 | direct: SRE book chapter on postmortems; the books page | 2 | 1 |
| G8 | direct: Jepsen analyses page | 1 | 1 |
| G9 | direct: Brewer, the 2000 PODC keynote slides | 1 | 1 |

### 5.1 Q/A sites

Strings SY1 to SY18 ran on 2026-10-29, one reviewer, grey tier 2. The [architecture-descriptions protocol](../architecture-descriptions/protocol.md#q-a-sites) gives the API call for these strings. It gives N = 30 by votes per site and k = 10 as the stopping parameters. It also gives the common limits, and how threads are read and scored.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| SY1 | `q=distributed system design` | Software Engineering | 30 | 0 | 0 |
| SY2 | `q=CAP theorem` | Software Engineering | 15 | 1 | 1 |
| SY3 | `q=eventual consistency` | Software Engineering | 30 | 2 | 2 |
| SY4 | `q=system design interview` | Software Engineering | 26 | 2 | 2 |
| SY5 | `title=REST API design` | Software Engineering | 28 | 0 | 0 |
| SY6 | `q=capacity planning` | Software Engineering | 30 | 0 | 0 |
| SY7 | `title=microservices communication` | Software Engineering | 1 | 0 | 0 |
| SY8 | `title=idempotent` | Software Engineering | 15 | 1 | 1 |
| SY9 | `tagged=distributed-system&q=design` | Software Engineering | 30 | 1 | 1 |
| SY10 | `title=API versioning` | Software Engineering | 12 | 0 | 0 |
| SY11 | `q=back of the envelope estimation` | Software Engineering | 2 | 0 | 0 |
| SY12 | `title=high availability` | Software Engineering | 9 | 1 | 1 |
| SY13 | `title=system design` | Stack Overflow | 30 | 1 | 1 |
| SY14 | `title=CAP theorem` | Stack Overflow | 30 | 3 | 3 |
| SY15 | `title=eventual consistency` | Stack Overflow | 30 | 1 | 1 |
| SY16 | `title=idempotent API` | Stack Overflow | 2 | 0 | 0 |
| SY17 | `title=API design` | Software Engineering | 30 | 1 | 1 |
| SY18 | `tagged=system-design&q=scalability` | Stack Overflow | 30 | 0 | 0 |
| Total | 18 strings | | 380 | 14 (distinct) | 14 |

**Selection and scoring**

- Opened: 14 threads chosen by title (high votes or a named sub-question), with the question and the top two answers read (first 700 characters of each answer). The other titles were not opened, so lower-voted relevant threads may be missed.
- Included: a thread that answers a sub-question with an argument or an experience, not a how-to; all 14 opened threads passed. Excluded by title: product-specific, language-specific and how-to threads, and threads of another topic (module design, git, licences).
- Scoring follows the [shared rules](../architecture-descriptions/protocol.md#q-a-sites). Objectivity is 4 when no vendor is involved.
- Below the threshold: 0.

**Stopping point**

- The run ended after SY18; the last string that added a new included thread was SY17.
- SY7, SY11 and SY16 returned 1 or 2 results and were read as weak queries, not absence.

**Limits specific to this search**

- Broad words return unrelated popular threads under `q` (SY1: 30 returned, none included).
- Votes, views and reputation are those of 2026-10-29.
- Threads are cited by title in references.md.

## 6. Stopping rule

- Fixed before searching: effort bounded at N = 6 results per relevance search and 30 per Q/A string, with saturation at k = 5 for web searches.
- Formal: effort bounded for the relevance searches; evidence exhaustion for leads (each checked).
- Practice: evidence exhaustion; the named producers were all visited.
- Q/A sites: see 5.1.

## 7. Selection

- Include: a source on principles, trade-offs, failures, estimation, interfaces, checking, standards or teaching of designing a running system; English; readable on the search date.
- Exclude:
  - module decomposition and styles (architecture-design);
  - specification languages in general and contracts (algorithm-design);
  - hardware computer architecture (the benchmarks ArchEval and QuArch);
  - vendor pages selling a product with no design content;
  - sources whose abstract could not be read and whose title does not settle relevance ("located only").
- Grey sources must also pass section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- For the 20 criteria, the tier scale and the threshold of 10 of 20, see the [evidence method](../README.md#method).
- Tiers as applied here: books, magazines, theses, standards and vendor guidance pages are tier 1. Presentations, project documentation, Q/A and wiki pages are tier 2. Blogs are tier 3.
- Impact is judged from stars, citations, views or votes.
- None of the grey sources fell below the threshold, so none is only an **example of practice**.
- A company page is its owner's claim about itself; the text says so.

## 9. Extraction and synthesis

- Extraction and synthesis follow the [evidence method](../README.md#method). Each number carries its location, and "(secondary)" when it came from an abstract or summary.
- The synthesis runs by question, Q1 to Q8; each claim traces to a row of sources.md.

## 10. Limits

- The limits shared by every review are in the [evidence method](../README.md#method).
- One reviewer, no second rater; the scores are one person's.
- Snowballing was one level, and forward only one page of 100 records.
- Seven formal sources are known by title and venue only after the second pass; sources.md says which.
- Q4 (capacity estimation) returned junk (604 hits for "capacity planning" and software, mostly hardware and IT). A better string was not found in the time, so absence of a study is not proof.
- Semantic Scholar answered some queries with errors on the day; those queries were repeated or replaced, and counts are from the successful calls.
