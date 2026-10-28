# Software design writing

How to write about software (architecture descriptions, decision records, design documents, pseudocode and diagrams
of a system) so that it costs the reader as little as possible.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository will add only what is particular to writing about software: its
evidence, and the shapes of its documents.

> **Status:** work in progress. Four literature reviews are written in [evidence/](evidence/), each a multivocal review of
> research and practice; their numbers are not audited yet, and the shapes and principles are not started. It is an
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
| out | how to design the system itself: modularity, coupling, architecture quality | another object, with its own evidence and its own checks |
| out | how code is laid out in files and folders | already covered by the collection principles of reader-ergonomics |

## Layout

The same as reader-ergonomics, so a reader of one can find their way in the other:

- `evidence/<topic>/`: one literature review per topic, one file per step (frame, review, state of the art, position,
  the case against, baseline), plus its protocol and its scored sources; written for four topics;
- `shapes/`: the skeleton of each kind of document, with the evidence behind each part (planned);
- `principles/`: only where writing about software differs from the general standard (planned).

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push; see [.github/workflows/checks.yml](.github/workflows/checks.yml).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
