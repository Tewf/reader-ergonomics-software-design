# Software design

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-software-design/)

How to design software at the abstract layer just before the code: its architecture, the running system, its
algorithms and their specifications. And how to write about it (architecture descriptions, decision records, design
documents, pseudocode and diagrams), at the least cost to the reader and to whoever implements it.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository will add only what is particular to software design and the writing
about it: its evidence, and the shapes of its documents.

> **Status:** work in progress. Seven literature reviews are written in [evidence/](evidence/), each a multivocal review of
> research and practice; their numbers were audited against the primary sources (four on 2026-10-28, three on 2026-10-29). Two shapes are
> written, the algorithm specification and the design document; the other shapes and the principles are not started. It is an
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
- [`shapes/`](shapes/): the skeleton of each kind of document, with the evidence behind each part; written are the
  [algorithm specification](shapes/algorithm-specification.md) and the [design document](shapes/design-document.md), and three more are planned;
- `principles/`: only where writing about software differs from the general standard (planned).

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
