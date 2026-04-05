# Doctrine Constitution

## Purpose

This file establishes the non-negotiable doctrine architecture rules for the Logos repository.

It exists because doctrine in this project is not merely a topic list.
It is a governed source layer that must remain:
- theologically serious
- recursively structured
- machine-legible
- provenance-aware
- stable enough for downstream derivation and decision systems

This file should be read as a constitutional layer for doctrine buildout.

## Core principle

A doctrine topic is not the same thing as a doctrinal view.
A doctrinal view is not the same thing as an assessment.
An assessment is not the same thing as a relation to another doctrine.

These distinctions must stay explicit.

## Constitutional distinctions

### 1. Doctrine topic
A doctrine topic is the stable theological question or object under consideration.

Examples:
- anthropology
- grace
- election
- baptism
- ecclesiology
- eschatology

A doctrine topic is the umbrella object.
It should remain reusable across traditions, thinkers, interpretations, and downstream applications.

### 2. Doctrine view
A doctrine view is a concrete answer, formulation, or position within a doctrine topic.

Examples:
- credobaptist view of baptism
- paedobaptist view of baptism
- supralapsarian view of election
- infralapsarian view of election
- forensic view of justification

A doctrine topic may contain many doctrine views.

### 3. Doctrine assessment
A doctrine assessment is a judgment made about a doctrine view relative to a governing baseline.

Examples:
- affirmed
- permitted
- disputed
- rejected
- false_doctrine
- not_addressed
- not_applicable

A doctrine view may be assessed differently by different traditions, confessions, institutions, or projects.

### 4. Baseline
A baseline is the authority frame from which an assessment is made.

Examples:
- Nicene Christianity
- Reformed confessional baseline
- Baptist confessional baseline
- project-specific Christian core baseline

No doctrine assessment should appear without an explicit baseline.

### 5. Evidence layer
No doctrine view or doctrine assessment should float without traceable grounding.
Where possible, doctrine work should preserve links to:
- scripture nodes
- interpretation nodes
- canon thinker nodes
- works
- councils
- confessions
- manuscripts, lexical, or translation layers where relevant

### 6. Coherence layer
Doctrine does not exist in isolation.
Every doctrine view should eventually be legible in relation to other doctrine views through typed theological relations.

Examples:
- depends_on
- presupposes
- entails
- strengthens
- weakens
- contrasts_with
- contradicts
- derived_from
- reacts_against
- synthesizes

## Constitutional rules

### Rule 1. Never collapse topic, view, and assessment
A doctrine topic must not be treated as if it were already a settled doctrinal judgment.
A doctrine view must not be treated as if it were universally affirmed.
An assessment must not be treated as if it belonged to the doctrine topic itself.

### Rule 2. False doctrine must be preserved as assessed history, not erased data
If a view is judged false, it should still remain represented as a doctrine view with explicit assessment metadata.
It should not be deleted from the architecture.

The project must preserve:
- historical existence
- doctrinal content
- assessment status
- baseline of judgment
- evidence and rationale where possible

### Rule 3. Every serious doctrine relation must be typed
Do not use vague prose alone where a recurring doctrinal relation exists.
If a relation matters repeatedly, it should eventually be represented with a controlled relation type.

### Rule 4. Coherence math is downstream of doctrine truth claims
The project may later compute coherence, tension, and misalignment across doctrinal systems.
But the scoring layer must remain downstream of the theological object layer.

The ontology stores structure.
The coherence engine computes tension.
These must not be collapsed into one layer.

### Rule 5. Bundles matter, not only pairs
Some doctrines only cohere when held together with other doctrines.
The project should therefore eventually support doctrine bundles or constraint bundles rather than only pairwise relations.

### Rule 6. Assertions should become first-class where needed
When a doctrinal claim needs provenance, confidence, scope, or review status, it should be modeled as an assertion object rather than left as unqualified prose.

### Rule 7. Tradition plurality must be explicit
Different traditions may:
- define the doctrine topic differently
- divide doctrine views differently
- assess the same doctrine view differently
- appeal to different scripture, confessions, or thinkers

The architecture must preserve that plurality without flattening it into relativism or silently imposing one tradition as universal.

## Required future objects

The doctrine layer should increasingly support the following governed objects:
- doctrine_topic
- doctrine_view
- doctrine_assessment
- doctrinal_baseline
- doctrinal_assertion
- coherence_relation
- constraint_bundle
- evidence_object

Not all must be built immediately.
But they should guide the architecture from now on.

## Build order rule

Doctrine buildout should proceed in this order:
1. doctrine topic
2. major doctrine views
3. baseline-aware assessments
4. evidence and provenance links
5. coherence relations
6. bundle constraints
7. downstream scoring or decision surfaces

This order prevents the project from jumping into system scoring before the theological objects are stable.

## Summary principle

Doctrine in Logos is not a flat list.
It is a governed system of:
- topics
- views
- assessments
- evidence
- relations
- coherence

If those layers stay distinct, the project can scale.
If they collapse into one another, the project will drift.
