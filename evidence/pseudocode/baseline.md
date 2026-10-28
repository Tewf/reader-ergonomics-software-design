# Baseline: what presentation rules are compared against

This file names the baseline a proposed rule on presenting algorithms must beat, and how the two would be compared.

## Named baselines

| Setting | Baseline | Source |
|---|---|---|
| Algorithm in a text or paper | Cormen et al. pseudocode conventions (CLRS) | Cormen 2003, from the authors' guide to their typesetting package; second edition read, printed conventions section and fourth edition not read |
| Exam or teaching | The board's reference language (OCR Exam Reference Language, Cambridge 9618 guide, College Board sheet) | OCR 2026, Cambridge 2024, College Board 2025 |
| Design before code | PDL, as tested against prose | Boehm-Davis 1983, Ramsey 1983 |
| Real code arm | A short program in the reader's own language | any; fix it in advance |
| Verification arm | PlusCal or TLA+ specification | Newcombe 2015 |

The main baseline is CLRS-style pseudocode: numbered lines, indentation for blocks, an assignment arrow, named procedures, comments marked.

## What the CLRS style fixes (from Cormen 2003)

1. Each line is numbered so text and trace can point to it.
2. Block structure is shown by indentation.
3. Assignment uses an arrow, not an equals sign.
4. Procedure names are set in small capitals; identifiers are typeset apart.
5. A comment symbol marks remarks.
6. A dedicated notation writes subarray ranges.

## How a comparison would be measured

| Element | Choice | Prior instrument |
|---|---|---|
| Reader task: trace | forward and backward tracing questions, plus input-output questions | Boehm-Davis 1983 |
| Reader task: implement | complete about fifteen missing lines | Boehm-Davis 1983 |
| Reader task: find a bug | three seeded errors per program, time to fix | Boehm-Davis 1983 |
| Reader task: comprehend | questions on time, errors, confidence, answer time, looks | Scanlan 1989 |
| Reader task: compose | share of algorithms that work | Glorfeld 1988 |
| Reader task: reimplement from a paper | tests that pass, as in a code-synthesis benchmark | Kulal 2019 |
| Effort | fixations, regressions, pupil size | Katona 2022, Obaidellah 2020 |
| Outcome | time, errors, correctness, preference | all of the above |

## Controls to state in advance

1. Equivalent content across formats; name every variable the same way (Boehm-Davis 1983, experiment 4).
2. Stimuli that are good examples of each format (Ramsey 1983; the dispute over Scanlan 1989).
3. Reader expertise recorded; professionals and students reported apart (Wyrich 2023).
4. Task length and domain reported; the algorithm is not a toy by default.
5. Layout fixed: indentation, line numbers, font (Hanenberg 2024, Bauer 2019, Cambridge 2024).

## A compare-against checklist for a document that presents an algorithm

1. State the inputs, outputs and a worked example before the steps.
2. Use one construct per idea, with the keywords and symbols defined once.
3. Number the lines and refer to them from the prose.
4. Name variables as the prose names them.
5. Say what is left informal, so the reader knows what to decide.
6. Where a mistake is costly and an executable form exists, ship it beside the text.

Items 1 to 5 are conventions, untested as a set. Item 6 rests on one company report and one practitioner case.
