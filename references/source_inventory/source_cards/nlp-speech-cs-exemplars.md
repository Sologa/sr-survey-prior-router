# Source Card: NLP/Speech/CS Exemplar Sources

source_ids: `acl_anthology`, `acl_anthology_github`, `acl_arr_authors`, `aclpub_formatting`, `tacl_submission`, `computational_linguistics`, `isca_archive`, `interspeech_policy`, `dblp`, `arxiv`, `paperswithcode`

related_source_ids: `crossref_api`, `openalex`, `openalex_snapshot`, `ieee_comst_guidelines`, `acm_dl`, `cacm_author_guidelines`

## Summary

NLP/speech/CS survey-writing prior needs exemplar corpora and venue norms in addition to general review methodology. ACL Anthology and ISCA Archive are primary field archives. DBLP, Crossref, and OpenAlex provide metadata backbones. TACL, Computational Linguistics, ARR/ACLPUB, INTERSPEECH, IEEE COMST, and ACM/CACM pages provide venue-specific norms.

Cross-family references here are for exemplar, venue, or metadata support, not method authority.

## Decision Boundary

These sources are useful for examples and metadata, but they are not methodology authorities. Full-text reuse must respect paper-level and publisher/license restrictions.

## Supported Uses

- Discover exemplar survey/tutorial/review papers.
- Build venue-aware source cards and section-structure examples.
- Seed metadata normalization and citation lookup.

## Gaps

- Local raw and Markdown snapshots now exist for retrieved venue/API documents under `../../canonical_sources/`, including official alternatives for TACL, Computational Linguistics, ISCA, and Papers with Code.
- Crossref, OpenAlex, IEEE COMST, ACM DL, and CACM are cross-family related sources; use their own source rows/cards before treating them as evidence.
- MIT Press canonical TACL/Computational Linguistics pages returned 403 from this environment; official TransACL and CL OJS/style-file alternatives are locally captured.
- No validated NLP/speech survey exemplar set has been selected yet.
- No paper-to-taxonomy assignment ledger exists yet.
- API and PDF reuse policies need per-source verification before bulk indexing.

last_reviewed: 2026-05-04
