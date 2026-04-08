# Evidence and Provenance Spine

## Purpose

This document defines the shared object spine that connects the repository's theological knowledge layer and its exceptions / learning-loop layer.

The goal is to make claims, support, review, and change pressure traceable without collapsing them into one another.

## Core design rule

The repository should distinguish between:
- what is asserted
- what supports the assertion
- who asserted, reviewed, or changed it
- what state the assertion is in
- where reality pushed back against the current model

That requires two linked object families.

## Knowledge-layer primitives

### 1. Claim

A first-class statement object rather than an unqualified edge.

Required fields:
- `id`
- `subject`
- `predicate`
- `object`
- `claim_type`
- `assertion_mode`
- `scope`
- `review_state`
- `confidence`
- `evidence_ids[]`
- `provenance_event_ids[]`

Allowed `claim_type` values:
- `asserted`
- `inferred`
- `imported`
- `extracted`
- `editorial`

Allowed `assertion_mode` values:
- `direct`
- `synthetic`
- `analogical`
- `probabilistic`

### 2. EvidenceItem

A support object attached to a claim.

Required fields:
- `id`
- `claim_id`
- `source_id`
- `source_tier`
- `evidence_grade`
- `support_type`
- `locator`
- `added_by`

Allowed `source_tier` values:
- `tier_1_primary`
- `tier_2_critical_scholarly`
- `tier_3_responsible_secondary`
- `tier_4_contextual_auxiliary`
- `tier_5_machine_provisional`

Allowed `evidence_grade` values:
- `A_direct`
- `B_strong`
- `C_moderate`
- `D_weak`
- `E_speculative`

### 3. ProvenanceEvent

A first-class editorial / derivational event.

Required fields:
- `id`
- `event_type`
- `actor`
- `timestamp`
- `target_object_id`

Optional but preferred fields:
- `used_source_ids[]`
- `tool_or_ruleset`
- `notes`
- `generated_artifact_ids[]`

Allowed `event_type` values:
- `asserted`
- `reviewed`
- `revised`
- `inferred`
- `promoted`
- `deprecated`
- `resolved_exception`

### 4. ReviewState

A lifecycle object or controlled state enum for claims and evidence.

Preferred lifecycle:
- `draft`
- `proposed`
- `reviewed`
- `approved`
- `stable`
- `disputed`
- `deprecated`
- `archived`

## Exceptions-layer primitives

### 5. Expectation

The rule, threshold, or relation the system expects to hold.

Required fields:
- `id`
- `expectation_type`
- `target_object_id`
- `expected_condition`
- `scope`

### 6. ObservationEvent

What was actually observed in operation.

Required fields:
- `id`
- `observed_object_id`
- `observed_condition`
- `timestamp`
- `captured_by`

### 7. ExceptionEvent

The located deviation between expectation and observation.

Required fields:
- `id`
- `expectation_id`
- `observation_event_id`
- `exception_type`
- `status`

Optional but preferred fields:
- `affected_claim_ids[]`
- `evidence_ids[]`
- `pressure_vector`
- `disposition`

Preferred `status` lifecycle:
- `detected`
- `triaged`
- `resolved`
- `promoted`
- `closed`

### 8. ResolutionAction

The action taken in response to an exception.

Required fields:
- `id`
- `exception_event_id`
- `action_type`
- `performed_by`
- `timestamp`

Preferred `action_type` values:
- `fix_instance`
- `adjust_rule`
- `update_taxonomy`
- `update_ontology`
- `escalate_governance`
- `no_change`

### 9. PromotionLog

The object that records when an exception-produced insight becomes governed change.

Required fields:
- `id`
- `exception_event_id`
- `promoted_object_id`
- `promotion_type`
- `timestamp`
- `approved_by`

## Linking rules

These relations should be treated as non-optional in the architecture.

- `Claim -> supported_by -> EvidenceItem`
- `Claim -> traced_by -> ProvenanceEvent`
- `Claim -> in_state -> ReviewState`
- `ExceptionEvent -> affects -> Claim`
- `ExceptionEvent -> cites -> EvidenceItem`
- `ResolutionAction -> resolves -> ExceptionEvent`
- `PromotionLog -> promotes -> Claim | Expectation | taxonomy object | ontology object`
- `ProvenanceEvent -> generated_from -> ResolutionAction`

## Separation rule

Asserted and inferred material must remain distinct.

Preferred graph partitioning:
- `graph/asserted`
- `graph/inferred`
- `graph/tradition-scoped`
- `graph/community`
- `graph/ai-extracted`
- `graph/exceptions`

No inferred or exception-derived object should silently overwrite an asserted object.

## Minimum validation rules

A contribution should fail validation if any of the following are true:
- a `Claim` has no `EvidenceItem`
- an `EvidenceItem` lacks `source_tier` or `locator`
- a `Claim` does not declare `claim_type`
- an `ExceptionEvent` points to neither an `Expectation` nor an `ObservationEvent`
- a `ResolutionAction` lacks `performed_by`
- a `PromotionLog` does not identify what was promoted

## Reviewer roles

Recommended roles:
- `proposer`
- `reviewer`
- `tradition_reviewer`
- `schema_steward`
- `provenance_auditor`
- `publisher`

## Summary principle

The knowledge layer stores what the repository currently judges to be true enough to publish.

The exceptions layer stores where the world, evidence, or governance process resisted the current model.

Both layers should meet at the same shared spine.
