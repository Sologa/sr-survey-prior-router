# PRESS Source Card v2

```yaml
source_id: press
source_family: sr_certainty_appraisal_bias_search
canonical_paths: []
canonical_urls:
  - https://www.cda-amc.ca/press-peer-review-electronic-search-strategies
authority_level: blocked_inventory_target
version_or_access_date: "2015 guideline/explanation published 2016; page updated 2026-02-26; checked 2026-05-04"
applies_to:
  - inventory target for peer review of electronic search strategies
not_for:
  - local evidence citation until access-approved canonical content is captured
  - whole-review conduct guidance
  - non-electronic search tasks
  - database API behavior
route_relevance:
  - evidence_grounding
  - source_audit
freshness_risk: high until recaptured; local environment had no canonical Markdown or raw content.
reuse_or_license_risk: CDA-AMC terms apply; do not redistribute or quote content until access-approved content is captured.
qa_status: local_access_blocked_403
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: PRESS is present in the source inventory as a candidate search-strategy peer-review authority, but local canonical capture is blocked.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: The manifest records CDA-AMC/CADTH 403 blocking and no local canonical Markdown/raw content.
  quote_or_locator: source_manifest.jsonl row with source_id=press; local_bundle_status=blocked_403_no_local_content
- claim: This card must not be used as evidence for PRESS checklist content, recommendations, or peer-review methods.
  supporting_canonical_paths:
    - references/source_inventory/source_manifest.jsonl
  support_type: blocked
  verification_note: There is no local canonical content to support PRESS method claims.
  quote_or_locator: source_manifest.jsonl row with evidence_use=candidate_only_until_recaptured
```

## Operational rules

- Use this card only to remember that `press` is a blocked inventory target.
- Do not cite PRESS claims from this pack until canonical content is captured and a new card can quote local evidence.
- If PRESS is needed, perform a separate access-approved retrieval or use another already-captured search-reporting source where appropriate.

## Common misuses

- Reconstructing PRESS checklist content from memory.
- Treating the manifest row as methodology evidence.
- Citing the blocked card as if it contained local canonical text.

## Evidence limits

There is no local canonical Markdown for this source. The only grounded claim is the inventory/blocking status recorded in the manifest.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=press`.
- Confirm absence of local canonical content: `references/canonical_sources/md/press/`.

## Unresolved gaps

- Need access-approved capture of the PRESS guideline/checklist before any source-card evidence claims can be made.
- Need license/reuse review after capture.
