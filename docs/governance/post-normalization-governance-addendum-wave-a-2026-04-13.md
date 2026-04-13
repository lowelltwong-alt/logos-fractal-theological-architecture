---
object_type: governance_addendum
trust_zone: canonical
lifecycle_status: active
provenance_note: "Authored on 2026-04-13 immediately after Wave A path normalization to record the new doctrine and schema authority model without rewriting 2026-04-08 baseline snapshots."
reason_for_inclusion: "Preserve historical governance baselines while providing one current post-normalization record of path authority after Wave A."
---

# Post-Normalization Governance Addendum (Wave A, 2026-04-13)

## Purpose

This addendum records the authority model established after Wave A path normalization.

It exists so that the repository can preserve older 2026-04-08 governance files as historical snapshots while still having one current statement of the post-normalization path model.

## Historical record note

The following governance files remain historical records of the pre-normalization repository state and should be read that way:
- `docs/governance/alignment-baseline-2026-04-08.md`
- `docs/governance/module-intentional-change-and-drift-notes-2026-04-08.md`
- `docs/governance/top-level-tree-map-2026-04-08.md`

Those files intentionally preserve the repository structure and ambiguity that existed before Wave A.
This addendum does not replace them as snapshots.
It supersedes them only for current path-authority interpretation.

## Wave A authority model

### Doctrine authority

- `docs/doctrine/` is the canonical doctrine authoring path.
- `docs/doctrines/` is a legacy redirect-only compatibility surface.
- Legacy doctrine paths are preserved for link stability, but they are not a second doctrine authority surface.

### Schema authority

- `schemas/` is the canonical machine-readable contract root.
- `schema/` is deprecated legacy template territory retained for compatibility and migration continuity.
- `docs/schemas/` is documentation/reference only and is not the machine-contract root.

## Ontology status in Wave A

- `ontology/` remains non-canonical authored source material for now.
- In this wave it functions as a migration buffer or draft/reference layer rather than an authoritative authored doctrine/governance surface.
- Ontology migration decisions are deferred to later cleanup waves.

## Interpretation rule

When path authority is ambiguous between the historical 2026-04-08 governance records and current repository operation, use this addendum for current-state interpretation after Wave A.
