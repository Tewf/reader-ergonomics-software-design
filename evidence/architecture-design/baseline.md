# Baseline: what this repository's rules are compared against

The review is finished only when it names the baseline. This file names three, one per role, and says how each is compared.

## The baselines

| Role | Baseline | Why this one |
|---|---|---|
| Method | ADD 3.0 (Cervantes 2016) | a named, repeatable method driven by quality attributes, set out in a practitioner book (publisher page read); it has no controlled test |
| Principle | information hiding (Parnas 1972) | the oldest stated criterion for decomposition in the leads; one Q/A answer still gives it as the reason for private members (SESE 2011k); the criterion has no controlled test, while the broader modularity measures have observational support (review.md 2) |
| Check | ATAM (Kazman 2000) | the evaluation most often cited before building; 31 projects of data exist (Bellomo 2015, secondary) |

- ATAM as Kazman 2000 prescribes it (read in full): nine steps in four groups. Presentation: the method, the business drivers, the architecture. Investigation: the architect names the approaches, a utility tree of quality attributes is built down to prioritised scenarios, and the approaches are analysed for risks, sensitivity points and tradeoff points. Testing: stakeholders brainstorm and vote on more scenarios, which are run against the approaches again. Reporting: the findings go back to the stakeholders. The report gives one case and no measure of effect.
- For a decision about monoliths and services, the practice baseline is Lewis 2014 with Fowler 2015 (monolith first).
- For a structural check in a build, the practice baseline is a fitness function (ThoughtWorks 2017).

## How a rule of this repository is compared

- Task: a person given a requirements brief produces a structure; judges rate it on the attribute scenarios the brief states.
- Conditions: with ADD 3.0 steps, with a plain list of the principles, and with no guide; a crossover design so each person meets each condition.
- Measures: scenarios met out of scenarios stated, hours spent, and a count of dependency cycles.
- Report effect sizes with sample sizes; mark any number from a summary "(secondary)".
- A decomposition rule is checked on a built system: the change cost of a stated change (files touched) before and after.

## What a win would be

- The new rule meets as many scenarios as ADD 3.0 in fewer hours, or meets more in the same hours.
- No such study exists yet; this is a proposal, not a result.

## Not compared

- Whether a structure is good in the abstract.
- Documentation of the structure: see [architecture-descriptions](../architecture-descriptions/baseline.md).
- Runtime behaviour across machines: system-design.
