# Changelog

Every release of this repository, newest first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
A move of the pin on reader-ergonomics is an entry here, not a decision record; the earlier moves are records 0002 to
0012 in [decisions/](decisions/README.md).

## [1.1.1] - 2026-11-07

### Changed

- Pinned reader-ergonomics v1.22.1 (`0206e69`), from v1.18.2 (`bfbe9f7`): front matter skipped and LaTeX maths blanked, a shape's skeleton skipped by duplication, escaped-pipe wikilinks resolved, `run.py --out`, `release-version`, and `standard-pin` moves a pin.

## [1.1.0] - 2026-11-07

### Added

- A sixth shape, the [model specification](shapes/model-specification.md): an optimisation model stated before it is coded for a solver, with the local check `model-specs` and an example ([decision 0013](decisions/0013-a-model-specification-beside-the-algorithm-specification.md)).
- "Reduction to a known model" among the techniques of the algorithm specification.

## [1.0.1] - 2026-11-04

### Changed

- The citation file and the Status line now cite the repository as release 1.0.0, no longer work in progress.
- Tag v1.0.1 and a GitHub release of the same name.

## [1.0.0] - 2026-10-29

### Changed

- Pinned reader-ergonomics v1.18.2 (bfbe9f7), from v1.13.0 (7a76cc6): grades per clause, the changelog form and its check, the Take your own version section, blueprint listed as the sixth extension.
