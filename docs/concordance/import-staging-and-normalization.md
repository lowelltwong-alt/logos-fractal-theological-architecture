# Import Staging and Normalization

## Purpose

This document explains how external concordances, biblical datasets, lexicons, and related source material should be brought into the concordance architecture.

The core rule is simple:

Imported data is input, not truth.

The project should be eager to ingest useful external material and conservative about promoting imported claims into trusted graph objects.

## Why this matters

External datasets can accelerate scale, but they also introduce risk.

Those risks include:
- hidden assumptions from another project’s ontology
- ambiguous relationship types
- doctrinal overclaim
- weak provenance
- low-quality bulk edges
- malicious poisoning in reused source material

A staging and normalization layer protects the core graph from these risks.

## Core rule

No external dataset should be imported directly into canonical graph objects.

The correct order is:
1. ingest
2. stage
3. document source and transformation
4. normalize into local schema
5. review
6. promote selected records into approved graph objects

## Recommended locations

External data should first enter:
- `data/sources/imported/`

Approved normalized graph objects should live under:
- `data/graph/`

This separation should remain visible.

## What should be documented for every import

Every imported dataset should preserve:
- source name
- source url or repository
- license status
- date imported
- import method
- transformation steps
- local schema mapping notes
- known limitations
- trust assumptions

## Normalization rule

Imported labels should not automatically become local controlled vocabulary.

If an external concordance uses broad labels such as:
- related
- similar verse
- theology
- prophecy

those should be mapped into the project’s local controlled structure only after review.

## Promotion rule

Imported records may become:
- imported_unreviewed nodes or edges
- community_proposed assertions
- editor_reviewed graph objects

They should not skip directly to canonical_locked.

## Summary principle

The import layer should make scale possible without making trust collapse.

That means imports must remain visible, traceable, and reviewable from the start.
