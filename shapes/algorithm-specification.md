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
| Problem and contract before the steps | [overview first](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/overview-first.md) |
| Interface with types before any use | [define before use](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/define-before-use.md) |
| Fixed sections, steps as a code block | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/page/signal-the-structure.md) |
| One worked example, then the implementer's own | [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/worked-examples-with-subgoals.md) |

## The skeleton

```markdown
# <Algorithm name>

**Shape:** [algorithm specification](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/shapes/algorithm-specification.md)

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

A filled specification, the lower bound of a sorted array: [Lower bound in a sorted array](../examples/lower-bound-in-a-sorted-array.md). It carries the
Shape line, so the checks run on it as on any algorithm specification of yours.
