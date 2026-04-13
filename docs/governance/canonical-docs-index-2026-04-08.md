---
object_type: canonical_index_snapshot
trust_zone: canonical
lifecycle_status: active
provenance_note: "Indexed on 2026-04-08 from the current repository state, then updated on 2026-04-13 during Wave A path normalization to record canonical doctrine and schema authority."
reason_for_inclusion: "Provide a reference index of canonical docs and authority-marked machine-readable assets used during cleanup."
---

# Canonical Docs Index (2026-04-08)

## A. `docs/` authority map

Canonical authored categories include:
- applications
- biblical-themes
- canon
- concepts
- concordance
- derivations
- doctrine
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
- plus selected phase and handoff docs at the top level of `docs`

Legacy compatibility path retained for link stability:
- doctrines -> redirect-only legacy surface that points to `docs/doctrine/`

Authority note:
- `docs/doctrine/` is the canonical doctrine authoring path.
- `docs/doctrines/` is not a second doctrine authority surface.
- `docs/schemas/` remains a documentation/reference branch inside `docs/`, not the machine-contract root.

## B. `docs/governance/` canonical governance corpus

Primary governance corpus currently includes:
- structural discipline (ontology, anchor, tag, relationship, node-type policies)
- trust-zone and promotion model docs
- AI workflow and HITL governance docs
- validation/CI and drift-detection policy docs
- retrieval, review queue, and feedback loop docs
- operating framework index and continuation guides

Reference root for this corpus: `docs/governance/README.md` and `docs/governance/operating-framework-index.md`.
Current post-Wave-A authority addendum: `docs/governance/post-normalization-governance-addendum-wave-a-2026-04-13.md`.

## C. Machine-readable authority points

Canonical machine-readable contract root:
- `CITATION.cff`
- `schemas/schema_registry.json`
- `schemas/logos_node_min.schema.json`
- `schemas/logos_claim_min.schema.json`

Deprecated legacy template surface:
- `schema/discernment-profile-template.json`
- `schema/fractal-decision-artifact-template-v2.json`

Documentation/reference-only schema branch:
- `docs/schemas/README.md`
- `docs/schemas/logos-governed-node-schema.md`
- `docs/schemas/concordance-node-template.json`
- `docs/schemas/logos-governed-node-template.json`

Note: no dedicated top-level manifests directory is currently present.
