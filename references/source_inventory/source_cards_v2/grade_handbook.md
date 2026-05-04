# GRADE Handbook Source Card v2

```yaml
source_id: grade_handbook
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  - references/canonical_sources/md/grade_handbook/official_gradepro_etd_overview_204000076798-etd-overview.md
  - references/canonical_sources/md/grade_handbook/official_gradepro_exporting_tables_204000077184-exporting-tables.md
canonical_urls:
  - https://gdt.gradepro.org/app/handbook/handbook.html
  - https://help.gradepro.org/support/solutions/articles/204000076798-etd-overview
  - https://help.gradepro.org/support/solutions/articles/204000077184-exporting-tables
authority_level: canonical_certainty_framework
version_or_access_date: "GRADE handbook updated October 2013; local corpus partial fetched 2026-05-04"
applies_to:
  - operational application of GRADE in systematic reviews
  - GRADE quality or certainty of evidence for quantitative effect estimates
  - evidence profiles and summary of findings tables
  - GRADE evidence-to-decision workflow for guideline panels
not_for:
  - AMSTAR 2 or ROBIS review appraisal
  - primary-study risk-of-bias assessment
  - qualitative synthesis confidence without CERQual routing
  - assuming all newer GRADE refinements are captured in the 2013 handbook
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate to high; the captured handbook says updated October 2013 and includes notices that sections have newer GRADE Book updates.
reuse_or_license_risk: Handbook permission text says reproduction or translation permission should be sought from the editors; verify terms before redistributing substantial excerpts or derived layouts.
qa_status: seed_verified_by_worker_c_with_local_locators_partial_bundle
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: The GRADE handbook is a handbook for grading quality of evidence and strength of recommendations using the GRADE approach, updated October 2013.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use the handbook title/introduction for version and scope claims.
  quote_or_locator: canonical_handbook.html.md:1-12; section_id=grade_handbook__canonical_handbook_html__s0001_grade_handbook
- claim: The handbook is intended as a guide for producing GRADE outputs, including evidence summaries and graded recommendations, for systematic review and HTA authors, guideline panelists, and methodologists.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use the handbook introduction before assigning target users or outputs.
  quote_or_locator: canonical_handbook.html.md:184-186; section_id=grade_handbook__canonical_handbook_html__s0001_grade_handbook
- claim: For systematic review authors, GRADE use typically terminates after rating quality of evidence for outcomes and presenting results in a GRADE Evidence Profile or Summary of Findings table; systematic reviews should typically not include health care recommendations.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Preserve the systematic-review versus guideline-panel boundary when using the handbook.
  quote_or_locator: canonical_handbook.html.md:248-250; section_id=grade_handbook__canonical_handbook_html__s0002_1_overview_of_the_grade_approach
- claim: In systematic reviews, GRADE quality of evidence reflects confidence that an estimate of effect is correct and is rated separately for each patient-important outcome.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use the Section 5 systematic-review definition for quantitative effect-certainty claims.
  quote_or_locator: canonical_handbook.html.md:630-636,3005-3007; section_ids=grade_handbook__canonical_handbook_html__s0021_5_quality_of_evidence, grade_handbook__canonical_handbook_html__s0080_9_glossary_of_terms_and_concepts
- claim: The GRADE approach grades quality of evidence as high, moderate, low, or very low.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use the quality-of-evidence table for exact category definitions.
  quote_or_locator: canonical_handbook.html.md:642-666; section_id=grade_handbook__canonical_handbook_html__s0021_5_quality_of_evidence
- claim: GRADE rating begins with study design, considers five reasons to rate down and three reasons to rate up, and requires transparent judgment rather than a purely quantitative scoring system.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use Section 5.1 for downgrading/upgrading factors and judgment transparency.
  quote_or_locator: canonical_handbook.html.md:668-722; section_id=grade_handbook__canonical_handbook_html__s0022_5_1_factors_determining_the_quality_of_evidence
- claim: GRADE evidence profiles and Summary of Findings tables present evidence synthesis results, quality ratings, and effect information by outcome.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/canonical_handbook.html.md
  support_type: direct
  verification_note: Use Chapter 4 table sections before generating or auditing GRADE evidence table content.
  quote_or_locator: canonical_handbook.html.md:548-586,590-608; section_ids=grade_handbook__canonical_handbook_html__s0019_4_2_grade_evidence_profile, grade_handbook__canonical_handbook_html__s0020_4_3_summary_of_findings_table
- claim: Evidence to Decision tables help guideline panels develop evidence-informed recommendations and include criteria such as desirable and undesirable effects, certainty of evidence of effects, resources, acceptability, feasibility, and equity.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_handbook/official_gradepro_etd_overview_204000076798-etd-overview.md
  support_type: direct
  verification_note: Use the GradePro EtD overview only for EtD workflow and table-structure claims.
  quote_or_locator: official_gradepro_etd_overview_204000076798-etd-overview.md:253-255,287-303,309-315; section_ids=grade_handbook__official_gradepro_etd_overview_204000076798_etd_overview__s0004_1_what_is_an_etd_table, grade_handbook__official_gradepro_etd_overview_204000076798_etd_overview__s0007_3_1_assessment, grade_handbook__official_gradepro_etd_overview_204000076798_etd_overview__s0009_3_3_type_of_recommendation
```

## Operational rules

- Use `grade_handbook` for detailed GRADE application to quantitative evidence/effect certainty, evidence profiles, Summary of Findings tables, and guideline-panel EtD workflow.
- Use `grade_working_group` first when the question is about current GRADE authority, minimal requirements, or whether a method can be called GRADE.
- Use `grade_cerqual` for confidence in qualitative evidence synthesis findings.
- Do not use the handbook as an AMSTAR 2 or ROBIS substitute for review appraisal.
- Treat this local bundle as partial and version-sensitive because the captured handbook points to newer GRADE Book updates.

## Common misuses

- Treating GRADE certainty ratings as a review-quality score.
- Treating a systematic review's GRADE certainty assessment as a healthcare recommendation.
- Applying quantitative-effect GRADE rules to qualitative synthesis confidence instead of using CERQual.
- Assuming the 2013 handbook alone captures all current GRADE guidance.

## Evidence limits

This card is a router aid. Final claims about GRADE handbook rules must cite the handbook or GradePro Markdown directly. Source manifests, route registries, section indexes, and this card are locator-only for substantive claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=grade_handbook`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=grade_handbook`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=grade_handbook`.
- Optional local section locators: `references/corpus_index/sections/by_source/grade_handbook.jsonl`.

## Unresolved gaps

- The bundle is marked partial in the local corpus index and has failed linked Example EtD PDF downloads in the download manifest.
- Several handbook sections point to newer GRADE Book updates; verify the current GRADE Book for up-to-date operational guidance when freshness matters.
- Original table/figure layout is not preserved in Markdown; inspect raw or live sources for exact table formatting.
