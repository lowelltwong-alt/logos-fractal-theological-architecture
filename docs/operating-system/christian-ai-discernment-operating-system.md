# Christian AI Discernment Operating System

Author: Lowell T. Wong
Status: draft
Purpose: define a layperson-usable operating system for analyzing AI through a Christian lens without requiring expert theological fluency.

## 1. Why this layer exists

This repository already treats theology as upstream of governance, design, and decision architecture. The next step is to make that architecture usable for a Christian layperson who is not a theological specialist but still wants to evaluate AI faithfully.

The goal of this operating system is not to flatten theology into a quiz or force premature denominational precision.

The goal is to help a user:
- identify what they already believe
- identify what they have not yet decided
- distinguish core doctrine from secondary doctrine
- compare tradition-specific options where needed
- leave some issues open where Christian faith permits that
- see how theology changes judgments about concrete AI use cases

In practical terms, this document defines the front-end logic that sits on top of the theological ontology.

## 2. Core operating thesis

The system should function as a Christian discernment operating system, backed by a governed theological ontology.

That means:
- theology remains upstream
- doctrine remains structured
- tradition differences remain explicit
- unresolved questions remain representable
- lay users receive guided paths rather than raw ontology dumps
- AI use-case evaluation is derived from theological commitments rather than capability-first logic

## 3. The four-layer model

The operating system should be built as four connected layers.

### Layer 1. Core Christian minimums

This layer captures beliefs broad enough to serve as a starting Christian frame.

Examples:
- God is morally authoritative
- human beings bear dignity and are not reducible to utility
- truth matters
- power can become corrupt or disordered
- stewardship matters
- love of neighbor matters
- technology is a tool and not a savior
- humans remain accountable for judgment and action

This layer should support a minimum viable Christian discernment path even when many secondary questions remain open.

### Layer 2. Tradition and denomination layer

This layer models how major traditions differ, overlap, or remain internally varied.

Examples:
- Roman Catholic
- Eastern Orthodox
- Protestant broad
- Evangelical broad
- Anglican
- Reformed
- Lutheran
- Baptist
- Pentecostal / Charismatic
- Non-denominational evangelical default

This layer should distinguish:
- broad Christian consensus
- major-tradition consensus
- denomination-specific positions
- disputed internal questions
- unresolved or open issues

### Layer 3. User belief-state layer

This layer models the actual user.

The system must allow a user to be:
- affirmed
- rejected
- undecided
- unexplored
- inherited but unexamined
- mixed or conflicted

This is essential. Undecided status is not failure. It is meaningful state.

### Layer 4. AI discernment layer

This layer maps theology into concrete AI analysis.

Examples:
- AI companions and pseudo-relationships
- AI-generated sermons
- AI in counseling or spiritual direction
- AI in hiring or surveillance
- AI replacing meaningful human labor
- AI persuasion and manipulation
- AI-generated religious imagery
- AI in education and discipleship

This layer should answer:
- which doctrines matter here
- which open questions materially affect judgment
- what risks follow from each theological path
- which conclusions remain stable across most Christian paths

## 4. User journey

The intended user journey is:

1. enter through plain-language questions
2. build a provisional belief profile
3. classify settled versus unsettled beliefs
4. identify which questions matter for the AI issue at hand
5. surface relevant doctrinal options and tradition-specific differences
6. provide a recommended discernment path
7. generate a human-readable explanation and machine-readable sidecar

The system should not require a user to settle every doctrinal question before proceeding.

## 5. Decision states the system must preserve

The operating system must preserve the following states as first-class metadata:
- settled
- unsettled
- unexplored
- tradition-defaulted
- mixed
- intentionally left open
- not required for the current discernment path

This prevents false precision and respects real Christian formation.

## 6. Doctrine tiering model

The system should classify doctrine into at least five tiers.

### Tier A. Core / essential
Questions central enough that the framework should assume or test them early.

Examples:
- doctrine of God
- human dignity / imago Dei
- truth and moral authority
- sin and corruption of power
- stewardship and accountability

### Tier B. Major but not always immediately decisive
Important for worldview and moral reasoning, but not required for every first-pass AI judgment.

Examples:
- vocation and work
- spiritual formation
- role of tradition
- embodied personhood
- authority and community discernment

### Tier C. Secondary / tradition-shaping
Important for denominational identity, sometimes relevant, but often not necessary for a broad Christian AI assessment.

### Tier D. Tertiary / low-immediacy
Questions that may matter for completeness but often do not need to be settled for most AI use cases.

### Tier E. Open or unresolved for current path
Questions the system may leave open because they do not change the present discernment outcome.

## 7. Non-denominational and minimally specified users

The system must not treat non-denominational identity as theology-free.

Instead it should model common non-denominational patterns such as:
- broad evangelical default
- Bible-first but under-specified tradition logic
- mixed Protestant inheritance
- low-formality but high-conviction Christianity
- seeker or exploring Christian

The system should offer a minimum faithful discernment path that does not force users into unnecessary denominational commitments.

## 8. Required node families

The operating system should introduce or strengthen the following node families:
- doctrine node
- tradition stance node
- belief-state node
- discernment question node
- AI issue node
- recommendation path node
- glossary node
- persona or profile node

## 9. Recommended repo structure

Recommended additions or strengthened branches:

- `docs/operating-system/`
- `schema/`
- planned top-level `profiles` branch
- planned top-level `discernment` branch
- governed `docs/` destinations for doctrine, tradition/profile, and AI-issue material as those branches are normalized
- preserved `ontology/doctrines/`, `ontology/traditions/`, and `ontology/ai-issues/` only as migration/reference-draft inputs during that normalization period
- `examples/`

## 10. Recommended profile and discernment object types

### `discernment_profile`
Represents a user’s present theological and practical state.

### `doctrine_tier_profile`
Represents which doctrines are required, helpful, optional, or not needed for a given use case.

### `ai_issue_profile`
Represents a concrete AI use case and its linked theological dependencies.

### `discernment_path`
Represents a branchable recommendation flow from user state to a decision explanation.

## 11. Bridge logic to the fractal schema

The fractal shell should remain stable.

This operating system should grow by:
1. modeling new concepts as nodes first
2. connecting them through typed relationships
3. expanding vocabulary only when needed
4. using belief-state and doctrine-tier metadata before redesigning structure

## 12. Recommended next build order

1. add schema support for belief state and doctrine tiering
2. add broad Christian core doctrine nodes
3. add tradition stance nodes for major traditions
4. add first AI issue taxonomy
5. create layperson profile templates
6. create worked examples for concrete AI questions
7. add sidecars and validation rules for discernment outputs

## 13. Success criteria

The operating system succeeds when a lay Christian can:
- understand the issue in plain language
- see which beliefs are doing the work
- know which questions remain open
- compare Christian options honestly
- avoid fake certainty
- reach a more faithful judgment about AI

The ontology succeeds when the same process remains machine-legible, governable, and extensible.
