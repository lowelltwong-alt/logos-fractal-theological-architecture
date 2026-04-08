---
object_type: canonical_index_snapshot
trust_zone: canonical
lifecycle_status: active
provenance_note: "Indexed on 2026-04-08 from the current repository state for alignment baseline work."
reason_for_inclusion: "Provide a fixed reference index of canonical docs and manifest-like assets used during cleanup."
---

# Canonical Docs Index (2026-04-08)

## A. `docs/` top-level canonical categories

- applications
- biblical-themes
- canon
- concepts
- concordance
- derivations
- doctrine
- doctrines
- governance
- hermeneutics
- instantiations
- integrations
- lairca
- manuscripts
- noncanonical
- operating-system
- orderings
- original-languages
- philosophy
- primary-sources
- roadmap
- schemas
- scripture
- translations
- weightings
- plus phase and handoff docs at `docs/*.md`

## B. `docs/governance/` canonical governance corpus

Primary governance corpus currently includes:
- structural discipline (ontology, anchor, tag, relationship, node-type policies)
- trust-zone and promotion model docs
- AI workflow and HITL governance docs
- validation/CI and drift-detection policy docs
- retrieval, review queue, and feedback loop docs
- operating framework index and continuation guides

Reference root for this corpus: `docs/governance/README.md` and `docs/governance/operating-framework-index.md`.

## C. Manifest / machine-readable index points

Observed manifest-like machine-readable artifacts:
- `CITATION.cff`
- `schemas/schema_registry.json`
- `schemas/logos_node_min.schema.json`
- `schemas/logos_claim_min.schema.json`
- `schema/discernment-profile-template.json`
- `schema/fractal-decision-artifact-template-v2.json`
- `docs/schemas/concordance-node-template.json`
- `docs/schemas/logos-governed-node-template.json`

Note: no dedicated top-level `manifests/` directory is currently present.
