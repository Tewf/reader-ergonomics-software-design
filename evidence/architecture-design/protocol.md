# Protocol: how the pool of sources was built

This file records how the architecture-design review was searched, screened and scored, so that someone else can repeat the search. The rules shared by all reviews are in the evidence index ([method](../README.md#method)). All searches of this review ran on 2026-10-29. The terms it uses (architecture, architectural knowledge, viewpoint) are defined in [architecture-descriptions](../architecture-descriptions/frame.md); decision records are in [design-decisions](../design-decisions/frame.md).

## 1. Why grey literature

Of the seven questions in Garousi 2019 Table 4, one yes would justify grey literature; all seven are yes for this topic.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: styles, methods and the monolith debate come from practice |
| 2 | Lack of volume or quality of evidence? | yes: few controlled experiments on structure (Zhang 2012 found 11) |
| 3 | Context important? | yes: team size, domain and scale decide which structure fits |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: practice moves between microservices and monoliths ahead of the evidence |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: the microservices survey alone has 1,502 respondents (Loukides 2020) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | Which design methods exist, and what do they share? |
| Q2 | What do modularity principles (information hiding, coupling, cohesion) predict, measured how? |
| Q3 | Do styles and patterns help maintenance, measured? |
| Q4 | How do quality attributes drive the structure (tactics, trade-offs)? |
| Q5 | How are architectures evaluated before building? |
| Q6 | How much design up front, in agile practice? |
| Q7 | How does structure follow the organisation (Conway, mirroring)? |
| Q8 | What do erosion and architectural debt cost, and how are they found? |
| Q9 | Monolith, modular monolith, microservices: what is the evidence and the practice? |
| Q10 | What is measured when an architecture or design is handed to a model that writes the code? |
| Q11 | How do architects reason while designing, and what biases affect them? |

Adjusted after the frame: Q10 was added as the brief's strand "designing for a model as implementer". Q11 was added in the second pass. Its strand, design reasoning, had not been searched in the first pass.

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, with strings R1 to R12 below, top hits by citation count read by title.
- Found: 14 reviews, maps or surveys. Of these, 9 were read by abstract, 3 by a summary of the abstract, 1 by a summary line, and 1 was located only. One more (Tofan 2014) is reviewed in design-decisions and linked.
- A tertiary study of software architecture in general was not found: R2 returned 2 hits, a study of systems of systems and a study of sustainability.
- They are placed in review.md strand 0.

## 4. Formal search

Counts come from the Semantic Scholar bulk search, title and abstract. They match words, not phrases, so they are noisy upper bounds. The arXiv counts are not obtained: its API answered HTTP 429 on the day for every call. The OpenAlex counts are not obtained either: it was not called (daily budget spent); the strings are in `openalex.tsv`, for counting later by script.

| Id | String as run | Semantic Scholar |
|---|---|---|
| R1 | "software architecture" +"systematic mapping study" | 72 |
| R2 | "software architecture" +"tertiary study" | 2 |
| R3 | "architectural technical debt" +"systematic" | 16 |
| R4 | "architecture erosion" +"systematic" | 14 |
| R5 | "architecture smells" +"systematic" | 20 |
| R6 | "architecture evaluation" +"systematic" | 208 |
| R7 | "Conway" +"socio-technical congruence" +"systematic" | 1 |
| R8 | "microservices" +"multivocal" | 19 |
| R9 | "monolith" +microservices +"migration" +"systematic" | 16 |
| R10 | "agile" +"software architecture" +"systematic literature review" | 9 |
| R11 | "architectural tactics" +"systematic" | 36 |
| R12 | "large language model" +"software architecture" +"systematic" | 29 |
| F1 | "software architecture design" +method | 396 |
| F2 | "attribute-driven design" +architecture | 76 |
| F3 | "architectural tactics" +"quality attributes" | 74 |
| F4 | "information hiding" +modularity +software | 175 |
| F5 | "design structure matrix" +software +architecture | 51 |
| F6 | "architecture evaluation" +"ATAM" | 84 |
| F7 | "architecture erosion" +software | 144 |
| F8 | "architectural technical debt" | 109 |
| F9 | "mirroring hypothesis" +"Conway" | 3 |
| F10 | "agile" +"up-front architecture" | 6 |
| F11 | "modular monolith" +microservices | 19 |
| F12 | "design patterns" +maintenance +"controlled experiment" | 17 |
| F13 | "fitness functions" +"evolutionary architecture" | 14 |
| F14 | "large language models" +"software architecture" +design | 95 |
| R13 | "design reasoning" +"software architecture" | 17 |
| R14 | "cognitive biases" +"software design" | 10 |
| R15 | "socio-technical congruence" +software | 57 |
| R16 | "architectural debt" +"design rule" | 4 |
| R17 | "decision making" +"software designers" +empirical | 11 |
| Total | 31 strings | 1,804 |

- R strings: the top 5 to 10 hits by citations were read by title (101 titles; R13 to R17 ran in the second pass).
- F strings: counts only; they test the scope of each field name. Their works were found through the leads and the reviews, not through screening these lists.
- Leads: each lead of the brief was looked up in Crossref by title and authors, three ways (title, authors, venue); a DOI is cited only when title and year matched.
- Leads restored in the second pass:
  - Shaw and Garlan 1996 (library record and table of contents);
  - Tang and colleagues, Razavian, Mohanani and Zannier (design reasoning);
  - Cataldo and Mauerer (congruence);
  - Kazman 2015, Mo 2015 and Nayebi 2019 (architectural roots);
  - Forsgren 2018 (publisher page; it does not mention architecture, so the claim stays with DORA 2025).
- Leads still not reached: the abstract of Stevens 1974, Ameller 2013, Kazman 2000, Baabad 2020 and Di Francesco 2018. Only a summary line was reached for Tang 2010 and 2015, Zannier 2007, Cataldo 2008 and Dobrica 2002. The full text of Parnas 1972 was not reached. The reasons are in sources.md.
- Snowballing: backward from Zhang 2012, Li 2022 and Esposito 2025 by abstract only; forward snowballing was not done. Both are partial.
- Routes used to read abstracts, none needing an identity:
  - the Semantic Scholar paper endpoint (abstract and summary line);
  - Crossref's abstract field;
  - a general web search whose summaries paraphrase the abstract;
  - the research groups' own pages and preprint abstract pages. Publisher copies, SEI and DTIC reports and several author pages answered 403 or refused the connection; no PDF was saved.

## 5. Grey search

- Types and producers, chosen because the questions are about practice:
  - practitioner articles (Fowler, Thoughtworks);
  - company engineering blogs (Segment, Shopify);
  - a standards summary (ISO) and vendor guidance (Azure, AWS);
  - a research programme page (DORA) and an industry survey (O'Reilly);
  - books by publisher page, and GitHub repositories for adoption counts.
- Engine: a general web search engine, first result page per string (about 10 results). Results personalise and change.

| Id | String as run (abridged) | Result |
|---|---|---|
| G1 | company moved from microservices back to monolith lessons learned | Segment and Istio leads |
| G2 | architectural fitness function evolutionary architecture Thoughtworks Radar | ThoughtWorks 2017 |
| G3 | Team Topologies Conway inverse Conway maneuver practitioner experience | summaries only; no new primary |
| G4 | O'Reilly microservices adoption survey 2020 | Loukides 2020 |
| G5 | Prime Video monolith 90% cost | primary page moved; secondary write-ups only; not included |
| G6 | ISO/IEC 25010:2023 characteristics | ISO 2023, secondary summary |
| G7 | ADD 3.0 steps | Cervantes 2016 table of contents, by search listing |
| P | direct visits to named producers: practitioner articles, company blogs, guidance pages, a survey, a research page, an author's page, 6 publisher book pages | 19 pages read; 5 not read (SEI page 404, ISO page refused, Prime Video page moved and its archive blocked, two book pages refused) |

### Q/A sites

Strings AR1 to AR15 ran on 2026-10-29, one reviewer, grey tier 2. The four Q/A searches share their stopping parameters, API call, reading and scoring, and common limits; these are in the [architecture-descriptions protocol](../architecture-descriptions/protocol.md#q-a-sites). Fixed parameters here: Stack Exchange API 2.3, `search/advanced`, `order=desc&sort=votes&pagesize=30`, no key, no login; the first 12 titles of each list were read.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| AR1 | `q=software architecture design process` | Software Engineering Stack Exchange; Stack Overflow | 60 | 1 | 1 |
| AR2 | `title=modular monolith` | Software Engineering Stack Exchange; Stack Overflow | 27 | 1 | 1 |
| AR3 | `title=microservices monolith` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AR4 | `title=Conway's law` | Software Engineering Stack Exchange; Stack Overflow | 2 | 1 | 1 |
| AR5 | `title=information hiding` | Software Engineering Stack Exchange | 5 | 1 | 1 |
| AR6 | `title=coupling cohesion` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AR7 | `title=microservices` | Software Engineering Stack Exchange | 30 | 3 | 3 |
| AR8 | `title=monolith` | Software Engineering Stack Exchange | 30 | 1 | 1 |
| AR9 | `title=coupling` | Software Engineering Stack Exchange | 30 | 2 | 2 |
| AR10 | `title=cohesion` | Software Engineering Stack Exchange | 24 | 0 | 0 |
| AR11 | `q=Conway's law team structure architecture` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AR12 | `title=big design up front` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AR13 | `title=architectural debt` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AR14 | `title=architectural patterns` | Software Engineering Stack Exchange | 6 | 0 | 0 |
| AR15 | `title=layered architecture` | Software Engineering Stack Exchange | 30 | 1 | 1 |
| Total | 15 strings | | 244 | 11 (distinct) | 11 |

- Twelve threads were opened and read with their top two answers; 11 are included; one (cohesion and coupling, a textbook definition) was excluded as a how-to.
- Scoring uses the shared rules (A1, A3 by reputation, M2, I, T, D). Below the threshold of 10: 1 (SO 2010c); it stays an example of practice only.
- The run ended after AR15. The last string that added a new included thread was AR15.
- Limits specific to this search:
  - strings with a phrase in `title` returned 0 to 6 results and were read as weak queries, not as absence;
  - the Stack Overflow site was searched only with AR1, AR2 and AR4;
  - the strings of Q9 return mostly how-to threads on data and transactions, which are in system-design.

## 6. Stopping rule

- Fixed before searching: effort bounded at N = 10 results per string, with saturation at k = 5. Five consecutive results adding no new concept end a string; G3 ended this way.
- Formal: effort bounded (top 7 to 10 per review string); the leads were checked one by one.
- Q/A: the parameters are in the subsection above; the run ended after AR15.

## 7. Selection

- Include: a source on the choice of structure of one software system, its method, principle, evaluation, change or cost; English; readable on the search date.
- Exclude:
  - documenting the architecture (architecture-descriptions), decision records (design-decisions), distributed runtime behaviour (system-design), specification languages (algorithm-design);
  - function-level planning for code generation (algorithm-design);
  - vendor posts selling a product.
- Grey sources must also pass section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- Criteria, tier scale and threshold (10 of 20): as in the [evidence method](../README.md#method).
- Tiers as applied here: books, magazines, standards, vendor guidance and reports are tier 1; project documentation and Q/A sites are tier 2; blogs are tier 3.
- Under the threshold a source is only an **example of practice**; no claim rests on it.
- A company page is its owner's claim about itself; the review says so.
- Books not opened are listed but not scored; no claim rests on them.

## 9. Extraction and synthesis

- Extraction and synthesis follow the [evidence method](../README.md#method); the synthesis runs by question, Q1 to Q10.

## 10. Limits

- The limits shared by every review are in the [evidence method](../README.md#method).
- One reviewer; no second rater was used.
- OpenAlex and arXiv counts are missing.
- No abstract was reached for 11 works (located only, or a summary line). For 18 more it was read in a search summary, not in the source. A number read in such a summary is marked "(secondary)".
- Forward snowballing was not done.
- Q/A threads: one scorer.
