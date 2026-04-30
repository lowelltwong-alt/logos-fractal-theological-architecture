---
object_type: ingestion_plan
trust_zone: incoming_research
lifecycle_status: draft
provenance_note: "Created 2026-04-30 as a staged Bible ingestion and RAGGraph plan."
reason_for_inclusion: "Plan whole-Bible and original-language ingestion safely without premature copyrighted corpus ingestion."
review_status: unreviewed
ai_usage_posture: planning_only_not_auto_ingest
---

# Bible Ingestion and RAGGraph Plan

## Goal

Build toward a governed Bible RAGGraph without contaminating the repository with unlicensed texts or generic graph edges.

## Do not start with full Bible ingestion

Start with source governance:

> source registry
> -> licensing review
> -> canonical reference model
> -> biblical connection vocabulary
> -> one-book pilot
> -> metadata sidecars
> -> chunking
> -> evidence objects
> -> graph relationships
> -> retrieval/rendering contracts

## Canonical object families

Future Bible ingestion should distinguish:

- BibleWork
- BibleBook
- BibleChapter
- BibleVerse
- BiblePassageRange
- Pericope
- TranslationEdition
- OriginalLanguageEdition
- ManuscriptWitness
- Reading
- Variant
- Lexeme
- Token
- MorphologyTag
- SemanticDomain
- CrossReference
- Quotation
- Allusion
- Echo
- Typology
- FulfillmentClaim
- DoctrineSupport

## Chunk types

Possible chunking units:

- book introduction;
- chapter;
- paragraph/pericope;
- verse range;
- individual verse;
- lexical unit;
- cross-reference cluster;
- doctrine-support bundle;
- evidence bundle.

## Required sidecar fields

Every future Bible chunk should carry at least:

- chunk_id
- source_id
- translation_or_edition
- book
- chapter
- verse_start
- verse_end
- osis_ref
- language
- text_kind
- license
- copyright_status
- trust_zone
- created_at
- source_url
- source_hash
- chunk_hash
- contains_full_text
- allowed_public_repo_use
- allowed_embedding_use
- review_status

## Open-text pilot

Preferred pilot:

- book: Romans or John;
- English: World English Bible or ASV 1901;
- optional: KJV with jurisdiction note;
- original language: public-domain or open Greek source only after source-file license review.

Do not begin with all sixty-six books. Prove the model with one book, one translation, and one original-language source if licensing permits.

## RAGGraph routes

A mature Bible RAGGraph should support multiple entry points:

- passage lookup;
- concept lookup;
- doctrine support;
- cross-reference exploration;
- lexical/lemma exploration;
- source/evidence bundle;
- profile comparison;
- review-ready diff.

## Relationship vocabulary dependency

Do not create generic `related_to` Bible edges.

The graph should wait for the governed biblical connection vocabulary bridge. Candidate predicates include:

- quotes
- alludes_to
- echoes
- typologically_corresponds_to
- claims_fulfillment_of
- has_lemma
- translated_as
- has_reading
- attested_by_witness
- interpreted_by
- grounds_doctrine
- supports_claim
- constrains_application

## Original-language route

Original-language ingestion is strategically strong, but must distinguish ancient text from modern edition and digital source.

Track separately:

- ancient work;
- edition;
- transcription;
- morphology database;
- lemma mapping;
- lexical source;
- manuscript image;
- apparatus.

## Whole-Bible path

After the pilot, expand in order:

1. Romans or John.
2. Gospel + Romans bundle.
3. New Testament open-text bundle.
4. Selected Old Testament books.
5. Whole Bible only after source registry, validators, and license governance are stable.

## Hard boundary

No ESV, NASB, NIV, CSB, NLT, NKJV, modern study Bible notes, proprietary lexicons, or modern critical apparatuses should be bulk-ingested, chunked, embedded, or redistributed in the public repo without explicit permission or compatible licensing.
