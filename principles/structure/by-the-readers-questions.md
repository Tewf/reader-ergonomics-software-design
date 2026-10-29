# Order a description by the reader's questions

**Claim:** an architecture description follows its readers' questions, in order: its readers, the system's surroundings, its parts, its invariants, its runtime and deployment, and its reasons.

- **Grade:** supported with caveat.
- **Evidence:** [architecture-descriptions review](../../evidence/architecture-descriptions/review.md); [baseline, the crosswalk](../../evidence/architecture-descriptions/baseline.md).
- **Check:** `shape-conformance` (exact): a description named in checks/config.toml holds the parts of the shape.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- Name the readers and their tasks first, then purpose and context on the first page.
- Give a map of the parts by the names a reader can search for, then invariants, runtime and deployment.
- Link the reasons to the decision records, and keep stable facts above detail that changes.

## Why

- Organising architectural knowledge by readers' questions went with better retrieval, in two case studies
  (de Graaf 2016, correlation).
- Readers ask for task-specific content and for documentation kept up to date (Rost 2013, 147 respondents,
  self-report); abstract, high-level documentation is trusted more and stays useful longer (Lethbridge 2003).

## Limits

- A structured description against an essay showed no significant effect on newcomers' scores; prior familiarity with
  the code dominated (Ernst 2023, 65 students, one system).
- No trial compares arc42, C4 or ARCHITECTURE.md.
- Repository overviews did not help coding agents in two test settings (Gloaguen 2026): keep the map short.
