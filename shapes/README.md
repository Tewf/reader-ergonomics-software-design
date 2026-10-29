# Shapes

A **shape** is the fixed skeleton of one kind of document: every document of that kind has the same parts in the same
order. These are the shapes particular to designing software before the code. The general ones (note, folder README,
report, commit message) and the reasons for shapes are in
[reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/shapes/README.md).

## Contents

| Shape | For |
|---|---|
| [algorithm-specification.md](algorithm-specification.md) | one algorithm stated before it is coded: contract, technique, steps, invariants, cost, examples, properties and a plan for the implementer, a person or a model |
| [design-document.md](design-document.md) | one design proposed before it is built: the decision asked, motivation and use cases, goals and non-goals, the design, the alternatives that lost, consequences, feasibility and open questions |
| [decision-record.md](decision-record.md) | one decision kept after it is taken: the decision first, its status, context, the options with why each lost, and consequences; its worked example is this repository's own [first record](../decisions/0001-pin-links-at-the-release-commit.md) |
| [architecture-description.md](architecture-description.md) | the structure of one system, ordered by the reader's questions: readers and tasks, context, a map of the parts, invariants, runtime, deployment, cross-cutting concepts, decisions linked, risks and a glossary |
| [system-diagram.md](system-diagram.md) | one diagram of a system: a title with type and scope, a key, typed elements, labelled one-way arrows, few layout flaws, and its source as text beside it |

## Choosing a shape

- One document, one shape: a text that needs two shapes is two documents.
- Each part of a shape cites the review that justifies it, with that evidence's grade; a part with no evidence says
  "convention, untested".
