# Source Integrity Repair Validation

Date: 2026-05-05

Scope: non-graphify repairs for PRISMA linked PDF stubs, Papers with Code redirect captures, and TACL/Computational Linguistics blocked-primary versus fallback provenance.

Supersession note: the PRISMA portion of this snapshot was later completed in `validation/prisma_2020_pdf_recapture_validation_2026-05-05.md`. The three PRISMA PMC rows are no longer `bad_capture`, and the two BMJ PDF rows are no longer `failed`.

Graphify supersession note: this repair snapshot deferred graphify refresh at the time it was written. That deferred state was later closed in `validation/graphify_refresh_validation_2026-05-05.md`; the live status is tracked in `validation/source_integrity_tracker.md`.

## Summary

- `prisma_2020`: initially downgraded three PMC linked `*.pdf` captures after live probes showed HTML stubs; a later same-day recapture replaced them with official PMC OA Cloud PDFs and added the two BMJ PDFs through White Rose repository copies.
- `paperswithcode`: downgraded `canonical_about` and `canonical_sota` to `bad_capture`; retained them as redirect provenance only and removed their 206 Hugging Face Trending sections.
- `tacl_submission`: made the MIT Press 403 primary locator and official TransACL fallback provenance explicit in manifest, document index, local corpus index, and source card.
- `computational_linguistics`: made the MIT Press 403 primary locator and official CL Journal OJS fallback provenance explicit in manifest, document index, local corpus index, and source card.
- `press` and `cacm_author_guidelines`: unchanged; manual browser capture provenance remains accepted.
- `graphify-out/`: not rebuilt or validated in this pass at the time of this snapshot. This was later superseded by `validation/graphify_refresh_validation_2026-05-05.md`.

## Live Probes

PRISMA PMC linked PDF probes before recapture:

- `https://pmc.ncbi.nlm.nih.gov/articles/instance/8005924/bin/pagm061899.w1.pdf`: HTTP 200 `text/html`, not PDF; body starts with "Preparing to download".
- `https://pmc.ncbi.nlm.nih.gov/articles/instance/8005924/bin/pagm061899.w2.pdf`: HTTP 200 `text/html`, not PDF; body starts with "Preparing to download".
- `https://pmc.ncbi.nlm.nih.gov/articles/instance/8005925/bin/pagm061901.w1.pdf`: HTTP 200 `text/html`, not PDF; body starts with "Preparing to download".
- `?download=1` and alternate NCBI paths did not produce a usable PDF.
- Later subagent research found official PMC OA Cloud object URLs for all three supplementary PDFs; those are now the local capture routes.

Papers with Code probes:

- `https://paperswithcode.com/about`: HTTP 302 to `https://huggingface.co/papers/trending`.
- `https://paperswithcode.com/sota`: HTTP 302 to `https://huggingface.co/papers/trending`.
- `https://portal.paperswithcode.com/` and `/site/data-policy`: scripted curl failed with SSL handshake failure in this environment.

TACL/Computational Linguistics probes:

- `https://direct.mit.edu/tacl/pages/submission-guidelines`: HTTP 403.
- `https://direct.mit.edu/coli`: HTTP 403.
- `https://transacl.org/index.php/tacl/about/submissions`: HTTP 200.
- `https://submissions.cljournal.org/index.php/cljournal/about/submissions`: HTTP 200.

## Local Validation

Commands run from `docs/agent_capability_packs/sr-survey-prior-router`:

```sh
python3 validation/validate_source_cards_v2.py
```

Result:

```text
source_cards_v2 validation: PASS
checked_cards: 65
source_manifest_sources: 65
```

```sh
for f in references/canonical_sources/download_manifest.jsonl references/corpus_index/document_index.jsonl references/corpus_index/section_index_manifest.jsonl references/source_inventory/source_manifest.jsonl; do jq -e . "$f" >/dev/null || exit 1; done
python3 -m json.tool references/source_inventory/local_corpus_index.json >/dev/null
```

Result: pass.

Bad-capture section contamination check:

```sh
rg -n 'linked_pagm061899|linked_pagm061901|canonical_about_trending|canonical_sota_trending' references/corpus_index/sections/by_source/prisma_2020.jsonl references/corpus_index/sections/by_source/paperswithcode.jsonl references/corpus_index/section_index_manifest.jsonl
```

Result: no matches.

Section manifest after same-day PRISMA recapture:

```text
paperswithcode  62   bad_capture_sections_removed=206
prisma_2020     584  prisma_pdf_recapture_complete_2026-05-05
```

Bad-capture manifest rows after same-day PRISMA recapture:

```text
paperswithcode   canonical_about           bad_capture  redirected_to_huggingface_trending  do_not_use_for_paperswithcode_claims
paperswithcode   canonical_sota            bad_capture  redirected_to_huggingface_trending  do_not_use_for_paperswithcode_claims
```

## Superseded Deferred Work

At the time of this snapshot, graphify artifacts were stale relative to the source-index changes. That work has since been completed and validated in `validation/graphify_refresh_validation_2026-05-05.md`; use `validation/source_integrity_tracker.md` for the current live status.
