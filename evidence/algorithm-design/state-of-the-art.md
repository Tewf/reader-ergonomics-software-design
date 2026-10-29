# State of the art

This file says who holds the record on each question, by what method, measured how. **Most adopted** (a practice record) is kept apart from **best evidence** (a research record).

Records of two further kinds are kept apart: upper bounds and lower bounds. An upper bound is what a method achieved on a benchmark or in a project. A lower bound is what that method cannot do.

No lower bound on cost or correctness was found for any method here. Each row therefore names only an upper bound. In a row, "(secondary)" marks a number read in an abstract or a summary.

## Q1 Design techniques and their taxonomy

| Record | Holder | Measured how |
|---|---|---|
| Best evidence on teaching | Liu 2024: 94 papers, 17 with controlled trials | systematic review of one database |
| Best argued taxonomy | Levitin 2000: four general techniques and three less general, by generality | argument from examples; no data |
| Best evidence on the taxonomy | none found | no test of soundness, completeness or predictive value |
| Most adopted | the technique chapters of textbooks (Kleinberg 2005; Skiena 2020) | publisher listings, books not opened |

- Students under-use recursion and reduction, and lean on greedy methods against counterexamples (Liu 2024, section 5.1, reading earlier studies).
- Four words name the category of a technique (CS 2020b, example only).

## Q2 Problem solving instruction

| Record | Holder | Measured how |
|---|---|---|
| Best evidence | Loksa 2016: explicit six-stage instruction raised productivity, independence and self-efficacy | 48 high school students, two camps, abstract read |
| Plan composition | Fisler 2014: over 200 solutions, five courses (secondary) | descriptive |
| Most adopted | the design recipe of HtDP 2026 (six steps) | none; teaching experience only |

- The recipe has a long classroom record and no controlled comparison was found.
- A recipe for algorithms (as against functions over data) was not found.

## Q3 Ways of stating behaviour

| Style | First statement | Held today by |
|---|---|---|
| Pre and postcondition, invariant | Hoare 1969 | assertions in code (Casalnuovo 2015) |
| Contract in the language | Meyer 1992 | Eiffel; library or tool elsewhere (SO 2009f) |
| Derivation from the specification | Dijkstra 1975; Kourie 2012 | teaching and tools; no adoption count found |
| Model-based notation | Abrial 2010; Jackson 2002 | specialist projects (Woodcock 2009) |
| Properties as tests | Claessen 2000 | Hypothesis 2026: 52,744,281 downloads in the last month, read 2026-10-29 |

- Assertions are the most adopted style: 69 of the 100 most popular C and C++ projects on one host hold more than a minimal number (Casalnuovo 2015, read).
- Only 4.6% of the methods in those projects carry an assertion (same source).

## Q4 Do specifications help, and at what cost

| Record | Holder | Measured how |
|---|---|---|
| Best evidence of benefit | Casalnuovo 2015, with Kochhar 2017: methods with asserts have fewer defects, a small effect | observational, 100 C and C++ projects; 185 Java projects (secondary) |
| Largest stated effect | Polikarpova 2013: strong specifications found twice as many bugs as standard contracts (secondary) | experiments by the method's authors, data structure libraries |
| Largest survey | Woodcock 2009: 62 projects, quality reported higher in 92% of cases | self-selected sample; the authors state the bias |
| Case study | Pfleeger 1997: no quantitative evidence of higher quality from formal design in one 200,000-line system; formal specification gave testable components | observational, read once in an author's copy |
| Quasi-experiment | Sobel 2002: 6 formal teams passed all six tests, 11 control teams 45.5% (secondary, as described by Berry 2003) | volunteers, not random; criticised in Berry 2003 |
| Cost evidence | Woodcock 2009: more time in specification, less later; one project found annotation the costly step | respondent comments |

- Upper bound reached: a four-year Dafny build of a production authorization engine, with a threefold speed gain (Chakarov 2025, the owner on itself).
- No controlled trial of a specification against none, at equal effort, on algorithms people write, was found.

## Q5 Readability of formal notation

| Record | Holder | Measured how |
|---|---|---|
| Best evidence | Kaufman 2026: judging generated assertions, 74% right on correct, 49% on incorrect, 86 programmers | controlled experiment, preprint |
| Oldest | Finney 1996: trained students did very poorly reading Z (secondary) | small experiment |
| Perception | Gleirscher 2020: ease of use rated negatively, N = 216 | survey, abstract read on the preprint |

## Q6 Practice

| Record | Holder | Measured how |
|---|---|---|
| Most adopted | assertions and tests; property-based testing in Python (Hypothesis 2026) | counts |
| Contracts | used less than expected in 200 Maven projects (Dietrich 2017); above 33% of elements in most of 21 contract-equipped projects (Estler 2014) | repository mining, abstracts read |
| Experts' view | 130 responses to 170 invitations; 62.3% say trustworthy design without formal methods is probably or definitely not possible (Garavel 2020, read) | survey of experts in the field |
| Standards | contracts in the C++26 draft since 2025, readiness disputed in 2026 (Neatu 2026) | committee paper |
| Property testing at one firm | 30 interviews (Goldstein 2024) | interview study |

- Best evidence of effect and most adopted are held by different things: the effect evidence is on assertions and contracts; the adoption is on tests.

## Q7 Algorithm engineering

| Record | Holder | Measured how |
|---|---|---|
| Methodology | Johnson 2002; McGeoch 2012; Sanders 2009 | guides and a definition; no measured effect found |
| Repeatability | Collberg 2016: 32.3% of 402 papers backed by code built within 30 minutes (secondary) | survey of papers |

## Q8 Models as implementers

| Record | Holder | Measured how |
|---|---|---|
| Planning, best independent evidence | Jin 2025: structured methods 2.5 to 4.4 points of Pass@1 over zero-shot, averaged over six models (its text: 5 to 12%) | benchmarks, preprint, table read |
| Planning, largest stated gain | Jiang 2023: up to 25.4% relative over direct generation | authors' own method |
| Intent through tests | Lahiri 2022: 22.5 to 54 points with Codex within 5 simulated interactions; Fakhoury 2024's own figures disagree (45.97%, 45.73%, about 33 points) | idealised user |
| Verified code | Misu 2024: 58% of 178 problems with a strong specification (GPT-4, five attempts); Loughridge 2024: 67.8% of 782 programs, hints only (Claude 3 Opus, ten attempts) | benchmarks, tables read |
| Most adopted | Spec Kit 2026: 143,670 stars; Kiro 2026 | counts; no effect on the pages |

- These numbers are upper bounds on small function-level benchmarks; they do not bound what a model does on a real algorithm design task.
- No comparison of a pre and postcondition specification against a plan or a test list, at equal prompt length, was found.
