# Concordance Review and Trust Model

## Purpose

This document defines how the concordance should remain trustworthy as it grows over time through many contributors, imported datasets, proposed links, and interpretive claims.

This file is intentionally strict.

A large scripture-linked knowledge system is vulnerable to:
- accidental error
- uncontrolled drift
- doctrinal overclaim
- ambiguous provenance
- low-quality bulk import
- malicious poisoning by a bad actor

For that reason, trust, review, and auditability must be treated as part of the architecture, not as optional administration.

## Core rule

No unreviewed claim should silently become canonical.

Every meaningful assertion, especially one that goes beyond direct reference identity, should carry:
- provenance
- review state
- reviewer traceability
- update history

This includes:
- verse-to-concept links
- verse-to-doctrine links
- tradition-specific interpretations
- external philosophical appropriations
- imported concordance claims

## Trust layers

The concordance should operate with explicit trust layers.

### 1. `imported_unreviewed`
Used for claims ingested from external datasets, concordances, or automated imports that have not yet been reviewed.

These should never be treated as canonical.

### 2. `community_proposed`
Used for contributor-added claims that are structurally valid but not yet editor-reviewed.

These are visible proposals, not locked truth.

### 3. `editor_reviewed`
Used when a recognized editor has reviewed the claim for structural fit, provenance, and basic content quality.

### 4. `scholar_reviewed`
Used when a higher-trust reviewer has checked the claim with stronger subject-matter standards.

### 5. `canonical_locked`
Used for claims or nodes that the project wishes to treat as stable, highly trusted, and not lightly editable.

This status should be rare and intentionally granted.

## What should require review before stronger trust is granted

The following should never move upward in trust by automation alone:
- doctrine support claims
- contested theological interpretations
- philosophy-theology appropriations
- strong conceptual links
- translation-sensitive claims
- links that could materially shape downstream AI reasoning

These are precisely the kinds of entries a malicious or careless actor could poison.

## Provenance requirements

A meaningful assertion should increasingly preserve:
- assertion id
- source refs
- derived from
- synthesizes
- appropriates from
- translation status
- alignment strength
- asserted by
- reviewed by
- last reviewed at
- review notes

If this information is absent, the claim should remain lower-trust by default.

## Imported concordance rule

Imported material is input, not truth.

If a concordance, lexicon, or verse-index dataset is imported, its claims should first live as:
- imported records
- candidate cross-reference edges
- unreviewed source assertions

They should not automatically become canonical graph relationships just because they came from an existing concordance.

A mature system may import aggressively, but it should approve conservatively.

## Poisoning resistance rule

The concordance should be built as if a sophisticated bad actor will eventually try to manipulate it.

That means:
- no silent promotion of low-trust claims
- no destructive or trust-changing automation without human approval
- no hidden merges of imported data into canonical objects
- no canonical status changes without traceable review
- no removal of provenance fields in later edits

## Contributor model

Not every contributor should have the same authority.

The system should distinguish among:
- contributor
- editor
- scholar reviewer
- maintainer

These roles do not exist merely for status. They exist to control how easily bad data can move upward in trust.

## Review workflow

A healthy review workflow should usually look like this:

1. create or import a proposed node or edge
2. validate structural fields and controlled vocabulary
3. require provenance fields where relevant
4. assign initial trust state
5. submit for editor review
6. escalate to scholar review where the claim is doctrinally heavy, contested, or interpretively sensitive
7. lock or stabilize only after review

## Audit requirements

The concordance should preserve an audit trail strong enough that future reviewers can ask:
- who added this
- what source supported it
- when it was changed
- what review state it holds
- whether it was imported or hand-curated
- what earlier version it replaced

If the project cannot answer those questions, it is not ready to trust the graph at scale.

## Branch and repository controls

At the Git level, the concordance should prefer:
- protected main branch
- required pull-request review
- CODEOWNERS for sensitive folders
- signed commits where possible
- validation checks before merge
- snapshot releases for high-trust datasets

The trust model should not rely only on personal confidence in contributors.

It should rely on enforceable process.

## Canonical vs non-canonical distinction

The concordance should explicitly distinguish between:
- canonical reference identity
- reviewed cross-reference claims
- interpretive traditions
- imported background material
- speculative or contested proposals

A bad concordance becomes dangerous when those layers blur together.

## What should be easiest to add

The easiest additions should be:
- stable verse nodes
- stable passage nodes
- entity mentions
- low-risk structural metadata

## What should be hardest to add

The hardest additions should be:
- doctrine support claims
- tradition-specific conclusions treated as universal
- philosophy-theology borrowings presented as direct equivalence
- canonical-lock status
- any claim that downstream systems might over-read as settled truth

## Summary principle

The concordance should grow in volume only as fast as it can preserve trust.

Scale is useful.
Trust is more important.
Machine readability without review discipline is dangerous.

The right architecture is one that makes poisoning expensive, audit easy, and trust status explicit.
