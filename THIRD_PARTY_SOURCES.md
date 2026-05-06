# Third-Party Sources

This skill routes across a prepared local source inventory. The inventory is useful for review and source-grounded synthesis, but most evidence-bearing text comes from third parties.

## Manifest Entry Points

- `references/source_inventory/source_manifest.jsonl`: source-level authority class, access, caveats, local document paths, and validation status.
- `references/canonical_sources/download_manifest.jsonl`: capture-level paths, conversions, failures, checksums, and manual-browser provenance.
- `references/source_inventory/redistribution_policy.yaml`: conservative machine-readable reuse policy.

## What Is Third-Party Material

Third-party material includes converted Markdown under `references/canonical_sources/md/`, raw captures under `references/canonical_sources/raw/`, browser-created PDF/Markdown captures, copied API schemas, publisher guidance pages, standards, checklists, article text, dataset documentation, and any source file listed in the manifests above.

The project license does not relicense those materials. A source being reachable on the open web, converted to Markdown, or tracked in Git does not mean it is open for bulk redistribution or reuse.

## What Is Project-Authored Derivative Material

Route files, source cards, coverage reports, validation notes, indexes, and graph/navigation outputs are derivative router layers. They may be project-authored, but they remain dependent on upstream sources for evidence. They should be used to choose what to read, not as standalone domain authority.

## Conservative Source Categories

- Manual browser captures: `press`, `cacm_author_guidelines`. These were captured manually after scripted fetches were blocked. Treat as rights-sensitive and refresh-sensitive.
- Publisher, venue, or archive-controlled sources: examples include `acm_dl`, `ieee_xplore_api`, `cacm_author_guidelines`, `tacl_submission`, `computational_linguistics`, `acl_anthology`, `isca_archive`, `nature_reviews_submission`, and `ieee_comst_guidelines`. Verify current terms before reuse.
- Commercial or licensed sources: examples include `dimensions_api`, `scite_api`, `lens_api`, `cochrane_library`, `ieee_xplore_api`, and licensed/premium uses of `acm_dl` or `core_api`. Do not treat local docs as permission to mirror data.
- CC/open-data claims: examples include `state_of_art_review_2022`, `kundisch_taxonomy_update_2021`, `opencitations`, `dblp`, `paperswithcode`, and parts of `openalex` or `crossref_api`. These remain conditional: verify the specific document/data item, attribution requirements, third-party content, and freshness before redistribution.
- Mixed or unknown terms: all other local source conversions default to "verify upstream terms first."

## Reuse Rules For Reviewers And Agents

- Do not apply the project `LICENSE` to third-party source text.
- Do not publish bulk third-party Markdown or raw captures as if they were project-authored.
- Prefer short attributed quotations and locators over long excerpts.
- Before public redistribution, check the exact source ID, document path, upstream URL, capture provenance, and current license/access terms.
- For current API behavior, venue requirements, or database rights, live-verify the upstream source rather than relying only on the captured Markdown.

This file is a boundary note, not legal advice.
