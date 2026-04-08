# Retrieval Neighborhoods

## Purpose

This folder is the entry point for governed retrieval neighborhoods and context packages in the Logos repository.

## Auto-generated governed bundles

Neighborhood bundles are auto-generated from:
- graph JSON objects (for typed edge context)
- claim YAML objects (for doctrinal and application linkage)
- trust-zone filters (`canonical`, `tradition-scoped`, `proposed`)

Generation command:

```bash
python3 scripts/generate_retrieval_neighborhoods.py
```

Validation command:

```bash
python3 scripts/validate_retrieval_neighborhoods.py
```

## Deterministic expansion rules

Neighborhoods are generated per neighborhood type (`passage`, `application`, `concept`, `doctrine`, `comparison`) with deterministic rules:
- bounded expansion depth per type
- predicate allow-lists per type
- lexical / translation / witness predicates (`clarifies`, `renders`, `attests`) auto-included for included text nodes
- typed-edge inclusion from graph `relationships.typed_edges` and relationship artifacts
- trust filtering before expansion

## Artifact outputs

For each high-value focus node, the generator emits both:
- `*-neighborhood.auto.yaml`
- `*-neighborhood.auto.json`

Artifacts include freshness metadata so stale bundles are flagged automatically by validation.
