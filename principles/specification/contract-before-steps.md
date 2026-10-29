# Contract before steps

**Claim:** an algorithm's specification states its contract before its steps: the precondition the caller ensures, and the postcondition the code ensures.

- **Grade:** convention, untested for the order; measured, observational and small for contracts in code.
- **Evidence:** [algorithm-design review, strands 2 and 3](../../evidence/algorithm-design/review.md); [state of the art](../../evidence/algorithm-design/state-of-the-art.md).
- **Check:** `algorithm-specs` (exact): the Contract is present and comes before the Steps; whether it is right is judgment.
- **Reader styles:** [a model as implementer](../../reader-styles/model-as-implementer.md) strengthens it: assertions a person checks when a model wrote them.

## What it asks

- Give the interface first: each input and output with its type and range.
- State the precondition and the postcondition, then the technique and the steps.
- When a model writes the contract, a person checks it against the examples before it is trusted.

## Why

- The triple of a precondition, a statement and a postcondition is the form of Hoare 1969; Meyer 1992 makes it a
  contract between caller and code.
- In 100 popular C and C++ projects, methods with assertions had fewer defects, an effect the authors call small
  (Casalnuovo 2015, observational).
- A reader who knows what must hold can judge the steps: the [overview first](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/overview-first.md)
  principle, applied to a specification.

## Limits

- No study compares ways of stating behaviour (triples, contracts, derivation, models) on a measured outcome.
- Contracts are used less than expected in the most popular Java projects of one repository (Dietrich 2017).
- Programmers accepted wrong generated assertions about half the time, as confidently as correct ones (Kaufman 2026,
  a preprint): a contract written by a model is not yet a contract.
