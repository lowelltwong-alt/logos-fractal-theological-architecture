---
object_type: integration_note
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-07 while integrating the exceptions-lake import request into native repository architecture."
reason_for_inclusion: "Record where imported exceptions-lake concepts landed so future contributors can trace absorption rather than treating the pack as a sidecar dump."
---

# Exceptions Lake Integration Note

## Intent

This note records how the exceptions-lake import material was absorbed into native repository locations.

## Landing map

- Core governance model and grammar:
  - `docs/governance/exceptions-lake-and-learning-loop.md`
- Roadmap integration extension:
  - `docs/roadmap/exceptions-lake-learning-loop-roadmap-extension.md`
- Graph machine-readable scheme:
  - `data/graph/schemes/exceptions-lake.md`
- Graph machine-readable template:
  - `data/graph/templates/exception-event-object-template.json`
- Root architecture orientation update:
  - `README.md`

## Preservation commitments

The integration preserves:

- canonical nine-layer address
  - `root.domain.capability.entity.instance.state.expectation.exception.adaptation`
- explicit distinction between expectation, exception, and adaptation
- AIRCA bridge logic (Architect, Inform, Rank, Commit, Act)
- governance-layer review path (worldview, institutional, operating, human, technical)
- pressure-vector lenses (theological, psychological, moral, political, economic, cultural)

## Architectural result

The exceptions-lake concept now sits in governed repository layers (README, governance, roadmap, graph support) and is not treated as a standalone import sidecar.

## Archival import preservation

The old PR #5 material is preserved under `incoming/exceptions-lake/` as archival incoming context only.

That folder is useful for provenance and handoff context, but it is not a canonical authored source and should not replace the normalized governance, roadmap, or graph surfaces listed above.
