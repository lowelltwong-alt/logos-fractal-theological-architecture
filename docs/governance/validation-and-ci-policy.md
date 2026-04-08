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
- external mapping integrity (namespace, duplicates, trust-zone direction)
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

## Standard validation command sequence

Run the repository validators in this order:

1. `python scripts/validate_node_frontmatter.py`
2. `python scripts/validate_claim_files.py`
3. `python scripts/validate_cross_references.py`
4. `python scripts/validate_trust_zone_vocabulary.py`
5. `python scripts/validate_external_mappings.py`

## CI rule

Once validation scripts exist, CI should run them on pull requests and major branch changes.

## Summary principle

Validation and CI should make the Logos architecture more durable, machine-legible, and review-safe without replacing human theological judgment.


## Current local validation routine

Run:

- `scripts/run_validations.sh`

This routine currently executes:
- `scripts/validate_node_frontmatter.py`
- `scripts/validate_cross_references.py`
- `scripts/validate_claim_files.py`
- `scripts/validate_internal_links.py`
- `scripts/validate_external_mappings.py`
