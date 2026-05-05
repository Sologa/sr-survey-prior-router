# CACM Author Guidelines Source Card v2

```yaml
source_id: cacm_author_guidelines
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_author_guidelines.md
  - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_cacm_overview.md
  - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_acm_submissions.md
  - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_acm_information_for_authors.md
canonical_urls:
  - https://cacm.acm.org/author-guidelines
  - https://authors.acm.org/magazines/cacm
  - https://www.acm.org/publications/authors/submissions
  - https://www.acm.org/publications/authors/information-for-authors
authority_level: venue_guidance
version_or_access_date: "manual browser PDF captures checked 2026-05-05; scripted fetch blocked"
applies_to:
  - CACM article audience, scope, and submission expectations
  - ACM publisher authoring workflow and policy navigation
  - venue-specific survey/review article positioning when targeting CACM
not_for:
  - systematic review or survey methodology
  - universal computing survey-writing rules
  - substituting ACM DL user-guide content for CACM author rules
  - venue advice without checking current official pages when requirements may have changed
route_relevance:
  - survey_writing_prior
  - source_audit
freshness_risk: high; CACM/ACM author pages can change and simple scripted capture still fails with Cloudflare/403.
reuse_or_license_risk: ACM/CACM publisher materials; no open license observed for guidance pages. Prefer short quotations and verify rights before public reuse.
qa_status: manual_browser_pdf_capture_page_addressable_scripted_fetch_blocked
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The CACM-specific author-guidelines page is now locally captured from a manual browser PDF download.
  supporting_canonical_paths:
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_author_guidelines.md
  support_type: direct
  verification_note: The capture contains the CACM author-guidelines text and should be preferred over ACM-wide fallback pages for CACM-specific venue guidance.
  quote_or_locator: manual_browser_pdf_author_guidelines.md:1-45
- claim: CACM/ACM author pages are venue or publisher guidance, not survey-methodology authority.
  supporting_canonical_paths:
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_author_guidelines.md
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_cacm_overview.md
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_acm_submissions.md
  support_type: direct
  verification_note: The captures describe CACM readership, article mechanics, author workflow, templates, and submission/policy navigation.
  quote_or_locator: canonical Markdown headers and captured PDF text sections
- claim: ACM-wide submissions and information-for-authors captures are supporting publisher context, not replacements for CACM-specific instructions.
  supporting_canonical_paths:
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_acm_submissions.md
    - references/canonical_sources/md/cacm_author_guidelines/manual_browser_pdf_acm_information_for_authors.md
  support_type: direct
  verification_note: Use these for ACM workflow/policy context while keeping CACM-specific claims anchored to the author-guidelines capture.
  quote_or_locator: manual_browser_pdf_acm_submissions.md:1-35; manual_browser_pdf_acm_information_for_authors.md:1-35
```

## Operational rules

- Use `manual_browser_pdf_author_guidelines.md` first for CACM-specific audience, article type, and submission guidance.
- Use ACM submissions and information-for-authors captures only for publisher-level workflow or policy context.
- Do not treat CACM/ACM author pages as cross-domain survey-methodology standards.
- Live-verify current official pages before exact venue-submission advice because these pages can change.
- Use the page-level section locators in `references/corpus_index/sections/by_source/cacm_author_guidelines.jsonl` before opening the full Markdown capture.

## Common misuses

- Filling CACM guidance gaps with ACM DL user-guide text.
- Treating ACM-wide author pages as CACM-specific rules.
- Treating venue advice as evidence-synthesis methodology.
- Copying large ACM/CACM text into public materials without checking reuse rights.

## Evidence limits

The local captures are browser print PDFs and include navigation/cookie artifacts. They are usable for source grounding, but not clean publisher XML/HTML captures. ACM/CACM reuse rights remain more restrictive than open-access method papers, so prefer short excerpts and current official links in public-facing outputs.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cacm_author_guidelines`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=cacm_author_guidelines` and `capture_method=manual_browser_pdf_download`.
- Canonical Markdown: `references/canonical_sources/md/cacm_author_guidelines/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=cacm_author_guidelines`.
- Page-level section locators: `references/corpus_index/sections/by_source/cacm_author_guidelines.jsonl`.
- Manual capture note: `validation/manual_browser_capture_2026-05-05.md`.

## Unresolved gaps

- Add finer line/section locators for CACM section types, length expectations, and review process details before high-stakes venue advice.
- Recapture from official HTML if Cloudflare/scripted access becomes available.
- Verify ACM/CACM reuse terms before public redistribution of full captured text.
