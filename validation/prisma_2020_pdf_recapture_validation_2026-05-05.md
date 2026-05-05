# PRISMA 2020 PDF Recapture Validation

Date: 2026-05-05

Scope: close every remaining `prisma_2020` manifest gap after the earlier source-integrity repair identified two failed BMJ PDF rows and three PMC linked-PDF HTML stubs.

## Result

All five target rows now have real local PDF raw files and Markdown conversions.

| label | local raw file | pages | capture route | direct/original URL result |
| --- | --- | ---: | --- | --- |
| `paper_bmj_statement_pdf` | `references/canonical_sources/raw/prisma_2020/paper_bmj_statement_pdf_bmj.n71.full.pdf.pdf` | 10 | White Rose repository copy of BMJ PDF: `https://eprints.whiterose.ac.uk/id/eprint/173303/1/bmj.n71.full.pdf` | BMJ direct PDF returned HTTP 403 text/html in this environment. |
| `paper_bmj_explanation_elaboration_pdf` | `references/canonical_sources/raw/prisma_2020/paper_bmj_explanation_elaboration_pdf_bmj.n160.full.pdf.pdf` | 37 | White Rose repository copy of BMJ PDF: `https://eprints.whiterose.ac.uk/id/eprint/173314/1/bmj.n160.full.pdf` | BMJ direct PDF returned HTTP 403 text/html in this environment. |
| `linked_pagm061899.w1.pdf` | `references/canonical_sources/raw/prisma_2020/linked_pagm061899.w1.pdf_pagm061899.w1.pdf.pdf` | 2 | PMC OA Cloud: `https://pmc-oa-opendata.s3.amazonaws.com/PMC8005924.1/pagm061899.w1.pdf` | PMC instance/bin URL returned HTTP 200 text/html "Preparing to download", not PDF. |
| `linked_pagm061899.w2.pdf` | `references/canonical_sources/raw/prisma_2020/linked_pagm061899.w2.pdf_pagm061899.w2.pdf.pdf` | 8 | PMC OA Cloud: `https://pmc-oa-opendata.s3.amazonaws.com/PMC8005924.1/pagm061899.w2.pdf` | PMC instance/bin URL returned HTTP 200 text/html "Preparing to download", not PDF. |
| `linked_pagm061901.w1.pdf` | `references/canonical_sources/raw/prisma_2020/linked_pagm061901.w1.pdf_pagm061901.w1.pdf.pdf` | 75 | PMC OA Cloud: `https://pmc-oa-opendata.s3.amazonaws.com/PMC8005925.1/pagm061901.w1.pdf` | PMC instance/bin URL returned HTTP 200 text/html "Preparing to download", not PDF. |

## Subagent Findings Used

- BMJ route subagent found no working BMJ-hosted direct PDF route from this environment. It identified White Rose and UCL repository PDFs; White Rose was selected for both BMJ artifacts.
- PMC route subagent found that the `instance/.../bin/*.pdf` URLs are HTML stubs, but the original supplementary PDFs are available through official PMC OA Cloud objects and the NCBI deprecated OA package tarballs.
- Local audit subagent enumerated the exact five manifest rows, target raw paths, and target Markdown paths that needed closure.

## Local Updates

- `references/canonical_sources/download_manifest.jsonl`: all five target rows now have `status=downloaded`, `content_type=application/pdf`, SHA-256, byte count, page count, `raw_path`, `md_path`, and capture provenance.
- `references/source_inventory/source_manifest.jsonl`: `prisma_2020` now has 26 local documents, 26 usable documents, and zero bad local documents.
- `references/source_inventory/local_corpus_index.json` and `.md`: `prisma_2020` now reports 26 local raw/Markdown documents and no bad/stub paths.
- `references/corpus_index/document_index.jsonl`: the three PMC rows were promoted from `bad_capture` to evidence-usable document locators; two BMJ PDF locators were added.
- `references/corpus_index/section_index_manifest.jsonl` and `sections/by_source/prisma_2020.jsonl`: PRISMA 2020 section locators were regenerated after recapture.
- `references/source_inventory/source_cards_v2/prisma_2020.md`: provenance caveats now point to the successful recapture routes instead of treating the three PMC rows as bad-capture evidence.

## Verification Commands

```sh
for f in \
  references/canonical_sources/raw/prisma_2020/paper_bmj_statement_pdf_bmj.n71.full.pdf.pdf \
  references/canonical_sources/raw/prisma_2020/paper_bmj_explanation_elaboration_pdf_bmj.n160.full.pdf.pdf \
  references/canonical_sources/raw/prisma_2020/linked_pagm061899.w1.pdf_pagm061899.w1.pdf.pdf \
  references/canonical_sources/raw/prisma_2020/linked_pagm061899.w2.pdf_pagm061899.w2.pdf.pdf \
  references/canonical_sources/raw/prisma_2020/linked_pagm061901.w1.pdf_pagm061901.w1.pdf.pdf
do
  file "$f"
  pdfinfo "$f" | rg '^Pages:'
done
```

Observed page counts: 10, 37, 2, 8, and 75.

```sh
jq -r 'select(.source_id=="prisma_2020") | [.label,.status,.content_type,.page_count] | @tsv' references/canonical_sources/download_manifest.jsonl
```

Result: no `failed` or `bad_capture` rows remain for `prisma_2020`.

```sh
python3 validation/validate_source_cards_v2.py
```

Result:

```text
source_cards_v2 validation: PASS
checked_cards: 65
source_manifest_sources: 65
```

Additional local gates passed: JSON/JSONL parsing for updated manifests and indexes, no remaining `prisma_2020` `failed`/`bad_capture` manifest rows, `git diff --check`, and no remaining macOS `._*` metadata files under the pack.

## Provenance Caveat

The local PDFs are complete captures, but two BMJ rows are not direct BMJ-hosted downloads because BMJ returned HTTP 403 from this environment. They are repository copies of the published BMJ PDFs. The three PMC supplementary rows are official PMC OA Cloud object captures, because the human-facing PMC `instance/.../bin/*.pdf` links returned HTML download stubs.
