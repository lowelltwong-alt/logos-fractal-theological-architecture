# Noncanonical and Heresy Classification

## Purpose

This file defines how the repository should classify and handle:
- deuterocanonical texts
- apocryphal and related literature
- pseudepigraphal texts
- forged texts
- heretical texts
- disputed or tradition-specific sources

The goal is to document these materials clearly without allowing them to blur into the canon layer or function as unmarked doctrinal sources.

## Core principle

Do not collapse these into one category:
- canonical scripture
- deuterocanonical scripture
- noncanonical but historically relevant text
- pseudepigraphal text
- forged text
- heretical text
- commentary or reception history

These may be related, but they are not equivalent in authority, trust, or doctrinal use.

## Protective rule

No noncanonical or disputed source may be treated as doctrinally usable by default.

Its status must be made explicit through controlled classification fields before it is used anywhere in the repository.

## Required classification fields

Every noncanonical, disputed, or questionable source should include the following fields:
- `canonical_status`
- `confessional_status`
- `historical_authenticity`
- `doctrinal_alignment`
- `use_case_limit`

## Field definitions

### `canonical_status`
What is the source's status relative to canon?

Recommended values:
- `canonical`
- `deuterocanonical`
- `noncanonical`
- `disputed_canonical_by_tradition`

### `confessional_status`
How is the source received across major Christian traditions?

Recommended values:
- `received_in_catholic`
- `received_in_orthodox`
- `received_in_oriental_orthodox`
- `received_in_ethiopian_tradition`
- `rejected_by_reformed`
- `rejected_by_catholic`
- `rejected_by_orthodox`
- `broadly_rejected`
- `mixed_reception`

### `historical_authenticity`
What is the source's historical status as a text?

Recommended values:
- `primary_ancient_witness`
- `ancient_translation_witness`
- `ancient_noncanonical_text`
- `pseudepigraphal`
- `forged`
- `disputed_authenticity`

### `doctrinal_alignment`
How does the source align with orthodox Christian theology as received in the relevant tradition?

Recommended values:
- `strong_alignment`
- `partial_alignment`
- `mixed_alignment`
- `weak_alignment`
- `contradictory`
- `heretical_by_tradition`

### `use_case_limit`
What may this source be used for in the repository?

Recommended values:
- `usable_for_doctrine`
- `usable_for_textual_history`
- `usable_for_background_context`
- `usable_for_comparative_theology`
- `caution_required`
- `do_not_use_for_doctrine`

## Interpretation rule

These fields should be read together, not in isolation.

For example:
- a source may be noncanonical but historically important
- a source may be deuterocanonical in one tradition and rejected in another
- a source may be ancient and influential while still doctrinally unsafe as an authority
- a source may be useful for background context but not for doctrine

## Use of the word "heretical"

The label `heretical_by_tradition` should be used carefully.

It should normally be reserved for cases where:
- a tradition explicitly classifies the source or its teachings as heretical
- the text is strongly tied to doctrinal systems rejected by orthodox Christianity
- the disagreement is doctrinal, not merely canonical or historical

Do not use `heretical` as a catch-all synonym for:
- noncanonical
- disputed
- pseudepigraphal
- unfamiliar
- outside one tradition's canon

## Documentation rule

Every noncanonical node should also explain briefly:
- why it is being included at all
- what it may help clarify historically or comparatively
- what it must not be used to establish

## Folder taxonomy recommendation

Use this structure for noncanonical material:

- `docs/noncanonical/README.md`
- `docs/noncanonical/deuterocanonical/`
- `docs/noncanonical/pseudepigrapha/`
- `docs/noncanonical/forgeries-and-heretical/`

### Deuterocanonical folder
Use for texts received as scripture in some Christian traditions but not others.

### Pseudepigrapha folder
Use for ancient noncanonical literature of historical, thematic, or comparative value.

### Forgeries-and-heretical folder
Use for texts that require the highest caution and strongest restriction.

These should never be allowed to blend into the canon, doctrine, or concept layers without explicit markers and warnings.

## Required warnings for high-risk sources

Any node classified as:
- `forged`
- `contradictory`
- `heretical_by_tradition`
- `do_not_use_for_doctrine`

should contain an explicit warning block near the top of the file.

## Example warning language

`Warning: This source is noncanonical and should not be used as doctrinal authority in this repository. It may be included only for historical, comparative, or reception-history purposes.`

For higher-risk cases:

`Warning: This source is classified in this repository as forged, doctrinally contradictory, or heretical by tradition. It is documented only for historical awareness, comparison, or boundary-setting and should not be used to establish doctrine.`

## Example classification patterns

### Example A: 1 Enoch
- `canonical_status`: `noncanonical`
- `confessional_status`: `mixed_reception`
- `historical_authenticity`: `ancient_noncanonical_text`
- `doctrinal_alignment`: `mixed_alignment`
- `use_case_limit`: `usable_for_background_context`

### Example B: Wisdom of Solomon
- `canonical_status`: `deuterocanonical`
- `confessional_status`: `received_in_catholic`
- `historical_authenticity`: `ancient_noncanonical_text`
- `doctrinal_alignment`: `strong_alignment`
- `use_case_limit`: `usable_for_comparative_theology`

### Example C: Gospel of Mary
- `canonical_status`: `noncanonical`
- `confessional_status`: `broadly_rejected`
- `historical_authenticity`: `ancient_noncanonical_text`
- `doctrinal_alignment`: `mixed_alignment`
- `use_case_limit`: `usable_for_comparative_theology`

### Example D: forged or strongly heretical text
- `canonical_status`: `noncanonical`
- `confessional_status`: `broadly_rejected`
- `historical_authenticity`: `forged`
- `doctrinal_alignment`: `heretical_by_tradition`
- `use_case_limit`: `do_not_use_for_doctrine`

## Summary principle

The repository should be able to document boundary texts without letting boundary texts quietly become authorities.

That means classifying them precisely, warning clearly, and limiting their use explicitly.
