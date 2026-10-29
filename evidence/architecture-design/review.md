# Review

This file reads the literature on choosing the structure of one software system, by strand.
The strands run in this order:

- existing reviews
- methods
- modularity
- patterns
- quality attributes and evaluation
- up-front design
- organisation
- erosion and debt
- monolith and services
- practice
- Q/A sites
- designing for a model
- how architects reason

The mark "(secondary)" flags a result read in a summary of an abstract or in another source, not in the paper. A work whose row in [sources](sources.md) says "located only" supports no result here. Grey scores are in [sources](sources.md); a source under 10 of 20 is named "example only".

## 0. Existing reviews

- Zhang 2012 (abstract read): a mapping of studies on the 23 Gang of Four patterns, to 2009. Of 611 candidate papers, a final set of 10 holds 11 formal experiments; 7 experience reports were added.
- Li 2022 (abstract read): 73 studies of architecture erosion; non-technical reasons deserve the same attention as technical ones.
- Mohanani 2020 (preprint abstract read): 65 articles on 37 cognitive biases in software engineering; few studies of how to mitigate them.
- Vera-Rivera 2021 (abstract read): 29 of 326 papers on microservice granularity; runtime properties are studied more than maintainability.
- Su 2024 (abstract read): a multivocal review of four returns from microservices to a monolith; the reasons are cost, complexity, scalability, performance and organisation.
- Mumtaz 2021 (abstract read): detection of architecture smells; many smells have no tool and empirical validation is limited.
- Falessi 2011, de Silva 2012, Besker 2018 (abstracts read in summaries, secondary). Their findings: there is no best decision technique; no single strategy stops erosion; a unified model of architectural debt exists.
- Babar 2004 (full text, an author copy in a university repository): four scenario-based evaluation methods compared; five common activities form a generic evaluation process.
- Dobrica 2002 (abstract read) compares eight representative architecture analysis methods.
- Baabad 2020 (read): a review of 74 primary studies of architecture degradation in open source; rapid evolution, frequent changes and developers' lack of awareness lead its causes.
- Tofan 2014 maps architectural decisions; reviewed in [design-decisions](../design-decisions/review.md), linked here.
- No tertiary study of software architecture design was found.

## 1. Design methods (Q1)

- Hofmeister 2007 (full text, through a library): five industrial methods share one general model, though they use different vocabulary; the model gives an evaluation grid for comparing methods (Section 5, Table 4).
- Cervantes 2016: ADD 3.0, a repeatable method around business goals and quality attributes; book not opened.
- ADD 3.0 iterates over drivers; its steps, from a table of contents, run from reviewing inputs to analysing the current design.
- Falessi 2011 (secondary): no technique is best; pick one by the difficulties to avoid.
- Nothing found compares ADD with no method in a controlled study.

## 2. Modularity: what division predicts (Q2)

- Parnas 1972 (abstract read in a summary, secondary): modularisation helps flexibility and comprehension depending on the criterion for division; shown on one small indexing problem with a conventional and an unconventional decomposition.
- Stevens 1974 (located only) introduced coupling and cohesion; Baldwin 2000 (book, not opened) is the theory of modularity behind the later measures.
- Basili 1996b (abstract read): in eight systems from identical requirements, several object-oriented design metrics predicted fault-prone classes better than traditional code metrics.
- Briand 2000 (secondary): coupling, cohesion and inheritance measures in a model that classified over 80% of classes correctly and found over 90% of the faulty ones; size, method invocations and inheritance depth drive fault-proneness.
- MacCormack 2006 (abstract read): with dependency matrices, Linux was more modular than the first Mozilla; Mozilla's redesign became more modular than both.
- Xiao 2014 (abstract read): in three large open source projects, a few design rule subspaces capture the error-prone files.
- Mo 2015 (secondary): hotspot patterns find the most error-prone and change-prone files in nine open source projects and one commercial project.
- Mo 2016 (secondary): a decoupling level over 108 open source and 21 industrial projects; a larger level means better maintainability, measured by proxies from revision history (change locality), not by effort.
- These are observational: they show prediction, not that restructuring lowers change cost.
- Müller 2020 (grey): Shopify made a 2.8 million line monolith modular; every component depended on over half of the others at the start.
- No controlled study of Parnas's criterion itself was found.

## 3. Styles and patterns (Q3)

- Shaw 1996 (book, not opened): its second chapter, from the table of contents in a library record, treats architectural styles such as pipes and filters, layers, repositories and event-based invocation.
- Prechelt 2002: two experiments with pattern documentation; 74 German graduate students with Java and 22 American undergraduates with C++ (secondary, draft abstract); pattern-relevant tasks were faster and had fewer errors.
- Prechelt 2001 (abstract read): professionals on nine maintenance tasks. In most tasks the pattern design cost no extra time or saved time against a simpler design, and in a few the simpler design was better.
  - A well-justified Observer use showed a negative effect; a Decorator use showed a positive effect despite unneeded flexibility.
- Vokac 2004 (secondary): a 500,000 line C++ product followed weekly for three years; defect rates of pattern classes ranged from 63% to 154% of the average.
- Khomh 2008 (technical report abstract, secondary): several quality attributes were affected negatively by patterns; the authors advise caution.
- Zhang 2012: firm support for the claims made for patterns in general could not be identified.

## 4. Quality attributes and evaluation (Q4, Q5)

- ISO 2023c: the product quality model of ISO/IEC 25010 has nine characteristics (read in a summary of the standard).
- AWS 2026d: six pillars; the page speaks of none of structure, modularity or coupling.
- Ameller 2013 (how architects consider non-functional requirements) is located only. Kazman 2000 (ATAM, read in full) is a method report with one case, not a test of effect. Babar 2004 and Dobrica 2002 compare methods (strand 0).
- Bellomo 2015 (abstract read): ATAM data over 31 projects; modifiability dominates in every kind of project, followed by performance, availability and interoperability; deployability rises in IT projects.
- No controlled study that evaluation before building improves the finished system was found.

## 5. How much up front (Q6)

- Abrahamsson 2010 (introduction read in a summary): architecture has a role in widening agile development; the abstract was not reached in full.
- Waterman 2015 (abstract read): grounded theory from 44 participants; six forces and five strategies decide how much up-front design is enough.
- Boehm 2008 (abstract read): from 161 projects, the cost gap between minimal and very thorough architecture and risk work is about 18% for small projects and 92% for very large ones.

## 6. Structure and the organisation (Q7)

- Conway 1968: organisations that design systems produce designs that copy their communication structures (reprint, conclusion).
- Colfer 2016 (full text, open access; MacCormack 2012 tests the same hypothesis, abstract partly read): mirroring predicts organisational ties that match technical dependencies. Of 142 studies, the descriptive industry and firm studies gave strong support in 70%, partial in 22% and none in 8%. In open collaborative projects, mostly software, 56% of the descriptive studies did not support it.
- Nagappan 2008 (abstract read): in Windows Vista, organisational metrics predicted failure-proneness and beat traditional metrics in precision and recall.
- Herbsleb 1999 (secondary): a case study of a distributed project; coordination suffered across sites as informal communication broke down.
- Cataldo 2013 (secondary): in two large projects from two companies, mismatch between required and actual coordination went with more failures and higher congruence with better productivity.
- Cataldo 2008 (summary line, secondary): modularisation has limits, so the work measures congruence between technical and work dependencies.
- Mauerer 2022 (abstract read): 25 large open source projects; socio-technical motif congruence was not related to bugs or churn in any temporal scenario.
- DORA 2025 (grey): loosely coupled teams depend on both architecture and team structure, designed together; no effect size is on the page.
- Forsgren 2018 (book, not opened): the publisher page says four years of research and rigorous statistical methods; the page does not mention architecture or the survey design.
- ThoughtWorks 2014 (Trial) and Skelton 2025 (book, not opened): shape the teams to get the structure wanted.

## 7. Erosion and architectural debt (Q8)

- Li 2022: erosion shows as violations and structural issues and also as quality and evolution problems.
- de Silva 2012 (secondary): three categories of control (minimise, prevent, repair), none sufficient alone; Le 2018 (located only) studies decay in open source.
- Verdecchia 2021 (abstract read): a grounded theory and focus groups give a model of architectural debt.
- Ernst 2015 (secondary): in a survey of 1,831 participants, architectural decisions ranked first as a source of technical debt.
- Kazman 2015 (secondary): in an industrial project, design rule spaces located files tied by architecture flaws, and economic models of the before and after states showed a return; no numbers were read.
- Nayebi 2019 (abstract read): a longitudinal case at one company, in three phases around a refactoring; improvements were quantified, no figures in the abstract.
- Fitness functions turn a structural rule into an automated check (ThoughtWorks 2017, Trial). Packwerk blocks pull requests that cross component boundaries (Müller 2020), and ArchUnit asserts architecture rules as tests. Adoption counts are in sources.

## 8. Monolith, modular monolith, microservices (Q9)

- Lewis 2014 defines microservices by nine characteristics and says it is too early to judge how they mature.
- Fowler 2015 advises a monolith first and says the evidence is sparse.
- Taibi 2017 (abstract read; it gives no count, and the listings disagree on 17 or 21): interviews with practitioners who migrated; maintainability and scalability drove migration; decomposition and data splitting stayed hard.
- Blinowski 2022 (abstract read): controlled experiments on one reference application; on one machine the monolith performed better, and vertical scaling was more cost-effective in the Azure cloud.
- Ghemawat 2023 (abstract read): argues microservices conflate logical and physical boundaries and proposes writing logical monoliths that a runtime distributes. A prototype cut latency up to 15 times and cost up to 9 times against the status quo (a company prototype).
- Mendonca 2021 (abstract read) and Noonan 2018: two companies moved from services to a monolith, each reporting its own decision; Noonan counts over 140 services merged.
- Di Francesco 2018 (full text): 18 practitioners in 16 companies who had migrated to microservices, after 5 exploratory interviews. The challenge named most was coupling in the old system (9 of 18), then finding service boundaries (7). To understand the old system they used its source code (13) and tests (11), architectural and textual documents (11 each), box-and-line diagrams (9) and UML diagrams (5).
- Loukides 2020: of 1,502 respondents recruited from mailing lists, over 23% do not use microservices, so at most 77% do; 92% of the respondents report some success.
- Prime Video's report of a 90% cost fall was read only in secondary write-ups; Su 2024 lists it among four cases.

## 9. Practice

- Most adopted structures: layered or n-tier, microservices, event-driven, as vendor guides list them, with when-to-use advice and no study (Microsoft 2025); Team Topologies 2026 (example only) cites "years of research" without a study.

## 10. Q/A sites

- SESE 2017h (108 votes): a microservice split moves organisational dysfunction from compile time to run time; another answer says components can be decoupled inside one deployment.
- SESE 2018d: for a sole developer, microservices turn the software into a distributed system.
- SESE 2020b: independent deployability is the aim; shared libraries break it.
- SESE 2025a: a team of five with about 200 services is told it decomposes to an absurd degree.
- SESE 2020c: names the **majestic monolith**, a single deployable with isolated modules.
- SESE 2012k and SESE 2020d: coupling and cohesion are measured by LCOM4, afferent and efferent coupling and instability; low coupling is a trade-off, not a rule.
- SESE 2011k and SESE 2022b: information hiding protects users from members that still change; layered and hexagonal differ in the direction of dependencies.
- SESE 2014d and SO 2010c (example only): teams hold the line between design and architecture as semantics; one answer says Conway's law holds by default.

## 11. Designing for a model as implementer (Q10)

- Schmid 2025: generating source code from an architectural design is underexplored; approaches mostly use simple prompting.
- Esposito 2025: generative AI is used mostly for decision support, reconstruction and architecture to code; testing of outputs is typically missing.
- Generating decision records with a model, the subject of [design-decisions](../design-decisions/README.md), which does not review these two yet:
  - Dhar 2024 (abstract partly read): a model generates decision records from a decision context, zero-shot, few-shot and fine-tuned.
  - Su 2026 (abstract partly read): 980 decision records across 109 repositories; models screened and validated decision violations.
- Li 2024: a benchmark over the whole life cycle, including design; current models, GPT-4 included, fail its challenges.
- Hong 2023: structured roles and documents between agents give more coherent solutions than chat-based systems (a preprint; abstract).
- Function-level planning before code is in algorithm-design; repository context files in [architecture-descriptions](../architecture-descriptions/review.md) (Gloaguen 2026).
- No study was found that gives a model an architecture and measures the architectural quality of the code returned.

## 12. How architects reason while designing (Q11)

- Zannier 2007 (summary line, secondary): in interviews, the more structured the design decision, the less a designer considers options; rational and naturalistic modes both appear.
- Tang 2010 (summary line, secondary): design planning, context switching, problem-solution co-evolution and reasoning techniques influence design effectiveness.
- Tang 2012 (secondary): two teams designing a traffic simulator; design strategy influenced effectiveness and should match problem complexity.
- Tang 2015 (summary line, secondary): most subjects needed only a few reasons before deciding, a satisficing behaviour.
- Razavian 2016 (abstract read, through a library): multiple case studies with 12 student groups; external reflection improved the quality of design discourse under preconditions.
- Mohanani 2020: cognitive biases are studied more than their mitigation; theory is poor.
