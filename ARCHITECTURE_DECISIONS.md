# Architecture Decisions

This file records design choices that should remain visible at the repository surface.

It exists so later contributors do not treat important structural patterns as disposable implementation details.

## AD-0001 — Keep a governed exceptions-lake and learning-loop layer

**Status:** accepted  
**Priority:** architectural  
**Scope:** repo-wide

### Decision

The repository intentionally keeps an exceptions-lake and learning-loop layer as part of the core architecture.

This layer should remain distinct from:
- ontology
- taxonomy
- doctrine content
- ordering profiles
- governance rules

### Why this stays

A living theological architecture needs a place to record where reality resists the current model without forcing silent doctrine drift.

That means the repository needs a governed memory surface for:
- expectation failure
- unresolved mismatch
- recurring pressure
- adaptation proposals
- reviewed promotion into rule, taxonomy, ontology, or governance updates

Without that layer, the architecture tends to fail in one of two ways:

1. **silent mutation**  
   The model changes informally under pressure, but no one can see when or why.

2. **rigid brittleness**  
   The model has no place to hold resistance, so pressure accumulates outside the architecture.

The exceptions-lake pattern is therefore intentional because it lets the repository learn while preserving lineage, review, and doctrinal accountability.

### Core principle

The system should be able to adapt without pretending that adaptation is the same thing as truth.

So the repository keeps these objects distinct:
- **expectation**
- **exception**
- **adaptation**
- **promotion decision**

### Design consequence

This is not an optional sidecar.

It is part of the repository DNA because the project is trying to become:
- recursive
- governable
- pressure-aware
- self-correcting under review
- resistant to silent deformation

### Implementation surfaces

This decision is expressed in:
- `README.md`
- `docs/governance/exceptions-lake-and-learning-loop.md`
- `docs/governance/exceptions-lake-integration-note.md`
- `docs/roadmap/exceptions-lake-learning-loop-roadmap-extension.md`
- `docs/roadmap/repository-integration-map.md`
- `data/graph/schemes/exceptions-lake.md`

### Future rule

Any proposal that weakens or removes the exceptions-lake / learning-loop layer should be treated as an architecture-level change, not a local cleanup.
