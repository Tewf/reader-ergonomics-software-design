# Architecture of reader-ergonomics-software-design

**For:** maintainers and coding agents, to find where a fact lives and what a change touches. **True as of:**
2026-10-29; kept current by the checks on every push.
**Shape:** [architecture description](../shapes/architecture-description.md)

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
