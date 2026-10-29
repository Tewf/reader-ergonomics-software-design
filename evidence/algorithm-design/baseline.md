# Baseline

This file names the baseline for the repository's rules on designing and specifying an algorithm. It also says how the rules are compared against that baseline. The review is finished only because a baseline can be named for each step.

## The baselines

| Step | Baseline | Source | Status |
|---|---|---|---|
| Design | the hierarchical taxonomy of design techniques (Levitin 2000; Levitin 1999) | named in the commissioning brief | read: both in full; argued from examples, never tested |
| Specification, minimum | a **precondition and a postcondition**, plus a **loop invariant** for each loop (Hoare 1969; Meyer 1992) | the field's own minimum | convention, untested as a minimum |
| Method taught | the **design recipe**: six steps from data definition to tests (HtDP 2026) | the most used taught method | convention, untested |
| Model as implementer | the task statement alone, no plan and no specification | every benchmark in strand 7 | measured, descriptive |

- Fallback if the 1999 paper stays unread: the technique chapters of Kleinberg 2005 or Skiena 2020, cited for what their publishers say; neither book was opened.
- Levitin 2000 level one: brute force, divide-and-conquer, decrease-and-conquer, transform-and-conquer; level two: local search (greedy, iterative improvement), dynamic programming, state-space-tree methods.
- Why these: each is the plainest form the field already uses; a rule that does not beat it has no reason to exist.
- What is not the baseline: a formal model in a notation such as Z, Event-B or Alloy; it is the next step up, not the minimum (Abrial 2010; Jackson 2002).

## Definition of the minimum specification (M0)

- M0 for a function: its precondition on the inputs, its postcondition on the output, written as checkable statements.
- M0 for a loop: an invariant that holds before and after each pass and, with the exit test, implies the postcondition (Furia 2014).
- M0 is executable when written as assertions (Casalnuovo 2015) or as a property test (Claessen 2000), and checkable by a person when written in a comment.
- M0 is not a proof. Dijkstra 1975 shows the step beyond M0: a calculus that derives the program and its proof together from the postcondition.

## How a proposed rule is compared

Reader and implementer tasks, with a crossover design (each participant meets both conditions on matched problems), effect sizes and a stated sample.

| Comparison | Participants | Task | Measure |
|---|---|---|---|
| Rule against design recipe | novices, then experienced programmers | design an algorithm for a matched problem | proportion correct on hidden tests; time |
| M0 against no specification | programmers | write an algorithm, then implement it | defects found by property tests; time spent |
| M0 against pseudocode alone | readers | check an algorithm, find a seeded bug | bugs found; time; confidence (reported apart from accuracy, as Kaufman 2026 does) |
| M0 against plan, test list | models | implement from the statement | Pass@1 on held-out problems; prompt length held equal |
| Specification against none, for design | students | choose a technique | agreement with the taxonomy label, if the taxonomy is first shown sound |

- Effect sizes are reported with confidence intervals; a result is "no difference found" when the interval spans zero, never "no effect".
- Report effort beside correctness: the cost of the specification is part of the outcome (Woodcock 2009).
- Report confidence beside accuracy, since confidence and accuracy part for incorrect specifications (Kaufman 2026).
- Hold out the problems; benchmark problems may be in a model's training data (position.md, not known).

## Prior numbers for planning a study

- Controlled trials in this field are few: 17 among 94 papers (Liu 2024).
- A 48-student study found effects of explicit instruction (Loksa 2016); a study of 86 programmers found a gap of 25 points in judging assertions (Kaufman 2026).
- Pass@1 gains from plans average 2.5 to 4.4 points over six models in an independent study (Jin 2025, Table 3); a model comparison should be powered to detect a gain of a few points.

## What would change the baseline

- A study showing a taxonomy of design techniques unsound or unpredictive: replace the design baseline.
- A controlled study where M0 costs more than it saves: M0 becomes optional, not minimum.
- A model study where a plan beats a specification at equal length on algorithm tasks: the rule for models splits from the rule for people.
