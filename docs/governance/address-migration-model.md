# Address Migration Model

## Purpose

This file defines how structural address changes should be handled without breaking repository integrity.

## Core rules

- semantic `id` must remain stable unless a separate governance decision requires change
- `address` may change only with recorded migration
- prior addresses should remain resolvable through a migration record

## Why this matters

Without migration discipline:
- links break
- references fail
- graph and retrieval systems lose continuity
- AI-assisted reasoning degrades when older structural handles disappear

With migration discipline:
- structure may evolve safely
- identity remains stable
- history remains interpretable
- older addresses may still resolve to newer ones

## Required migration record

Every address migration should preserve at least:
- `object_id`
- `old_address`
- `new_address`
- `reason`
- `timestamp`
- `version_change`
- `reviewer`

## Example migration record

```json
{
  "object_id": "doctrine.anthropology",
  "old_address": "christian_ai_theology.theology.anthropology.core.doctrine.doctrine_node.anthropology.primary",
  "new_address": "christian_ai_theology.theology.anthropology.foundation.doctrine.doctrine_node.anthropology.primary",
  "reason": "module restructuring",
  "timestamp": "ISO8601",
  "version_change": "v1 -> v2",
  "reviewer": "human_reviewer_id"
}
```

## Resolution rule

Systems using the repository should be able to:
- resolve an old address to the current address
- preserve the lineage of structural movement
- distinguish semantic continuity from structural relocation

## Summary principle

Address changes are governance-significant events, not silent renames.
