# GRADE Working Group Source Card v2

```yaml
source_id: grade_working_group
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/grade_working_group/canonical.md
  - references/canonical_sources/md/grade_working_group/linked_1_criteria_for_using_grade_2016-04-05.pdf.md
  - references/canonical_sources/md/grade_working_group/linked_2_grade-working-group-newsletter-202409.pdf.md
canonical_urls:
  - https://www.gradeworkinggroup.org/
  - https://www.gradeworkinggroup.org/docs/Criteria_for_using_GRADE_2016-04-05.pdf
authority_level: canonical_certainty_framework
version_or_access_date: "minimal requirements updated 2023-05; local corpus fetched 2026-05-05"
applies_to:
  - GRADE certainty or quality of evidence
  - GRADE evidence profiles and summary of findings routing
  - GRADE evidence-to-decision and recommendation logic
  - current source-of-truth routing for GRADE family materials
not_for:
  - AMSTAR 2 or ROBIS appraisal of systematic reviews
  - primary-study risk-of-bias assessment
  - qualitative synthesis confidence without CERQual routing
  - making recommendations without systematic review or evidence-synthesis support
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate; the working group page includes minimal requirements updated 2023-05, while linked resources and GRADE Book/handbook materials may update separately.
reuse_or_license_risk: Official site and linked resource terms apply; verify terms before redistributing substantial excerpts or mirrored files.
qa_status: seed_verified_with_local_locators_and_dropbox_pdf_repair
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The GRADE Working Group developed a common, transparent approach to grading quality or certainty of evidence and strength of recommendations.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
  support_type: direct
  verification_note: Use the "What is GRADE?" section for the top-level GRADE role.
  quote_or_locator: canonical.md:31-35,47; section_id=grade_working_group__canonical__s0004_what_is_grade
- claim: GRADE certainty in evidence is also called quality of evidence or confidence in estimates, and GRADE defines it around whether the true effect, accuracy measure, or association lies on one side of a threshold or in a range.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
  support_type: direct
  verification_note: Use the 2023-05 minimal requirements before making terminology claims about certainty, quality, or confidence.
  quote_or_locator: canonical.md:65-67; section_id=grade_working_group__canonical__s0004_what_is_grade
- claim: Using GRADE requires explicit consideration of GRADE certainty domains and outcome-level certainty categories such as high, moderate, low, and very low.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
    - references/canonical_sources/md/grade_working_group/linked_1_criteria_for_using_grade_2016-04-05.pdf.md
  support_type: direct
  verification_note: Use the official minimal requirements and criteria document for claims about correct GRADE use.
  quote_or_locator: canonical.md:69-71; section_id=grade_working_group__canonical__s0004_what_is_grade; linked_1_criteria_for_using_grade_2016-04-05.pdf.md:29-35; section_id=grade_working_group__linked_1_criteria_for_using_grade_2016_04_05_pdf__s0002_page_1
- claim: GRADE evidence tables, including evidence profiles or summary of findings tables, should present evidence synthesis results and certainty assessments and should be based on systematic reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
    - references/canonical_sources/md/grade_working_group/linked_1_criteria_for_using_grade_2016-04-05.pdf.md
  support_type: direct
  verification_note: Use this requirement when deciding whether GRADE evidence has enough provenance.
  quote_or_locator: canonical.md:73; section_id=grade_working_group__canonical__s0004_what_is_grade; linked_1_criteria_for_using_grade_2016-04-05.pdf.md:36-40; section_id=grade_working_group__linked_1_criteria_for_using_grade_2016_04_05_pdf__s0002_page_1
- claim: GRADE separates evidence certainty from recommendation decisions; additional Evidence to Decision criteria apply when making recommendations or decisions.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
  support_type: direct
  verification_note: Do not treat certainty grading alone as a complete recommendation.
  quote_or_locator: canonical.md:75-81; section_id=grade_working_group__canonical__s0004_what_is_grade
- claim: The GRADE Working Group discourages modified GRADE approaches that differ from the working group's approach.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_working_group/canonical.md
    - references/canonical_sources/md/grade_working_group/linked_1_criteria_for_using_grade_2016-04-05.pdf.md
  support_type: direct
  verification_note: Use this when evaluating claims that a source used a nonstandard or locally modified GRADE method.
  quote_or_locator: canonical.md:59-63; section_id=grade_working_group__canonical__s0004_what_is_grade; linked_1_criteria_for_using_grade_2016-04-05.pdf.md:16-23; section_id=grade_working_group__linked_1_criteria_for_using_grade_2016_04_05_pdf__s0002_page_1
```

## Operational rules

- Use `grade_working_group` for current GRADE-family authority, minimal requirements, terminology, and source routing.
- Use `grade_handbook` for detailed operational steps in applying GRADE to systematic reviews, HTAs, and guidelines.
- Use `grade_cerqual` for confidence in findings from qualitative evidence syntheses.
- Do not use GRADE sources to appraise the methodological quality or risk of bias of a systematic review; route those to `amstar2` or `robis`.

## Common misuses

- Calling a locally modified grading method "GRADE" without checking the working group's minimal requirements.
- Treating certainty of evidence as the same thing as strength or direction of a recommendation.
- Treating GRADE as a review-quality appraisal tool.
- Using GRADE Working Group pages alone when detailed handbook application rules are needed.

## Evidence limits

This card is a router aid. Final claims about the GRADE approach must cite the official GRADE Working Group Markdown or specific linked GRADE resources directly. Source manifests, route registries, section indexes, and this card are locator-only for substantive claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=grade_working_group`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=grade_working_group`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=grade_working_group`.
- Optional local section locators: `references/corpus_index/sections/by_source/grade_working_group.jsonl`.
- Linked newsletter capture: `linked_2_grade-working-group-newsletter-202409.pdf.md` was recaptured from the Dropbox `dl=1` route after the original `dl=0` local capture was found to be an HTML preview, not a PDF.

## Unresolved gaps

- The official site points to GRADE Book and GRADEpro resources that may be newer than the captured handbook material.
