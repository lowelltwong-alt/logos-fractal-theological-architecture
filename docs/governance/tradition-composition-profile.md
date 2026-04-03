# Tradition Composition Profile

## Purpose

This file defines how theological traditions may be modeled in a compositional, inspectable, and reusable way within the Logos architecture.

The repository already includes:
- canon thinkers
- doctrine nodes
- concept nodes
- comparison nodes
- synthesis nodes
- ordering and weighting logic

This file does not replace those layers.
It defines how those layers can be combined into a governed tradition profile that can later support:
- LAIRCA instantiation
- institutional overlays
- decision architecture translation
- AI-assisted but human-governed decision models

## Core principle

A tradition should be treated as a structured composition rather than a flat label.

Instead of:
- a single denomination name

A tradition profile should make visible:
- which sources shape it
- how strongly they shape it
- how they are ordered
- what correctives are active
- what constraints are non-negotiable
- what historical form is being modeled

## Relation to existing repository layers

A tradition composition profile is downstream of:
- canon thinker nodes
- doctrine nodes
- concept nodes
- comparison nodes
- synthesis nodes

It does not replace those.
It draws from them.

In repository terms, it behaves most like a:
- `synthesis_node`
- with structured weighting and ordering fields

Future versions may justify formal node types such as:
- `weighting_profile`
- `ordering_profile`

as already anticipated in:
- `node-types.md`

## Core components of a tradition profile

A usable tradition composition profile should normally make the following elements explicit.

### 1. Primary sources

These are the strongest shapers of the tradition.

Examples:
- Augustine
- Aquinas
- Calvin
- Luther
- Kuyper

These define the center of gravity.

### 2. Secondary sources

These provide balance, correction, or extension.

Examples:
- Willard for formation
- Niebuhr for realism about power
- Keller for public theology

They do not define the whole system, but they prevent distortion.

### 3. Tertiary modifiers

These are recurring principles or themes that shape application.

Examples:
- subsidiarity
- sphere sovereignty
- anti-utopianism
- servant leadership
- limits / Sabbath

They influence outcomes without fully governing the tradition.

### 4. Doctrinal commitments

These anchor the profile in explicit theology.

Examples:
- imago Dei
- sin and fallenness
- grace and redemption
- authority of scripture

### 5. Ordering logic

Ordering answers:
- what is consulted first
- what constrains what
- what outranks what

This is distinct from weighting.

### 6. Weighting logic

Weighting answers:
- how strongly each source or concept influences outcomes

This is distinct from ordering.

### 7. Non-negotiables

These are constraints that should not be overridden by downstream convenience.

Examples:
- human moral accountability must remain visible
- truth is not subordinate to efficiency

### 8. Historical snapshot

A tradition is not static.

Profiles should be able to represent:
- classical form
- historical snapshot (e.g., 20 years ago)
- current institutional form

This prevents confusion between:
- doctrinal center
- contemporary expression

### 9. Translation layer

The profile should be able to support translation into:
- governance language
- institutional constraints
- decision architecture

This aligns with:
- LAIRCA
- AIRCA downstream use

## Relation to institutional overlays

A tradition profile is not the same as an institution.

An institution overlay should:
- inherit from a tradition profile
- adapt it to mission, governance, and context

Examples:
- Habitat-style nonprofit overlay
- ADF-style legal advocacy overlay

This separation helps preserve:
- theological clarity
- institutional specificity

## Relation to decision architecture

A tradition composition profile is upstream of decision models.

It should be able to translate into:
- constraints
- permissions
- escalation rules
- human-in-the-loop requirements
- governance expectations

This aligns with:
- UAIRCA (ultimate frame)
- LAIRCA (Christian instantiation)
- AIRCA (operational decision architecture)

## Human-in-the-loop implication

A tradition profile should help determine:
- what must remain human judgment
- what may be assisted by AI
- what requires escalation
- what requires justification and review

This prevents silent delegation of moral responsibility.

## Governance rule

A tradition composition profile should be:
- inspectable
- comparable
- revisable under governance
- clearly separated from raw source nodes

It should not be:
- a hidden assumption
- a vague label
- an untraceable synthesis

## Promotion rule

A tradition profile should be created when:
- multiple sources are being combined consistently
- institutional application requires a stable configuration
- contributors would otherwise recreate the same synthesis repeatedly

Do not create profiles prematurely.
Promote when reuse becomes real.

## Summary principle

Tradition should be modeled as a structured composition of sources, doctrines, ordering, weighting, and constraints.

That composition should remain traceable, comparable, and usable for downstream decision architecture without replacing the underlying theological source nodes that ground it.
