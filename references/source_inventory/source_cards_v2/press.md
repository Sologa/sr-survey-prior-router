# PRESS Source Card v2

```yaml
source_id: press
source_family: sr_certainty_appraisal_bias_search
canonical_paths: []
canonical_urls:
  - https://www.cda-amc.ca/press-peer-review-electronic-search-strategies
  - https://www.cda-amc.ca/press-peer-review-electronic-search-strategies-2015-guideline-explanation-and-elaboration
  - https://www.cda-amc.ca/sites/default/files/attachments/2023-06/PRESS%20Peer%20Review%20Electronic%20Search%20Strategies_%202015%20Guideline%20Explanation%20and%20Elaboration%20%28PRESS%20E%26E%29.pdf
  - https://www.cda-amc.ca/sites/default/files/archive/127686/CP0015_PRESS_Update_Report_2016.pdf
authority_level: blocked_inventory_target
version_or_access_date: "2015 guideline/explanation published 2016; page updated 2026-02-26; browser-live checked 2026-05-05"
applies_to:
  - inventory target for peer review of electronic search strategies
  - future browser-assisted or access-approved PRESS capture
not_for:
  - local evidence citation until access-approved canonical content is captured
  - whole-review conduct guidance
  - non-electronic search tasks
  - database API behavior
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: high until local canonical content is captured; browser access worked on 2026-05-05 but scripted fetch still hit Cloudflare 403.
reuse_or_license_risk: CDA-AMC terms apply; subagent observed non-commercial/no-modification/credit conditions in the official E&E PDF.
qa_status: browser_live_verified_scripted_fetch_blocked_no_local_content
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: PRESS is no longer best described as dead; browser-live access found official hub, detail, and E&E PDF URLs on 2026-05-05.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: The manifest records browser-verified URLs but no local canonical Markdown/raw content.
  quote_or_locator: source_manifest.jsonl row with source_id=press; browser_verified_urls
- claim: PRESS still cannot be used as local canonical evidence in this pack.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
    - references/canonical_sources/download_manifest.jsonl
  support_type: blocked
  verification_note: Simple local fetch attempts remain 403-blocked and no tracked Markdown exists under canonical_sources/md/press/.
  quote_or_locator: source_manifest.jsonl row with local_content_status=blocked; download_manifest rows with source_id=press
- claim: The best future capture target is the official PRESS E&E PDF plus the current hub/detail pages, not stale standalone table URLs.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: This is a browser-live locator claim from the 2026-05-05 subagent check, not local canonical evidence.
  quote_or_locator: source_manifest.jsonl row with browser_verified_urls
```

## Operational rules

- Use this card only to remember that `press` is a browser-live but locally uncaptured search-strategy peer-review authority.
- Do not cite PRESS checklist or recommendation content from this pack until canonical content is captured.
- If PRESS is needed, use browser/manual or another access-approved route and store the hub/detail/E&E PDF capture with license notes.
- Treat PRESS as search strategy QA, not whole-review conduct guidance.

## Common misuses

- Reconstructing PRESS checklist content from memory.
- Treating the browser-live locator as local evidence.
- Treating the failed `download_manifest` rows as proof that official PRESS content is unavailable.
- Using PRESS for non-search or whole-review method claims.

## Evidence limits

There is still no tracked local canonical Markdown for PRESS. The safe local claim is limited to inventory status, browser-live locator status, and the continuing need for access-approved capture.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=press`.
- Failed scripted download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=press`.
- Confirm local absence: `references/canonical_sources/md/press/`.
- Live recapture note: `validation/live_recapture_2026-05-05.md`.

## Unresolved gaps

- Need browser-assisted or access-approved capture of the PRESS hub, detail page, and official E&E PDF.
- Need local Markdown conversion and source-card upgrade before using PRESS content as evidence.
