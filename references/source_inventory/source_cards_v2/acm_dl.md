# ACM Digital Library Source Card v2

```yaml
source_id: acm_dl
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/acm_dl/official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md
canonical_urls:
  - https://www.acm.org/publications/digital-library
  - https://libraries.acm.org/binaries/content/assets/libraries/new_acm-digital-library-user-guide.pdf
authority_level: canonical_publisher_corpus_doc
version_or_access_date: "ACM DL user guide captured 2026-05-04; several official web pages blocked"
applies_to:
  - ACM Digital Library search-interface orientation
  - ACM publisher-corpus and Guide-to-Computing-Literature routing
  - computing literature discovery and source-audit planning
not_for:
  - CACM author guidelines
  - systematic review or survey methodology
  - unrestricted article or metadata harvesting
  - API behavior unless a separate ACM API document is captured
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for DL interface, access tiers, search behavior, usage policies, and licensing; verify live ACM pages before operational use.
reuse_or_license_risk: ACM DL access and reuse are license-constrained; the local user guide does not grant scraping, full-text reuse, or bulk metadata rights.
qa_status: partial_local_user_guide_verified_with_blocked_policy_pages
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The captured ACM DL user guide describes ACM DL as containing ACM journals, conference proceedings, newsletters, and books, with ACM Books noted separately for subscription purposes.
  supporting_canonical_paths:
    - references/canonical_sources/md/acm_dl/official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md
  support_type: direct
  verification_note: Use this as publisher-corpus orientation, not as a method or venue-author guideline.
  quote_or_locator: official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md:56-63
- claim: The local ACM DL evidence is a user guide for accounts, search, alerts, binders, and access workflows.
  supporting_canonical_paths:
    - references/canonical_sources/md/acm_dl/official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md
  support_type: direct
  verification_note: This supports interface/discovery routing only.
  quote_or_locator: official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md:68-69,113-124,187-229,392-468
- claim: The user guide documents basic and advanced search features, including search over article citation fields and the Guide to Computing Literature.
  supporting_canonical_paths:
    - references/canonical_sources/md/acm_dl/official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md
  support_type: direct
  verification_note: Do not infer API access or bulk-harvest rights from web-interface search features.
  quote_or_locator: official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md:197-229
- claim: Several ACM web pages, including DL home/usage-policy, remain outside this card; CACM author pages are now captured separately under `cacm_author_guidelines`, so this card remains limited to ACM DL user-guide coverage.
  supporting_canonical_paths:
    - references/canonical_sources/download_manifest.jsonl
  support_type: locator_only
  verification_note: Use the download manifest to audit which ACM URLs failed and which PDF user guide succeeded.
  quote_or_locator: download_manifest.jsonl:213-221
```

## Operational rules

- Use this card for ACM DL discovery-interface orientation and source-audit routing.
- Do not use ACM DL user-guide content as CACM author guidance.
- Do not infer scraping, API, bulk-download, or full-text reuse permissions from the captured user guide.
- Live-verify current ACM DL usage policies before any automated collection, metadata export, or full-text workflow.

## Common misuses

- Treating ACM DL as a survey-writing method authority.
- Treating search UI availability as permission for automated harvesting.
- Substituting ACM DL user-guide material for CACM author guidelines now captured under `cacm_author_guidelines`.
- Assuming Guide-to-Computing-Literature coverage is complete or current without checking ACM documentation.

## Evidence limits

The local canonical content for this card is a user guide PDF only. CACM author pages are captured separately under `cacm_author_guidelines`; more authoritative ACM DL home and policy pages still need live verification before legal/usage-policy conclusions.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=acm_dl`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=acm_dl`.
- Canonical Markdown: `references/canonical_sources/md/acm_dl/official_dl_user_guide_pdf_new_acm-digital-library-user-guide.pdf.md`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=acm_dl`.

## Unresolved gaps

- Capture or manually verify ACM DL usage-policy pages before automating access.
- Capture a current ACM API or export documentation source if API behavior becomes relevant.
- Use `cacm_author_guidelines` for CACM-specific official content; do not route CACM author-guideline claims through the ACM DL user-guide card.
