# Institution Overlay

## Purpose

This file defines how a specific institution should be modeled downstream from the shared theological and tradition-composition architecture.

It should be read together with:
- `tradition-composition-profile.md`
- `build-priority-policy.md`
- `commit-mutation-protocol.md`
- `ontology-discipline.md`
- `fractal-rules.md`

## Core principle

An institution is not identical to a tradition.

A tradition composition profile answers questions such as:
- what theological sources shape the frame
- what doctrines and concepts govern it
- what ordering and weighting logic apply
- what constraints are non-negotiable

An institution overlay answers different questions such as:
- what kind of institution this is
- what mission it serves
- what governance environment it operates in
- what stakeholder mix it must address
- what decisions recur inside its context
- how the theological frame must be translated into institutional and decision architecture

## Why this layer matters

Without an institution overlay, a contributor risks one of two errors:

### 1. Abstract theology without institutional traction
The tradition profile remains too general to govern real decisions.

### 2. Institution-specific drift into pseudo-theology
One institution's habits, language, or incentives begin to masquerade as if they were the tradition itself.

The overlay layer prevents both errors.

## Relation to existing repository layers

An institution overlay is downstream of:
- source theology
- doctrine and concept structure
- comparison and synthesis work
- tradition composition profiles

It is upstream of:
- institutional decision models
- use-case filters
- workflow constraints
- governance translations
- downstream AIRCA / LAIRCA implementation patterns

## Required overlay dimensions

A serious institution overlay should normally make the following dimensions explicit.

### 1. Institution identity
What kind of institution is this?

Examples:
- nonprofit network
- advocacy organization
- church network
- educational institution
- philanthropic foundation

### 2. Mission identity
What is the institution trying to do?

### 3. Governance environment
What forms of authority and review shape its operation?

Examples:
- board governance
- executive authority
- distributed affiliates
- legal review
- doctrinal oversight
- donor or public-accountability pressures

### 4. Stakeholder map
Who must be considered in translation and governance?

Examples:
- board
- executive leadership
- staff
- affiliates
- families served
- clients
- congregants
- donors
- regulators
- public audiences

### 5. Decision environment
What kinds of recurring decisions define this institution's operating life?

Examples:
- service design decisions
- escalation decisions
- workforce and capability decisions
- public-positioning decisions
- partner selection decisions
- technology adoption decisions

### 6. Mission-constrained translation layer
How should the shared theological and tradition logic be translated into this institution's governance and operating language?

### 7. Human-in-the-loop implications
What decisions must remain visibly human, escalated, or review-gated inside this institution?

### 8. Prohibited drifts
What kinds of shortcuts would distort the institution's role even if they looked efficient?

## Overlay build pattern

An institution overlay should generally be built in this order:

1. Name the inherited upstream profile
2. Identify institution type and mission
3. Identify governance pressures
4. Identify recurring decision classes
5. Translate into downstream constraints and decision-support logic

## Coded instantiation rule

When developing concrete institutional overlays inside the repository, contributors should use stable coded names rather than relying on public-facing institution names in the core governance grammar.

Suggested pattern:
- `inst.alpha`
- `inst.beta`
- `inst.gamma`
- `inst.delta`

This helps preserve:
- abstraction discipline
- portability
- reduced premature attachment to one local case

## Example coded overlay families

### `inst.alpha`
A distributed mission-driven service network with mixed board, donor, leadership, and beneficiary-facing governance pressures.

### `inst.beta`
A public-facing advocacy institution operating with stronger conflict, public-positioning, and escalation burdens.

These are placeholders showing how reusable coded overlays may be named.

## Summary principle

An institution overlay is the governed layer that translates shared theological and tradition architecture into the mission, governance, stakeholder, and decision realities of a specific coded institution.
