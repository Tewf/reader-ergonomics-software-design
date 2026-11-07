# Shape: model specification

This shape states one optimisation model before it is coded for a solver. "Model" here means the mathematical
program, not a language model. With it, an implementer (a person or a model) writes the sets, data, variables,
objective and constraints as the statement meant them, and a reviewer can check each line against the sentence it
stands for. It says what is decided, measured and limited before any solver is named; then whether the relaxation
is exact, and what tests it.

## When to use it

- Before a linear, integer or mixed program is written in a modelling language or a solver's API, by someone else,
  by a model, or by you later.
- When a problem may be a known model in disguise (an assignment, a flow, a covering), so that the reduction is
  stated and the solver chosen on it.
- Not for an algorithm: that is an [algorithm specification](algorithm-specification.md), and a model solved by a
  combinatorial algorithm is one of its techniques, reduction to a known model.
- Not for a one-constraint program a reader can hold whole: the sentence is the specification.

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Problem | one sentence: what is decided, measured and limited, from what data | define before use (reader-ergonomics) | convention |
| Sets and data | each index set and each datum with its type, unit and source | the data against variable split of modelling courses; no study of the written form | convention, untested |
| Variables | each decision with its type, unit and domain: real, integer or binary | the "how much" against "is there" rule of modelling courses | convention, untested |
| Objective | what is measured, linear in the variables, with its unit | textbook convention | convention |
| Constraints | one family per rule of the statement, each with the sentence it stands for | a constraint read back as a sentence is the one check a reviewer can run; no study of the practice | convention, untested |
| Relaxation | whether dropping integrality keeps the answer, with the reason (a matrix family, a theorem) or the witness that it does not | Hoffman 1956 for the theorem; the writing of it is a convention | convention, untested for the writing; the theorem is mathematics |
| Examples | instances with their optimum and one optimal point, small ones first | tests that clarify intent raised models' pass rates (Lahiri 2022), as in the algorithm specification | measured, benchmarks, by analogy |
| Properties | statements true for every instance, ready for property-based tests: feasibility of a known point, a bound | Claessen 2000, as in the algorithm specification | convention; descriptive |
| Plan | the order in which to implement and test: the examples, then a slow exact solver, then the real one | planning before code (Jin 2025), as in the algorithm specification | measured, benchmarks, modest |
| Out of scope | what the model does not decide, and open questions | no natural-language specification is unambiguous (algorithm-design review) | convention, untested |

Whether the shape as a whole helps an implementer is untested. The parts shared with the algorithm specification
carry its evidence; the parts particular to a model (sets and data, variables, constraints as sentences, relaxation)
have none in this repository's reviews. Each key (Author Year) is listed in the
[bibliography](../evidence/bibliography.md); Hoffman 1956 is a theorem, cited as such.

## The principles it applies

| Part | Principle |
|---|---|
| Problem, sets and variables before the constraints | [define before use](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/document/define-before-use.md) |
| Fixed parts, each constraint on its own line with its sentence | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/page/signal-the-structure.md) |
| The problem and the relaxation before the solver | [overview first](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/document/overview-first.md) |
| One worked example, then the implementer's own | [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/principles/document/worked-examples-with-subgoals.md) |

## The skeleton

```markdown
# <Model name>

**Shape:** [model specification](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/shapes/model-specification.md)

**Problem.** One sentence: what is decided, what is measured, what limits it, from what data.

**Sets and data.**
- Set `<I>`: <what it indexes>.
- Datum `<a_ij>`: <type>, <unit>, <where it comes from>.

**Variables.**
- `<x_ij>`: <what one unit of it is>, <real | integer | binary>, <range>.

**Objective.** <maximise | minimise> `<expression>`: <what it measures, in what unit>.

**Constraints.**
- For each `<i in I>`: `<expression> <= <datum>`: "<the sentence of the statement it stands for>".

**Relaxation.** <exact | not exact>, because <the matrix family and the theorem, or the fractional witness>.
Solver: <the LP alone | an integer solver | a combinatorial algorithm, named>.

**Examples.**
| Instance | Optimum | One optimal point | Why this case |
|---|---|---|---|

**Properties.**
- <a statement true for every instance: a known feasible point, a bound, a symmetry>

**Plan.**
1. Write the examples as tests, each with its optimum.
2. Implement the model line by line after the constraints; solve the examples with a slow exact method first.
3. Check the relaxation's claim on the examples, then run the properties on random instances.

**Out of scope.** <what the model does not decide>. **Open questions.** <none, or each one>.
```

## The rules

1. Every constraint carries the sentence it stands for; a sentence of the statement with no constraint is a bug, and
   a constraint with no sentence is one.
2. A number of the statement is a datum, never a variable; a variable is an answer to a question the statement
   leaves open.
3. The domain line is the last decision, and the Relaxation part says what it costs: exact with the reason, or a
   bound with the witness.
4. A model that is a known one in disguise says which (assignment, transportation, flow, cut, covering) in the
   Relaxation part, with the reduction's proof both ways named in a property.
5. Examples start small: an instance a reader can solve by hand, then the boundary cases (empty, one item, a tie).
6. A property states a relation the solver's answer must satisfy, so a generator can test it on any instance.
7. When a model writes the constraints, a person reads each back as its sentence against the statement.

## Worked example

A filled specification, students placed on projects with quotas:
[Students to projects](../examples/students-to-projects-as-a-model.md). It carries the Shape line, so the checks run
on it as on any model specification of yours.
