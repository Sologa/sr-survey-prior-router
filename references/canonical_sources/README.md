# Canonical Sources

Generated first by `temp_artifact/20260504_research_prior_canonical_sources/download_and_convert_sources.py`.

Augmented by `temp_artifact/20260504_research_prior_canonical_sources/augment_prisma_docx_and_blockers.py`, scoped subagent logs, and 2026-05-05 manual browser PDF captures.

This directory stores local raw and Markdown copies of official/source-inventory documents where retrieval succeeded. Markdown conversions under `md/` are tracked in the GitHub draft so reviewers and agents can inspect canonical text without a separate corpus download. Raw captures under `raw/` remain local by default and may be distributed separately through Git LFS, release assets, object storage, or another large-file channel if needed. Licensing and source-specific reuse restrictions still apply.

Do not use this directory as the first route entrypoint. Start with `../route-source-index.yaml`, `../source_inventory/local_corpus_index.*`, and `../corpus_index/` to choose source IDs, documents, and line/page locators. Open `md/<source_id>/...` or `raw/<source_id>/...` only after that selection.

- raw files present: 210
- PDF raw files present: 63
- DOCX raw files present: 13
- Markdown files present: 210
- download/skip/failure/manual-capture attempt records: 254
- skipped records retained for non-mirrored bulk/commercial sources: 10

See `download_manifest.jsonl` for row-level paths, checksums, conversions, remaining failures, and manual-browser capture provenance.

## Script-Blocked URLs With Manual Browser Captures

The 2026-05-05 live recapture pass repaired `state_of_art_review_2022` and added ClinicalTrials.gov OpenAPI/version captures. A later user-assisted manual browser step added local PDF/Markdown captures for PRESS and CACM/ACM author pages. Simple scripted fetches for those sites still returned 403-style blocks, so the failed rows below remain in the manifest as refresh caveats rather than current local-evidence gaps.

- `press` `canonical`: https://www.cda-amc.ca/press-peer-review-electronic-search-strategies (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/press-peer-review-electronic-search-strategies'))
- `cacm_author_guidelines` `canonical`: https://cacm.acm.org/author-guidelines (HTTPError('403 Client Error: Forbidden for url: https://cacm.acm.org/author-guidelines'))
- `press` `canonical_cda_amc_press_page`: https://www.cda-amc.ca/press-peer-review-electronic-search-strategies (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/press-peer-review-electronic-search-strategies'))
- `press` `table_10_press_assessment_form_pdf`: https://www.cda-amc.ca/sites/default/files/PRESS_Peer_Review_Electronic_Search_Strate/Table_10_PRESS.pdf (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/sites/default/files/PRESS_Peer_Review_Electronic_Search_Strate/Table_10_PRESS.pdf'))
- `press` `table_9_press_evidence_checklist_pdf`: https://www.cda-amc.ca/sites/default/files/PRESS_Peer_Review_Electronic_Search_Strate/Table_9-PRESS.pdf (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/sites/default/files/PRESS_Peer_Review_Electronic_Search_Strate/Table_9-PRESS.pdf'))
- `press` `press_explanation_elaboration_pdf_2021_url`: https://www.cda-amc.ca/sites/default/files/attachments/2021-07/CP0015_PRESS_Update_Report_2016_0.pdf (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/sites/default/files/attachments/2021-07/CP0015_PRESS_Update_Report_2016_0.pdf'))
- `press` `press_explanation_elaboration_pdf_2023_url`: https://www.cda-amc.ca/sites/default/files/attachments/2023-06/PRESS%20Peer%20Review%20Electronic%20Search%20Strategies_%202015%20Guideline%20Explanation%20and%20Elaboration%20%28PRESS%20E%26E%29.pdf (HTTPError('403 Client Error: Forbidden for url: https://www.cda-amc.ca/sites/default/files/attachments/2023-06/PRESS%20Peer%20Review%20Electronic%20Search%20Strategies_%202015%20Guideline%20Explanation%20and%20Elaboration%20%28PRESS%20E%26E%29.pdf'))
- `cacm_author_guidelines` `canonical_author_guidelines`: https://cacm.acm.org/author-guidelines (HTTPError('403 Client Error: Forbidden for url: https://cacm.acm.org/author-guidelines'))
- `cacm_author_guidelines` `official_authors_acm_cacm_overview`: https://authors.acm.org/magazines/cacm (HTTPError('403 Client Error: Forbidden for url: https://authors.acm.org/magazines/cacm'))
- `cacm_author_guidelines` `official_acm_author_submissions`: https://www.acm.org/publications/authors/submissions (HTTPError('403 Client Error: Forbidden for url: https://www.acm.org/publications/authors/submissions'))
- `cacm_author_guidelines` `official_acm_information_for_authors`: https://www.acm.org/publications/authors/information-for-authors (HTTPError('403 Client Error: Forbidden for url: https://www.acm.org/publications/authors/information-for-authors'))

## Manual Browser Capture Notes

- `press`: use `md/press/manual_browser_pdf_press_ee_2015.md` as the primary local PRESS evidence. Hub/detail captures are locator/context pages.
- `cacm_author_guidelines`: use `md/cacm_author_guidelines/manual_browser_pdf_author_guidelines.md` as the primary local CACM evidence. ACM submissions and information-for-authors captures are publisher-level context.
- Browser print/PDF captures may include navigation, cookie, date, and footer artifacts.
- ACM/CACM guidance pages do not have an observed open license; verify reuse rights before public redistribution or long quotation.
