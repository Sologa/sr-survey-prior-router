# Computational Linguistics Journal Source Card v2

```yaml
source_id: computational_linguistics
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/computational_linguistics/official_ojs_journal_home_cljournal.md
  - references/canonical_sources/md/computational_linguistics/official_ojs_submission_guidelines_submissions.md
  - references/canonical_sources/md/computational_linguistics/official_ojs_original_submission_checklist_originalsubmissionchecklist.md
  - references/canonical_sources/md/computational_linguistics/official_ojs_revision_final_checklist_resubmissionsandfinalaccepts.md
  - references/canonical_sources/md/computational_linguistics/official_ojs_style_guide_styleguide.md
  - references/canonical_sources/md/computational_linguistics/official_style_manual_pdf_coli_manual.pdf.md
  - references/canonical_sources/md/computational_linguistics/official_style_template_pdf_coli_template.pdf.md
  - references/canonical_sources/md/computational_linguistics/official_style_file_cls_clv2025.cls.md
canonical_urls:
  - https://submissions.cljournal.org/index.php/cljournal
  - https://submissions.cljournal.org/index.php/cljournal/about/submissions
authority_level: canonical_venue_policy
version_or_access_date: "checked 2026-05-04; style-file references updated 2025-01-01 in local capture"
applies_to:
  - Computational Linguistics journal scope and submission categories
  - CL/NLP survey article venue expectations
  - CL journal formatting and submission checklist routing
not_for:
  - universal survey methodology standards
  - systematic review conduct rules
  - ACL conference or TACL policy without separate verification
  - corpus API behavior
route_relevance:
  - survey_writing_prior
  - source_audit
  - evidence_grounding
  - synthesis_writing
freshness_risk: high because journal policy, editor information, deadlines, style files, and article categories can change.
reuse_or_license_risk: local pages describe open access and ACL copyright in some places, but reuse must be checked against the specific article and current journal terms.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Computational Linguistics is described as the official flagship journal of ACL and a venue for computational linguistics, NLP, and related computational study of language.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_journal_home_cljournal.md
  support_type: direct
  verification_note: Use this for venue identity and scope, not methodology authority.
  quote_or_locator: official_ojs_journal_home_cljournal.md:30-40
- claim: The journal accepts multiple submission categories, including Survey Articles, and asks authors to indicate article type.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Use this for CL venue category routing.
  quote_or_locator: official_ojs_submission_guidelines_submissions.md:54-57
- claim: The captured CL guidance welcomes survey articles that offer comprehensive, insightful overviews and serve as entry points and references for CL/NLP researchers.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_submission_guidelines_submissions.md
  support_type: direct
  verification_note: This is a CL journal norm for CL/NLP surveys, not a universal survey standard.
  quote_or_locator: official_ojs_submission_guidelines_submissions.md:76-90
- claim: CL survey proposals should include an outline up to 5 pages, author biographies, three expert reviewer names, and a citation-rich description of the body of work.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Verify current proposal requirements before live submission.
  quote_or_locator: official_ojs_submission_guidelines_submissions.md:92-104
- claim: CL original submissions use a single-blind review process and require author names and affiliations on the first page.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_original_submission_checklist_originalsubmissionchecklist.md
  support_type: direct
  verification_note: Do not apply this to TACL or ACL conference submissions.
  quote_or_locator: official_ojs_original_submission_checklist_originalsubmissionchecklist.md:48-56
- claim: CL articles are typeset using LaTeX and the journal style-file page points to current CL LaTeX macros and related files in the local capture.
  supporting_canonical_paths:
    - references/canonical_sources/md/computational_linguistics/official_ojs_style_guide_styleguide.md
  support_type: direct
  verification_note: Check the live style page before final formatting.
  quote_or_locator: official_ojs_style_guide_styleguide.md:40-56
```

## Operational rules

- Use this card for Computational Linguistics journal scope, survey article expectations, proposal requirements, and CL-specific formatting.
- Keep CL survey guidance scoped to CL/NLP journal publishing norms.
- Route TACL questions to `tacl_submission` and ACL conference formatting to `aclpub_formatting`.
- Cite canonical CL pages or the live journal site for final answers.

## Common misuses

- Treating CL's survey article guidance as a general methodology standard for all surveys.
- Confusing CL single-blind review with TACL double-blind review or ACL conference anonymity.
- Applying CL page limits or style files to other venues.
- Treating current issue and editor details as stable without rechecking.

## Evidence limits

The local capture contains journal pages, checklists, style files, and converted PDFs. It does not include a complete set of accepted survey examples or a current live policy check beyond the captured date.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=computational_linguistics`.
- Canonical Markdown directory: `references/canonical_sources/md/computational_linguistics/`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=computational_linguistics`.
- Optional local section locators: `references/corpus_index/sections/by_source/computational_linguistics.jsonl`.

## Unresolved gaps

- Current editorial team, deadlines, and style-file versions should be rechecked live before operational submission advice.
- This card does not analyze accepted CL survey articles as exemplars.
