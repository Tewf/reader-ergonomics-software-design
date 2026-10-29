# Shapes

A **shape** is the fixed skeleton of one kind of document: every document of that kind has the same parts in the same
order. These are the shapes particular to designing software before the code. The general ones (note, folder README,
report, commit message) and the reasons for shapes are in
[reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/README.md).

## Contents

| Shape | For |
|---|---|
| [algorithm-specification.md](algorithm-specification.md) | one algorithm stated before it is coded: contract, technique, steps, invariants, cost, examples, properties and a plan for the implementer, a person or a model |

## Planned

| Shape | Baseline it starts from |
|---|---|
| design document | the proposal shape of PEP 12 and design-doc practice ([design-decisions](../evidence/design-decisions/baseline.md)) |
| decision record | Nygard's five parts, with the rejected alternatives kept ([design-decisions](../evidence/design-decisions/baseline.md)) |
| architecture description | arc42, C4 and Views and Beyond, ordered by the reader's questions ([architecture-descriptions](../evidence/architecture-descriptions/baseline.md)) |
| diagram key | C4 with a key that says what each arrow means ([system-diagrams](../evidence/system-diagrams/baseline.md)) |

## Choosing a shape

- One document, one shape: a text that needs two shapes is two documents.
- Each part of a shape cites the review that justifies it, with that evidence's grade; a part with no evidence says
  "convention, untested".
