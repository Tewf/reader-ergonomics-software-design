# Contributing to this repository

For anyone changing this repository, person or language model. To design software with it, read
[standard.md](standard.md) instead; this file is about this repository only. It extends reader-ergonomics through the
interface in that repository's [extending.md](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/extending.md), and relies on nothing else there.

## Before writing

1. Read reader-ergonomics' [standard.md](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/standard.md), then this repository's [standard.md](standard.md). A
   principle that reader-ergonomics holds is linked, never restated here.
2. A principle belongs here only when software design changes it: the reader is often an implementer, a person or a
   model, who builds from the text.
3. A document follows a shape when it says so: a `**Shape:**` line that links the shape's file. The local checks find
   their documents by that line.
4. A choice about this repository itself (its scope, a pin, a check) is a record in [decisions/](decisions/README.md):
   a new record supersedes an old one, never an edit of its decision.

## Rules for claims

- The rules for claims are reader-ergonomics' own, as [its AGENTS.md](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/AGENTS.md) lists them:
  - every principle has a grade;
  - the text cites `Author Year`, with one entry in [evidence/bibliography.md](evidence/bibliography.md);
  - the evidence against a claim is kept in `against.md`;
  - a number read only in a summary is marked "(secondary)".
- A new claim comes from a review in [evidence/](evidence/README.md), written to its protocol and audited against its
  sources. A claim no review holds needs a review strand first.
- Every link into reader-ergonomics names the commit CI checks against, and moves with the pin
  ([decision 0001](decisions/0001-pin-links-at-the-release-commit.md)).

## Before handing back

```sh
READER_ERGONOMICS_CHECKS=<reader-ergonomics>/checks python3 -m unittest discover -s checks   # the local checks' tests
python3 <reader-ergonomics>/checks/run.py . --tiers program,meaning --judge flag            # the standard's checks and this repository's
python3 <reader-ergonomics>/checks/program/standard_card.py . --write                       # after changing a principle
```

- Answer every judgment question in `checks/judgments.toml` from the file it is about, quoting the file: the
  judgment-quotes check refuses an answer that quotes nothing, or quotes what is not there.
- The card's table and `llms.txt` are generated; edit the principle files, never the table.
