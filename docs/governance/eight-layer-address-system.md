# Eight-Layer Address System

## Purpose

This file defines the structural address system for the Logos repository.

The address system should make structural placement explicit without replacing stable semantic identity.

## Core principle

Stable ID answers what an object is.
Structural address answers where it sits in the larger architecture.

These should not be collapsed into one field.

## Required distinction

Every serious governed object should normally have:
- a stable semantic `id`
- a stable or deliberately migrated structural `address`

## Canonical eight-layer pattern

The preferred address pattern is:

`domain.surface.branch.module.family.object_type.object_key.facet`

## Layer meanings

### 1. `domain`
The widest project domain.

Example:
- `christian_ai_theology`

### 2. `surface`
The major surface or top-level operating region.

Examples:
- `theology`
- `scripture`
- `languages`
- `translations`
- `manuscripts`
- `boundary`
- `graph`
- `applications`

### 3. `branch`
The local branch under that surface.

Examples:
- `anthropology`
- `genesis`
- `hebrew`
- `mainstream_modern`
- `pseudepigrapha`

### 4. `module`
A repeated internal grouping, cluster, or structural subdivision.

Examples:
- `creation`
- `governance`
- `lexical`
- `comparison`
- `witnesses`

### 5. `family`
The structural family inside the module.

Examples:
- `text`
- `theme`
- `doctrine`
- `concept`
- `claim`
- `artifact`

### 6. `object_type`
The specific governed object type.

Examples:
- `scripture_text`
- `doctrine_node`
- `concept_node`
- `claim_object`
- `translation_witness`

### 7. `object_key`
The stable local key for the object inside the address.

Examples:
- `genesis_1_26_28`
- `imago_dei`
- `tselem`

### 8. `facet`
The current structural facet or declared surface of the object.

Examples:
- `primary`
- `comparison`
- `classification`
- `retrieval`
- `review`

## Example addresses

- `christian_ai_theology.scripture.genesis.creation.text.scripture_text.genesis_1_26_28.primary`
- `christian_ai_theology.theology.anthropology.core.doctrine.doctrine_node.imago_dei.primary`
- `christian_ai_theology.languages.hebrew.lexical.term.original_language_term.tselem.primary`
- `christian_ai_theology.boundary.noncanonical.pseudepigrapha.text.noncanonical_text.1_enoch.classification`

## What should not normally live in the address

The address should not normally encode:
- trust zone
- review status
- lifecycle state
- epistemic status
- overlay scope
- version

Those are governance fields, not structural slots.

## Address rule

Addresses should be:
- deterministic enough to be reusable
- semantically meaningful
- stable enough to support machine traversal
- changeable only through governed migration when structural movement is necessary

## Summary principle

Use the address system to make structural placement explicit.
Use IDs to preserve durable semantic identity.
Do not overload the address with every governance concern.
