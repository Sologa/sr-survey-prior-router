# Corpus Index

Generated: 2026-05-03T19:11:29+00:00

These indexes are locator artifacts for the local canonical source corpus.
They do not replace canonical sources and should not be treated as claim evidence by themselves.

- `document_index.jsonl`: one row per local Markdown document.
- `section_index_manifest.jsonl`: one row per source-level section index.
- `sections/by_source/<source_id>.jsonl`: one row per Markdown heading or page-style section for that source only.

Document rows: 201
Section rows: 4578

## Documents By Family

- `codex_skill_packaging`: 2
- `nlp_speech_cs_exemplar_sources`: 32
- `scholarly_databases_and_apis`: 47
- `sr_certainty_appraisal_bias_search`: 20
- `sr_reporting_and_conduct`: 65
- `survey_writing_methods`: 35

## Use

1. Select a route in `../route-registry.md`.
2. Use `../route-source-index.yaml` and `../source_inventory/local_corpus_index.md` to choose source IDs.
3. Query `document_index.jsonl` for candidate documents under those source IDs.
4. Query `section_index_manifest.jsonl` for the source-level section index, then query only that source's `sections/by_source/<source_id>.jsonl` for line/page locators.
5. Verify important claims against the selected canonical Markdown or raw source.
