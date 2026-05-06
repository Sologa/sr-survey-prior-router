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
- claim: The PRESS E&E PDF contains guideline explanation/elaboration text for peer review of electronic search strategies.
  supporting_canonical_paths:
    - references/canonical_sources/md/press/manual_browser_pdf_press_ee_2015.md
  support_type: direct
  verification_note: Use the 79-page E&E capture for substantive PRESS source claims, and use provenance notes separately for local capture status.
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

## Local bundle provenance

```yaml
- claim: PRESS is locally captured in this pack through three manual browser/PDF downloads added on 2026-05-05 after scripted HTTP fetches remained blocked.
  supporting_provenance_paths:
    - references/canonical_sources/download_manifest.jsonl
    - validation/manual_browser_capture_2026-05-05.md
    - validation/source_integrity_tracker.md
  support_type: capture_provenance
  verification_note: This is repo-local capture provenance, not PRESS source content; cite canonical PRESS Markdown separately for search-strategy peer-review claims.
  locator: download_manifest rows with source_id=press and capture_method=manual_browser_pdf_download; manual capture note PRESS section; source_integrity_tracker row press
- claim: Local QA designates manual_browser_pdf_press_ee_2015 as the primary clean PRESS capture, while the hub and detail captures are locator/context PDFs with navigation artifacts.
  supporting_provenance_paths:
    - references/canonical_sources/download_manifest.jsonl
    - validation/manual_browser_capture_2026-05-05.md
  support_type: repo_qa
  verification_note: This priority is local bundle guidance about which capture to open first; it does not replace canonical source verification.
  locator: manual capture note Captures Added and Quality Notes sections; download_manifest evidence_use and notes fields for source_id=press
- claim: Future PRESS refreshes may require manual or browser-based capture because simple scripted fetches still return blocked responses for CDA-AMC URLs in this environment.
  supporting_provenance_paths:
    - references/canonical_sources/download_manifest.jsonl
    - validation/manual_browser_capture_2026-05-05.md
    - validation/source_integrity_tracker.md
  support_type: capture_provenance
  verification_note: Treat this as refresh planning state for the local bundle.
  locator: failed scripted PRESS rows in download_manifest; manual capture note Quality Notes; source_integrity_tracker row press
```

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
