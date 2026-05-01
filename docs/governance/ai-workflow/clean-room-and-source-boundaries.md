---
object_type: source_boundary_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: mandatory_source_boundary_guidance
provenance_note: "Created 2026-04-30 to define clean-room and source-use boundaries for AI-assisted work."
reason_for_inclusion: "Define clean-room limits and source-use boundaries so AI-assisted work does not import leaked material, private prompts, protected source text, or private corpus artifacts."
---

# Clean-Room and Source Boundaries

## Clean-room rule

Do not copy leaked code, private prompts, private model instructions, or leak-derived repositories.

Allowed clean-room lessons include:

- mode separation;
- permission boundaries;
- allow, ask, deny policies;
- hooks and validation gates;
- approval packets;
- run/audit trails;
- source boundaries;
- trust zones;
- read/plan/execute separation.

## Source-use categories

### Public and open sources

Public-domain or open-license material may be used only after source status is reviewed and recorded.

### Reference-only sources

Modern copyrighted theology books, Bible translations, proprietary lexicons, and study notes may be used only as reference/profile/citation surfaces unless there is explicit permission or compatible licensing.

### Private licensed sources

Private licensed material must remain outside the public repository unless permission allows public inclusion.

The repo may store connector policy, source manifests, and non-sensitive metadata, but not private source text, chunks, or embeddings.

## Hard no for public repo

Do not commit:

- full protected modern Bible translations;
- full modern theology books;
- full Grudem text;
- proprietary lexicon entries;
- private corpus chunks;
- private embeddings;
- private prompts;
- leaked code;
- leak-derived artifacts;
- secrets or credentials.

## Allowed public repo surfaces

Allowed where appropriate:

- source profiles;
- metadata;
- route templates;
- citation pointers;
- original summaries;
- short review excerpts where lawful and necessary;
- public-domain or open-license text after source review;
- private connector policy without source text.

## AI output boundary

AI-generated text may stage research, templates, summaries, and drafts. It must not silently become doctrine, claim objects, graph truth, source registry truth, or ingestion output without the correct route and review path.
