---
object_type: governance_metadata_audit
trust_zone: canonical
lifecycle_status: active
provenance_note: "Audit executed on 2026-04-08 by scanning docs/governance markdown files and validating required frontmatter fields."
reason_for_inclusion: "Provide a concrete checkpoint for required metadata coverage and remediation planning for governed governance documents."
---

# Governed Metadata Audit (2026-04-08)

## Audit scope

- Path audited: `docs/governance/`
- File type: `*.md`
- Required metadata fields:
  - `object_type`
  - `trust_zone`
  - `lifecycle_status` (or `lifecycle_state`)
  - `provenance_note`
  - `reason_for_inclusion`

## Results summary

- Markdown files in scope: **78**
- Files with frontmatter and required keys: **19**
- Files missing frontmatter metadata block: **59**
- Files with invalid trust-zone vocabulary among audited frontmatter files: **0**

## Gap interpretation

Current validator behavior confirms metadata quality only for files that already contain frontmatter.
The remaining 59 governance markdown files should be treated as metadata backlog until each receives a compliant metadata block.

## Remediation queue (next steps)

1. Add required frontmatter to high-authority governance entrypoints first:
   - `docs/governance/README.md`
   - `docs/governance/operating-framework-index.md`
   - `docs/governance/trust-zones.md`
   - `docs/governance/doctrine-constitution.md`
2. Extend `scripts/validate_governance_metadata.py` in a follow-up to fail when governed files are missing frontmatter, after initial backlog reduction.
3. Track remaining backlog in batches to keep reviews small.
