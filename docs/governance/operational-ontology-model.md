# Operational Ontology Model

## Purpose

This file defines the repository's intended ontology model as an **operational layer** rather than a merely descriptive archive.

The central idea is that the ontology should not only describe what things are.
It should also govern how things are added, linked, reviewed, promoted, deprecated, trusted, and used by future retrieval systems, graph tooling, and AI agents.

This file should be read together with:
- `research-synthesis-ai-era-ontology-takeaways.md`
- `inference-policy.md`
- `trust-zones.md`
- `deterministic-id-policy.md`
- `schema-compatibility-policy.md`

## Core principle

A serious ontology needs more than nouns.
It also needs governed verbs, stable interfaces, trust layers, and validation discipline.

This repository should therefore be built as a semantic operating layer.

## Core primitives

The research strongly supports treating these as the main ontology primitives:
- object types
- link types
- interfaces
- shared properties
- action types
- trust and status layers

These primitives should remain small in number, stable in meaning, and reusable across the repository.

## Object types

Object types define what kind of thing an object is.

Examples in this repository include:
- canon thinker
- doctrine
- concept
- scripture node
- lexical node
- translation witness
- manuscript witness
- noncanonical boundary node
- relationship object
- graph object

Object types should be explicit, version-aware, and governed.

## Link types

Link types define the meaning of relationships.

A strong ontology should avoid casual relationship sprawl.

Links should be:
- typed
- intentional
- reusable
- semantically narrow enough to mean something stable

When a relationship needs provenance, confidence, or review logic, it should often be represented as a governed relationship object rather than an unstructured edge alone.

## Interfaces

Interfaces define reusable shapes and expectations that multiple object families can share.

Examples may include:
- node
- citable text span
- witness
- assertion
- term-like entity
- tradition-scoped entity
- reviewable object
- machine-readable object

Interfaces are one of the cleanest fractal mechanisms in the repository.

## Shared properties

Shared properties reduce vocabulary drift.

These are fields whose meaning should remain stable across many object families.

Examples include:
- id
- anchor
- title
- status
- provenance fields
- review fields
- trust-zone fields
- language fields

Shared properties should be governed centrally whenever practical.

## Action types

Action types define the governed ways the repository changes.

Examples include:
- add node
- add witness
- add relationship object
- propose concept mapping
- promote object
- deprecate object
- split or merge lexical senses
- publish a new graph view

This repository may currently implement action types through GitHub workflows, review templates, and CI rather than through a separate software platform, but the ontology should still recognize those actions conceptually.

## Trust and status layers

A strong ontology does not treat every object as equally authoritative.

Trust and lifecycle status should remain first-class governance dimensions.

Examples:
- core trusted
- reviewed specialized
- working proposed
- boundary restricted
- experimental graph

Status and trust should not be flattened into one vague signal.

## Why this matters for future AI use

Future AI systems will not use this repository well if it is only a pile of labeled files.

They will work better if the repository can tell them:
- what kind of object something is
- which links are governed
- what trust zone applies
- what provenance supports it
- whether a result is asserted or inferred
- what actions are legitimate versus ad hoc

That is the practical meaning of an operational ontology in this repository.

## Fractal rule

The same operating grammar should recur across scales.

That means the repository should use similar patterns for:
- small nodes
- doctrinal nodes
- scripture nodes
- witness objects
- graph domains
- validation shapes
- larger branch structures

Fractal discipline does not mean identical content.
It means repeated governance grammar.

## Summary principle

This repository should not remain only a semantic archive.

It should become a governed semantic operating layer for theology, scripture, language, comparison, and future AI-assisted knowledge work.
