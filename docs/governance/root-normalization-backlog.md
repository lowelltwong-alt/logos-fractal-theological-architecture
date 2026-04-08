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

- `docs/scripture/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/hermeneutics/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/biblical-themes/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/translations/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/original-languages/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/manuscripts/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/noncanonical/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/scripture/genesis/README.md` ✅ normalized in phased run (2026-04-08)
- `docs/scripture/genesis/1.md` ✅ normalized in phased run (2026-04-08)
- `docs/original-languages/hebrew/tselem.md` ✅ normalized in phased run (2026-04-08)
- `docs/original-languages/hebrew/demut.md` ✅ normalized in phased run (2026-04-08)
- `docs/translations/mainstream-modern/esv.md` ✅ normalized in phased run (2026-04-08)
- `docs/manuscripts/mt.md` ✅ normalized in phased run (2026-04-08)

## Next phased run target

Root normalization backlog is complete for the current high-priority list.
Next phase should validate metadata depth (not just presence) and tune any address refinements through migration records when needed.

## Normalization rule

When normalizing older files:
1. preserve existing IDs and anchors
2. add address rather than replacing identity
3. do not silently change theological content while only normalizing metadata
4. use migration records if an address later changes after initial normalization

## Summary principle

Normalization should make older nodes legible to the new operating framework without breaking their semantic continuity.
