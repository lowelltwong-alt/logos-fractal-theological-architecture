# Fractal Decision Schema and Ontology Bridge

Author: Lowell T. Wong
Status: draft
Purpose: explain how the recursive decision artifact schema should be used inside the Logos theological repository and its future Christian AI discernment operating system.

## 1. Why this bridge file exists

This repository already has strong governance, vocabulary discipline, trust-boundary, and ontology-direction documents. What it still needs is a direct bridge between:
- the fractal decision artifact schema
- ontology best practices
- the theological repository structure
- the layperson-facing Christian AI discernment operating system

This file defines that bridge.

## 2. Core principle

Keep the recursive shell stable.

The recursive shell is the durable operating structure. New concepts should be modeled primarily through:
- node identity
- controlled classification
- typed relationships
- logic blocks
- governance and provenance
- recursive subnodes

Structural redesign should be rare.

## 3. Primary architectural rule

The repository should operate as:

`human-readable theology -> governed ontology -> discernment logic -> machine-readable decision artifacts`

That means prose, ontology, and discernment outputs should not be treated as competing layers. They are connected layers of one system.

## 4. What the fractal schema is doing here

The fractal decision schema is not only for business artifacts. It is useful here because this project is also building governed decision logic.

The schema allows this repository to represent:
- doctrine nodes
- tradition stances
- belief-state objects
- AI issue profiles
- discernment paths
- governance rules
- validation rules
- examples and worked applications

under one repeating shell.

## 5. Fit order for this repository

When adding a new theological or discernment concept, use this order:

1. can it be represented as a node?
2. can it fit an existing node family?
3. can it fit through classification or controlled vocabulary extension?
4. can it be linked by existing relationship verbs?
5. can it be represented as a subnode or profile rather than a new top-level structure?
6. only then consider a new optional field family

## 6. Recommended node families in this repo

This bridge recommends the following primary node families:
- doctrine
n- theologian
- tradition
- scripture-theme
- lexical or term node
- AI issue
- discernment question
- discernment profile
- recommendation path
- governance policy
- example or worked case

## 7. Required structural distinctions

The repository should maintain clear distinctions between:
- doctrine versus ordering
- ordering versus weighting
- source versus synthesis
- assertion versus inference
- tradition stance versus user stance
- ontology object versus decision artifact
- canonical source versus boundary or noncanonical source

These distinctions matter for trust, retrieval quality, and future automation safety.

## 8. What should inherit and what should not

Recommended inheritance behavior:

May inherit if blank:
- domain
- subdomain
- owner
- review cycle
- visibility
- artifact tier
- lifecycle state

Should never inherit:
- node identity
- canonical id
- title
- source provenance origin
- created_at
- direct user belief-state values

## 9. Repository-specific extensions recommended

The default fractal template should be extended in this repository through controlled usage patterns rather than shell redesign.

Recommended recurring patterns:
- `classification.object_type` for node family
- `entity_model.canonical_status` for source trust and canonical handling
- `evidence.confidence_model` for confidence-aware theology and textual handling
- `relationships.relationship_metadata` for dependency strength and boundary handling
- `validation.interpretation_checks` for safe handling of blank or dormant values
- `content.summary` for plain-language layperson readability
- `execution.ai_prompt_template` only where safe and governed

## 10. Discernment-specific additions recommended

For Christian AI discernment, the schema should routinely support:
- doctrine tier
- consensus scope
- decision pressure
- user belief state
- user confidence
- required-for-current-path flag
- tradition default if blank
- issue relevance

These should usually be represented in classification, logic, validation, or controlled optional field groups before any shell redesign.

## 11. Practical modeling rules

### Model doctrines as reusable objects
A doctrine should not be rewritten inside every use case.

### Model use cases as dependent objects
An AI issue should point to doctrines, not absorb them all into one giant page.

### Model user state separately
A tradition says one thing. A user may believe another thing or remain undecided.

### Model unresolved status explicitly
Unknown or open should be data, not omission.

### Model governance as first-class
This repo is meant to resist drift, poisoning, and quiet category collapse.

## 12. Anti-drift rule

Repeated new concepts should first be reviewed for promotion into:
- controlled vocabulary
- typed node family
- governed relationship type
- reusable profile object

This should happen before contributors create freeform extensions.

## 13. Recommended uses of the schema in this repo

Highest-value uses:
- machine-readable sidecars for doctrine nodes
- machine-readable sidecars for AI issue analyses
- discernment-profile outputs
- worked example outputs
- governance and validation objects
- future graph object generation

## 14. Success condition

The schema is working in this repository when:
- theology remains readable
- ontology remains governed
- new concepts fit without shell breakage
- layperson discernment outputs are traceable back to upstream doctrine
- AI systems can navigate the structure without inventing authority or collapsing distinctions.