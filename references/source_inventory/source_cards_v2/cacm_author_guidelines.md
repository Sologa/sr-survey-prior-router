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
version_or_access_date: "inventory target checked 2026-05-04; local canonical capture blocked"
applies_to:
  - future CACM venue-author-guideline capture
  - candidate broad-audience computing venue prior after canonical content is captured
  - source-audit tracking for blocked local evidence
not_for:
  - current evidence-backed CACM author guidance
  - systematic review or survey methodology
  - substituting ACM DL user-guide content for CACM author rules
  - venue advice without live or locally captured official content
route_relevance:
  - survey_writing_prior
  - source_audit
freshness_risk: high because no local canonical author-guideline content is available; any CACM venue claim requires live verification or a successful recapture.
reuse_or_license_risk: ACM/CACM author pages are publisher materials; reuse and submission advice require current official terms after access is resolved.
qa_status: blocked_no_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: CACM author guidelines are present in the source inventory as a venue-guidance target, but no local canonical Markdown content is available.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
    - references/canonical_sources/download_manifest.jsonl
  support_type: blocked
  verification_note: The manifest has an inventory row, and local download attempts for CACM/ACM author pages failed with access errors.
  quote_or_locator: source_manifest.jsonl:43; download_manifest.jsonl:112,218-221
- claim: This card must not be used to answer CACM author-guideline questions until official content is captured or live-verified.
  supporting_canonical_paths:
    - references/canonical_sources/download_manifest.jsonl
  support_type: blocked
  verification_note: Download rows show failed captures for the CACM and ACM author-guideline URLs.
  quote_or_locator: download_manifest.jsonl:218-221
- claim: ACM DL local material is not a substitute for CACM author guidance.
  supporting_canonical_paths:
    - references/source_inventory/source_registry.yaml
  support_type: blocked
  verification_note: The registry explicitly separates the blocked CACM target from the ACM DL user-guide/publisher-corpus source.
  quote_or_locator: source_registry.yaml:96-108
```

## Operational rules

- Treat this as a blocked source placeholder and source-audit reminder.
- Do not cite it for CACM style, article type, submission, or author-policy claims.
- If CACM guidance is needed, live-verify the official CACM/ACM author pages or create a new local canonical capture first.
- Keep CACM author guidance separate from `acm_dl`, which is a publisher corpus/search-interface source.

## Common misuses

- Filling the gap with ACM DL user-guide text.
- Treating the inventory row as proof of CACM author-guideline content.
- Using this blocked card as a venue norm for computing surveys.
- Applying CACM claims to ACM journals, proceedings, or magazines without specific official evidence.

## Evidence limits

There is no local canonical Markdown evidence for CACM author guidelines. The only local support for this card is the inventory and failed-download state, so the card is valid only for blocked-source routing and gap tracking.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cacm_author_guidelines`.
- Failed download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=cacm_author_guidelines`.
- Registry caveat: `references/source_inventory/source_registry.yaml` under `survey_writing_methods`.

## Unresolved gaps

- Capture or manually verify official CACM author guidelines.
- Decide whether CACM needs a separate venue-family card after official content is available.
