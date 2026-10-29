# Algorithm design: how an algorithm is designed and its behaviour stated before it is coded

Question: how is an algorithm designed and its intended behaviour stated before it is coded? The aim is that an implementer, a person or a model, builds it correctly and a reader can check it. The review asks what the evidence says about the methods.

| Steps | [frame](frame.md) | [review](review.md) | [state of the art](state-of-the-art.md) | [position](position.md) | [against](against.md) | [baseline](baseline.md) | [protocol](protocol.md) | [sources](sources.md) | [bibliography](../bibliography.md) |
|---|---|---|---|---|---|---|---|---|---|

Method: a multivocal literature review after Garousi 2019 (see the [evidence method](../README.md#method)), one reviewer, searched on 2026-10-29.

- Scope: published research and public practice.
- It holds 78 formal and 24 grey sources, 102 in all. The grey ones are 8 from the web and repositories and 16 threads from Q/A sites. Four of them fall below the threshold of 10 out of 20 (2 web pages, 2 Q/A threads) and are used as examples only.
- It makes no claim to be a standard, a new result or the state of the art.
- A number read only in an abstract or summary is marked "(secondary)"; a source read by title only supports no claim.
- It stops where [pseudocode](../pseudocode/README.md) starts (presenting an algorithm to a reader); TLA+ at a cloud provider is reviewed in the system-design topic.

## Claims

| Claim | Grade | Where |
|---|---|---|
| Research on teaching algorithm design is thin: 94 papers in one database, 17 with controlled trials | measured, descriptive (systematic review, preprint, read in part) | review.md 0 |
| Students under-use recursion and reduction and over-use greedy methods, as reported across earlier studies | measured, descriptive (secondary to the cited studies) | review.md 1 |
| Explicit teaching of a problem solving process raised productivity, independence and self-efficacy in 48 high school students | measured, one study, small | review.md 1 |
| No test of whether a taxonomy of design techniques is sound or predictive was found | measured, descriptive (this search) | review.md 1 |
| Methods with assertions had significantly fewer defects in 100 popular C and C++ projects; the authors call the effect small | measured, observational | review.md 3 |
| In one air traffic control system, formal design showed no quantitative quality gain over informal design, and formal specification gave testable components | measured, case study, one system (read) | review.md 3 |
| A student quasi-experiment found the formal group passing more tests (6 teams all six tests; 45.5% of 11 control teams) and was criticised for volunteer, non-random groups | measured, quasi-experiment (secondary, as described by its critics) | review.md 3; against.md |
| In 62 industrial projects formal techniques were reported to raise quality in 92% of cases; the sample is self-selected | measured, descriptive, biased | review.md 3 |
| Strong specifications found twice as many bugs as standard contracts when testing data structures (the authors' method) | measured, one group (secondary) | review.md 3 |
| Contracts are used less than expected in the 200 most popular Java projects of one repository | measured, descriptive | review.md 5 |
| Programmers judged incorrect generated assertions at 49% and correct ones at 74%, with equal confidence (86 programmers) | measured, controlled, preprint | review.md 4 |
| Property-based testing is valued for complex code and costly to write, in 30 interviews at one firm | measured, descriptive | review.md 5 |
| Self-planning and structured reasoning raise Pass@1 on function-level benchmarks; an independent study gives 2.5 to 4.4 points over six models (its text says 5 to 12%), and naive chain of thought can lower accuracy | measured, benchmarks | review.md 7 |
| Asking for tests to clarify intent raised Pass@1 by about 22 to 54 points with Codex, with an idealised simulated user | measured, benchmarks (abstracts and tables; the follow-up's abstract, text and table disagree) | review.md 7 |
| GPT-4, in five attempts, produced a verified Dafny method with a strong specification for 58% of 178 problems with a chain of thought plus retrieval prompt, and 19% with no context | measured, benchmarks (table read) | review.md 7 |
| Experts agree: 62.3% of 130 responses say trustworthy design without formal methods is probably or definitely not possible | measured, descriptive, experts in the field | review.md 5 |
| Spec-driven tools have large adoption (143,670 stars on one) and their pages report no effect | adoption measured, descriptive; effect convention, untested | review.md 7 |
| Ways to state behaviour (triples, contracts, derivation, models) have not been compared on a measured outcome | convention, untested | review.md 2 |
| A specification before coding bounds scope and marks completion, and no natural language one is fully unambiguous | convention, untested (Q/A answers) | review.md 8 |

## Named baseline

- Design: the hierarchical taxonomy of design techniques (Levitin 1999 and Levitin 2000, both read in full). Fallback: the technique chapters of Kleinberg 2005 or Skiena 2020, cited from their publishers' pages.
- Specification: a precondition and a postcondition, plus an invariant for each loop (Hoare 1969; Meyer 1992).
- Method taught: the design recipe (HtDP 2026).
- Comparison: tasks for people and for models, crossover designs, effect sizes (baseline.md).

## General principles linked, not reviewed again

- [Define before use](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/define-before-use.md)
- [Worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/worked-examples-with-subgoals.md)
- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/overview-first.md)
- Readers that are models: the [LLM readers review](https://github.com/Tewf/reader-ergonomics/tree/40cd9fb3ed21a01a8913788edc46ade9562a797d/evidence/llm-readers).
