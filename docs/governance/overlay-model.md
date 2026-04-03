# Overlay Model

## Purpose

This file defines how the Logos repository should support a shared Christian core while also allowing governed extensions for tradition, institution, and application contexts.

## Core principle

The repository should not force a false choice between:
- one flattened generic Christianity
- many disconnected siloed overlays

Instead, the repository should support:
- a shared core
- governed overlays
- explicit scope declarations

## Overlay families

### 1. Shared core
This is the broadest reusable repository layer.

Use for material intended to function across a wide Christian audience without depending on one narrower confessional overlay.

### 2. Tradition overlays
Use for material shaped by a particular Christian tradition.

Examples:
- reformed
- baptist
- anglican
- catholic
- orthodox

### 3. Institution overlays
Use for material shaped by a specific institutional context.

Examples:
- small_business
- ministry
- school
- nonprofit
- publisher
- network

### 4. Application overlays
Use for material shaped by a recurring use case.

Examples:
- ai_governance
- hiring
- stewardship
- education
- board_governance

## Required overlay fields

Serious nodes that use overlays should normally declare:
- `overlay_scope`
- `shared_core_status`
- `tradition_scope` where relevant
- `institution_scope` where relevant
- `application_scope` where relevant

## Overlay rule

A node may belong to:
- shared core only
- one overlay only
- shared core plus one or more overlays

But its scope should remain explicit rather than assumed.

## Anti-flattening rule

Do not silently present overlay-specific material as if it were universal shared-core doctrine.

## Anti-fragmentation rule

Do not create tradition-specific overlays for concepts that still function well inside the shared core.

## Summary principle

The overlay model should make Logos more reusable without making it vague, sectarian by default, or structurally fragmented.
