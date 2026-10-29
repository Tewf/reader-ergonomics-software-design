# Software design

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-software-design/)

How to write the documents that design software before the code: algorithm specifications, design documents,
decision records, architecture descriptions and system diagrams. Each is written at the least cost to its reader, and
to whoever implements it, a person or a model. Five shapes give each document its skeleton, and checks find a document by its
Shape line, so they can run in CI.

Three reviews also read the evidence on designing itself. Algorithm design feeds two principles and the algorithm
specification, and system design feeds one principle. Architecture design is a review with no rule drawn from it yet.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The general principles, their grades and the
checks live there and are not repeated here. This repository adds only what is particular to software design and the writing
about it: its evidence, its principles and the shapes of its documents.

Start with the [card](standard.md). [En français](README.fr.md).

## Use it

Ten minutes, without reading the reviews. The family's general form is reader-ergonomics'
[Take your own version](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/README.md#take-your-own-version); here is what it means for software design:

1. **Pin the standard by commit**, so its checks do not change under you:
   `git clone https://github.com/Tewf/reader-ergonomics && git -C reader-ergonomics checkout bfbe9f7` (v1.18.2).
2. **Copy what you need, once.** Take the skeleton of a [shape](shapes/README.md), with its `**Shape:**` line, and
   [`checks/local/`](checks/local/) into your repository's `checks/local/`. The copies are yours: a later change here
   touches nothing you copied. Note the commit you copied from, to compare later.
3. **Configure** with a `checks/config.toml`:

   ```toml
   extends = "reader-ergonomics"

   [readable_measure]
   stylesheets = []   # no site stylesheet to measure

   [sufficient_contrast]
   stylesheets = []
   ```

4. **Fill and check.** Keep the documents in a folder named for what they serve, such as `design/`, and run
   `python3 reader-ergonomics/checks/run.py .`, in CI too. A document is checked against the shape its Shape line
   links, and every Mermaid diagram against the diagram rules. A filled [example](examples/README.md) of each shape
   passes; start from one if you prefer.
5. **Disagree** by opening an issue on this repository, with the evidence; a rule of the standard itself goes to
   reader-ergonomics' issues.

| Check | Checks | Fails when |
|---|---|---|
| `algorithm-specs` | algorithm specifications | a part is missing, the contract comes after the steps, the steps are prose, or the examples are no table |
| `design-docs` | design documents | the decision asked is not first, a required part or the table of alternatives is missing |
| `diagram-keys` | every Mermaid diagram | a diagram has no key, or a flowchart arrow no label |
| `decision-records`, in reader-ergonomics | the records in `decisions/` | a record breaks one of the shape's four rules |

> **Status:** version 1.0.0, released 2026-10-29. Seven literature reviews are written in [evidence/](evidence/), each a multivocal review of
> research and practice; their numbers were audited against the primary sources (four on 2026-10-28, three on 2026-10-29). The five shapes are
> written (algorithm specification, design document, decision record, architecture description, system diagram); eight principles and the [card](standard.md) are written. It is an
> informal reading of published research and practice: not an official standard, not a peer-reviewed study, not a new result, and not a claim to the
> state of the art.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. AI agents draft the literature reviews; every reference is resolved by script, and a
> number read only in a summary is marked "(secondary)". Corrections are welcome as issues.

## Scope

| | What | Why |
|---|---|---|
| in | documents about a system: architecture descriptions, decision records, design documents, pseudocode, component and data-flow diagrams | the reader is the object, as in reader-ergonomics |
| in | designing the system at the abstract layer before the code: architecture design, system design, algorithm design and specification | the design is what an implementer, a person or a model, works from |
| out | programming languages and their implementation | another object, with its own evidence and its own checks |
| out | how code is laid out in files and folders | already covered by the collection principles of reader-ergonomics |

## Layout

The same as reader-ergonomics, so a reader of one can find their way in the other:

- `evidence/<topic>/`: one literature review per topic, one file per step (frame, review, state of the art, position,
  the case against, baseline), plus its protocol and its scored sources; written for seven topics;
- [`shapes/`](shapes/): the skeleton of each kind of document, with the evidence behind each part. Written are the
  [algorithm specification](shapes/algorithm-specification.md), the [design document](shapes/design-document.md), the
  [decision record](shapes/decision-record.md), the [architecture description](shapes/architecture-description.md) and the
  [system diagram](shapes/system-diagram.md);
- [`examples/`](examples/README.md): a filled document of each shape, checked in CI like any other;
- [`decisions/`](decisions/): the records of this repository's own design choices;
- [`principles/`](principles/README.md): only where software design differs from the general standard, eight in three
  groups (specification, decision, structure), gathered on the [card](standard.md);
- [`reader-styles/`](reader-styles/README.md): readers particular to this genre, a model as implementer and a newcomer;
- [`AGENTS.md`](AGENTS.md) and [`llms.txt`](llms.txt): how to change this repository, and its index for language models;
- `checks/`: the settings that extend reader-ergonomics' and the local checks, with their tests.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error ([checks.yml](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/.github/workflows/checks.yml)). The
badge at the top is its last result: the proof that this repository obeys the standard it extends.
Every push to master also renders the site, [tewf.github.io/reader-ergonomics-software-design](https://tewf.github.io/reader-ergonomics-software-design/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/.github/workflows/pages.yml)).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
