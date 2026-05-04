# Source card v2: SANRA

```yaml
source_id: sanra
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  - references/canonical_sources/md/sanra/linked_1_s41073-019-0064-8.pdf.md
canonical_urls:
  - https://link.springer.com/article/10.1186/s41073-019-0064-8
authority_level: canonical_appraisal_tool
version_or_access_date: 2019 article; local capture reviewed 2026-05-04
applies_to:
  - quality assessment of narrative review articles
  - narrative review writing prior
  - distinguishing narrative review appraisal from systematic review reporting
not_for:
  - systematic review reporting
  - systematic review methodological quality appraisal
  - formal taxonomy development methodology
  - database/API source selection
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: low; original article is stable, but publisher page layout may change.
reuse_or_license_risk: article is open access; verify license and linked instrument terms before redistributing forms.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "SANRA was developed for assessing the quality of narrative review articles."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The abstract and background state the gap and purpose."
  quote_or_locator: "Abstract / Background and Conclusions."

- claim: "SANRA consists of six items scored from 0 to 2, with a maximum sum score of 12."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Methods section lists the six revised scale items and scoring."
  quote_or_locator: "Methods section beginning 'The six items that form the revised scale...'."

- claim: "The six SANRA domains cover importance, aims, literature search, referencing, scientific reasoning/evidence level, and endpoint data."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Methods section states the six topics."
  quote_or_locator: "Methods section discussing Fig. 1 and the six items."

- claim: "SANRA is a critical appraisal tool, not a reporting guideline."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Discussion explicitly states SANRA is a critical appraisal tool and not a reporting guideline."
  quote_or_locator: "Discussion / Validity."

- claim: "SANRA should not be used as a strict universal grading scale because the article warns about validity limits, lack of established cut-offs, and the need for rater training."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Discussion notes rater training, limitations, and caution around cross-setting comparisons/cutoffs."
  quote_or_locator: "Discussion / Inter-rater reliability, Validity, and Limitations."
```

## Operational rules

1. Use SANRA when the user asks about narrative review quality or how to improve a non-systematic review.
2. Do not apply SANRA to systematic reviews as a replacement for PRISMA, AMSTAR 2, ROBIS, or Cochrane/JBI.
3. Use SANRA to flag narrative-review quality dimensions: aim, search description, referencing, scientific reasoning, and endpoint data.
4. When a survey is closer to an NLP/CS literature survey than a biomedical narrative review, use SANRA as partial guidance only and pair it with taxonomy/survey-writing and venue/exemplar sources.

## Common misuses

1. Treating SANRA as a formal reporting guideline.
2. Treating SANRA score thresholds as universally validated.
3. Using SANRA to rate systematic review conduct.
4. Ignoring the article’s caution that validity and reliability depend on setting, raters, and training.

## Evidence limits

- SANRA was developed and tested in a medical editorial context.
- It is not enough for taxonomy-building methodology; pair with Nickerson/Kundisch taxonomy sources.
- It does not supply database search reporting standards comparable to PRISMA-S or TARCiS.
- It is not venue policy.

## Verification paths

1. `references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md`
2. `references/canonical_sources/md/sanra/linked_1_s41073-019-0064-8.pdf.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Add a quote-level locator for the exact six-item list after section indexes are rebuilt or made available.
- Confirm whether the linked instrument/download has separate reuse conditions.
