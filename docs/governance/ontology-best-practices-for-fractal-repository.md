# Ontology Best Practices for the Fractal Theological Repository

Author: Lowell T. Wong
Status: draft
Purpose: define repository-specific ontology best practices that preserve machine legibility, governability, theological clarity, and long-term extensibility.

## 1. Design for stable identity

Every important reusable concept should have:
- a stable identifier
- a stable anchor or slug
- a clear node family
- a canonical source-of-truth location
- aliases where naming varies across traditions or translations

Do not use file path alone as identity.

## 2. Prefer typed objects over loose mentions

If a concept will recur across many files, promote it into a typed object rather than relying on repeated prose mentions.

High-priority promotion targets:
- doctrines
- traditions
- theologians
- scripture themes
- AI issues
- discernment questions
- profile objects
- governance policies

## 3. Use controlled vocabularies aggressively

Controlled vocabularies should govern:
- node types
- relationship verbs
- doctrine tiers
- consensus scope
- belief-state values
- canonical status
- trust zone
- confidence values
- action permissions

Freeform language belongs in prose explanation, not in the core semantic control layer.

## 4. Separate assertion from inference

The repository should clearly distinguish:
- asserted claims
- inferred links
- speculative links
- translated equivalences
- contested relationships

This is essential for theology, manuscript handling, and AI-assisted retrieval.

## 5. Separate source from synthesis

A directly sourced theological claim is not the same as an author synthesis.

The ontology should preserve distinctions such as:
- direct derivation
- multi-source synthesis
- appropriation
- adaptation
- analogy
- translation burden
- conceptual misalignment

## 6. Treat trust and authority boundaries as structural

This repository needs trust-aware modeling.

That means preserving distinctions such as:
- canonical
- deuterocanonical if later used in a tradition-aware way
- noncanonical
- heretical or condemned in some traditions
- modern commentary
- boundary or comparison source
- non-Christian philosophical source

These are not mere tags. They are ontology-relevant trust classifications.

## 7. Preserve provenance at every important layer

Important objects should preserve provenance for:
- source references
- derivation method
- transformation history
- authoring mix
- review status
- confidence rationale

Without provenance, theological structure becomes much harder to trust.

## 8. Model relationships as first-class structure

Do not treat relationships as decorative.

Relationships should carry meaning such as:
- derives_from
- depends_on
- supports
- constrains
- interpreted_by
- contested_by
- translated_as
- aligned_with
- misaligned_with
- requires_discernment_of
- materially_changes_judgment_on

Where a relationship is important, relationship metadata should capture strength, direction, confidence, and any trust implications.

## 9. Preserve human-readable and machine-readable pairing

This repository should not become graph-only or prose-only.

The best pattern is:
- prose for explanation
- structured metadata for retrieval and comparison
- sidecars or governed graph objects for machine use

## 10. Design for partial knowledge and unresolved states

Christian theology and Christian discernment contain real unresolved or tradition-varying questions.

The ontology must preserve states such as:
- unknown
- unresolved
- disputed
- tradition-dependent
- undecided by user
- not required for current issue

Blank space should never silently imply consensus.

## 11. Keep ontology broad but operational

A useful ontology is not only hierarchical. It should support real use.

This repository’s ontology should be operational enough to support:
- retrieval
- cross-comparison
- branchable discernment
- profile construction
- decision support
- governance review
- future graph objects

## 12. Promote repeated decision logic into reusable objects

If the same question keeps reappearing, do not leave it buried in prose.

Promote it into reusable objects such as:
- discernment question nodes
- issue profiles
- doctrine tier profiles
- recommendation paths

## 13. Use validation to protect meaning

Validation should cover more than required fields.

It should also check for:
- invalid vocabulary drift
- broken relationship expectations
- contradictory canonical status
- belief-state misuse
- weakening of parent protections
- unsafe interpretation of blank values
- improper source or trust-zone mixing

## 14. Prefer graph complement, not graph replacement

Graph structures should complement human-readable theology.

The graph layer should help with:
- typed links
- concordance navigation
- crosswalks
- provenance tracing
- validation
- machine traversal

It should not replace theological explanation.

## 15. Optimize for future AI traversal without surrendering authority

This repo should be machine-legible by design, but AI systems must not be allowed to invent authority from sparse structure.

Therefore:
- preserve explicit trust boundaries
- preserve interpretation rules
- preserve dormant optional field semantics
- preserve required human review points
- preserve source-of-truth references

## 16. Keep promotion and extension disciplined

When a new concept appears repeatedly, ask in order:
1. should this become a node?
2. should this become a controlled vocabulary value?
3. should this become a typed relationship?
4. should this become a reusable profile object?
5. only then, should this alter structure?

## 17. Repository-specific best-practice summary

For this repository, world-class ontology practice means:
- stable ids
- typed reusable nodes
- explicit trust zones
- provenance-aware structure
- direct versus inferred separation
- controlled vocabulary discipline
- validation of meaning, not just syntax
- human-readable first, machine-ingestible by design
- operational support for Christian AI discernment

## 18. Practical test

A strong ontology here should let a user or system move from:
- doctrine
- to tradition stance
- to user belief state
- to AI issue
- to discernment recommendation
- to governance rationale

without losing provenance, confidence, or theological distinctions.