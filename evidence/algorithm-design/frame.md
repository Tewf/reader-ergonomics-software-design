# Frame: the problem and its names

This file states the problem of designing an algorithm and stating its intended behaviour, in one sentence. It then gives the names that research and practice use for the problem.

## The problem in one sentence

Decide how an algorithm is designed and how its behaviour is stated before any code. The full question, with its two kinds of reader, is in the [README](README.md).

## Two activities, one boundary

| Activity | Question | Output |
|---|---|---|
| **Design** | how is a solution found | a method, a plan, a derivation |
| **Specification** | what must the solution do | pre and postconditions, invariants, contracts, a formal model, properties |

- Presenting the result to a reader is the subject of [pseudocode](../pseudocode/frame.md); this review stops where that one starts.
- Wirth 1971 (stepwise refinement) is reviewed there; only its link to derivation is used here.

## What the field calls it

| Thing | Field name | Source |
|---|---|---|
| Families of solution methods | **algorithm design techniques**, paradigms, strategies | Levitin 1999 |
| General problem solving | **heuristic** (Polya 1945), **problem solving process** | Polya 1945; Loksa 2016 |
| Standard fragments of solutions | **programming plans**, plan composition | Soloway 1986; Spohrer 1985 |
| Method taught in a course | **design recipe** | Felleisen 2004 |
| Stating behaviour with logic | **axiomatic basis**, **Hoare triple**, precondition, postcondition | Hoare 1969 |
| Behaviour as a contract | **design by contract** | Meyer 1992 |
| Facts true at each loop pass | **loop invariant** | Furia 2014 |
| Building the program from its specification | **program derivation**, **correctness by construction**, **refinement calculus** | Dijkstra 1975; Back 1998; Kourie 2012 |
| Model-based notations | **formal specification**, Z, VDM, B and Event-B, Alloy, TLA+ | Abrial 2010; Jackson 2002 |
| Verification-aware language | Dafny | Misu 2024 |
| Properties run as tests | **property-based testing** (PBT), QuickCheck | Claessen 2000 |
| Engineering algorithms with experiments | **algorithm engineering**, **experimental algorithmics** | Sanders 2009; McGeoch 2012 |
| Spec handed to a model | **specification-driven development**, user-intent formalization | Piskala 2026; Lahiri 2024 |

## What practitioners call it

- "Design doc" and "write the spec first" in team talk; "assertions" and "guard clauses" for contracts without the name (SESE 2012l).
- "Property tests" or "QuickCheck-style tests" for PBT; "fuzzing" is a neighbour with its own literature, not reviewed here.
- **Spec-driven development** (SDD) for requirements, design and task files given to a coding assistant (Thoughtworks 2025; Kiro 2026; Spec Kit 2026).
- "Plan before you code" (SESE 2011l) for the informal version of everything above.
- The words differ more than the content: a specification is a statement of what, checked by something (a prover, a test, a reader).

## Review questions

| Id | Question |
|---|---|
| Q1 | Which design techniques are taught and used, and is their taxonomy sound? |
| Q2 | Does problem solving instruction (recipes, plans, stepwise design) improve the algorithms people produce? |
| Q3 | Which ways of stating intended behaviour exist? |
| Q4 | Do specifications improve correctness, and at what cost? |
| Q5 | Are formal notations readable? |
| Q6 | What does practice use: contracts, formal methods, property-based testing? |
| Q7 | How are algorithms engineered and evaluated by experiment? |
| Q8 | Does a specification or a plan given to a model improve the code it writes? |

## Search terms tried, three ways

- Academic: algorithm design techniques, algorithmic problem solving, design recipe, programming plans, correctness by construction, design by contract, loop invariants, formal specification, property-based testing, algorithm engineering.
- Acronym: DbC, PBT, CbC, SDD, JML, ACSL, VDM, TLA+, SLR, SMS.
- Author: Polya, Levitin, Hoare, Dijkstra, Gries, Meyer, Morgan, Furia, Woodcock, Garavel, Finney, Claessen, Fisler, Soloway, Sanders, Johnson, McGeoch, Jackson, Lahiri, Endres.
- Practice: textbook publishers, standards committee papers, tool repositories, vendor documentation, practitioner blogs, Q/A sites.
- For existing reviews: systematic literature review, mapping study, survey, multivocal review, combined with each topic string.
- Terms that returned nothing relevant: "design recipe" on the Q/A sites (0 results on two sites), and a title search for "algorithm engineering" on the Computer Science Q/A site (0). The field files these under teaching and under theory, so the query was wrong, not the topic.

## Not reviewed here

- How an algorithm is written for a reader: [pseudocode](../pseudocode/frame.md).
- TLA+ and formal methods at a cloud provider as system design: Newcombe 2015, reviewed in the system-design topic; here only a link.
- Decisions and their records: [design decisions](../design-decisions/frame.md).
- Findings that are general reading principles: [define before use](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/define-before-use.md), [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/worked-examples-with-subgoals.md).
