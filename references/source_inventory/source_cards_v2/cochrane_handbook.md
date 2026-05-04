# Cochrane Handbook Source Card v2

```yaml
source_id: cochrane_handbook
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/cochrane_handbook/canonical_current.md
  - references/canonical_sources/md/cochrane_handbook/chapter_01_chapter-01.md
  - references/canonical_sources/md/cochrane_handbook/chapter_15_chapter-15.md
canonical_urls:
  - https://training.cochrane.org/handbook
  - https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current
authority_level: canonical_conduct_manual
version_or_access_date: "Version 6.5, 2024; local corpus fetched 2026-05-04"
applies_to:
  - Cochrane intervention-review conduct methods
  - health and healthcare intervention-effect systematic reviews
  - review protocol, search, synthesis, risk-of-bias, GRADE, and interpretation routing
not_for:
  - non-health or non-intervention reviews without adaptation
  - standalone reporting checklist claims
  - treating Cochrane review conclusions as clinical practice recommendations
  - Cochrane-specific mandatory standards without checking MECIR
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate because the online Handbook is versioned and chapters may be updated; verify the current online chapter before publication-sensitive method claims.
reuse_or_license_risk: Cochrane terms apply; verify permissions before redistributing substantial excerpts or mirrored files.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: The local Cochrane Handbook capture is the current Cochrane Handbook for Systematic Reviews of Interventions, version 6.5, 2024.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/canonical_current.md
  support_type: direct
  verification_note: Use the current landing page before selecting chapter-level evidence.
  quote_or_locator: canonical_current.md:82-88; section_id=cochrane_handbook__canonical_current__s0004_sri_handbook
- claim: The Handbook covers end-to-end Cochrane review methods, including scope, eligibility, search and selection, data collection, risk of bias, meta-analysis, synthesis without meta-analysis, summary of findings, GRADE, and interpretation.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/canonical_current.md
  support_type: direct
  verification_note: The table of contents is a locator for which chapter to open for a precise method claim.
  quote_or_locator: canonical_current.md:109-143; section_id=cochrane_handbook__canonical_current__s0006_part_2_core_methods
- claim: The Handbook scope is systematic reviews on effects of interventions, specifically Cochrane methods, with a primary purpose of informing health or health-care decisions.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/chapter_01_chapter-01.md
  support_type: direct
  verification_note: Preserve the health and intervention-effect boundary when routing non-health or non-intervention questions.
  quote_or_locator: chapter_01_chapter-01.md:132-136; section_id=cochrane_handbook__chapter_01_chapter_01__s0007_1_1_why_do_a_systematic_review
- claim: Cochrane systematic review methods emphasize pre-specified questions and methods, explicit eligibility criteria, comprehensive searching, accounting for bias, and impartial analysis.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/chapter_01_chapter-01.md
  support_type: direct
  verification_note: Use this span for high-level conduct-method claims, then open task-specific chapters for details.
  quote_or_locator: chapter_01_chapter-01.md:118-120,134; section_ids=cochrane_handbook__chapter_01_chapter_01__s0006_key_points, __s0007_1_1_why_do_a_systematic_review
- claim: MECIR handles Cochrane expectations for conduct, reporting, updating, and plain-language summaries, while PRISMA recommendations are incorporated into Cochrane reporting expectations.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/chapter_01_chapter-01.md
  support_type: direct
  verification_note: Route mandatory Cochrane-standard questions to cochrane_mecir and generic reporting-checklist questions to PRISMA sources.
  quote_or_locator: chapter_01_chapter-01.md:186-192; section_id=cochrane_handbook__chapter_01_chapter_01__s0013_1_4_1_expectations_for_the_conduct_and_reporting_of_cochrane_reviews
- claim: Cochrane review authors should not make recommendations because specific action recommendations require additional evidence and judgments beyond most Cochrane reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_handbook/chapter_15_chapter-15.md
  support_type: direct
  verification_note: Keep review conclusions separate from clinical practice guideline recommendations.
  quote_or_locator: chapter_15_chapter-15.md:743-749; section_ids=cochrane_handbook__chapter_15_chapter_15__s0037_15_6_1_conclusions_sections_of_a_cochrane_review, __s0038_15_6_2_implications_for_practice
```

## Operational rules

- Use this card to choose the right Handbook chapter; cite the selected canonical chapter for final method claims.
- For Cochrane mandatory or highly desirable expectations, route to `cochrane_mecir` after using the Handbook for method context.
- For generic reporting-checklist wording, route to PRISMA sources rather than treating the Handbook as the reporting guideline.
- For non-health, non-intervention, scoping, qualitative, or social-policy review designs, check JBI or Campbell before transferring Cochrane intervention-review methods.
- Do not turn Cochrane review conclusions into clinical practice recommendations without separate guideline-development evidence.

## Common misuses

- Treating the Handbook as a universal systematic-review manual outside its health and intervention-effect focus.
- Citing the table of contents for detailed search, synthesis, risk-of-bias, or GRADE rules without opening the relevant chapter.
- Using Cochrane conduct guidance as a substitute for PRISMA reporting checklist items.

## Evidence limits

This card is a router aid. Final answers must cite the canonical Handbook chapter or official Cochrane URL. The local capture is marked partial in document indexes because only selected linked documents were downloaded, even though the Handbook chapter set is locally represented.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cochrane_handbook`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=cochrane_handbook`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=cochrane_handbook`.
- Optional local section locators: `references/corpus_index/sections/by_source/cochrane_handbook.jsonl`.

## Unresolved gaps

- Some linked supplementary documents from Handbook chapters failed or are partial in the local download manifest; verify linked external resources separately.
- The card does not enumerate all 23 locally captured chapters; use the document and section indexes for exact chapter selection.
