# Root Normalization Backlog

## Purpose

This file records the remaining in-place normalization work for older branch-root files that still need the newer operating-framework metadata shell.

## Why this backlog exists

The repository now has an address model, trust model extensions, claim layer, and AI-build governance files. Some older branch roots were written before that operating shell existed and therefore still need in-place normalization.

## Target fields to add where missing

The highest-priority normalization fields are:
- `address`
- `trust_zone`
- `lifecycle_state`
- `epistemic_status`
- `overlay_scope`
- `shared_core_status`
- `source_basis`
- `ai_usage_posture`

## Highest-priority files

- `docs/scripture/README.md`
- `docs/hermeneutics/README.md`
- `docs/biblical-themes/README.md`
- `docs/translations/README.md`
- `docs/original-languages/README.md`
- `docs/manuscripts/README.md`
- `docs/noncanonical/README.md`
- `docs/scripture/genesis/README.md`
- `docs/scripture/genesis/1.md`
- `docs/original-languages/hebrew/tselem.md`
- `docs/original-languages/hebrew/demut.md`
- `docs/translations/mainstream-modern/esv.md`
- `docs/manuscripts/mt.md`

## Normalization rule

When normalizing older files:
1. preserve existing IDs and anchors
2. add address rather than replacing identity
3. do not silently change theological content while only normalizing metadata
4. use migration records if an address later changes after initial normalization

## Summary principle

Normalization should make older nodes legible to the new operating framework without breaking their semantic continuity.
