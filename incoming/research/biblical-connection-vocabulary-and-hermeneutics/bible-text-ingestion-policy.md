---
id: research_packet.biblical_connection_vocabulary_and_hermeneutics.bible_text_ingestion_policy
anchor: research.biblical_connection_vocabulary_and_hermeneutics.bible_text_ingestion_policy
title: Bible Text Ingestion and Translation Policy Seed
node_type: research_policy_seed
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: proposed
created: 2026-04-29
created_by: ChatGPT
ai_usage_posture: staging_only_not_auto_promote
---

# Bible Text Ingestion and Translation Policy Seed

## Short answer

Do not add full Markdown Bible files yet.

First define reference anchors, licensing rules, original-language data policy, translation scope, and relationship vocabulary.

## Why full text should wait

### 1. Modern translations have copyright and retrieval restrictions

Many modern English translations are not compatible with bulk public repository storage.

ESV, NASB, NIV, NRSV, and most modern commentaries should not be bulk-imported into this public CC BY repository without formal permission or an explicitly licensed API arrangement.

### 2. Translation comparison is not only text storage

A translation comparison layer needs metadata: translation name, edition, copyright and permission status, language, source text basis, verse or passage anchor, translator note status, quotation boundary, source locator, and whether storage is allowed or only external reference is allowed.

### 3. Original-language text also needs source-specific review

Greek and Hebrew source options differ by license. Potentially promising resources include SBL Greek New Testament, Open Scriptures Hebrew Bible morphology and lemma data, public-domain Hebrew text forms depending on distribution and edition, and other source corpora only after license review.

### 4. References can be added before text

The repo can create canonical passage anchors before storing verse text.

A safe early pattern is passage anchor -> source text reference -> translation reference -> morphology reference -> relationship vocabulary -> small quotation only if licensed.

## Recommended ingestion levels

### Level 0: reference only

Store only canonical reference IDs, book/chapter/verse ranges, and metadata. This should be the near-term default.

### Level 1: short quotation under explicit permission

Store limited quotations only when permission and attribution rules are satisfied. Use sparingly.

### Level 2: open-license source text

Store text only when the source license is compatible with the repository license and intended retrieval use.

### Level 3: external licensed API

Do not store the text. Store API source metadata and fetch externally under permitted terms.

### Level 4: internal/private licensed corpus

Not appropriate for this public repo unless separated into a private licensed repository or protected data store.

## Recommended first Bible-data work

Do first: canonical reference format policy, source/translation license registry, original-language source registry, relationship vocabulary, textual evidence vocabulary, and hermeneutic method vocabulary.

Do later: selected open Greek text samples, selected Hebrew morphology examples, public-domain translation examples, translation comparison sidecars, and full corpus ingestion only after license and schema review.

## Red flags

Do not paste full ESV, NASB, NIV, NRSV, or other copyrighted translation books into the repo. Do not paste full modern commentary text into the repo. Do not create verse files without license metadata. Do not create AI retrievable text corpora without permission.

## Good first contribution

A good first contribution is a translation-source registry or policy note, not a Bible text dump.
