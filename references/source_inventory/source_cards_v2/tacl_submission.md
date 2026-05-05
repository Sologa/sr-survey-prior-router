# TACL Submission Guidelines Source Card v2

```yaml
source_id: tacl_submission
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  - references/canonical_sources/md/tacl_submission/official_transacl_submission_formatting_pdf_tacl2021v1-submission-formatting-instructions.pdf.md
  - references/canonical_sources/md/tacl_submission/official_transacl_finalversion_formatting_pdf_tacl2021v1-finalversion-formatting-instructions.pdf.md
  - references/canonical_sources/md/tacl_submission/official_transacl_style_file_tacl2021v1.sty.md
  - references/canonical_sources/md/tacl_submission/official_transacl_template_tex_tacl2021v1-template.tex.md
  - references/canonical_sources/md/tacl_submission/official_transacl_bibliography_style_acl_natbib.bst.md
canonical_urls:
  - https://transacl.org/index.php/tacl/about/submissions
blocked_primary_urls:
  - https://direct.mit.edu/tacl/pages/submission-guidelines
authority_level: canonical_venue_policy
version_or_access_date: "checked 2026-05-04; MIT Press primary locator 403 and official TransACL fallback verified 2026-05-05"
applies_to:
  - TACL submission policies
  - TACL formatting and final-version preparation
  - TACL-specific treatment of survey papers
  - NLP journal venue norms
not_for:
  - universal survey methodology standards
  - ACL conference formatting outside TACL
  - systematic review reporting or conduct rules
  - corpus access or metadata API behavior
route_relevance:
  - survey_writing_prior
  - source_audit
  - evidence_grounding
  - synthesis_writing
freshness_risk: high because submission deadlines, policies, templates, and eligibility rules can change.
reuse_or_license_risk: TACL papers are described as ACL copyright with CC-BY distribution, but older volumes have caveats; verify the specific paper and page before reuse.
qa_status: primary_locator_blocked_403_official_fallback_captured
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: TACL requires complete information for all primary and co-authors and warns that incomplete submissions may be desk rejected or not proceed to review.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Use this for TACL submission-prep checks only.
  quote_or_locator: official_transacl_submission_guidelines_submissions.md:40-58
- claim: TACL submissions must follow official TACL style requirements and the submission formatting instructions.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_formatting_pdf_tacl2021v1-submission-formatting-instructions.pdf.md
  support_type: direct
  verification_note: Use the PDF instructions for exact formatting rules.
  quote_or_locator: guidelines lines 143-163; formatting PDF lines 109-169
- claim: TACL uses double-blind reviewing with specific anonymization requirements in the captured policy.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Verify current ACL/TACL anonymity updates before live submission.
  quote_or_locator: official_transacl_submission_guidelines_submissions.md:271-279
- claim: TACL does not allow dual submissions while a paper is under consideration by TACL.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Use this only for TACL, not for all ACL-family venues.
  quote_or_locator: official_transacl_submission_guidelines_submissions.md:309-311
- claim: TACL has no special survey-paper category; survey papers must meet the same bar as regular submissions and must provide broad themes and new insights rather than only descriptive enumeration.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  support_type: direct
  verification_note: This is a TACL venue norm, not a universal survey methodology standard.
  quote_or_locator: official_transacl_submission_guidelines_submissions.md:319-321
- claim: The captured TACL copyright notice says TACL papers are ACL copyright and distributed under CC-BY, with caveats for some early volumes.
  supporting_canonical_paths:
    - references/canonical_sources/md/tacl_submission/official_transacl_submission_guidelines_submissions.md
  support_type: direct
  verification_note: Verify the specific published PDF for older volumes before reuse.
  quote_or_locator: official_transacl_submission_guidelines_submissions.md:343-347
```

## Operational rules

- Use this card for TACL-specific submission, formatting, anonymity, dual-submission, and survey-paper norm questions.
- Use `aclpub_formatting` for ACL conference formatting and `acl_arr_authors` for ARR process questions.
- For survey writing support, treat TACL's survey note as a venue expectation about publishable CL/NLP surveys, not as a general method rule.
- For final answers, cite canonical TACL paths or the official TACL pages.

## Common misuses

- Treating TACL's 10-page survey constraint as universal survey-writing guidance.
- Applying TACL double-blind and resubmission rules to ACL conferences or Computational Linguistics without verification.
- Treating final-version formatting warnings as evidence for manuscript substance.
- Ignoring older-volume license caveats.

## Evidence limits

Primary MIT Press locator: https://direct.mit.edu/tacl/pages/submission-guidelines; local scripted capture returned HTTP 403. Evidence-bearing local Markdown was captured from the official TransACL fallback at https://transacl.org/index.php/tacl/about/submissions and linked TransACL template files. Use the fallback Markdown/final_url rows for direct source claims; keep the MIT Press URL only as a blocked publisher locator and future live-check target. The local capture does not guarantee current monthly deadlines or current live policy text.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=tacl_submission`.
- Canonical Markdown directory: `references/canonical_sources/md/tacl_submission/`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=tacl_submission`.
- Blocked primary locator row: `canonical_mit_submission_guidelines` in `references/canonical_sources/download_manifest.jsonl`.
- Optional local section locators: `references/corpus_index/sections/by_source/tacl_submission.jsonl`.

## Unresolved gaps

- Live TACL monthly deadlines and current template versions should be checked before giving submission advice.
- The local card does not inspect individual accepted TACL survey examples.
