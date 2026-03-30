# Translation Trust and Sectarian Classification

## Purpose

This file defines how the repository should classify Bible translations, ancient versions, and sectarian or disputed renderings.

The goal is to let the project say not only which translation is being used, but also:
- what textual base it depends on
- what translation philosophy it uses
- whether its provenance claims are well supported
- whether it shows strong doctrinal or sectarian tendency
- whether it should be used for doctrine, comparison, caution, or exclusion

## Core principle

Do not treat all Bible translations as equally reliable, equally transparent, or equally suitable for doctrine.

A translation is not identical with:
- the canonical text
- the manuscript witness behind it
- the original-language term itself
- an interpretive tradition

A translation may be careful, uneven, sectarian, doctrinally tendentious, poorly sourced, or intentionally shaped by a movement's theology.

Those possibilities should be documented explicitly rather than argued case by case without standards.

## Protective rule

No translation witness should be treated as doctrinally usable by default without at least minimal metadata describing:
- translation philosophy
- textual base
- confessional or sectarian association
- notable rendering tendencies
- use-case limits where needed

Claims such as "oldest," "most original," or "restored" should not be accepted at face value. They should be documented and evaluated.

## Required classification fields

Every translation witness node should include the following fields:
- `translation_class`
- `translation_philosophy`
- `textual_base_quality`
- `provenance_claim_status`
- `doctrinal_tendency`
- `confessional_or_sectarian_association`
- `use_case_limit`
- `manipulation_risk`

## Field definitions

### `translation_class`
What kind of translation or version is this?

Recommended values:
- `mainstream_modern_translation`
- `ancient_version`
- `study_translation`
- `liturgical_translation`
- `paraphrase`
- `sectarian_translation`
- `restorationist_translation`
- `disputed_translation`

### `translation_philosophy`
How does the translation generally render the source text?

Recommended values:
- `formal_equivalence`
- `essentially_literal`
- `dynamic_equivalence`
- `mediating`
- `literary`
- `paraphrastic`
- `mixed`
- `opaque_or_undisclosed`

### `textual_base_quality`
How strong and transparent is the translation's textual base?

Recommended values:
- `well_documented_mainstream_base`
- `ancient_version_with_known_limits`
- `mixed_base`
- `restricted_or_selective_base`
- `poorly_documented_base`
- `disputed_base_claim`

### `provenance_claim_status`
How should the translation's claims about antiquity, source recovery, or manuscript status be handled?

Recommended values:
- `standard_claims`
- `supported_historical_claims`
- `partially_supported_claims`
- `disputed_claims`
- `unsupported_or_misleading_claims`

### `doctrinal_tendency`
How doctrinally neutral or tendentious is the translation likely to be?

Recommended values:
- `low_tendency`
- `moderate_tendency`
- `strong_tendency`
- `sectarian_tendency`
- `doctrinally_manipulative`

### `confessional_or_sectarian_association`
What kind of movement or community is the translation tied to?

Recommended values:
- `broad_ecumenical`
- `reformed_association`
- `catholic_association`
- `orthodox_association`
- `evangelical_association`
- `sectarian_association`
- `restorationist_association`
- `mixed_or_unclear`

### `use_case_limit`
What may this translation be used for in the repository?

Recommended values:
- `usable_for_doctrine`
- `usable_for_comparison`
- `usable_for_translation_history`
- `caution_required`
- `do_not_use_as_primary_doctrinal_witness`

### `manipulation_risk`
How much concern is there that the translation reflects tendentious or agenda-shaped rendering choices?

Recommended values:
- `low`
- `moderate`
- `high`
- `very_high`

## Interpretation rule

These fields should be read together.

For example:
- a translation may be ancient and valuable, yet limited by its status as a version rather than an original-language witness
- a translation may be modern and widely used, yet still shaped by a confessional register
- a translation may be heavily sectarian without being useless for comparative analysis
- a translation may be unsuitable as a primary doctrinal witness even if historically important to a movement

## Claims of antiquity or textual superiority

The repository should be especially cautious with claims such as:
- oldest Bible
- original restored Bible
- hidden manuscript tradition now recovered
- translation based on uniquely preserved truth text

Such claims should be documented under `provenance_claim_status` and should not be accepted without clear textual and historical support.

## Use of the terms "bad," "corrupt," or "manipulated"

The repository should prefer precise classification over vague condemnation.

Instead of only saying a translation is "bad," document:
- whether its textual base is weak or disputed
- whether its renderings are sectarian or doctrinally tendentious
- whether its provenance claims are unsupported
- whether it should be excluded from doctrinal use

The strongest warning language should be reserved for cases where there is clear evidence of systematic doctrinal manipulation, extreme sectarian shaping, or misleading provenance claims.

## Required warnings for high-risk translations

Any translation classified as:
- `sectarian_translation`
- `restorationist_translation`
- `unsupported_or_misleading_claims`
- `sectarian_tendency`
- `doctrinally_manipulative`
- `high` or `very_high` manipulation risk
- `do_not_use_as_primary_doctrinal_witness`

should contain an explicit warning block near the top of the file.

## Example warning language

`Warning: This translation is not treated in this repository as a neutral or primary doctrinal witness. It may be useful for comparison, movement history, or translation analysis, but its textual base, provenance claims, or doctrinal tendencies require caution.`

For stronger cases:

`Warning: This translation is classified in this repository as sectarian, doctrinally tendentious, or based on disputed or misleading provenance claims. It should not be used as a primary doctrinal witness and is documented only for comparison, movement analysis, or boundary-setting.`

## Suggested folder taxonomy

- `docs/translations/README.md`
- `docs/translations/ancient-versions/`
- `docs/translations/mainstream-modern/`
- `docs/translations/sectarian-and-disputed/`

### Ancient versions
Use for Septuagint, Vulgate, Peshitta, Targums, and related major versions.

### Mainstream modern
Use for broadly used modern translations with transparent editorial history.

### Sectarian and disputed
Use for translations requiring stronger caution because of sectarian control, tendentious renderings, disputed provenance claims, or high manipulation risk.

## Example classification patterns

### Example A: mainstream modern translation
- `translation_class`: `mainstream_modern_translation`
- `translation_philosophy`: `essentially_literal`
- `textual_base_quality`: `well_documented_mainstream_base`
- `provenance_claim_status`: `standard_claims`
- `doctrinal_tendency`: `moderate_tendency`
- `confessional_or_sectarian_association`: `evangelical_association`
- `use_case_limit`: `usable_for_doctrine`
- `manipulation_risk`: `low`

### Example B: ancient version
- `translation_class`: `ancient_version`
- `translation_philosophy`: `mixed`
- `textual_base_quality`: `ancient_version_with_known_limits`
- `provenance_claim_status`: `supported_historical_claims`
- `doctrinal_tendency`: `moderate_tendency`
- `confessional_or_sectarian_association`: `mixed_or_unclear`
- `use_case_limit`: `usable_for_translation_history`
- `manipulation_risk`: `low`

### Example C: sectarian or movement-controlled translation
- `translation_class`: `sectarian_translation`
- `translation_philosophy`: `opaque_or_undisclosed`
- `textual_base_quality`: `restricted_or_selective_base`
- `provenance_claim_status`: `disputed_claims`
- `doctrinal_tendency`: `sectarian_tendency`
- `confessional_or_sectarian_association`: `sectarian_association`
- `use_case_limit`: `do_not_use_as_primary_doctrinal_witness`
- `manipulation_risk`: `high`

### Example D: disputed restorationist claim
- `translation_class`: `restorationist_translation`
- `translation_philosophy`: `mixed`
- `textual_base_quality`: `disputed_base_claim`
- `provenance_claim_status`: `unsupported_or_misleading_claims`
- `doctrinal_tendency`: `doctrinally_manipulative`
- `confessional_or_sectarian_association`: `restorationist_association`
- `use_case_limit`: `do_not_use_as_primary_doctrinal_witness`
- `manipulation_risk`: `very_high`

## Candidate examples rule

Named examples may be added to the repository only when their file documents the evidence for their classification.

Do not classify a translation merely by reputation or internet polemics. The repository should document:
- textual base notes
- editorial transparency
- provenance claim issues if any
- notable doctrinally significant renderings
- why the use-case limit is being applied

## Summary principle

The repository should be able to say not only which translation is cited, but whether that translation should be trusted, limited, compared cautiously, or excluded as a primary doctrinal witness.

That protects the project from quiet doctrinal contamination at the translation layer.
