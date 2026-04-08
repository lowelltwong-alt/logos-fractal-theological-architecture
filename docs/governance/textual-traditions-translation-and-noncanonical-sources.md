---
object_type: governance_policy
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to restore canonical governance references and formalize textual-source handling boundaries."
reason_for_inclusion: "This document is the canonical target for repository references about textual traditions, translation governance, and noncanonical source boundaries."
---

# Textual Traditions, Translation, and Noncanonical Sources

## Purpose

Define the governance boundary for how this repository handles:
- original-language textual traditions
- modern translation layers
- manuscript witness materials
- noncanonical and disputed source classes

## Scope boundary

This file establishes high-level structural rules.
Detailed classification and trust application are delegated to:
- `docs/governance/translation-trust-and-sectarian-classification.md`
- `docs/governance/noncanonical-and-heresy-classification.md`
- `docs/primary-sources/ontology-and-taxonomy.md`

## Structural rules

1. Keep source identity separate from interpretive claims.
2. Preserve witness, transcription, reconstruction, and translation as distinct layers.
3. Do not treat noncanonical materials as canonical by default.
4. Record trust-zone assignment explicitly for source-adjacent objects.
5. Preserve provenance and confidence posture for every governed source object.

## Placement rules

- Governance policy for source handling belongs in `docs/governance/`.
- Future machine-readable source objects belong in `data/graph/`.
- Source examples belong in `data/graph/examples/primary-sources/`.

## Cross-reference policy

When linking to source-adjacent governance, prefer explicit relative paths and canonical filenames.
Do not reference deprecated aliases once canonical replacement paths are available.
