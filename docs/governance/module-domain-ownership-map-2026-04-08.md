---
object_type: domain_ownership_map
trust_zone: canonical
lifecycle_status: active
provenance_note: "Authored on 2026-04-08 from observed repository layout, then updated on 2026-04-13 during Wave A path normalization to lock doctrine and schema authority boundaries."
reason_for_inclusion: "Document module intent and stewardship boundaries after canonical doctrine and schema path decisions are fixed."
---

# Module / Domain Ownership Map (2026-04-08)

Operating assumption: this repository is in solo-maintainer mode, so all domains are currently stewarded by the maintainer unless explicitly delegated.

| Module path | Domain responsibility | Current steward | Notes |
|---|---|---|---|
| `.github/workflows/` | CI policy enforcement and automation controls | Solo maintainer | Operational guardrails for governed change |
| `data/` | Runtime and generated data surfaces (claims, graph, retrieval, AI output) | Solo maintainer | Keep generated/inferred artifacts distinct from canonical authored doctrine |
| `docs/` | Human-readable canonical documentation | Solo maintainer | Phase docs and topic docs live here, except explicitly deprecated compatibility paths |
| `docs/doctrine/` | Canonical doctrine authoring surface | Solo maintainer | Primary doctrine path |
| `docs/doctrines/` | Legacy doctrine redirect surface | Solo maintainer | Preserve old links only; no substantive doctrine edits |
| `docs/governance/` | Governance rules and operating contracts | Solo maintainer | Canonical structural source for contributor discipline |
| `docs/schemas/` | Schema documentation and reference examples | Solo maintainer | Prose/reference only; not the machine-contract root |
| `ontology/` | Ontology migration-buffer and reference-draft candidates | Solo maintainer | Non-canonical authored source area for now; files may be classified as migrate or reference-only |
| `reports/` | Review and quality reporting outputs | Solo maintainer | Evidence for promotion/revision loops |
| `schema/` | Deprecated legacy templates | Solo maintainer | Legacy template territory retained for compatibility; no canonical contract authority |
| `schemas/` | Canonical machine-readable contracts | Solo maintainer | Schema registry and contract source of truth |
| `examples/` | Worked examples and demonstrations | Solo maintainer | Present but currently sparse |
| `scripts/` | Utility scripts for maintenance and migration | Solo maintainer | Should remain support layer, not canonical doctrine source |

## Ownership boundary note

Canonical doctrine/governance intent should be authored in `docs/` and `docs/governance/` first, then reflected into machine-readable schema and data layers without reversing authority direction.

Wave A authority lock:
- authored doctrine content belongs in `docs/doctrine/`
- `docs/doctrines/` is legacy redirect-only
- machine-readable contracts belong in `schemas/`
- `schema/` is deprecated legacy template territory
- `docs/schemas/` is documentation/reference only
- `ontology/` may inform later migration work, but it is not the canonical authored source and should be treated as migrate/reference-only support until target homes exist
