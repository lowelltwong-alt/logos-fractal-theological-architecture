# Claim and Evidence Validation Contract

## Purpose

This document defines the first validation contract for the shared evidence / provenance spine.

It is intentionally small enough to enforce early, but strong enough to prevent silent structural drift.

## Target object families

This contract currently focuses on:
- `Claim`
- `EvidenceItem`
- `ProvenanceEvent`
- `ReviewState`
- `ExceptionEvent`
- `ResolutionAction`
- `PromotionLog`

## Required validation rules

### Claim rules

A `Claim` must:
- have a stable `id`
- declare `subject`, `predicate`, and `object`
- declare `claim_type`
- declare `assertion_mode`
- declare a `review_state`
- point to at least one `evidence_id`
- point to at least one `provenance_event_id`

### EvidenceItem rules

An `EvidenceItem` must:
- have a stable `id`
- point to a `claim_id`
- declare `source_id`
- declare `source_tier`
- declare `evidence_grade`
- declare `support_type`
- include a `locator`

### ProvenanceEvent rules

A `ProvenanceEvent` must:
- have a stable `id`
- declare `event_type`
- declare `actor`
- declare `timestamp`
- point to `target_object_id`

### ExceptionEvent rules

An `ExceptionEvent` must:
- have a stable `id`
- point to an `expectation_id`
- point to an `observation_event_id`
- declare `exception_type`
- declare `status`

### ResolutionAction rules

A `ResolutionAction` must:
- have a stable `id`
- point to an `exception_event_id`
- declare `action_type`
- declare `performed_by`
- declare `timestamp`

### PromotionLog rules

A `PromotionLog` must:
- have a stable `id`
- point to an `exception_event_id`
- identify the `promoted_object_id`
- declare `promotion_type`
- declare `timestamp`
- declare `approved_by`

## Failure conditions

Validation should fail immediately when:
- a claim has zero evidence items
- a claim does not declare asserted vs inferred status
- an evidence item has no locator
- an evidence item has no source tier
- a provenance event has no actor
- an exception event is disconnected from expectation or observation
- a resolution action has no performer
- a promotion log does not identify the promoted object

## Preferred future implementation

The repository can later express these as:
- SHACL shapes
- JSON sidecar schema checks
- CI lint rules
- import guards for machine-generated graph objects

## Summary principle

The point of early validation is not completeness.

It is to make the minimum trustworthy structure mandatory before the graph layer scales.
