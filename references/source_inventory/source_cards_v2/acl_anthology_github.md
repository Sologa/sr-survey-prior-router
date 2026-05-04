# ACL Anthology GitHub Repository Source Card v2

```yaml
source_id: acl_anthology_github
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md
canonical_urls:
  - https://github.com/acl-org/acl-anthology
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04"
applies_to:
  - ACL Anthology metadata repository routing
  - source audit of Anthology metadata and build infrastructure
  - locating the ACL Anthology Python package entry point
not_for:
  - universal survey methodology standards
  - direct evidence for individual paper claims
  - replacing Anthology PDFs or paper pages
  - relicensing papers from repository code license
route_relevance:
  - source_audit
  - evidence_grounding
  - survey_writing_prior
freshness_risk: high because the local Markdown is a GitHub web capture and repository contents, counts, and branch state change frequently.
reuse_or_license_risk: repository/code license does not automatically apply to Anthology paper PDFs or paper text.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The ACL Anthology GitHub repository contains metadata for papers, authors, and venues on the ACL Anthology website.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md
  support_type: direct
  verification_note: Use the repository README section in the captured GitHub page for repository role claims.
  quote_or_locator: canonical_acl-anthology.md:415-425
- claim: The repository also contains code and instructions for generating the Anthology website.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md
  support_type: direct
  verification_note: Keep metadata/source-infrastructure claims separate from paper-content evidence.
  quote_or_locator: canonical_acl-anthology.md:417-423
- claim: The captured repository page identifies a Python package for accessing ACL Anthology metadata.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md
  support_type: direct
  verification_note: Use package docs for API behavior; this card only confirms repository-level availability.
  quote_or_locator: canonical_acl-anthology.md:423-429
- claim: This source is best used for source audits and metadata provenance, not as canonical evidence for paper findings or survey-writing rules.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md
  support_type: indirect
  verification_note: The captured repository page describes repository contents, not survey methodology or paper conclusions.
  quote_or_locator: canonical_acl-anthology.md:415-425
```

## Operational rules

- Use this source when the task asks where ACL Anthology metadata or build code comes from.
- Use `acl_anthology` or per-paper Anthology records for corpus access and paper-level grounding.
- Treat GitHub UI counts, branches, issues, stars, and commit counts as stale unless rechecked live.
- Do not infer PDF licensing from the repository page.

## Common misuses

- Treating the repository as a substitute for canonical paper PDFs or Anthology paper pages.
- Applying the repository license to paper content.
- Citing repository UI boilerplate as source evidence.
- Treating ACL Anthology coverage as a universal standard for survey methodology.

## Evidence limits

The local capture is a GitHub HTML page and includes substantial GitHub interface boilerplate. It is useful for locating repository role statements but not for precise current repository state.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=acl_anthology_github`.
- Canonical Markdown: `references/canonical_sources/md/acl_anthology_github/canonical_acl-anthology.md`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=acl_anthology_github`.
- Optional local section locators: `references/corpus_index/sections/by_source/acl_anthology_github.jsonl`.

## Unresolved gaps

- Current branch, commit, and file contents should be verified in GitHub or a live checkout before operational use.
- This local capture does not provide per-paper records or full package documentation.
