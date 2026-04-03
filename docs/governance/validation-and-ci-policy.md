# Validation and CI Policy

## Purpose

This file defines how validation and CI should reinforce the Logos repository's architecture.

## Core principle

Validation should enforce structure, not invent theology.

CI belongs to the repository DNA because it turns governance commitments into executable constraints.

## Minimum validation targets

At minimum, the repository should validate:
- required metadata fields
- valid address structure
- valid node types
- valid trust zones
- valid epistemic statuses for claim objects
- valid relationship verbs where governed
- resolvable references to IDs where required
- duplicate ID collisions
- missing migration records when address changes occur
- overlay scope consistency where overlay fields are used

## Validation layers

### 1. Metadata validation
Checks whether required fields exist and use approved values.

### 2. Address validation
Checks whether the structural address follows the approved eight-layer grammar.

### 3. Cross-reference validation
Checks whether referenced IDs and links resolve.

### 4. Claim validation
Checks whether claim objects preserve required subject / predicate / object and evidence posture.

### 5. Drift detection hooks
Checks for vocabulary drift, duplicate nodes, or invalid promotion patterns.

## CI rule

Once validation scripts exist, CI should run them on pull requests and major branch changes.

## Summary principle

Validation and CI should make the Logos architecture more durable, machine-legible, and review-safe without replacing human theological judgment.
