---
object_type: quarantine_data_readme
trust_zone: proposed
lifecycle_status: active
provenance_note: "Created on 2026-04-08 as storage lanes for AI-generated proposals and review artifacts."
reason_for_inclusion: "Provide a governed staging area where AI output can be normalized and reviewed before any promotion decision."
---

# AI Output Quarantine Data Layout

- `proposals/`: raw AI draft objects.
- `normalized/`: deterministically normalized proposal objects.
- `suggestions/`: suggested links and edge candidates.

All artifacts here are non-canonical until explicit reviewer promotion.
