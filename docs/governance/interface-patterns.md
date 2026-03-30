# Interface Patterns

## Purpose

This file defines how the repository should use interface-like patterns across node families so different object types can share a common shape, capability set, or governance expectation without collapsing into one undifferentiated type.

This is important because a world-class ontology does not only model isolated types. It also models shared structure across types.

This file should be read together with:
- `node-types.md`
- `node-types-scripture-and-boundary-extension.md`
- `fractal-rules.md`
- `schema-compatibility-policy.md`

## Core principle

A node type answers: what kind of object is this?

An interface answers: what reusable shape, capability, or governance pattern does this object participate in?

A node may implement one node type and several interfaces.

## Why interfaces matter here

Without interface-like patterns, the repository risks:
- duplicating the same structural expectations across many node types
- inventing ad hoc exceptions for trust, review, provenance, or machine-readability
- making cross-domain tooling harder because similar objects do not advertise shared capabilities

With interface patterns, the repository can say that multiple otherwise different nodes are all:
- reviewable
- boundary-sensitive
- scripture-grounded
- machine-readable
- graph-linkable
- promotion-eligible

## Recommended interface families

### `reviewable_node`
Use for any node that should carry a meaningful review state.

Typical expectations:
- `review_status`
- `review_cycle`
- `reviewed_by`
- `last_reviewed`

### `boundary_sensitive_node`
Use for nodes where trust, doctrine, translation, or source-status limits matter.

Typical expectations:
- warning fields where relevant
- explicit use-case limits
- classification metadata
- stronger review expectations

Typical examples:
- disputed translations
- noncanonical texts
- forged or heretical source nodes
- contested relationship objects

### `scripture_grounded_node`
Use for nodes that should be tied to scripture passages or scripture-derived evidence.

Typical expectations:
- scripture refs or source refs
- passage-level links
- doctrinal grounding traceability

Typical examples:
- biblical themes
- doctrine nodes with explicit text grounding
- some concept nodes

### `machine_readable_object`
Use for nodes or objects expected to support graph or concordance workflows.

Typical expectations:
- stable IDs
- structured relationships
- compatibility-aware schema discipline
- provenance fields

Typical examples:
- graph node objects
- relationship objects
- translation witness objects

### `promotion_candidate`
Use for repeated local material that may need escalation into a reusable node.

Typical expectations:
- recurrence across parents
- retrieval value
- reusable conceptual load

### `translation_witness_like`
Use for objects that function as translation witnesses or translation-comparison carriers.

Typical expectations:
- translation philosophy
- textual base quality
- provenance claim status
- doctrinal tendency
- use-case limit

### `source_boundary_object`
Use for noncanonical, pseudepigraphal, sectarian, forged, or otherwise boundary-sensitive sources.

Typical expectations:
- explicit classification fields
- warning text where appropriate
- doctrinal-use limits
- provenance and reception notes

## Interface rule

Do not turn interfaces into a second uncontrolled taxonomy.

Add an interface only when a shared structural or governance expectation recurs across multiple node families.

## Suggested use pattern

A node may be described conceptually like this:
- node type: `noncanonical_text`
- interfaces: `reviewable_node`, `boundary_sensitive_node`, `machine_readable_object`, `source_boundary_object`

Or:
- node type: `biblical_theme_node`
- interfaces: `reviewable_node`, `scripture_grounded_node`, `promotion_candidate`

## Why this is fractal

Interfaces make the repository more fractal because they allow the same structural logic to recur across different domains without forcing all domains into one flat type system.

The same governance grammar can therefore recur in:
- canon
- scripture
- doctrine
- graph
- boundary layers

while preserving meaningful object-type differences.

## Summary principle

Node types define what an object is.
Interfaces define what reusable structural or governance pattern it participates in.

Both are needed for a strong ontology.
