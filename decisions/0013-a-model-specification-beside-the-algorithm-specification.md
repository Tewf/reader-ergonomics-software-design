# 0013: A model specification beside the algorithm specification

**Decision:** This repository holds a sixth shape, the model specification, for an optimisation model written before
it is coded for a solver. The algorithm specification names reduction to a known model among its techniques.

**Status:** accepted, 2026-11-07. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** the
S7 vault's work on linear programs and flows, 2026-11-07, where a formulation template was written with no shape to
hold it.

## Context

- The algorithm specification states what is computed and how; a linear or integer program states what is decided,
  measured and limited, and leaves the how to a solver. Its parts are different: sets and data, variables with a
  domain, constraints that each stand for a sentence of the statement, and whether the relaxation is exact.
- A problem is often a known model in disguise: an assignment, a flow, a cut, a covering. The algorithm
  specification's Technique list (brute force, divide, decrease, transform and conquer) has no word for that step.
  Students under-use reduction (Liu 2024b, in the algorithm-design review).
- No review in this repository covers optimisation modelling; the parts particular to a model enter as conventions,
  and the parts shared with the algorithm specification carry its evidence.

## Decision

A shape `model-specification.md` with the parts Problem, Sets and data, Variables, Objective, Constraints,
Relaxation, Examples, Properties, Plan and Out of scope. A local check `model-specs` finds its documents by their
Shape line. One example. The phrase "reduction to a known model" enters the algorithm specification's Technique list.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stretch the algorithm specification to models | its Steps and Invariants have no meaning for a program a solver runs; the Contract becomes the constraints by force | rejected: one shape, two documents |
| A design document per model | a design document decides between alternatives; a model is a specification handed to an implementer | rejected: wrong reader |
| A shape of its own, checked like the algorithm specification | one more shape and check to keep; the parts fit the documents the vault and the courses write | chosen |

## Consequences

- Good: a model handed to a person or a language model is read line by line against the statement, and the question
  "is the LP enough" is answered before the solver is chosen.
- Bad: the parts particular to a model have no reviewed evidence here; a review strand on modelling is owed before
  any of them claims more than convention.
- To keep it true: keep the example passing the check in CI; when a modelling review is written, raise the grades in
  the shape from it, and nowhere else.

## See also

- The [decisions](README.md) of this repository; the [shape](../shapes/model-specification.md) and its
  [example](../examples/students-to-projects-as-a-model.md); the
  [algorithm specification](../shapes/algorithm-specification.md), whose Technique list grew by one entry.
