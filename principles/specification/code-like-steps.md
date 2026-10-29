# Code-like steps

**Claim:** an algorithm's steps are written as constrained, code-like pseudocode, one statement per line, not as prose.

- **Grade:** measured, in old and small experiments.
- **Evidence:** [pseudocode review, strand 1](../../evidence/pseudocode/review.md); [against](../../evidence/pseudocode/against.md).
- **Check:** `algorithm-specs` (exact): the Steps hold a code-like block; whether its statements are constrained is judgment.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- Use assignment, conditions and loops only, one statement per line, with names from the interface.
- Keep the steps free of any one programming language, so any implementer can follow them.
- Put the explanation beside the steps, not inside them.

## Why

- Code-like design text beat plain English prose for coding and debugging time in two experiments with professionals,
  with a trend in a third (Boehm-Davis 1983). Part of the gap was naming: giving the prose the code's names shrank it.
- Detailed flowcharts gave no reliable gain over text for writing, reading, debugging or changing programs in the
  older studies of the same review.

## Limits

- The experiments are old and small.
- Structured flowcharts beat pseudocode for comprehension in two independent groups (Scanlan 1989; Andrzejewska 2022),
  and the first one's stimuli were disputed: the comparison is contested.
- The notation must match the conventions its readers expect; five exam boards each publish their own.
