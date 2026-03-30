# Asserted, Inferred, and Boundary Layers

## Purpose

This file defines how the repository should distinguish between:
- asserted material
- inferred material
- tradition-scoped or boundary-sensitive material
- AI-generated or quarantine material

This distinction is one of the most important structural protections in the repository.

This file should be read together with:
- `inference-policy.md`
- `trust-zones.md`
- `operational-ontology-model.md`
- `research-synthesis-ai-era-ontology-takeaways.md`

## Core principle

The repository should never casually flatten together all knowledge into one undifferentiated layer.

A future AI system, graph tool, or human reader should be able to distinguish what is:
- directly curated
- computed or derived
- scoped to a tradition or boundary definition
- provisional, quarantined, or low-trust

## Asserted layer

The asserted layer contains local, governed, directly authored material.

Typical contents:
- direct node definitions
- direct citations and references
- direct typed edges that have been intentionally authored
- direct trust classifications
- direct scheme memberships

The asserted layer should be the main source of local truth.

## Inferred layer

The inferred layer contains material derived from governed structure.

Typical contents:
- transitive closures
- ancestor or descendant traversals
- broader or narrower expansions
- graph neighborhood expansions
- concordance rollups
- repeated pattern detection

The inferred layer should remain reproducible and separable.

Inference should enrich traversal, not silently replace authored meaning.

## Boundary or tradition-scoped layer

Some materials are not globally universal across the repository.

They are scoped to:
- a tradition
- a canon definition
- a translation boundary
- a manuscript or textual witness boundary
- a noncanonical classification framework

Those should remain explicitly scoped.

Examples:
- canonicality under a particular tradition
- deuterocanonical or apocryphal classification
- sectarian translation warnings
- tradition-specific doctrinal mappings

## Quarantine or low-trust layer

The repository may also contain material that is intentionally isolated from normal trust assumptions.

Examples:
- AI-extracted candidates
- bulk imports awaiting review
- provisional comparative claims
- low-confidence mappings
- suspicious or unstable candidate edges

Such content should not silently appear as if it were fully reviewed repository truth.

## Why this separation matters

Without layer separation, the repository becomes easier to poison, easier to misread, and harder to govern.

A downstream system may otherwise confuse:
- derivation with assertion
- comparison with endorsement
- tradition-local claims with global claims
- AI suggestions with reviewed material

## Governance rule

Every important object, edge, or graph view should be capable of being located within one of these layer families.

That does not always require a dedicated software implementation yet.
It does require that the architecture preserve the distinction conceptually and structurally.

## Promotion rule

Material may move between layers only through governed review.

Examples:
- from quarantine candidate to asserted working proposal
- from inferred pattern to promoted relationship object
- from tradition-local classification to broadly stable comparative metadata

These moves should not happen silently.

## Query and retrieval rule

Future retrieval systems should be able to filter or prioritize content by layer.

Examples:
- only asserted and high-trust nodes
- asserted plus inferred expansion
- one tradition-specific layer plus the core layer
- exclusion of quarantine or experimental material by default

## Fractal rule

Layer distinctions should recur across scales.

That means they may apply to:
- a single edge
- a node
- a branch
- a graph domain
- a dataset export

## Summary principle

A mature theological ontology does not only say what things mean.
It also preserves what kind of claim is being made, how strongly it may be trusted, and how it was produced.
