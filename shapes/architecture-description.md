# Shape: architecture description

This shape describes the structure of one system for the people, and the models, who must work on it. It is ordered
by the questions a reader brings, so each reader reaches their answer without reading the rest:

- who the description is for;
- what is around the system, and what its parts are;
- what must always hold;
- how it runs, and where;
- why it has this shape, answered by a link to the decision records rather than a copy.

## When to use it

- For a system that a newcomer must find their way in, or that more than one team changes.
- Kept beside the code, as one file for a small system or one folder for a large one.
- Not for the reasons behind the structure: those are [decision records](decision-record.md), linked from here.
- Not for one algorithm or one proposal: those are an [algorithm specification](algorithm-specification.md) and a
  [design document](design-document.md).

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Readers and tasks | who the description serves, and which questions it answers | stakeholders and concerns (ISO 2022); readers wish for task-specific content (Rost 2013) | convention; measured, descriptive (147 respondents, self-report) |
| Purpose and context | what the system is for and what it touches, on the first page | newcomers want the whole early (Dagenais 2010); C4 level 1 (Brown 2026a); arc42 section 3 (Starke 2026) | supported with caveat |
| Map of the parts | each part in one line, by the name a reader can search for | the [codemap](../evidence/architecture-descriptions/frame.md) of ARCHITECTURE.md (matklad 2021); C4 containers and components | convention, untested |
| Invariants and boundaries | what must always hold, including what must be absent | matklad 2021 | convention, untested |
| Runtime | how the parts interact while running | arc42 section 6; the component-and-connector views of Views and Beyond | convention, untested |
| Deployment | where the parts run | arc42 section 7; Kruchten 1995 | convention, untested |
| Cross-cutting concepts | what holds everywhere, written once and linked | arc42 section 8; perspectives (Rozanski 2011) | convention, untested |
| Decisions | a pointer to the decision records | the rationale of ISO 2022 and Views and Beyond, kept in one place | convention |
| Risks and quality goals | what could fail, and what the structure must deliver | arc42 sections 10 and 11 | convention, untested |
| Glossary | each term once | arc42 section 12 | convention |
| Date and upkeep | when it was true, and how it is kept so | readers rank up-to-date first among their wishes (Rost 2013) | measured, descriptive (self-report) |

- Why stable facts first: abstract, high-level documentation is trusted more and stays useful when detail goes stale
  (Lethbridge 2003, supported with caveat).
- Why by readers' questions: organising architectural knowledge that way went with better retrieval, in two case
  studies (de Graaf 2016, supported with caveat).
- What is not known: a structured description against an essay showed no significant effect on newcomers' scores,
  and prior familiarity with the code dominated (Ernst 2023, measured, 65 students, one system). No trial compares
  arc42, C4 or ARCHITECTURE.md; the [baseline](../evidence/architecture-descriptions/baseline.md) names the
  comparison.
- For a coding agent as reader: about 7 in 10 agent context files carry an architecture section (Chatlatanagulchai
  2026), yet repository overviews did not help coding agents in two test settings (Gloaguen 2026, measured). Keep the
  map short and searchable rather than long.

## The principles it applies

| Part | Principle |
|---|---|
| Readers, purpose and context before the parts | [overview first](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/overview-first.md) |
| Cross-cutting concepts and decisions linked, not repeated | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/collection/one-place-per-fact.md) |
| A glossary, terms defined before use | [define before use](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/define-before-use.md) |
| Context, runtime and deployment drawn | [draw relations](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/page/draw-relations.md) |

## The skeleton

```markdown
# Architecture of <system>

**For:** <readers>, to <the tasks this answers>. **True as of:** <date>; kept current by <how>.

## Purpose and context
<What the system is for, who uses it, what it touches. A context diagram with a key.>

## Parts
| Part | Where (searchable name) | What it does |
|---|---|---|

## Invariants and boundaries
- <What must always hold, and what must never appear where.>

## Runtime
<How the parts interact while running; a diagram with a key.>

## Deployment
<Where each part runs.>

## Cross-cutting concepts
- <A concept that holds everywhere, stated once: errors, configuration, security.>

## Decisions
See `decisions/`, one record per decision.

## Risks and quality goals
- <A quality the structure must deliver, and what could break it.>

## Glossary
| Term | Meaning |
|---|---|
```

## The rules

1. The first lines name the readers and their tasks; a reader not served there knows to stop.
2. Purpose and context fit on the first page, before any part.
3. Each part is named as it is named in the code, so a reader can search for it; addresses that go stale are avoided.
4. Invariants include absences: what must never depend on what, what must never appear where.
5. Runtime and deployment are separate sections, so an operator reaches them directly.
6. A concept that holds everywhere is written once and linked from the parts that use it.
7. Reasons are links to decision records, not copies of them.
8. The description says when it was true and how it is kept so; a description nobody updates says that too.

## Worked example

# Architecture of reader-ergonomics-software-design

**For:** maintainers and coding agents, to find where a fact lives and what a change touches. **True as of:**
2026-10-29; kept current by the checks on every push.

## Purpose and context
A body of evidence and templates for designing software before the code. It extends reader-ergonomics, whose checks
CI runs on it at a pinned release commit. A site is built from it on each push.

## Parts
| Part | Where | What it does |
|---|---|---|
| Evidence | `evidence/<topic>/` | one multivocal review per topic, with its protocol and scored sources |
| Bibliography | `evidence/bibliography.md` | every cited work, once |
| Shapes | `shapes/` | the templates, each part with its evidence |
| Decisions | `decisions/` | this repository's own decision records |
| Local checks | `checks/local/`, `checks/config.toml` | what this repository checks beyond the standard |

## Invariants and boundaries
- Nothing here copies a principle of reader-ergonomics: it links it, at the pinned commit.
- Every work cited has one bibliography row, and every judgment answer quotes its own file.

## Runtime
On each push, CI checks out this repository and reader-ergonomics at the pinned commit. It runs the standard's checks
and this repository's tests; the site is then rendered and published.

## Deployment
GitHub Actions runs the checks; GitHub Pages serves the site.

## Cross-cutting concepts
- Grades: every claim carries one (measured, supported with caveat, convention, untested).

## Decisions
See [decisions/](../decisions/README.md).

## Risks and quality goals
- A rename in reader-ergonomics could break links; [record 0001](../decisions/0001-pin-links-at-the-release-commit.md)
  pins them.

## Glossary
| Term | Meaning |
|---|---|
| shape | the fixed skeleton of one kind of document |
| multivocal review | a review of research and grey literature together |
