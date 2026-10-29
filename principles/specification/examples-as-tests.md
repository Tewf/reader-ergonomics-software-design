# Examples and properties as tests

**Claim:** a specification handed to an implementer, a person or a model, carries examples with their expected outputs, edge cases first, and properties that hold for every valid input.

- **Grade:** measured, on model benchmarks; convention, untested for people.
- **Evidence:** [algorithm-design review, strands 5 and 7](../../evidence/algorithm-design/review.md); [against](../../evidence/algorithm-design/against.md).
- **Check:** `algorithm-specs` (exact): an Examples table with at least one row; it warns under three rows.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- Write the examples as a table of input, expected output and why the case matters, edge cases first: empty, one
  element, boundaries, duplicates.
- State properties as relations, not values, so a generator can test them on any input.
- Make the examples the implementer's first tests.

## Why

- Asking for tests to clarify intent raised models' pass rates by about 22 to 54 points with Codex and a simulated
  user (Lahiri 2022, benchmarks).
- A written plan before code gained 2.5 to 4.4 points, averaged over six models (Jin 2025, its Table 3).
- Property-based testing is valued for complex code in practice, and costly to write (Goldstein 2024, 30 interviews).

## Limits

- The user in those benchmarks is simulated and idealised, and the tasks are single functions.
- The largest gains reported are the method authors' own; independent replications are smaller.
- No study measures examples in a specification read by people.
