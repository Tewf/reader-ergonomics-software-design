# Shape: algorithm specification

This shape states one algorithm before it is coded. With it, an implementer (a person or a model) builds the
algorithm correctly, and a reviewer can check it. It says what the algorithm must do before how it does it. The
contract comes first; then the technique, the steps, the invariants and the cost; then the examples and properties
that test it, and a plan for whoever implements it.

## When to use it

- Before an algorithm is coded by someone else, by a model, or by you later.
- When correctness is not obvious: a loop or a recursion, an edge case, a bound on cost.
- Not for a whole running system: that is a design document.
- Not for an algorithm presented in a paper: the [pseudocode](../evidence/pseudocode/) review and the paper's own
  conventions govern that.
- Not for a one-line function: its name and its type are the specification.

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Problem | one sentence: what is computed, from what | define before use (reader-ergonomics) | convention |
| Interface | each input and output with its type, unit and range | Hoare 1969; Meyer 1992 | convention, untested |
| Contract | the precondition the caller ensures and the postcondition the code ensures | Hoare 1969; Meyer 1992. In code, methods with assertions had fewer defects, a small effect (Casalnuovo 2015); strong specifications found more bugs (Polikarpova 2013) | convention for the form; measured, observational and one group, for the effect |
| Technique | names the design technique and says why it fits | the taxonomy of Levitin 1999 (brute force, divide, decrease, transform and conquer); no test of any taxonomy was found | argued, untested |
| Steps | constrained, code-like pseudocode | code-like design text beat prose for coding and debugging time, partly through naming (Boehm-Davis 1983) | measured, old and small |
| Invariants | one per loop, with the variant that shows it ends | Hoare 1969 (the rule of iteration, without termination); Furia 2014; derived with the program in Dijkstra 1975 | convention, untested |
| Cost | time and space, worst case, with the size named | textbook convention (Cormen 2003) | convention |
| Examples | inputs with their expected outputs, edge cases first | tests that clarify intent raised models' pass rates by about 22 to 54 points with Codex and a simulated user (Lahiri 2022) | measured, benchmarks |
| Properties | statements true for every valid input, ready for property-based tests | Claessen 2000; valued for complex code and costly to write (Goldstein 2024) | convention; descriptive |
| Plan | the order in which to implement and test | planning before code gained 2.5 to 4.4 points over six models (Jin 2025); naive reasoning can lower accuracy | measured, benchmarks, modest |
| Out of scope | what the algorithm does not do, and open questions | no natural-language specification is unambiguous (Q/A answers, algorithm-design review) | convention, untested |

Whether the shape as a whole helps an implementer is untested: the [baseline](../evidence/algorithm-design/baseline.md)
gives the comparison it should face. Each key (Author Year) is listed in the [bibliography](../evidence/bibliography.md).

## The principles it applies

| Part | Principle |
|---|---|
| Problem and contract before the steps | [overview first](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/overview-first.md) |
| Interface with types before any use | [define before use](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/define-before-use.md) |
| Fixed sections, steps as a code block | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/page/signal-the-structure.md) |
| One worked example, then the implementer's own | [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/worked-examples-with-subgoals.md) |

## The skeleton

```markdown
# <Algorithm name>

**Problem.** One sentence: what is computed, from what.

**Interface.**
- Input `<name>`: <type>, <range or unit>.
- Output `<name>`: <type>, <range>.

**Contract.**
- Precondition: <what the caller ensures; the algorithm may assume it>.
- Postcondition: <what holds on return, in terms of the inputs>.

**Technique.** <brute force | divide and conquer | decrease and conquer | transform and conquer | other>,
because <one reason>.

**Steps.**
    <constrained pseudocode, one statement per line>

**Invariants.**
- Loop <n>: <what holds before and after every pass>. Variant: <a quantity that strictly decreases>.

**Cost.** Time <O(...)> worst case, in <the size named>; space <O(...)> beyond the input.

**Examples.**
| Input | Expected output | Why this case |
|---|---|---|

**Properties.**
- <a statement true for every input that meets the precondition>

**Plan.**
1. Write the examples as tests.
2. Implement the steps with the invariants as assertions.
3. Test the properties on random inputs against a simple, slow version.

**Out of scope.** <what it does not do>. **Open questions.** <none, or each one>.
```

## The rules

1. Contract before steps: a reader who knows what must hold can judge the steps.
2. Every name in the steps appears in the interface or is defined where it first appears.
3. The precondition is assumed, not checked, unless checking it is cheap; say which.
4. Each loop has an invariant and a variant; each recursion has a decreasing measure.
5. Steps are code-like but language-free: assignment, conditions and loops only, one statement per line.
6. Examples start with the edge cases: empty input, one element, boundaries, duplicates.
7. A property states a relation, not a value, so a generator can test it on any input.
8. When a model writes the contract or the assertions, a person checks them against the examples: programmers
   accepted wrong generated assertions about half the time, as confidently as correct ones (Kaufman 2026, a preprint).

## Worked example

# Lower bound in a sorted array

**Problem.** Find the first position in a sorted array whose value is at least `x`.

**Interface.**
- Input `a`: an array of `n` comparable values, `n` ≥ 0. Input `x`: a value of the same type.
- Output `i`: an integer with 0 ≤ `i` ≤ `n`.

**Contract.**
- Precondition: `a` is sorted in non-decreasing order.
- Postcondition: every `a[j]` with `j` < `i` is less than `x`, and every `a[j]` with `j` ≥ `i` is at least `x`.

**Technique.** Decrease and conquer, halving the interval at each pass, because the order lets one comparison discard
half of what is left.

**Steps.**

    lo ← 0; hi ← n
    while lo < hi:
        mid ← lo + (hi − lo) div 2
        if a[mid] < x: lo ← mid + 1
        else: hi ← mid
    return lo

**Invariants.**
- The loop: 0 ≤ `lo` ≤ `hi` ≤ `n`; every `a[j]` with `j` < `lo` is less than `x`; every `a[j]` with `j` ≥ `hi`
  is at least `x`. Variant: `hi − lo` strictly decreases, since `mid` lies in [`lo`, `hi`). At exit `lo` = `hi`, and
  the invariant gives the postcondition.

**Cost.** At most ⌈log₂(`n` + 1)⌉ passes, so time O(log `n`) in the length of `a`; space O(1).

**Examples.**

| Input `a`, `x` | Expected `i` | Why this case |
|---|---|---|
| [], 5 | 0 | empty array |
| [1, 3, 3, 7], 0 | 0 | every value at least `x` |
| [1, 3, 3, 7], 9 | 4 | every value less than `x` |
| [1, 3, 3, 7], 3 | 1 | duplicates: the first of them |
| [1, 3, 3, 7], 4 | 3 | `x` absent: where it would go |

**Properties.**
- `i` equals the number of values in `a` less than `x`.
- Inserting `x` at position `i` keeps `a` sorted.

**Plan.**
1. Write the five examples as tests.
2. Implement the loop with the invariant as an assertion in a debug build.
3. Test both properties on random sorted arrays against a linear scan.
4. Keep `mid` as `lo + (hi − lo) div 2`, which cannot overflow in fixed-width integers.

**Out of scope.**
- Unsorted input: the precondition is not checked, since checking it costs O(`n`).
- A flag saying whether `x` was found.

**Open questions.** None.

The examples, both properties and the bound on passes were run before publication: 20,000 random cases with arrays of
up to 64 values.
