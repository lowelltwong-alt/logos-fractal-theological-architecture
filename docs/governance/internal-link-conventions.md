---
object_type: governance_policy
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to define stable internal link conventions and prevent broken-reference regressions."
reason_for_inclusion: "Provides a canonical policy for relative internal links, path naming, and validation expectations."
---

# Internal Link Conventions

## Purpose

Define how internal file references should be written so links remain stable and machine-checkable.

## Relative path style

- Use repository-relative paths from the repo root when citing files in prose, such as:
  - `docs/governance/README.md`
  - `data/graph/README.md`
- In markdown links, use relative targets that resolve from the current file location.
- Prefer explicit filenames over directory-only links.
- When referencing sections, keep the file path plus anchor (for example: `docs/governance/README.md#files-in-this-folder`).

## Naming policy

- Keep filenames lowercase.
- Use hyphen-separated words.
- Prefer descriptive, stable names over temporary migration aliases.
- Do not repurpose an existing canonical filename for unrelated content.
- If scope changes substantially, create a new file and deprecate the old one through references.

## Validation requirement

- Internal markdown links and backtick path references must resolve to existing local targets.
- Use `scripts/validate_internal_links.py` as part of local validation before commit.
- Treat unresolved paths as blocking validation failures.
