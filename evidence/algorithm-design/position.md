# Position

This file says what is known, what is not, and where practice and evidence part. "Nobody has done this" is kept apart from "this search did not find it".

## Known

- Teaching algorithm design has a thin evidence base: 94 papers in one database, 17 with controlled trials (Liu 2024b). Grade: measured, descriptive.
- Students under-use recursion and reduction and over-use greedy methods, as reported across studies (Liu 2024b, section 5.1). Grade: measured, descriptive, secondary to the cited studies.
- Explicit teaching of a problem solving process helped 48 high school students on several outcomes (Loksa 2016). Grade: measured, one study, small.
- Methods with assertions show fewer defects in observational data, a small effect that a second dataset repeated (Casalnuovo 2015; Kochhar 2017, secondary). Grade: measured, observational.
- Industrial formal methods users report higher quality, and the sample is self-selected (Woodcock 2009). Grade: measured, descriptive, biased.
- In one air traffic control system, formal design showed no quantitative quality gain over informal design, and formal specification gave testable components (Pfleeger 1997). A student quasi-experiment favoured the formal group and was criticised for non-random assignment (Sobel 2002; Berry 2003). Grade: measured, one case and one quasi-experiment.
- Contracts are used less than expected (Dietrich 2017); property-based testing is valued for complex code and costly to write (Goldstein 2024). Grade: measured, descriptive.
- Programmers misjudge incorrect assertions (Kaufman 2026). Grade: measured, one study, preprint.
- On benchmarks, a written plan or a test list in the prompt raises the pass rate, by amounts that depend on the model and the method (Jin 2025; Jiang 2023b; Lahiri 2022). Grade: measured, benchmarks.

## Not known (not found by this search)

| Open question | Why it matters |
|---|---|
| Is a taxonomy of design techniques sound and predictive? | it is the baseline for the design step (baseline.md) |
| Does a pre and postcondition specification, written before coding, improve the correctness of an algorithm a person writes, at equal effort? | the minimum specification of this review rests on it |
| How much does an invariant add beyond the pre and postcondition? | it is the extra step that costs most |
| Does a specification help a reader check an algorithm more than pseudocode does? | the link with the [pseudocode review](../pseudocode/position.md) |
| Does a specification given to a model beat a plan or a test list at equal length, on algorithm tasks beyond small functions? | spec-driven tools assume it |
| Do the effects on people hold for models, and the reverse? | the two literatures never meet |

## Where practice runs ahead of the evidence

- Spec-driven development: one tool has 143,670 stars (Spec Kit 2026) and a radar entry at the Assess level (Thoughtworks 2025). None of the three tool pages reports an effect, and the radar page offers observation only. Grade: convention, untested; adoption measured, descriptive.
- The design recipe: used in courses for decades (HtDP 2026) without a controlled comparison found here. Grade: convention, untested.
- Property-based testing: a large library, 52,744,281 downloads in a month (Hypothesis 2026), and evidence limited to interviews at one firm (Goldstein 2024). Grade: adoption measured; effect untested.
- Contracts in a language standard: C++ contracts entered the 2025 draft while a 2026 paper doubts readiness (Neatu 2026); the effect evidence is the assertion studies above.

## Where the evidence is ignored by practice, or practice moves away from it

- Respondents rate ease of use of formal methods low (Gleirscher 2020, secondary). A small experiment found trained students reading Z badly (Finney 1996, secondary). The notations are still taught and tools still ship them.
- Contracts in Java are used less than the literature would lead one to expect (Dietrich 2017), while assertions are common (Casalnuovo 2015).
- Q/A answers split on whether specifications help. The top answers in two threads say a spec marks when work is done and bounds scope (SESE 2011n). They also say it should precede coding but not cover the whole program (SESE 2011l). Grade: convention, untested.

## What this repository adds

- A map: eight questions, each with its record, its best evidence and its gap.
- A named baseline and a comparison design for each gap (baseline.md).
- It adds no new result. The rule it may propose, to state a pre and postcondition and an invariant before the pseudocode, is a hypothesis to test, not a finding.
- The boundary with the pseudocode review is one rule: the specification says what; the pseudocode says how, to a reader.
