# Schemas and Machine-Readable Templates

## Purpose

This folder defines the schema layer for the Logos Fractal Theological Architecture repository.

The schema layer exists to translate the repository’s governance logic, ontology discipline, controlled vocabulary, provenance rules, and recursive architecture into machine-readable structures that can be reused across artifacts.

This branch does not replace the human-readable branches. It gives them a governed machine-readable companion.

That means this folder should hold:
- schema reference documents
- machine-readable templates
- migration notes from older templates into the newer governed structure
- field-family guidance for provenance, ontology, lifecycle, inheritance, and permissions

## Why this branch matters

The repository is designed for:
- human-readable theological architecture
- semantic retrieval and RAG-style use
- recursive node buildout
- future ontology promotion
- explicit provenance and vocabulary discipline

Because of that, machine-readable templates should not drift away from the repo’s governance logic.

If the prose architecture and the machine-readable structures diverge, the repository becomes much harder to reuse consistently. That is especially dangerous in a project where future AI systems may interrogate, compare, transform, or extend artifacts through their sidecars.

## Dominant node types

The dominant node types in this branch are:

- `governance_node`
- `synthesis_node`
- `crosswalk_node`

This is because the schema branch is primarily about governed translation, reusable structural patterns, and alignment between the repository’s ontology and its machine-readable templates.

## Design rule

The schema branch should follow the same project rule as the rest of the repository:

**keep the recursive shell stable, and let controlled vocabulary and typed nodes do most of the work**

That means:
- prefer extending governed vocabulary before redesigning the skeleton
- prefer typed node families before generic overloading
- prefer explicit provenance fields before vague influence language
- prefer alignment, misalignment, and translation-status fields over casual comparison language
- prefer stable branch-level templates before ad hoc sidecar invention

## What this branch should produce over time

A mature schema branch should make it possible to:
- create governed sidecars for major repository artifacts
- encode theology, governance, and philosophy nodes in a reusable way
- represent provenance, synthesis, appropriation, and adaptation explicitly
- preserve lifecycle and permissions for long-term AI use
- align human-readable branch logic with machine-readable structures
- support migration from older fractal decision artifacts into the newer Logos-governed ontology

## Key files to expect here

This branch should eventually include:
- a governed schema reference document
- a canonical JSON template for governed nodes
- a migration guide from older decision-node templates
- examples of theology-side and application-side sidecars

## Related governance files

This branch should be read alongside:
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/relationship-registry.md`
- `docs/governance/node-types.md`
- `docs/governance/node-header-template.md`
- `docs/governance/provenance-and-appropriation.md`

## Summary principle

The schema branch should not merely store JSON patterns.

It should function as the machine-readable translation layer for the governed theological architecture of the repository.
