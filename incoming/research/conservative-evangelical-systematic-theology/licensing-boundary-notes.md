---
object_type: licensing_boundary_notes
trust_zone: incoming_research
lifecycle_status: draft
provenance_note: "Created 2026-04-30 as staged notes on copyright-safe theology and Bible source strategies."
reason_for_inclusion: "Brainstorm lawful alternatives to copyrighted source ingestion for Bible and theology RAGGraph work."
review_status: unreviewed
ai_usage_posture: planning_only_not_legal_advice
---

# Licensing Boundary Notes and Copyright-Safe Paths

## Principle

The goal is not to avoid copyright by hiding copying. The goal is to design the repository so it can use lawful, open, public-domain, licensed, or private sources without contaminating public graph truth.

## Paths around copyright constraints

### 1. Public-domain English Bible route

Use English translations that are public domain or clearly open.

Candidates to verify:

- KJV in the United States, with jurisdiction note;
- ASV 1901;
- World English Bible;
- possibly Open English Bible;
- other open translations with clear licenses.

Pros:

- public ingestion possible;
- easy pastor/lay readability;
- useful for RAG pilot.

Cons:

- KJV language is older;
- public-domain modern translations may not match church-preferred ESV/NASB/NIV usage;
- source quality and translation philosophy need profile notes.

### 2. Open-license Bible route

Use open Bible translation projects with explicit licenses.

Candidates to verify:

- World English Bible;
- Open English Bible;
- unfoldingWord ULT/UST and translation resources;
- other Creative Commons projects.

Pros:

- newer language possible;
- explicit reuse terms.

Cons:

- attribution/share-alike obligations may affect repository licensing;
- some conservative churches may not recognize the translation as preferred.

### 3. Original-language route

Use original-language texts and build your own reference/translation layer.

Pros:

- closer to source;
- avoids dependence on modern copyrighted English translations;
- excellent for lexeme/token/lemma graph work;
- enables conservative contributors with Greek/Hebrew skills to review.

Cons:

- modern editions and morphology databases may still be licensed;
- needs qualified reviewers;
- translation/rendering layer is harder for lay users.

### 4. Public-domain theology route

Use older orthodox and conservative Protestant works whose source editions are public domain.

Candidate families:

- Charles Hodge;
- A. A. Hodge;
- B. B. Warfield;
- W. G. T. Shedd;
- John Owen;
- Jonathan Edwards;
- Calvin;
- Luther;
- Augustine;
- Athanasius.

This gives the repo actual ingestible theology without copying modern copyrighted works.

### 5. Modern theology reference-only route

Use modern sources as profile, citation, and routing surfaces only.

Examples:

- Wayne Grudem;
- J. I. Packer;
- D. A. Carson;
- R. C. Sproul;
- Tim Keller;
- John Piper;
- Michael Horton;
- Kevin DeYoung.

Allowed:

- source profile;
- doctrine map;
- short review quotations;
- original summaries;
- citation pointers.

Not allowed without permission:

- full-text ingestion;
- full-text chunking;
- full-text embeddings;
- public RAG index.

### 6. Private licensed connector route

A user, church, seminary, or institution may create a private licensed index outside the public repo.

Public repo may store:

- connector policy;
- source manifest schema;
- retrieval rules;
- no source text;
- no chunks;
- no embeddings.

### 7. Permission route

Ask publishers/authors for permission to create a limited educational/research index.

Possible structures:

- private contributor-only index;
- limited chapter metadata only;
- quote-limited index;
- approved excerpt corpus;
- public profile but private source text.

### 8. User-supplied local corpus route

Allow a future local tool to index files supplied by a user who is responsible for rights.

Rules:

- must not commit to public repo;
- must not upload chunks to public artifacts;
- must not leak text into claim objects;
- must not use modern translations as hidden source;
- should begin with small books/passages, not whole Bible.

### 9. Verse-reference and metadata route

Even without text ingestion, build graph infrastructure around references.

Allowed:

- book/chapter/verse identifiers;
- OSIS-style references;
- cross-reference objects;
- doctrine-to-passage references;
- source profiles;
- license registry.

This is the safest first step.

## Recommended first lawful corpus stack

For public ingestion pilot:

> WEB Romans
> ASV Romans
> KJV Romans with jurisdiction note
> public-domain Greek Romans if source license is verified

For theology ingestion pilot:

> Charles Hodge selected public-domain sections
> Calvin public-domain sections
> Augustine / Athanasius public-domain sections

For modern conservative profile routing:

> Grudem source profile only
> Carson source profile only
> Sproul source profile only
> Packer source profile only
> Keller source profile only

## Hard no for public repo

Do not commit:

- ESV full text;
- NASB full text;
- NIV full text;
- CSB full text;
- NLT full text;
- NKJV full text;
- full Grudem text;
- full modern commentaries;
- proprietary lexicon entries;
- modern critical apparatuses;
- private licensed source chunks;
- private licensed embeddings.
