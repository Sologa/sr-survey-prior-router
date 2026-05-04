# Cochrane Chapter 12 Source Card v2

```yaml
source_id: cochrane_ch12
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
canonical_urls:
  - https://training.cochrane.org/handbook/current/chapter-12
authority_level: canonical_conduct_manual
version_or_access_date: "Handbook version 6.5, 2024; chapter last updated October 2019; local corpus fetched 2026-05-04"
applies_to:
  - chapter-specific routing for synthesis and presentation when meta-analysis of effect estimates is not possible
  - acceptable and unacceptable non-meta-analytic synthesis methods in Cochrane intervention reviews
  - structured tabulation and visual presentation of review findings without meta-analysis
  - caution around unspecified narrative summaries and vote counting
not_for:
  - whole-Handbook claims outside Chapter 12
  - preliminary grouping and study-characteristic preparation covered by Chapter 9
  - generic narrative-review or state-of-art review writing methods
  - qualitative evidence synthesis or realist/meta-narrative standards
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
- claim: This card covers Cochrane Handbook Chapter 12 specifically, not the whole Handbook.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: The canonical Markdown title, breadcrumb, table of contents, and citation all identify Chapter 12 and its chapter-level scope.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:1-3,70-84,90-120,138; section_ids=cochrane_ch12__canonical_chapter_12__s0001_cochrane_handbook_chapter_12_synthesizing_and_presenting_findings_using_other_me, cochrane_ch12__canonical_chapter_12__s0005_table_of_contents
- claim: Chapter 12 addresses cases where meta-analysis of effect estimates is not possible and other synthesis methods may need to be considered.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: Use Chapter 12 after checking the pre-synthesis setup in Chapter 9 when needed.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:124-136,140-184; section_ids=cochrane_ch12__canonical_chapter_12__s0006_key_points, cochrane_ch12__canonical_chapter_12__s0008_12_2_statistical_synthesis_when_meta_analysis_of_effect_estimates_is_not_possibl
- claim: Chapter 12 says authors should report the specific methods used instead of merely saying they conducted a narrative synthesis or narrative summary.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: This is a direct support point for discouraging vague synthesis labels in Cochrane-style review writing.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:186-190; section_id=cochrane_ch12__canonical_chapter_12__s0008_12_2_statistical_synthesis_when_meta_analysis_of_effect_estimates_is_not_possibl
- claim: Chapter 12 treats summarizing effect estimates, combining P values, and vote counting based on direction of effect as acceptable alternatives in specified data circumstances, but each has limitations.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: Cite the relevant subsection for the exact method and data requirements.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:192-271,272-316; section_ids=cochrane_ch12__canonical_chapter_12__s0008_12_2_statistical_synthesis_when_meta_analysis_of_effect_estimates_is_not_possibl, cochrane_ch12__canonical_chapter_12__s0010_12_2_1_1_summarizing_effect_estimates, cochrane_ch12__canonical_chapter_12__s0011_12_2_1_2_combining_p_values, cochrane_ch12__canonical_chapter_12__s0012_12_2_1_3_vote_counting_based_on_the_direction_of_effect
- claim: Chapter 12 says vote counting based on statistical significance has serious limitations and is unacceptable.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: Use this for warning against conventional significance-based vote counting, not against all direction-based synthesis.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:136,318-324; section_id=cochrane_ch12__canonical_chapter_12__s0014_12_2_2_1_vote_counting_based_on_statistical_significance
- claim: Chapter 12 emphasizes tabulation and visual display for transparent reporting in reviews without meta-analysis.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md
  support_type: direct
  verification_note: Use the structured tabulation and visual display sections for presentation claims.
  quote_or_locator: references/canonical_sources/md/cochrane_ch12/canonical_chapter-12.md:132-134,332-338,358-380; section_ids=cochrane_ch12__canonical_chapter_12__s0016_12_3_visual_display_and_presentation_of_the_data, cochrane_ch12__canonical_chapter_12__s0017_12_3_1_structured_tabulation_of_results_across_studies
```

## Operational rules

- Route to `cochrane_ch12` for questions about synthesis and presentation when a meta-analysis of effect estimates is not possible.
- Use `cochrane_ch09` first when the question is about whether studies are similar enough, how PICO elements are grouped, or what data are available.
- Do not reduce Chapter 12 to "narrative synthesis"; it expects specific method naming, limitations, and cautious conclusions.
- For vote counting, distinguish direction-of-effect methods from statistical-significance or subjective-rule vote counting.

## Common misuses

- Treating Chapter 12 as a generic narrative-review writing guide.
- Citing Chapter 12 for whole-Handbook or Cochrane organizational requirements.
- Using "no meta-analysis" as permission for unstructured study-by-study prose.
- Treating harvest/effect-direction plots as automatically valid when the underlying categorization rule is unsupported.

## Evidence limits

The local capture is a single Cochrane Handbook chapter. It supports Chapter 12 claims about non-meta-analytic synthesis and presentation in intervention reviews, but not qualitative synthesis, scoping-review standards, or ordinary narrative literature reviews.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cochrane_ch12`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=cochrane_ch12`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=cochrane_ch12`.
- Section locators: `references/corpus_index/sections/by_source/cochrane_ch12.jsonl`.

## Unresolved gaps

- The local card does not recapture or compare current live Cochrane text after 2026-05-04.
- Chapter 12 remains health/intervention-review guidance; transfer to general survey writing requires explicit adaptation.
