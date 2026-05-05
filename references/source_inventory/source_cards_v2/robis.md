# ROBIS Source Card v2

```yaml
source_id: robis
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  - references/canonical_sources/md/robis/extra_1_robisguidancedocument.pdf.md
canonical_urls:
  - https://www.bristol.ac.uk/media-library/sites/social-community-medicine/robis/robisjclinepi.pdf
  - https://www.bristol.ac.uk/media-library/sites/social-community-medicine/robis/robisguidancedocument.pdf
authority_level: canonical_appraisal_tool
version_or_access_date: "ROBIS article 2016; guidance document local corpus fetched 2026-05-04"
applies_to:
  - risk of bias in systematic reviews
  - overviews of systematic reviews
  - review-level bias assessment for guideline development
not_for:
  - primary-study risk-of-bias assessment
  - broad methodological quality scoring of reviews
  - AMSTAR 2-style broad quality appraisal
  - certainty grading of bodies of quantitative evidence
  - reporting guideline compliance
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for the 2016 ROBIS article and captured guidance; verify the current host page if download URLs or guidance files have changed.
reuse_or_license_risk: The article states CC BY for the JCE article; verify Bristol-hosted guidance document terms before mirroring or redistributing substantial excerpts.
qa_status: seed_verified_by_worker_c_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: ROBIS is a tool for assessing risk of bias in systematic reviews rather than in primary studies.
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  support_type: direct
  verification_note: Use the article abstract/title for the review-level scope.
  quote_or_locator: canonical_robisjclinepi.pdf.md:10,25,37,195-197; section_ids=robis__canonical_robisjclinepi_pdf__s0002_page_1, robis__canonical_robisjclinepi_pdf__s0003_page_2
- claim: ROBIS distinguishes bias in the review from bias in included primary studies, and a review can be low risk of bias if it appropriately assesses and considers primary-study bias.
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  support_type: direct
  verification_note: Use the development/scope section before equating ROBIS with primary-study appraisal.
  quote_or_locator: canonical_robisjclinepi.pdf.md:134-153; section_id=robis__canonical_robisjclinepi_pdf__s0003_page_2
- claim: ROBIS is aimed at systematic reviews in health care settings covering interventions, diagnosis, prognosis, and etiology, with target users including guideline developers, overview authors, and review authors.
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  support_type: direct
  verification_note: Check the target categories before applying ROBIS outside its intended review types.
  quote_or_locator: canonical_robisjclinepi.pdf.md:28-30,155-167,199-208; section_ids=robis__canonical_robisjclinepi_pdf__s0002_page_1, robis__canonical_robisjclinepi_pdf__s0003_page_2
- claim: "ROBIS is completed in three phases: optional relevance assessment, identifying concerns with the review process, and judging risk of bias in the review."
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  support_type: direct
  verification_note: Use phase structure from the article or guidance before designing an assessment workflow.
  quote_or_locator: canonical_robisjclinepi.pdf.md:30-36,209-220,357-365; section_ids=robis__canonical_robisjclinepi_pdf__s0002_page_1, robis__canonical_robisjclinepi_pdf__s0003_page_2, robis__canonical_robisjclinepi_pdf__s0005_page_4
- claim: Phase 2 covers four review-process domains, and Phase 3 considers whether the systematic review as a whole is at risk of bias.
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
    - references/canonical_sources/md/robis/extra_1_robisguidancedocument.pdf.md
  support_type: direct
  verification_note: Use the article for the compact domain list and the guidance document for implementation details.
  quote_or_locator: canonical_robisjclinepi.pdf.md:440-470,630-647; section_ids=robis__canonical_robisjclinepi_pdf__s0006_page_5, robis__canonical_robisjclinepi_pdf__s0007_page_6, robis__canonical_robisjclinepi_pdf__s0008_page_7; extra_1_robisguidancedocument.pdf.md:1720-1731; section_id=robis__extra_1_robisguidancedocument_pdf__s0031_page_30
- claim: ROBIS should not be used to generate a summary quality score.
  supporting_canonical_paths:
    - references/canonical_sources/md/robis/canonical_robisjclinepi.pdf.md
  support_type: direct
  verification_note: Preserve the risk-of-bias judgment boundary when presenting ROBIS results.
  quote_or_locator: canonical_robisjclinepi.pdf.md:648-671; section_id=robis__canonical_robisjclinepi_pdf__s0008_page_7
```

## Operational rules

- Use `robis` when the task asks whether a systematic review is at risk of bias.
- Keep ROBIS separate from primary-study bias tools such as RoB 2 or ROBINS-I.
- Present ROBIS judgments by phase/domain and overall review-level risk of bias, not as a numerical quality score.
- Route broad review-quality appraisal questions to `amstar2` when the user is not specifically asking about review-level bias.

## Common misuses

- Using ROBIS as a primary-study bias tool.
- Treating ROBIS as a general review-quality or reporting-quality score.
- Skipping Phase 2 domain reasoning and reporting only a final label.
- Treating the optional relevance assessment as evidence of review bias by itself.

## Evidence limits

This card is a router aid. Final claims about ROBIS must cite the ROBIS article or guidance Markdown directly. Source manifests, route registries, section indexes, and this card are locator-only for substantive claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=robis`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=robis`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=robis`.
- Optional local section locators: `references/corpus_index/sections/by_source/robis.jsonl`.

## Unresolved gaps

- The local capture does not include a current ROBIS website page beyond the Bristol-hosted article and guidance PDFs.
- Original PDF layout should be checked if exact form fields, figures, or assessment templates matter.
