# Cochrane Chapter 9 Source Card v2

```yaml
source_id: cochrane_ch09
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
canonical_urls:
  - https://training.cochrane.org/handbook/current/chapter-09
authority_level: canonical_conduct_manual
version_or_access_date: "Handbook version 6.5, 2024; chapter last updated October 2019; local corpus fetched 2026-05-04"
applies_to:
  - chapter-specific routing for summarizing study characteristics before synthesis
  - grouping studies by PICO elements for each synthesis
  - checking data availability, multiplicity, and decision rules before synthesis
  - transparent preparation of comparisons and study-characteristic tables
not_for:
  - whole-Handbook claims outside Chapter 9
  - detailed meta-analysis methods from Chapters 10 or 11
  - non-meta-analytic synthesis method claims from Chapter 12
  - generic narrative-review writing advice outside systematic reviews of interventions
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate because this is an online Cochrane chapter within a versioned Handbook; verify the current chapter before publication-sensitive method claims.
reuse_or_license_risk: Cochrane terms apply; verify permissions before redistributing substantial excerpts or mirrored files.
qa_status: created_from_local_canonical_markdown_and_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: This card covers Cochrane Handbook Chapter 9 specifically, not the whole Handbook.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: The canonical Markdown title, breadcrumb, and citation all identify Chapter 9 and its chapter-level scope.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:1-3,70-84,128; section_ids=cochrane_ch09__canonical_chapter_09__s0001_cochrane_handbook_chapter_9_summarizing_study_characteristics_and_preparing_for_, cochrane_ch09__canonical_chapter_09__s0003_breadcrumb
- claim: Chapter 9 defines synthesis as bringing together data from included studies and includes synthesis of study characteristics, with possible statistical synthesis of findings.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: Use this for high-level Chapter 9 scope, then open later Chapter 9 sections for step-specific guidance.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:118-126,130-144; section_ids=cochrane_ch09__canonical_chapter_09__s0006_key_points, cochrane_ch09__canonical_chapter_09__s0007_9_1_introduction
- claim: Chapter 9's preparation stage includes summarizing each study, comparing whether studies are similar enough to group, determining data availability, considering changes to planned comparisons or outcomes, and synthesizing study characteristics for each comparison.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: This supports routing to Chapter 9 for pre-synthesis comparison setup and study-characteristic work.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:146-176; section_id=cochrane_ch09__canonical_chapter_09__s0008_9_2_a_general_framework_for_synthesis
- claim: Chapter 9 recommends tabulating study characteristics to compare PICO elements, support grouping decisions, and make subjective grouping decisions more transparent.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: Use this for structured study-characteristic tables, not for final effect-synthesis methods.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:176,233-241,318-322; section_ids=cochrane_ch09__canonical_chapter_09__s0011_9_3_2_determine_which_studies_are_similar_enough_to_be_grouped_within_each_compa, cochrane_ch09__canonical_chapter_09__s0014_9_3_5_synthesize_the_characteristics_of_the_studies_contributing_to_each_compari
- claim: Chapter 9 discusses checking what data are available for synthesis, including multiplicity and pre-specified decision rules for selecting outcomes.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: Use this when the task concerns outcome selection or whether enough data exist for a planned synthesis.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:296-312; section_id=cochrane_ch09__canonical_chapter_09__s0012_9_3_3_determine_what_data_are_available_for_synthesis_step_2_3
- claim: Chapter 9 points readers to Chapter 12 for other statistical synthesis methods and structured presentation when meta-analysis is not possible.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md
  support_type: direct
  verification_note: Route method claims about non-meta-analytic synthesis to `cochrane_ch12` after using Chapter 9 for preparation logic.
  quote_or_locator: references/canonical_sources/md/cochrane_ch09/canonical_chapter-09.md:330-332; section_id=cochrane_ch09__canonical_chapter_09__s0016_9_5_types_of_synthesis
```

## Operational rules

- Route to `cochrane_ch09` when the task is about preparing included studies for synthesis, especially grouping by PICO, study-characteristic tables, multiplicity, or data-availability checks.
- Keep this source chapter-specific. For whole-Handbook scope, use `cochrane_handbook`; for non-meta-analytic synthesis methods, use `cochrane_ch12`.
- Cite the canonical Chapter 9 Markdown for final claims; this card is only a router and source briefing.
- Preserve the Cochrane intervention-review context when adapting Chapter 9 ideas to broader survey-writing work.

## Common misuses

- Treating Chapter 9 as a full narrative-synthesis guide.
- Using Chapter 9 to justify a specific non-meta-analytic synthesis method when Chapter 12 is the better source.
- Applying Chapter 9's table and grouping advice to non-systematic literature surveys without labeling the adaptation.
- Making whole-Handbook claims from this chapter-specific card.

## Evidence limits

The local capture is a single Cochrane Handbook chapter. It supports claims about Chapter 9's preparation-for-synthesis guidance, not detailed meta-analysis, GRADE, risk-of-bias, or reporting-checklist requirements.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cochrane_ch09`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=cochrane_ch09`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=cochrane_ch09`.
- Section locators: `references/corpus_index/sections/by_source/cochrane_ch09.jsonl`.

## Unresolved gaps

- The local card does not recapture or compare current live Cochrane text after 2026-05-04.
- Chapter 9 examples are health/intervention-review examples; non-health survey uses require explicit adaptation.
