---
object_type: governance_addendum
trust_zone: canonical
lifecycle_status: active
provenance_note: "Authored on 2026-04-13 during Wave D to formalize ontology/ as a preserved migration buffer and non-canonical authored source area."
reason_for_inclusion: "Lock ontology path authority so contributors do not treat ontology/ as a competing canonical publication surface while migration planning is still incomplete."
---

# Ontology Migration Buffer Addendum (Wave D, 2026-04-13)

## Purpose

This addendum formalizes the current role of `ontology/` after the earlier doctrine, schema, validator, and link-normalization waves.

Its purpose is to preserve useful draft/reference material without allowing `ontology/` to function as a second canonical authored source surface beside `docs/`.

## Authority rule

- `docs/` remains the canonical authored source area for governed human-readable publication surfaces.
- `ontology/` is a preserved migration buffer, reference-draft layer, and non-canonical authored source area for now.
- Files under `ontology/` are not current canonical publication surfaces, even when they contain useful upstream theological or AI-governance material.

## Why `ontology/` is being preserved

`ontology/` is being preserved because it still contains source material that is useful for:
- migration planning into governed `docs/` paths
- reference comparison while canonical homes are being established
- draft preservation so potentially valuable work is not lost or silently overwritten

Preservation does not imply authority.
It means the material remains available until governed target homes and migration notes exist.

## Current classification rule

Ontology material should currently be treated under one of these statuses:

- `migrate`: the file contains substantive material that should eventually be normalized into a governed `docs/` path when an appropriate target home exists
- `reference-only`: the file is useful as seed/reference material but does not yet have, or may never need, a direct canonical publication home in its current form

Neither status makes the ontology file itself canonical.

## Migration rule

Material should move from `ontology/` into governed `docs/` paths only when:
1. a target home exists or is created under `docs/`
2. the migration target is identified explicitly
3. a migration note or governance record explains what moved and why

Until then, ontology files may inform planning and authored migration work, but they should not be edited as if `ontology/` were the canonical publication surface.

## Retirement rule

No ontology file should be retired or deleted merely because a future target is anticipated.

Retirement/deletion is deferred until:
- a governed target home exists
- the relevant material has been migrated or intentionally classified as reference-only
- migration notes are recorded so the transition remains auditable

## Interpretation rule

If contributors encounter overlapping material between `docs/` and `ontology/`, treat `docs/` as authoritative for current authored state and treat `ontology/` as migration/reference support only unless a later governance note explicitly changes that rule.
