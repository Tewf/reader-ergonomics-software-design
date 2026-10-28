# Review

This file reviews the literature on architecture descriptions by strand: existing reviews, surveys, standards and models, readers and their needs, experiments, what projects write, then practice. The pool and its scores are in [sources](sources.md); the method is in [protocol](protocol.md).
A number marked (secondary) was read in an abstract or a summary only; the others were read in the paper. Grey sources below 10 of 20 are marked "example of practice" and support no claim.

## 0. Existing reviews

Nineteen secondary studies were found; none was read in full. The abstract (or a search summary) was read for ten, the title only for nine.

- **Closest to this topic:**
  - Ding 2014a: 60 studies on knowledge-based approaches in software documentation, with an emphasis on architecture documentation (secondary). Architecture understanding is the top benefit found; the cost of retrieving information is the main concern.
  - Weinreich 2016: 56 approaches to architecture knowledge management in 115 studies, 2004 to 2015 (secondary). Most approaches serve using captured knowledge, which is also the best validated activity; capture and maintenance are weak.
  - Júnior 2019 maps descriptions based on 42010 (title only). Guessi 2012 and Guessi 2015 review descriptions of embedded systems and of systems of systems (title only).
  - Viglioni 2024 maps executable architecture descriptions, 45 studies (secondary).
  - Li 2013, Nakagawa 2010 and Farenhorst 2009 map knowledge-based approaches and the state of architecture knowledge management (titles only). Capilla 2016 looks back over ten years of the field (title only).
- **Documentation in general:**
  - Zhi 2015: 69 papers from 1971 to 2011 on the cost, benefits and quality of development documentation (full text read).
  - Theunissen 2022: 63 studies on documentation in continuous development; the practices found include architecture frameworks, and it recommends minimal documentation upfront (secondary).
  - Islam 2023: 74 studies on agile documentation (secondary).
- **Architecture information:**
  - de Dieu 2024: 104 studies on mining architectural information. Architectural description is the most mined kind, and architecture understanding the most supported activity (secondary).
  - Soliman 2025 maps mining repositories for architecture (title only).
- **Readers who are newcomers:**
  - Steinmacher 2015: 20 studies of barriers faced by newcomers to open-source projects, 15 barriers in five categories, one of them documentation (full text read; 291 studies retrieved from 4 libraries).
  - Santos 2025: 32 studies of software solutions for onboarding (secondary).
  - Ribeiro 2026 is a multivocal review of onboarding (title only).
- **Grey and formal together:** Harhio 2022 (a thesis) reviews 36 sources on documenting architecture design decisions, 17 scientific and 19 grey. Twelve of the 19 grey sources concern decision records; it finds no single method best, since suitability depends on the project.
- **How this review differs:**
  - Their subjects are notations, knowledge tools, documentation in general or mined information. This review asks how the written account is divided and entered for a reader.
  - It scores the grey sources and reads practice beside research.
  - It ends on a named baseline and a measurement plan.
- This search did not find a systematic review whose subject is the organisation of an architecture description for its reader.

## 1. Surveys

- Malavolta 2013: interviews with 48 practitioners from 40 companies in 15 countries about architectural languages (secondary). Practitioners were satisfied with design features and not with analysis; the languages used mostly came from industry, not research.
- Aghajani 2019 mined 878 documentation artefacts into a taxonomy of documentation issues (secondary).
- Aghajani 2020 surveyed 146 practitioners on issues and on which documentation types help which tasks, software structure and architecture design among the tasks (secondary).

## 2. Standards and models

- Perry 1992 opened the field. Soni 1995 surveyed industrial systems and found four structures: conceptual, module interconnection, execution, code (secondary).
- Kruchten 1995 proposed five concurrent views: logical, process, development, physical, and scenarios that tie them together.
- Clements 2010 (Views and Beyond): document by views of three kinds (module, component-and-connector, allocation) plus information that applies across views. The SEI template opens with a roadmap and ends with mappings between views, referenced material and a glossary (outline read in a summary, secondary).
- Rozanski 2011: a catalogue of viewpoints (context and six core ones) and cross-cutting perspectives. It argues against one overloaded model.
- ISO 2022 (42010, second edition): a conforming description identifies stakeholders and concerns, and defines viewpoints that frame them. It gives views, records correspondences between views, and gives rationale for key decisions (requirements as listed for the 2011 edition, ISO 2022 FAQ).
- The second edition (2022) adds stakeholder perspectives, architecture aspects, and entity of interest in place of system of interest.
- 42010 defines no required viewpoint and no format; its authors do not claim that conformance gives better systems, only more understandable descriptions.
- Emery 2009: every description needs a framework, meaning the conventions that choose the viewpoints.
- Grade of all of the above: convention, untested for reader outcomes.

## 3. Readers and their needs

- Lethbridge 2003 (three studies, one a survey of 48 engineers at a telecom company, 25 answering the timing question; full text read, figures checked against the paper):
  - Documentation is often not updated; stale documentation is still useful (81% of 45 respondents agreed: 53% somewhat, 28% strongly).
  - The more abstract a document, the more engineers trusted it; accuracy and consultation correlated at 0.41 for architectural documents (p < .05).
  - 61% rated documentation effective for learning a system, 46% for big-picture information, 35% for maintaining one.
  - In observation they consulted documentation in 12 of 357 logged events (3%), which the authors read as use even lower than the survey reported.
- Rost 2013: survey of 147 industrial participants (46% developers, 23% architects, 20% managers).
  - Overall quality rated average by 48%, good by 29%, poor by 18% (N=106).
  - Top problem in finding information, in open answers: unclear structure (13 answers; the table's N and percentage disagree). The top problem overall was outdated documentation (25).
  - Wishes: up to date (19 mentions), in sync with code (18), specific to stakeholder and task (14), a system overview (11), rationale (10).
  - Natural language and UML dominate; formal languages are rare; information is usually scattered across documents.
  - Lima Neto 2015 reports the 31 Brazilian respondents of the same 147 (abstract): they need updated documents with the right information, and want automation. It is the same survey, not a second sample.
- Dagenais 2010: grounded theory from 18 newcomers in 18 projects (secondary). Newcomers sought the architecture mostly for a broader view and to see where their task fitted (quoted in Ernst 2023).
- de Dieu 2022: survey of 103 developers on searching for architectural information (secondary). The top challenges were dispersion and abundance of sources.
- Wan 2023: interviews with 32 practitioners from 21 organisations; the challenges of architecture work centre on management, documentation, tooling and process (abstract, secondary).
- Manai 2019 (a student essay, two companies, 24 survey respondents, two interviews, two work diaries; abstract only): documents complement conversation; outdated and incomplete documents are the main complaint.
- Rukmono 2026: interviews with 17 professionals (9 explainers, 8 explainees) show that written documentation is incomplete, so teams explain orally; a good explanation fits the explainee's role, experience and goal.
- Grade: supported with caveat; all are perceptions, and the one behavioural number (3%) is below the stated use.

## 4. Experiments and field trials

- Ernst 2023: 65 students at two universities read about 800 words (Views and Beyond) or about 1,000 (essay) on a 10 kSLOC system, in 75 minutes. They then answered four questions from Bloom level I to VI.
  - Formats: Views and Beyond (9 headers, 13 list items, 6 links) against an essay (no headers); same content, three diagrams each.
  - Result: no significant association between format and score. Prior exposure to the code was the dominant factor (+0.95 points, 95% credible interval 0.28 to 1.68, on a four-point scale).
  - Navigability was rated favourable by 80% with the structured format and 55% with the essay; not significant.
  - Authors' reading: the essay may suit overviews and the structured format coding tasks.
- Heijstek 2011 compared text-dominant and diagram-dominant architecture descriptions in an experiment: 47 participants, no difference in efficiency between the media overall, and those who mostly used text scored better (abstract, secondary). Schoonewille 2011 observed developers thinking aloud over a design as text and as UML: over 60% of answers used one medium only (secondary).
- de Graaf 2016: two industrial case studies compared file and directory organisation with an ontology and wiki organisation. Better organisation correlated with retrieval efficiency and effectiveness (secondary).
- Rost 2016 argues that splitting a description by concerns makes it harder for a developer with one task, and proposes an excerpt generated for each task. A later thesis reports better efficiency and accuracy of retrieval (search summary, secondary).
- Kazman 2016: the authors wrote and publicised an architecture document for the Hadoop file system and tracked its effects. Results were mixed by measure; the issue tracker already held architectural discussion; newcomers and adopters still needed explicit documentation (secondary).
- Arisholm 2006 and Dzidek 2008 (UML design documents in maintenance, a different object from an overview): correctness improved on complex tasks. Dzidek reports +54% functional correctness and +14% time, the time difference not significant (secondary).
- Robillard 2016: interviews with 18 authors of essay chapters on open-source architecture, on what shapes their content (secondary).

## 5. What projects actually write

- Ding 2014b: of 2,000 open-source projects, 108 had some architecture documentation (secondary); natural language was the usual form.
- Muszynski 2022: six open-source systems; mostly natural language on websites and wikis; most stayed at the first maturity level (secondary).
- Migliorini 2024: 15 thousand architecture views from 12.2 thousand repositories (abstract only: no access to the chapter. The abstract confirms 15 thousand views and a sample of 373; the other figures here were not checked).
  - Most projects keep one view; 96% of 373 sampled views are informal, 7% of the views with colour carry a legend.
  - 75% of views are never updated; over 92% have one contributor.
  - 53% show the whole system and 53% are at a coarse granularity; deployment and control flow are the common viewpoints.

## 6. Practice (industry)

Owners' claims about themselves unless stated; grade convention, untested; an adoption count is measured, descriptive. Scores are in [sources](sources.md).

- **arc42** (Starke 2026, 9.5 of 20, example of practice; since 2005 by its own account): twelve sections, with a one-page canvas.
  - They run from Introduction and Goals through Context and Scope, Building Block View, Runtime View, Deployment View and Crosscutting Concepts, to Glossary.
  - Its FAQ says the authors know no statistically relevant adoption numbers and that use is mostly in German-speaking countries (Starke 2026b, 10 of 20).
  - The template repository had 1,315 stars on GitHub on 2026-10-28 (Arc42 2026a; measured, descriptive).
  - docToolchain 2026 (10.5) builds on it for docs as code and shows 872 stars, with four company logos as the adoption claim.
  - Knauf 2022 (10.5, a consultancy blog) is a worked docs-as-code setup with no data.
- **C4** (Brown 2026a, 10.5): four levels (system, container, component, code), notation independent.
  - Brown 2018 (10.5) adds that each diagram needs a title and a key; the C4 FAQ claims teaching to over 10,000 people but cites no study (Brown 2026c, 9, example of practice).
  - IcePanel 2025 (10.5, vendor survey, 75 respondents): 70% moderately or very confident with C4. Context diagrams were used by 81%, containers 79%, components 41%.
  - The rise in context use since 2024 was significant by the vendor's test. Keeping documentation current was the top challenge.
  - IcePanel 2024 (9, example of practice) had 96 respondents and no stated method.
  - Jongeling 2025: one embedded-software company, C4 in text diagrams beside the code; most of 48 respondents were positive two years on (abstract only).
- **ARCHITECTURE.md** (matklad 2021, 13.5): for projects of 10 to 200 thousand lines. A bird's-eye overview, a codemap that answers where the thing that does X lives, named invariants, boundaries, cross-cutting concerns; keep it short and to stable facts. The claim that finding the place to change costs ten times more for an outsider is the author's anecdote.
  - rust-analyzer's architecture page (Rust 2026c, score 11) follows that pattern: Bird's Eye View, Entry Points, Code Map, Cross-Cutting Concerns, with marked invariants.
- **Panels and books:** Penchikala 2009 (11, a panel of SEI and other authors) advises a defined purpose and audience, module, runtime and deployment views, a notation key, and short wikis over a weighty tome. Its speakers point to their own books.
- **Docs as code:** Backstage 2020 (8.5, example of practice) says its documentation plugin accounts for about 20% of Spotify's portal traffic, an owner's claim. Thoughtworks 2020 (10.5) put diagrams as code at Trial.
- **A vendor how-to** (Gliffy 2023, 4.5, example of practice) lists common mistakes with no data.
- **Agent context files:** Chatlatanagulchai 2025 (2,303 files, 1,925 repositories) found architecture content in 68.1%. Zarzycki 2026 found such files in 26.3% of 22,854 popular repositories; architecture in about 70% of instruction sets and a system overview in about 48% (corrected estimates).
  - Gloaguen 2026 tested context files on coding agents: no general gain in task success, over 20% more cost on average. Repository overviews were not helpful in two settings (SWE-bench and a new set of repositories with developer files).
  - De Luca 2026 generates a description from a repository, by a template taken from 42010, Views and Beyond and C4. 22 developers judged it valuable and broadly accurate; diagrams, context and deployment views were weak (abstract).
  - Larsen 2026 extends arc42 and C4 for AI systems; six practitioners rated coverage of one regulation, not reader outcomes (abstract). Elberzhager 2026 found model and architect ratings of documents agreed more when the document was better (abstract).
- Forward citations: Rost 2013 is cited by the OSS and view studies above and by de Graaf 2016. this search (sources.md, forward snowballing) found no citing paper that replicates Ernst 2023.

Q/A sites (Software Engineering Stack Exchange and Stack Overflow, searched 2026-10-28; 21 threads, scores in [sources](sources.md)). Opinion and experience, no data. Three threads score under 10 of 20 (SESE 2011b, SO 2011a, SO 2008a): examples of practice only.

- The threads mostly repeat what the pool holds from the owners: the 4+1 views, IEEE 1471, arc42, C4 and the stale-document warning. Four points are new.
- Which views practitioners name:
  - Two threads send a newcomer to the 4+1 views (SESE 2017a, SESE 2017b) and one to the IEEE 1471 chain of stakeholder, concern and viewpoint (SESE 2012a).
  - SESE 2014a (42,890 views on the day): the model fixes who needs which information, and no one-to-one mapping to UML diagrams exists. This agrees with the reading of the views as independent of notation; it adds no measurement.
- As-built, not as-intended (new):
  - SESE 2015a: a description of a system that exists states what the code does, calls out where it departs from the intended architecture and, where known, why.
  - Nothing in the pool states this. It bears on how a description is kept true (Q6).
- What belongs in a description (Q1):
  - SESE 2013a (top answer by a very high reputation answerer): technologies belong when they are hard to change, on the definition of architecture as what is hardest to change.
  - SESE 2011b says the same by level of document (solution architecture yes, enterprise architecture no), at 9.5 of 20: example of practice only.
- Event-driven systems (new, one thread): SO 2018a lists the events, says per component which it produces and consumes, and draws sequence diagrams only for the hard flows. One answer with 9 votes: an example of a form, not evidence.
