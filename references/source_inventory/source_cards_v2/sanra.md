# SANRA Source Card v2

```yaml
source_id: sanra
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  - references/canonical_sources/md/sanra/linked_1_s41073-019-0064-8.pdf.md
canonical_urls:
  - https://researchintegrityjournal.biomedcentral.com/articles/10.1186/s41073-019-0064-8
authority_level: canonical_appraisal_tool
version_or_access_date: "2019; local corpus fetched 2026-05-04"
applies_to:
  - appraisal of narrative review article quality
  - survey writing audit heuristics when clearly labeled as appraisal support
not_for:
  - end-to-end narrative review conduct guidance
  - systematic review reporting requirements
  - taxonomy design methodology
  - universal grading cutoffs across all settings
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for the 2019 SANRA paper; moderate for any downstream consensus or cutoff claims.
reuse_or_license_risk: Open access article terms apply; verify license text before redistributing substantial excerpts.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: SANRA was developed to assess the quality of narrative review articles.
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: Use the canonical article abstract/background/conclusion before applying SANRA.
  quote_or_locator: canonical_s41073-019-0064-8.md:80-83,139,220; section_ids=sanra__canonical_s41073_019_0064_8__s0004_background, __s0013_background, __s0023_conclusion
- claim: SANRA has six items, each scored from 0 to 2, for a maximum score of 12.
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: Use the methods/results sections for item count and scoring.
  quote_or_locator: canonical_s41073-019-0064-8.md:84-90,147; section_ids=sanra__canonical_s41073_019_0064_8__s0005_methods, __s0014_methods
- claim: The six SANRA domains are justification of importance, aims, literature search, referencing, scientific reasoning, and data presentation.
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: Use the exact item list before turning SANRA into an audit checklist.
  quote_or_locator: canonical_s41073-019-0064-8.md:86,149; section_id=sanra__canonical_s41073_019_0064_8__s0014_methods
- claim: SANRA is a critical appraisal tool, not a reporting guideline or conduct manual.
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: Preserve the appraisal-vs-reporting boundary when routing survey-writing questions.
  quote_or_locator: canonical_s41073-019-0064-8.md:137-139,208; section_ids=sanra__canonical_s41073_019_0064_8__s0013_background, __s0021_validity
- claim: The SANRA authors discuss feasibility, training, inter-rater reliability, validity, and limitations rather than presenting a universal grade scale.
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: Keep cutoff language narrow; the article includes a very-poor-quality example but warns about broader comparison limits.
  quote_or_locator: canonical_s41073-019-0064-8.md:192,200-202,206-216; section_ids=sanra__canonical_s41073_019_0064_8__s0018_feasibility, __s0020_inter_rater_reliability, __s0021_validity, __s0022_limitations
```

## Operational rules

- Use SANRA to support appraisal or audit of narrative-review quality.
- When applying SANRA to NLP/CS literature surveys, label the transfer as local routing/appraisal guidance unless the target source itself is a narrative review article.
- Do not use SANRA as the primary authority for SR reporting, search conduct, evidence certainty, or taxonomy construction.

## Common misuses

- Treating SANRA as a recipe for writing a narrative review from start to finish.
- Treating SANRA as a PRISMA substitute.
- Presenting SANRA score thresholds as universal quality grades without the article's limitations.

## Evidence limits

This card is a source-selection aid. Final claims should cite the SANRA article path or URL. Cross-domain use for general survey writing is an agent routing inference, not a direct SANRA article claim.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=sanra`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=sanra`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=sanra`.
- Optional local section locators: `references/corpus_index/sections/by_source/sanra.jsonl`.

## Unresolved gaps

- If this card is used for domain-specific literature surveys, add target-domain examples or a separate survey-writing claim ledger rather than expanding SANRA beyond its stated scope.
