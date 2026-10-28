# Evidence against and open controversies

This file gathers the evidence against the rules on architecture descriptions: null results, disputed studies, and practice that a study contradicts.

## Against the view and viewpoint model

- 42010 requires no viewpoint and no format, and its authors do not claim that conformance gives better systems (ISO 2022). It is a framework for choosing, not a tested remedy.
- Readers ask for content fitted to their task (Rost 2013); a fixed set of views is a supply-side answer to a demand-side wish.
- Rozanski 2011 argues that one overloaded model fails every reader. This is an argument from experience, graded convention, untested.
- Open-source projects mostly keep a single, informal view with no legend (Migliorini 2024), so the multi-view ideal is rarely met in practice.

## Against the view model for developers

- Rost 2016 argues in its title that splitting a description by concerns is counterproductive for developers with a task; a later thesis reports better retrieval with a generated task excerpt (search summary, secondary). The full conference text was not read.

## Against structure as the lever

- The controlled comparison found (Ernst 2023) saw no significant effect of structured against essay format. Prior familiarity with the code mattered more. An earlier experiment found no overall difference between text and diagram descriptions; those who mostly used text scored better (Heijstek 2011, secondary).
- Participants rated the structured format easier to navigate (80% against 55%) and more useful for coding (83% agreeing), but the difference was not significant.
- The authors suggest the essay may suit overviews and the structured format coding tasks: format and task interact, which one reader style cannot satisfy.

## Limits of the one experiment

- Students, not professionals, with 18% non-participation.
- One system of 10 kSLOC and about 800 words (Views and Beyond) or about 1,000 (essay) per document.
- The two universities differed in familiarity with the system and in training in the structured format, so site and familiarity are partly confounded.
- Participants knew a comparison was being made (observer expectancy).
- Only Views and Beyond was tested, not arc42 (Starke 2026), C4 or a codemap.
- A result that is not significant in 65 people is not evidence that formats are equivalent.

## Against documentation as the answer

- Engineers consulted documentation in 3% of logged events, much below their own report (Lethbridge 2003; figure not checked).
- A document added to a live project had mixed effects (Kazman 2016); the issue tracker already served core members.
- Design documents helped correctness on complex tasks but did not save time, and the update effort cancelled simple tasks (Arisholm 2006, Dzidek 2008; secondary).
- Oral explanation is the working route when documents are incomplete (Rukmono 2026); the document competes with a person.

## What the Q/A threads add against

- Against documentation as the answer:
  - SESE 2010b: formal architecture documents fall by the wayside, and an openly communicating team beats them.
  - SESE 2011a: large open-source projects ship no architecture document and readers go to the code (the two top answers have 19 and 12 votes).
  - SESE 2017c: tests and code carry part of the design, and design before code was never the ideal.
  - They agree with the practice caveats below and with Ernst 2023 being a single experiment. They are opinions with no data.
- Against the view model for developers: SESE 2017a (second answer) says UML is a poor fit for real architectures and proposes data-flow diagrams. SESE 2014b: for the structure of a program, show many code examples. Both are single answers.
- C4 and arc42 limits:
  - SO 2021a: C4 is a simple abstraction for early work and team talk, not for process or infrastructure; its supplementary diagrams or other notations cover those.
  - SO 2014a and SO 2014b: arc42 users disagree on where a database schema goes and on how to keep the target architecture apart from the current one (decisions and constraints chapters). A template of twelve sections still leaves placement open (Q5, how a reader finds information).

## Against the practice evidence

- arc42's claim to be proven in practice since 2005 and Spotify's claim that its documentation plugin's popularity shows success are owners' statements about themselves.
- IcePanel 2025 comes from a vendor of C4 tooling, with 75 respondents, 57% of them architects; its year-on-year differences were mostly not significant.
- Jongeling 2025 is one company's report on its own change, with no control group.
- The ten-times claim in matklad 2021 is an anecdote by a maintainer, not a measurement.
- No adoption count for ARCHITECTURE.md or arc42 was found; a platform search count was unstable and is not used. The arc42 authors say they know no statistically relevant numbers (Starke 2026b); repository stars are a weak signal.
- Eight of the 41 grey sources score below 10 of 20 (sources.md). They are examples of practice only: the arc42 site, Backstage 2020, IcePanel 2024, the C4 FAQ, a vendor blog and three Q/A threads.
- IcePanel 2024 and 2025 disagree on the 2024 shares. The page of 2025 restates the 2024 wiki share as 29%; the 2024 page gave 30%. Year-on-year figures are read only where the vendor tested them.
- The reviews and the Helsinki thesis were read through abstracts; findings drawn from them are marked secondary.

## Against overviews for machine readers

- Gloaguen 2026 found repository overviews unhelpful to coding agents in two settings (SWE-bench and a new set of repositories with developer files), while Zarzycki 2026 finds them in many files. The reader is a model, and the finding may not transfer to people or to other tasks.

## Open controversies

- **Standardise or tailor:** one template for all readers against a document per task.
- **Complete or short:** Lethbridge 2003 and matklad 2021 point to short and stable; the standards point to complete coverage of concerns.
- **Notation independence:** C4 is notation independent, yet respondents report teams reading its levels differently (IcePanel 2025).
- **Document or tool:** a document under version control against a model in a tool with generated views; Rost 2013 argues for generation, practice favours Markdown beside code.
