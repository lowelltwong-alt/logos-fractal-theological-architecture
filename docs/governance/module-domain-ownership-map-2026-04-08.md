---
object_type: domain_ownership_map
trust_zone: canonical
lifecycle_status: active
provenance_note: "Authored on 2026-04-08 from observed repository layout and solo-maintainer governance mode."
reason_for_inclusion: "Document module intent and stewardship boundaries before structural normalization."
---

# Module / Domain Ownership Map (2026-04-08)

Operating assumption: this repository is in solo-maintainer mode, so all domains are currently stewarded by the maintainer unless explicitly delegated.

| Module path | Domain responsibility | Current steward | Notes |
|---|---|---|---|
| `.github/workflows/` | CI policy enforcement and automation controls | Solo maintainer | Operational guardrails for governed change |
| `data/` | Runtime and generated data surfaces (claims, graph, retrieval, AI output) | Solo maintainer | Keep generated/inferred artifacts distinct from canonical authored doctrine |
| `docs/` | Human-readable canonical documentation | Solo maintainer | Phase docs and topic docs live here |
| `docs/governance/` | Governance rules and operating contracts | Solo maintainer | Canonical structural source for contributor discipline |
| `ontology/` | Ontology-ready doctrinal/tradition nodes | Solo maintainer | Candidate structured theology core |
| `reports/` | Review and quality reporting outputs | Solo maintainer | Evidence for promotion/revision loops |
| `schema/` | Template-style schema artifacts | Solo maintainer | Contains decision artifact templates |
| `schemas/` | Schema registry and minimal validation schemas | Solo maintainer | Naming collision with `schema/` to resolve later |
| `examples/` | Worked examples and demonstrations | Solo maintainer | Present but currently sparse |
| `scripts/` | Utility scripts for maintenance and migration | Solo maintainer | Should remain support layer, not canonical doctrine source |

## Ownership boundary note

Canonical doctrine/governance intent should be authored in `docs/` and `docs/governance/` first, then reflected into machine-readable schema and data layers without reversing authority direction.
