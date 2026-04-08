# Claim Layer Model

## Purpose

This file defines the claim layer for the Logos repository.

The claim layer exists so that important reasoning does not remain only in prose or in naked graph edges.

## Core principle

Claims should become first-order governed reasoning objects.

A node says what an object is.
A claim says what is being asserted, inferred, hypothesized, disputed, or superseded about the relationship between objects.

## Minimum claim fields

Every serious claim object should normally preserve:
- `claim_id`
- `subject`
- `predicate`
- `object`
- `epistemic_status`
- `trust_zone`
- `review_status`
- `evidence_refs`
- `source_basis`
- `lineage`
- `ai_usage_posture`
- `reviewer`
- `notes`

## Required epistemic statuses

At minimum, the claim layer should distinguish:
- `asserted`
- `inferred`
- `hypothesis`
- `disputed`
- `superseded`

These should not be flattened together.

## Example claim pattern

A claim may express things such as:
- a text grounds a biblical theme
- a biblical theme informs a doctrine node
- an original-language term clarifies a text node
- a translation witness renders a passage
- a manuscript witness attests a reading
- a thinker partially aligns with a concept

## Claim rule

Claims should preserve reasoning status and evidence rather than pretending every edge has the same weight.

## Example

```yaml
claim_id: claim.text.genesis_1_26_28.grounds.image_of_god
subject: text.genesis.1.26-28
predicate: grounds
object: biblical_theme.image_of_god
epistemic_status: asserted
trust_zone: proposed
review_status: review_pending
evidence_refs:
  - text.genesis.1.26-28
source_basis:
  - scripture_text
ai_usage_posture: retrieval_ok_not_auto_promote
notes: Primary grounding claim connecting Genesis 1:26-28 to the image of God theme.
```

## Summary principle

The claim layer should preserve reasoning posture, evidence, and review so Logos can grow into a serious theological reasoning architecture rather than only a collection of nodes and links.
