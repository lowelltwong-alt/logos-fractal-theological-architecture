# Retrieval Neighborhood Model

## Purpose

This file defines how retrieval context should be expanded around governed repository objects.

## Core principle

Retrieval should be governed rather than ad hoc.

The repository should move beyond:
- naive keyword search
- unconstrained vector similarity
- raw graph adjacency without trust or review awareness

## Retrieval neighborhood idea

A retrieval neighborhood is a governed context package around a node, claim, or passage.

A neighborhood may include:
- the focal object
- its immediate parents and children
- directly relevant claims
- directly relevant lexical or translation notes
- trust and review posture
- overlay-relevant context where appropriate

## First recommended neighborhood types

### 1. Passage neighborhood
For a scripture text or pericope.

### 2. Doctrine neighborhood
For a doctrine node and its core grounding objects.

### 3. Concept neighborhood
For reusable cross-branch concepts.

### 4. Comparison neighborhood
For thinker, doctrine, or tradition comparison work.

### 5. Application neighborhood
For downstream institutional or governance use.

## Retrieval rule

Neighborhood expansion should respect:
- trust zones
- review status
- boundary limits
- overlay scope

## Summary principle

The retrieval layer should package governed context in a way that is useful to both humans and future AI systems without flattening review posture, trust, or theological boundaries.
