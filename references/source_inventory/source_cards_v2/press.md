# PRESS Source Card v2

```yaml
source_id: press
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/press/manual_browser_pdf_press_ee_2015.md
  - references/canonical_sources/md/press/manual_browser_pdf_hub_page.md
  - references/canonical_sources/md/press/manual_browser_pdf_ee_detail_page.md
canonical_urls:
  - https://www.cda-amc.ca/press-peer-review-electronic-search-strategies
  - https://www.cda-amc.ca/press-peer-review-electronic-search-strategies-2015-guideline-explanation-and-elaboration
  - https://www.cda-amc.ca/sites/default/files/attachments/2023-06/PRESS%20Peer%20Review%20Electronic%20Search%20Strategies_%202015%20Guideline%20Explanation%20and%20Elaboration%20%28PRESS%20E%26E%29.pdf
  - https://www.cda-amc.ca/sites/default/files/archive/127686/CP0015_PRESS_Update_Report_2016.pdf
authority_level: methodology_guideline
version_or_access_date: "2015 guideline/explanation published 2016; page updated 2026-02-26; manually captured 2026-05-05"
applies_to:
  - peer review of electronic search strategies
  - systematic-review and health-technology-assessment search QA
  - checking search-strategy elements, translation, syntax, limits, and documentation
not_for:
  - whole-review conduct guidance
  - non-electronic search tasks
  - study appraisal, certainty grading, or bias assessment
  - database API behavior
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: medium; the E&E PDF is a stable 2016 guideline, but hub/detail pages and access conditions can change and scripted fetch still returns 403.
reuse_or_license_risk: CDA-AMC terms apply; the E&E PDF allows non-commercial reproduction if unmodified and credited, but verify terms before public redistribution or translation.
qa_status: manual_browser_pdf_capture_page_addressable_scripted_fetch_blocked
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: PRESS is now locally captured in this pack through manual browser PDF downloads.
  supporting_canonical_paths:
    - references/canonical_sources/md/press/manual_browser_pdf_press_ee_2015.md
    - references/canonical_sources/md/press/manual_browser_pdf_hub_page.md
    - references/canonical_sources/md/press/manual_browser_pdf_ee_detail_page.md
  support_type: direct
  verification_note: These Markdown files were converted from user-downloaded browser/PDF captures on 2026-05-05; simple scripted fetches still failed with 403.
  quote_or_locator: canonical Markdown headers and download_manifest rows with capture_method=manual_browser_pdf_download
- claim: The PRESS E&E PDF is the primary local PRESS evidence for search-strategy peer-review guidance.
  supporting_canonical_paths:
    - references/canonical_sources/md/press/manual_browser_pdf_press_ee_2015.md
  support_type: direct
  verification_note: The 79-page E&E capture contains the guideline explanation/elaboration text and is preferred over hub/detail print captures for substantive PRESS claims.
  quote_or_locator: manual_browser_pdf_press_ee_2015.md:1-40
- claim: PRESS should be used only for electronic-search-strategy peer review/search QA, not as a whole-review methodology source.
  supporting_canonical_paths:
    - references/canonical_sources/md/press/manual_browser_pdf_press_ee_2015.md
  support_type: direct
  verification_note: The source title and scope are electronic search strategies and peer review of those strategies.
  quote_or_locator: manual_browser_pdf_press_ee_2015.md:1-40
```

## Operational rules

- Prefer `manual_browser_pdf_press_ee_2015.md` for substantive PRESS evidence.
- Use the hub/detail page captures for official locator, version, and access context.
- Keep scripted-fetch 403 rows in mind for refresh planning; recapture may require browser/manual access again.
- Treat PRESS as search-strategy QA, not whole-review conduct guidance.
- Use the page-level section locators in `references/corpus_index/sections/by_source/press.jsonl` before opening the full Markdown capture.

## Common misuses

- Using PRESS for non-search or whole-review method claims.
- Treating the browser print/PDF hub page as the primary checklist/guideline text when the E&E PDF is available.
- Assuming standalone Table 8, Table 9, or Table 10 URLs are separately captured; use the E&E PDF first.
- Ignoring CDA-AMC reuse terms when copying or redistributing the source.

## Evidence limits

The local hub/detail captures are browser print PDFs and include navigation/footer artifacts. The E&E PDF is the primary clean guideline capture. Simple local HTTP fetch still fails for CDA-AMC URLs, so future refreshes should record whether capture was browser/manual or scripted.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=press`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=press` and `capture_method=manual_browser_pdf_download`.
- Canonical Markdown: `references/canonical_sources/md/press/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=press`.
- Page-level section locators: `references/corpus_index/sections/by_source/press.jsonl`.
- Manual capture note: `validation/manual_browser_capture_2026-05-05.md`.

## Unresolved gaps

- Add finer line/section locators for individual PRESS checklist items before high-stakes claim reuse.
- Optional: separately capture standalone table PDFs if exact table-file provenance becomes important.
- Recheck CDA-AMC access and reuse terms before public redistribution or translation.
