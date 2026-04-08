---
object_type: alignment_baseline
trust_zone: canonical
lifecycle_status: active
provenance_note: "Baseline authored on 2026-04-08 from direct repository inspection before cleanup sequencing."
reason_for_inclusion: "Establish immutable alignment reference for subsequent naming, placement, and schema normalization work."
---

# Alignment Baseline (2026-04-08)

> Baseline rule: this file is an immutable reference checkpoint for cleanup planning after 2026-04-08.

## 1) Intended architecture sources of truth

Primary intended sources of truth (highest practical authority first):
1. Repository governance contract at root (`AGENTS.md`)
2. Canonical governance discipline in `docs/governance/`
3. Canonical phase/topic docs in `docs/`
4. Structured ontology layer in `ontology/`
5. Machine-readable schema and template layers (`schemas/`, `schema/`, `docs/schemas/`)
6. Data and report layers (`data/`, `reports/`) as derived/operational outputs

## 2) Current observed structure

Observed root modules:
- governance and prose: `docs/`, especially `docs/governance/`
- ontology concepts: `ontology/`
- data and operational outputs: `data/`, `reports/`
- schemas/templates: `schemas/`, `schema/`, `docs/schemas/`
- automation: `.github/`, `scripts/`
- examples: `examples/`

Cross-cutting observation:
- multiple similarly named domains (`doctrine`/`doctrines`, `schema`/`schemas`) coexist and appear partially overlapping.

## 3) Known mismatch list

| ID | Type | Mismatch | Evidence | Baseline treatment |
|---|---|---|---|---|
| MM-001 | naming | Parallel directories `docs/doctrine/` and `docs/doctrines/` create naming ambiguity for canonical doctrine docs. | Both directories exist with overlapping topic intent. | Preserve for now; normalize later via deprecation/migration plan. |
| MM-002 | naming | Parallel top-level directories `schema/` and `schemas/` create schema-layer ambiguity. | Both directories contain machine-readable schema/template files. | Preserve for now; define target naming and migration sequence. |
| MM-003 | placement | Machine-readable schema/template assets are split across `schema/`, `schemas/`, and `docs/schemas/` instead of one coherent placement policy. | JSON schema/template files observed in all three locations. | Keep as-is in baseline; converge placement policy before moves. |
| MM-004 | schema | Mixed artifact roles (minimal validation schemas, templates, and prose schema docs) are not yet clearly separated by schema contract tier. | `schemas/*.schema.json` and template JSON files coexist with markdown schema guidance. | Establish explicit contract tiers before consolidating files. |
| MM-005 | dependency direction | Operational/data layers risk becoming de facto sources when canonical-to-derived direction is not explicitly enforced in module contracts. | `data/ai-output/` and other generated layers coexist with canonical sources. | Reassert direction rule: canonical docs -> schemas -> data outputs. |
| MM-006 | deprecated-but-active | Legacy/alternate naming tracks appear active rather than formally deprecated (especially doctrine/doctrines and schema/schemas). | No explicit deprecation markers in current folder names. | Introduce deprecation markers and migration notes before structural moves. |

## 4) Classification key for mismatch tags

Allowed mismatch classes used in this baseline:
- `naming`
- `placement`
- `schema`
- `dependency direction`
- `deprecated-but-active`

## 5) Immutability statement

This baseline is fixed to the repository state observed on **2026-04-08**.
Subsequent cleanup work should reference this file and add new dated deltas rather than rewriting this snapshot.
