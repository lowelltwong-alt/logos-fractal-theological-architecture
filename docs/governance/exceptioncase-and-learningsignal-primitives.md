---
object_type: governance_primitive_note
trust_zone: canonical
lifecycle_status: active
provenance_note: "Added on 2026-04-13 while salvaging the ExceptionCase and LearningSignal design note from old PR #17 onto the cleaned baseline."
reason_for_inclusion: "Make the repository's learning primitives explicit so adaptation pressure stays reviewable and separate from approved change."
---

# ExceptionCase and LearningSignal Primitives

## Purpose

This note makes explicit two primitives that sit around the stable doctrinal core and help the architecture learn without silently rewriting itself.

They are governance primitives, not content shortcuts.

## Why add them

The repository already assumes:
- stable ontology and doctrine layers
- governed changes
- reviewable impact
- iterative learning

What is still easy to lose is the distinction between:
- a problem the model encountered
- a repeated signal that the model should adapt
- an approved structural change

If those collapse together, the repository drifts.

## Primitive 1: `ExceptionCase`

`ExceptionCase` is the bounded object for recording where the current architecture cannot cleanly absorb a case.

Typical uses:
- contradiction between nodes or claims
- unresolved scope conflict between profiles or traditions
- missing dependency edge
- benchmark miss
- retrieval failure
- reviewer override against current output
- ambiguity about canon, authority, or doctrinal boundary

### Expected shape

A strong `ExceptionCase` should capture at least:
- `exception_id`
- `exception_type`
- `trigger_context`
- `affected_nodes`
- `affected_profiles`
- `severity`
- `frequency`
- `linked_benchmarks`
- `review_notes`
- `status`

### Why it matters

This primitive prevents edge pressure from disappearing into informal notes, memory, or silent edits.

It gives the system a durable place to remember where the model strained.

## Primitive 2: `LearningSignal`

`LearningSignal` is the governed object that aggregates one or more exceptions into a candidate adaptation pressure.

It does not mean the system has already changed. It means the repository has enough repeated evidence to consider a structural response.

Typical uses:
- repeated exceptions of the same type
- multiple benchmark failures pointing to the same missing dependency
- recurring reviewer corrections against one profile rule
- repeated ambiguity about one canon or authority boundary
- clustered retrieval misses around a doctrine hub

### Expected shape

A strong `LearningSignal` should capture at least:
- `signal_id`
- `source_exception_ids`
- `signal_pattern`
- `candidate_change_type`
- `candidate_target`
- `confidence`
- `recommended_reviewers`
- `impact_estimate`
- `promotion_status`

### Why it matters

This primitive lets the repository learn from repetition instead of reacting to isolated noise.

It also keeps pressure to change separate from approved change.

## Relationship to existing primitives

The architecture becomes more stable when these objects are held in sequence:

1. `Profile`
2. `Dependency`
3. `ChangeEvent`
4. `ImpactReport`
5. `ExceptionCase`
6. `LearningSignal`

Read in operation, the pattern is:
- profiles and dependencies define the current model
- change events and impact reports govern approved mutation
- exception cases capture failure at the edge
- learning signals convert repeated failure into candidate adaptation

## Design rule

The system should be able to learn through reviewable escalation, not through silent self-modification.

That means:
- `ExceptionCase` does not directly mutate ontology
- `LearningSignal` does not directly mutate ontology
- only governed changes should become `ChangeEvent`

## Recommended promotion flow

```text
ExceptionCase -> clustered review -> LearningSignal -> decision review -> ChangeEvent -> ImpactReport
```

This is the practical bridge between a stable theological architecture and a living operating system.

## Preservation rule

If the repository becomes more automated over time, these distinctions should become more important, not less.

The architecture should never confuse:
- anomaly
- adaptation pressure
- approved doctrinal or structural change
