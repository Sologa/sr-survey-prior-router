# Source Map

This staged pack now contains a seed source inventory under `source_inventory/` plus a first downloaded source corpus under `canonical_sources/`. The inventory records candidate official, method-authority, venue, and database sources for future survey/SR prior work. The local corpus contains raw documents and Markdown conversions where retrieval succeeded; it is still not an exhaustive retrieval corpus for every listed API, venue, or blocked source.

## Implemented Seed Artifacts

- `source_inventory/coverage_report.md`: coverage status, scope limits, and recommended gates before claiming knowledge-heavy coverage.
- `source_inventory/source_manifest.jsonl`: row-level source inventory with URLs, authority class, scope, not-for boundary, fit, and validation status.
- `source_inventory/source_registry.yaml`: curated grouped registry for router use.
- `source_inventory/source_cards/*.md`: compressed family-level source cards for fast bootstrapping.
- `source_inventory/local_corpus_index.md` and `.json`: source-level lazy-load index for local Markdown/raw availability.
- `route-source-index.yaml`: route-to-source bridge with priority source IDs, source-card defaults, and first-load limits.
- `corpus_index/document_index.jsonl`: document-level locator index for the local Markdown corpus.
- `corpus_index/section_index_manifest.jsonl`: source-level manifest for split section indexes.
- `corpus_index/sections/by_source/<source_id>.jsonl`: section/page/heading locators for one selected source at a time.
- `graphify-navigation.md`: optional graph navigation contract for narrowing candidate sources/sections without treating graph output as evidence.
- `../scripts/build_graphify_index_graph.py`: rebuilds the index-scope graphify graph without reading canonical fulltext.
- `../graphify-out/graph.json`, `GRAPH_REPORT.md`, `manifest.json`, and `graph.html`: rebuildable local graph outputs for route/source/document/section navigation.
- `canonical_sources/raw/<source_id>/`: downloaded source documents, including HTML, PDF, and DOCX where available.
- `canonical_sources/md/<source_id>/`: Markdown conversions for local model reading.
- `canonical_sources/download_manifest.jsonl`: row-level download attempts, checksums, local paths, conversion status, and remaining blocked URLs.
- `../validation/agent_qa_validation_2026-05-04.md`: two-agent validation of route-first and lazy-load behavior.

Treat these as seed inventory and local-corpus artifacts. For important claims, follow each row back to the canonical URL or local canonical path before writing a supported conclusion.

## Local Corpus Boundary

`canonical_sources/raw/` and `canonical_sources/md/` are the complete local backing corpus, not the normal route boot surface. Agents should reach them through `route-source-index.yaml`, `source_inventory/local_corpus_index.*`, `corpus_index/document_index.jsonl`, and the selected `corpus_index/sections/by_source/<source_id>.jsonl` file.

For GitHub-facing review or future publication of this pack, keep the portable surface small: router docs, registries, source cards, coverage reports, source-level/document-level indexes, `corpus_index/section_index_manifest.jsonl`, `canonical_sources/README.md`, and `canonical_sources/download_manifest.jsonl`. The raw/Markdown corpus and split `corpus_index/sections/by_source/` locators are generated/local backing data and should not be treated as ordinary PR review material unless a maintainer explicitly chooses Git LFS, release assets, object storage, or another large-file channel.

## Suggested Artifact Types

- `source_manifest.jsonl`: row-level inventory of source files, URLs, docs, papers, guidelines, and tool pages.
- `source_registry.yaml`: curated authority map with source role, version/date, scope, load mode, and QA gate.
- `taxonomy.yaml`: domain taxonomy for concepts, review types, source roles, and synthesis dimensions.
- `source_cards/*.md` or `source_cards/*.yaml`: compressed per-source cards for fast bootstrapping.
- `document_index.jsonl` and split `sections/by_source/<source_id>.jsonl`: locator indexes for lazy fulltext access.
- `graphify-out/`: optional rebuildable graph navigation output, kept local and locator-only unless a maintainer explicitly chooses a durable distribution channel.
- `claim_ledger.jsonl`: claim-to-source ledger for synthesized writing and audits.
- `tool_registry.yaml`: workflow tools, APIs, licenses, capabilities, limits, and not-for boundaries.

Some names above are still placeholders for future or external artifacts. If a task depends on one of them, first verify whether it actually exists in the current project.

## Suggested Registry Fields

- `source_id`
- `type`
- `authority_level`
- `version_date`
- `applies_to`
- `not_for`
- `load_mode`
- `retrieval_tags`
- `qa_gate`
- `canonical_path`
- `derivative_paths`

## Authority Classes

- `project_policy`: repo rules such as `AGENTS.md` and task-specific safety boundaries.
- `methodology_guideline`: reporting or conduct authorities such as PRISMA, Cochrane, JBI, Campbell, GRADE, AMSTAR 2, ROBIS, or PRESS.
- `primary_research`: papers or datasets being reviewed.
- `tool_documentation`: software docs, API docs, workflow tools, and platform pages.
- `registry_database`: registries and bibliographic databases such as PROSPERO, PubMed, ClinicalTrials.gov, WHO ICTRP, or OpenAlex.
- `derivative_summary`: source cards, compiled wiki, RAG chunks, previous chat summaries, and agent-generated reports.

## Canonical vs Derivative

Canonical sources can support claims directly when they are current and in scope. Derivative artifacts can help locate evidence, but important claims must be traced back to canonical sources before being written as supported conclusions.
