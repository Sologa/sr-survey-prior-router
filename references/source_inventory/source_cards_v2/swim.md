# SWiM Source Card v2

```yaml
source_id: swim
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md
  - references/canonical_sources/md/swim/linked_1_synthesis-without-meta-analysis-swim-checklist.docx.md
  - references/canonical_sources/md/swim/linked_2_synthesis-without-meta-analysis-swim-checklist.pdf.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline/
  - https://www.equator-network.org/wp-content/uploads/2020/01/Synthesis-without-Meta-analysis-SWiM-Checklist.docx
  - https://www.equator-network.org/wp-content/uploads/2020/01/Synthesis-without-Meta-analysis-SWiM-Checklist.pdf
authority_level: canonical_reporting_guideline
version_or_access_date: "BMJ 2020; EQUATOR record last updated 2021-11-19; local corpus fetched 2026-05-04"
applies_to:
  - reporting synthesis without meta-analysis in systematic reviews of interventions
  - PRISMA-extension routing for non-meta-analytic synthesis reporting
  - methods, results, and discussion reporting checks for SWiM items
not_for:
  - deciding whether a meta-analysis is statistically appropriate
  - search strategy design, screening, or eligibility criteria
  - qualitative evidence synthesis reporting
  - ordinary narrative reviews or taxonomy-driven field surveys without systematic-review synthesis
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for the 2020 reporting guideline and 2021 EQUATOR record metadata; verify newer extensions or website templates before layout-sensitive reuse.
reuse_or_license_risk: EQUATOR page and linked checklist terms apply; verify source-specific license before redistributing substantial checklist excerpts or converted files.
qa_status: worker_d_verified_against_local_canonical_markdown
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: SWiM is a reporting guideline for synthesis without meta-analysis in systematic reviews of interventions.
  supporting_canonical_paths:
    - references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md
  support_type: direct
  verification_note: Use the EQUATOR record for source identity and scope, then open the linked checklist for item wording.
  quote_or_locator: references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md:53-57; section_id=swim__canonical_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline__s0003_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline
- claim: The EQUATOR record links both Word and PDF SWiM checklist files and gives the BMJ 2020 bibliographic reference.
  supporting_canonical_paths:
    - references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md
  support_type: direct
  verification_note: Use the linked local checklist Markdown for checklist-item support rather than relying only on the registry page.
  quote_or_locator: references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md:59-61; section_id=swim__canonical_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline__s0003_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline
- claim: The captured checklist says SWiM is intended to complement and be used as an extension to PRISMA.
  supporting_canonical_paths:
    - references/canonical_sources/md/swim/linked_1_synthesis-without-meta-analysis-swim-checklist.docx.md
    - references/canonical_sources/md/swim/linked_2_synthesis-without-meta-analysis-swim-checklist.pdf.md
  support_type: direct
  verification_note: Prefer the DOCX conversion for compact table text; use the PDF conversion when page-level locators matter.
  quote_or_locator: references/canonical_sources/md/swim/linked_1_synthesis-without-meta-analysis-swim-checklist.docx.md:14; references/canonical_sources/md/swim/linked_2_synthesis-without-meta-analysis-swim-checklist.pdf.md:15; section_ids=swim__linked_1_synthesis_without_meta_analysis_swim_checklist_docx__s0002_table_1, swim__linked_2_synthesis_without_meta_analysis_swim_checklist_pdf__s0002_page_1
- claim: The local checklist capture provides nine SWiM reporting items spanning methods, results, and discussion.
  supporting_canonical_paths:
    - references/canonical_sources/md/swim/linked_1_synthesis-without-meta-analysis-swim-checklist.docx.md
    - references/canonical_sources/md/swim/linked_2_synthesis-without-meta-analysis-swim-checklist.pdf.md
  support_type: direct
  verification_note: Item-level claims are allowed for SWiM because local checklist Markdown exists; quote exact item text from the checklist, not from this card.
  quote_or_locator: references/canonical_sources/md/swim/linked_1_synthesis-without-meta-analysis-swim-checklist.docx.md:16-30; references/canonical_sources/md/swim/linked_2_synthesis-without-meta-analysis-swim-checklist.pdf.md:22-59,73-112; section_ids=swim__linked_1_synthesis_without_meta_analysis_swim_checklist_docx__s0002_table_1, swim__linked_2_synthesis_without_meta_analysis_swim_checklist_pdf__s0002_page_1, swim__linked_2_synthesis_without_meta_analysis_swim_checklist_pdf__s0003_page_2
- claim: The EQUATOR record classifies SWiM as applying to narrative sections, procedure/method, and results.
  supporting_canonical_paths:
    - references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md
  support_type: direct
  verification_note: Use this for routing within report sections, not as a license to apply SWiM outside systematic-review synthesis.
  quote_or_locator: references/canonical_sources/md/swim/canonical_synthesis-without-meta-analysis-swim-in-systematic-reviews-reporting-guideline.md:77-79; section_id=swim__canonical_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline__s0003_synthesis_without_meta_analysis_swim_in_systematic_reviews_reporting_guideline
```

## Operational rules

- Route to SWiM when the task concerns reporting a systematic-review synthesis that does not use meta-analysis.
- For item-level reporting checks, open the local Word or PDF checklist conversion and cite the exact item lines.
- Pair SWiM with PRISMA only as a reporting extension; do not use it as a standalone conduct manual.
- Keep qualitative-synthesis, realist-synthesis, and meta-narrative questions on their own source IDs unless the task explicitly combines methods.

## Common misuses

- Treating SWiM as a method for deciding whether meta-analysis is possible.
- Applying SWiM to broad literature surveys that do not report a systematic-review synthesis.
- Citing the EQUATOR registry page for checklist item wording when the local checklist files are available.

## Evidence limits

This card is a router aid. Final answers should cite the canonical EQUATOR page or the linked checklist Markdown. The EQUATOR page supports identity, scope, links, study design, and applicability metadata; the linked checklist supports item-level SWiM reporting claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=swim`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=swim`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=swim`.
- Optional local section locators: `references/corpus_index/sections/by_source/swim.jsonl`.

## Unresolved gaps

- The BMJ explanation-and-elaboration article is linked from the EQUATOR record but is not represented here as a separate local full-text source; use only the captured EQUATOR/checklist Markdown unless that article is added and verified.
