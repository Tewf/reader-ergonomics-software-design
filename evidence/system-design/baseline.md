# Baseline: what this repository's rules are compared against

The review is finished when the baseline is named. This file names it and says how a comparison would run.

## Named baseline

- Checklist: Lampson 1983 and its revision Lampson 2020 (hints, goals STEADY, techniques AID); the alternative checklist is the AWS Well-Architected Framework with six pillars (AWS 2026p).
- Check: Newcombe 2015, a precise model of the design checked before code exists.
- Taught method: Primer 2026, four steps from use cases to scaling, the most adopted by stars.
- Failure benchmark: the failure classes of Yuan 2014 and Alquraan 2018, as the things a design must survive.

## What is compared

- This repository's rules are about writing the design down: state load, failure model and consistency assumptions beside the design.
- The baseline has no rule about the document; it has rules about the system. The comparison is therefore of what a reader finds, not of a rule list.

## How, as a proposal (not run)

- Reader tasks: "find what the design assumes about failure" and "find a flaw in a seeded design", on designs with known flaws from Alquraan 2018.
- Conditions: the design written with the repository's rules, and the same design written in the primer's four steps.
- Design: crossover, so each reader sees both documents on different designs; order balanced.
- Measures: flaws found, time, and wrong beliefs about the failure model; effect sizes with intervals.
- Control for the reader's experience; report the sample.

## What would count as a failure of the rules

- Readers find no more seeded flaws with the rules than with the primer's steps.
- Readers state more wrong assumptions about the failure model.

## Unknown

- No study of design documents for running systems was found, so no effect size exists to power the comparison.
