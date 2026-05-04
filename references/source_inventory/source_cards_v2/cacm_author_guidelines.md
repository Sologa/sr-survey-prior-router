# CACM Author Guidelines Source Card v2

```yaml
source_id: cacm_author_guidelines
source_family: survey_writing_methods
canonical_paths: []
canonical_urls:
  - https://cacm.acm.org/author-guidelines
  - https://authors.acm.org/magazines/cacm
  - https://www.acm.org/publications/authors/submissions
  - https://www.acm.org/publications/authors/information-for-authors
authority_level: blocked_inventory_target
version_or_access_date: "browser-live check 2026-05-05; local scripted fetch blocked"
applies_to:
  - future CACM venue-author-guideline capture
  - browser-live fallback verification of CACM/ACM author pages
  - source-audit tracking for blocked local evidence
not_for:
  - current local evidence-backed CACM author-guideline claims
  - systematic review or survey methodology
  - substituting ACM DL user-guide content for CACM author rules
  - venue advice without live or locally captured official content
route_relevance:
  - survey_writing_prior
  - source_audit
freshness_risk: high because the CACM-specific target remains blocked and browser-live fallback pages can change.
reuse_or_license_risk: ACM/CACM pages are publisher materials; no open license was observed for guidance pages in the 2026-05-05 live check.
qa_status: browser_live_fallback_verified_scripted_fetch_blocked_no_local_content
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The CACM-specific author-guidelines page remains blocked for usable local capture.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
    - references/canonical_sources/download_manifest.jsonl
  support_type: blocked
  verification_note: The manifest and failed download rows record no local canonical Markdown for the CACM-specific page.
  quote_or_locator: source_manifest.jsonl row with source_id=cacm_author_guidelines; download_manifest rows with source_id=cacm_author_guidelines
- claim: Browser-live access found official CACM/ACM fallback pages, but those are not tracked local canonical evidence.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: The manifest records browser_verified_urls for the ACM Authors Gateway and ACM author pages.
  quote_or_locator: source_manifest.jsonl row with browser_verified_urls
- claim: CACM and ACM author pages are venue or publisher guidance, not survey-methodology authority.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: The inventory class is venue guidance and the source remains no-local-content.
  quote_or_locator: source_manifest.jsonl row with authority_class=venue_guidance and not_for boundary
```

## Operational rules

- Treat this as a blocked/no-local-content source placeholder.
- Use browser-live official pages only for current CACM venue guidance after explicit verification.
- Do not cite this card for CACM style, article type, submission, or author-policy claims.
- Keep CACM author guidance separate from `acm_dl`, which is a publisher corpus/search-interface source.

## Common misuses

- Filling the CACM gap with ACM DL user-guide text.
- Treating ACM-wide author pages as survey methodology.
- Treating a browser-live fallback summary as local canonical evidence.
- Applying CACM venue expectations to ACM journals, proceedings, or magazines without specific official evidence.

## Evidence limits

There is no tracked local canonical Markdown evidence for CACM author guidelines. The card supports only blocked-source routing, browser-live fallback locator status, and the boundary that CACM/ACM pages are venue/publisher guidance.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cacm_author_guidelines`.
- Failed scripted download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=cacm_author_guidelines`.
- Registry caveat: `references/source_inventory/source_registry.yaml` under `survey_writing_methods`.
- Live recapture note: `validation/live_recapture_2026-05-05.md`.

## Unresolved gaps

- Need browser-assisted or access-approved capture of the CACM-specific author-guidelines page.
- Need local Markdown for CACM/ACM fallback pages before any non-live evidence-backed venue advice.
