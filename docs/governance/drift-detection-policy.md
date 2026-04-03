# Drift Detection Policy

## Purpose

This file defines how the Logos repository should detect structural and semantic drift before drift becomes architectural incoherence.

## Core principle

Fractal repositories do not fail only through missing content.
They also fail through silent drift.

## Drift categories

### 1. Vocabulary drift
Unregistered terms, tags, relation verbs, or node labels begin appearing inconsistently.

### 2. Structural drift
Branches stop using the shared metadata shell or begin inventing local object grammars without governance.

### 3. Identity drift
Stable objects begin receiving new IDs or anchors without migration or justification.

### 4. Address drift
Address patterns become inconsistent or over-encode governance concerns that belong in metadata.

### 5. Trust drift
Draft, experimental, reviewed, and boundary-restricted materials begin being treated as if they were interchangeable.

### 6. Overlay drift
Overlay-specific materials begin appearing as if they were shared core, or shared-core materials fragment unnecessarily into overlays.

## Detection targets

The repository should eventually detect:
- inconsistent field names
- inconsistent address patterns
- duplicate or near-duplicate concept nodes
- unstable relation-verb use
- unreviewed material being reused as trusted core
- repeated unresolved migration aliases

## Review rule

When significant drift is detected, the preferred response is:
1. diagnose the drift type
2. isolate affected branches or files
3. repair governance or metadata shell first
4. only then continue expansion

## Summary principle

Drift detection should protect the repository from becoming a loosely related pile of files that only appears fractal on the surface.
