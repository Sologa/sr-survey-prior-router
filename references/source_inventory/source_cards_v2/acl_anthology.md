# ACL Anthology Programmatic Access Source Card v2

```yaml
source_id: acl_anthology
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/acl_anthology/canonical_api.md
canonical_urls:
  - https://aclanthology.org/faq/api/
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; site build captured 2026-05-03"
applies_to:
  - ACL Anthology metadata access
  - NLP and computational linguistics paper corpus discovery
  - locating Anthology PDFs and Python package documentation
not_for:
  - universal survey methodology standards
  - systematic review conduct rules
  - unrestricted PDF redistribution
  - judging paper quality or inclusion eligibility
route_relevance:
  - survey_writing_prior
  - source_audit
  - evidence_grounding
  - synthesis_writing
freshness_risk: medium because the Anthology site, repository commit, Python module, and licensing notices can change.
reuse_or_license_risk: paper licensing varies by publication era and rights holder; verify the specific Anthology record before redistributing full text or large excerpts.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The ACL Anthology exposes its paper, author, volume, and event metadata through the ACL Anthology GitHub repository and Python module.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology/canonical_api.md
  support_type: direct
  verification_note: Use the official API FAQ before relying on Anthology metadata access assumptions.
  quote_or_locator: canonical_api.md:20-26
- claim: The ACL Anthology stores metadata separately from PDFs; PDFs are hosted on Anthology servers.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology/canonical_api.md
  support_type: direct
  verification_note: Treat metadata access and PDF access as different operations with different reuse constraints.
  quote_or_locator: canonical_api.md:22
- claim: Anthology material has era-dependent licensing, with pre-2016 material and 2016-or-later material under different Creative Commons terms in the captured page.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology/canonical_api.md
  support_type: direct
  verification_note: Verify the exact paper page and rights notice for any final reuse claim.
  quote_or_locator: canonical_api.md:28
- claim: This source supports NLP/CL corpus discovery and grounding, not general claims about how surveys or systematic reviews should be conducted.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology/canonical_api.md
  support_type: indirect
  verification_note: The canonical page describes Anthology access and rights, not survey methodology.
  quote_or_locator: canonical_api.md:20-30
```

## Operational rules

- Use this card to route questions about ACL Anthology corpus access, metadata provenance, and Anthology PDF location.
- For evidence in final answers, cite the canonical Markdown or official ACL Anthology URL, not this card.
- For paper-level claims, open the specific Anthology paper page or PDF; this API FAQ is only a corpus-access source.
- Check licensing at the target paper level before storing, redistributing, or quoting substantial text.

## Common misuses

- Treating Anthology metadata as a universal survey-writing standard.
- Assuming programmatic metadata access grants bulk PDF reuse rights.
- Inferring paper quality, peer-review status, or methodological rigor from Anthology presence alone.
- Citing the source card or section index instead of canonical Anthology evidence.

## Evidence limits

The local capture is a compact API FAQ page. It does not include the Python module documentation, per-paper metadata records, or per-paper license pages. It also does not define survey, review, or synthesis-writing methodology.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=acl_anthology`.
- Canonical Markdown: `references/canonical_sources/md/acl_anthology/canonical_api.md`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=acl_anthology`.
- Optional local section locators: `references/corpus_index/sections/by_source/acl_anthology.jsonl`.

## Unresolved gaps

- The local card does not verify the current PyPI/readthedocs API behavior.
- Per-paper licenses and PDF availability must be checked at the paper page level.
