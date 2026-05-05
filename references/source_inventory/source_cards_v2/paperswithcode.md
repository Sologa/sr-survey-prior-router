# Papers with Code Source Card v2

```yaml
source_id: paperswithcode
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/paperswithcode/official_github_data_readme_readme.md.md
  - references/canonical_sources/md/paperswithcode/official_github_data_repo_paperswithcode-data.md
  - references/canonical_sources/md/paperswithcode/official_github_client_readme_readme.md.md
  - references/canonical_sources/md/paperswithcode/official_github_client_repo_paperswithcode-client.md
canonical_urls:
  - https://raw.githubusercontent.com/paperswithcode/paperswithcode-data/master/README.md
  - https://github.com/paperswithcode/paperswithcode-data
  - https://raw.githubusercontent.com/paperswithcode/paperswithcode-client/master/README.md
  - https://github.com/paperswithcode/paperswithcode-client
bad_capture_paths:
  - references/canonical_sources/md/paperswithcode/canonical_about_trending_33783fc6.md
  - references/canonical_sources/md/paperswithcode/canonical_sota_trending_87d86935.md
redirected_website_urls:
  - https://paperswithcode.com/about
  - https://paperswithcode.com/sota
authority_level: derivative_not_canonical
version_or_access_date: "official GitHub docs fetched 2026-05-04; website redirects rechecked 2026-05-05"
applies_to:
  - ML/NLP/CS exemplar and benchmark enrichment
  - task, dataset, code-link, method, and evaluation-table discovery
  - secondary prior for field trends and leaderboard context
not_for:
  - canonical bibliographic authority
  - systematic review or survey methodology
  - unrestricted reuse of submitted or mirrored benchmark data
  - stable current website state without live verification
route_relevance:
  - general_domain_prior
  - survey_writing_prior
  - source_audit
freshness_risk: very high for website pages, daily data regeneration, API status, leaderboard content, and repository maintenance; verify live before use.
reuse_or_license_risk: captured data README states CC-BY-SA for data; client code is separately licensed; website captures and third-party linked papers/code have separate rights.
qa_status: redirected_website_captures_invalid_official_github_docs_usable
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Papers with Code data docs provide downloadable dumps for papers with abstracts, paper-code links, evaluation tables, methods, and datasets.
  supporting_canonical_paths:
    - references/canonical_sources/md/paperswithcode/official_github_data_readme_readme.md.md
  support_type: direct
  verification_note: Use this for enrichment-data routing, not as a canonical bibliography.
  quote_or_locator: official_github_data_readme_readme.md.md:6-16
- claim: The captured data README says the data is regenerated daily and licensed under CC-BY-SA.
  supporting_canonical_paths:
    - references/canonical_sources/md/paperswithcode/official_github_data_readme_readme.md.md
  support_type: direct
  verification_note: Freshness and license details should be rechecked live before reuse.
  quote_or_locator: official_github_data_readme_readme.md.md:21-27
- claim: The captured client README describes a paperswithcode.com read/write API client and gives read and write-mode examples.
  supporting_canonical_paths:
    - references/canonical_sources/md/paperswithcode/official_github_client_readme_readme.md.md
  support_type: direct
  verification_note: API status, endpoints, and package maintenance need live verification before implementation.
  quote_or_locator: official_github_client_readme_readme.md.md:6-20,30-42,44-57
- claim: The captured client README describes competition leaderboard mirroring and says submitted competition data is licensed under CC-BY-SA 4.0.
  supporting_canonical_paths:
    - references/canonical_sources/md/paperswithcode/official_github_client_readme_readme.md.md
  support_type: direct
  verification_note: Use for API/doc boundary awareness; do not assume all Papers with Code content has the same rights.
  quote_or_locator: official_github_client_readme_readme.md.md:44-57,183-190
- claim: The local website captures for about and SOTA redirected to Hugging Face trending pages, so they are exemplar snapshots rather than reliable Papers with Code policy pages.
  supporting_canonical_paths:
    - references/canonical_sources/download_manifest.jsonl
    - references/canonical_sources/md/paperswithcode/canonical_about_trending_33783fc6.md
    - references/canonical_sources/md/paperswithcode/canonical_sota_trending_87d86935.md
  support_type: locator_only
  verification_note: Do not use the redirected captures as official Papers with Code about/SOTA documentation without live verification.
  quote_or_locator: download_manifest.jsonl:238-239; canonical_about_trending_33783fc6.md:1-6; canonical_sota_trending_87d86935.md:1-6
```

## Operational rules

- Use Papers with Code as secondary enrichment for ML/CS tasks, datasets, code links, methods, and evaluation tables.
- Prefer the official GitHub data/client README captures over redirected website snapshots for grounded claims.
- Recheck data freshness, API availability, repository status, and licenses live before implementation or redistribution.
- Keep Papers with Code separate from bibliographic authorities such as DBLP, Crossref, OpenAlex, Semantic Scholar, or venue proceedings.

## Common misuses

- Treating Papers with Code as a canonical source of publication metadata.
- Using trending-page captures as stable evidence for Papers with Code policy or SOTA coverage.
- Assuming daily regenerated data is immutable or reproducible without snapshot pinning.
- Reusing submitted competition or dataset content without honoring CC-BY-SA and third-party rights.

## Evidence limits

The strongest local evidence is from official GitHub README captures for data and client behavior. The `canonical_about` and `canonical_sota` local website captures redirect to Hugging Face Trending Papers and are bad captures, not Papers with Code evidence. This source is not a methodology authority.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=paperswithcode`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=paperswithcode`.
- Canonical Markdown: `references/canonical_sources/md/paperswithcode/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=paperswithcode`.

## Unresolved gaps

- Verify current Papers with Code API and data-dump availability live before use.
- Replace the redirected Hugging Face trending captures only if a clean Papers with Code website capture becomes available.
- Pin data snapshots if the pack starts relying on Papers with Code enrichment reproducibly.
