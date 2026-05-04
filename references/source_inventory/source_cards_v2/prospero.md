# PROSPERO Source Card v2

```yaml
source_id: prospero
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/prospero/canonical_maintenanceprospero.html.md
canonical_urls:
  - https://www.crd.york.ac.uk/CRDWeb/maintenancePROSPERO.html
authority_level: locator_only
version_or_access_date: "sitewide update date not visible; checked 2026-05-04"
applies_to:
  - locating PROSPERO as a systematic review protocol registry
  - protocol registration and duplicate-checking context
not_for:
  - peer review or endorsement of a protocol
  - review conduct methodology
  - reporting guideline evidence
  - appraisal or certainty grading
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high; local capture is a short maintenance page and registry availability/status can change.
reuse_or_license_risk: record reuse and access terms should be checked before bulk use.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The local PROSPERO capture identifies PROSPERO as an international prospective register of systematic reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/prospero/canonical_maintenanceprospero.html.md
  support_type: direct
  verification_note: This supports only registry identity, not method or endorsement claims.
  quote_or_locator: canonical_maintenanceprospero.html.md:6-10
- claim: The local PROSPERO capture is too sparse for detailed operational claims about registration workflow, fields, eligibility, or API behavior.
  supporting_canonical_paths:
    - references/canonical_sources/md/prospero/canonical_maintenanceprospero.html.md
  support_type: direct
  verification_note: The file is a 39-line maintenance-oriented capture with no detailed registration documentation.
  quote_or_locator: canonical_maintenanceprospero.html.md:1-39
```

## Operational rules

- Use this card to route to PROSPERO as a protocol-registry locator.
- Do not infer protocol quality, endorsement, or review-method correctness from PROSPERO registration.
- Recheck the live registry before advising on registration workflow, eligibility, or current availability.

## Common misuses

- Treating a PROSPERO record as peer review.
- Treating registration as proof that methods were followed.
- Making detailed registration workflow claims from the current local capture.

## Evidence limits

The canonical Markdown capture is minimal. It can support only basic identity and maintenance-status observations.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=prospero`.
- Canonical capture: `references/canonical_sources/md/prospero/canonical_maintenanceprospero.html.md`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=prospero`.
- Optional local section locator: `references/corpus_index/sections/by_source/prospero.jsonl`.

## Unresolved gaps

- Need a fuller PROSPERO capture for registration fields, eligibility rules, record export, or duplicate-checking workflows.
- Need current terms review before bulk record reuse.
