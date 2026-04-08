# Data Layer

## Purpose

This folder holds the machine-first object layer for the Logos repository.

Unlike the `docs/` branch, which explains architecture, rationale, governance, and contributor logic in human-readable form, the `data/` branch is where stable machine-readable objects should increasingly live.

For the concordance buildout, this folder is the practical home for:
- verse nodes
- passage nodes
- translation witness nodes
- lemma nodes
- entity nodes
- concept nodes
- doctrine nodes
- relationship objects where the edge itself becomes important enough to preserve as its own governed artifact
- provenance objects and validation shapes later on

## Design rule

The `data/` branch should be treated as the machine-readable companion to the governed architecture defined in `docs/`.

That means:
- object identity should be stable
- filenames should track canonical ids or anchors where practical
- node families should stay separated
- imported material should not be confused with approved graph objects
- provenance and review state should remain visible when meaningful

## Recommended long-term layout

```text
/data
  /sources
    /bible
    /imported
  /graph
    /verses
    /passages
    /translations
    /lemmas
    /entities
    /topics
    /concepts
    /doctrines
    /philosophy
    /interpretations
    /relationships
  /provenance
  /shapes
  /snapshots
```

## What is being built first

The concordance is being made concrete in this order:
1. sample verse nodes
2. sample passage node
3. sample translation witness node
4. sample entity and concept nodes
5. typed relationship examples

That order is intentional.

The project is trying to make the immutable reference and low-risk graph layers concrete before heavier interpretive or imported-data layers appear.

## Summary principle

The `data/` branch should grow slowly, clearly, and with stable typed objects.

It is better to have a small trustworthy graph than a large ambiguous one.

## Cross-reference validator ID sources

`scripts/validate_cross_references.py` resolves object IDs from a unified set of machine- and human-readable sources.

Supported object ID sources:
- `docs/**/*.md` frontmatter field: `id`
- `data/graph/**/*.json` object fields:
  - `identity.id`
  - top-level `id`
  - `address.id`

Supported claim ID source:
- `data/claims/*.yaml` field: `claim_id`

Validation currently checks:
- `data/claims/*.yaml`: `subject`, `object`
- `data/retrieval/*.yaml`: `included_objects`, `included_claims`
