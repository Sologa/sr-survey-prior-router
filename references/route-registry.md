# Route Registry

This file is the main knowledge-navigation index. Route definitions live here; consult this index before changing router docs.

Each route should define: `route_id`, `trigger_terms`, `do_not_use_when`, `missing_context_signals`, `reference_files`, `lookup_surfaces`, `answer_guidance`, `risk_flags`, and `optional_notes`.

`reference_files` are relative to this `references/` directory. `optional_notes` are relative to the skill root and are background material, not required execution steps. When a route needs local full-document evidence, use `route-source-index.yaml` first and then the lazy indexes named there; do not open `canonical_sources/md/` directly from this registry. Lookup surfaces that name `corpus_index/sections/by_source/<source_id>.jsonl` mean "use when available locally"; in a public checkout without split section locators, fall back to `corpus_index/document_index.jsonl`, `source_inventory/source_cards_v2/<source_id>.md`, and targeted search inside selected canonical Markdown. When graphify is available, use `graphify-navigation.md` only after route selection and treat graph results as locators, not evidence.

## Routes

### `general_domain_prior`

- `route_id`: `general_domain_prior`
- `trigger_terms`: domain prior, knowledge packaging, large resource pile, agent prior, layered context, prepared corpus.
- `do_not_use_when`: the task is only about one SR guideline, one citation, or one paper-level claim.
- `missing_context_signals`: resource type, intended agent task, or known source locations are unclear.
- `reference_files`: `task-routing.md`, `source-map.md`, `retrieval-adapter-notes.md`, `graphify-navigation.md`, `route-source-index.yaml`.
- `lookup_surfaces`: repo search, file search/RAG, graphify when already available, MCP/resource connectors when configured, `source_inventory/local_corpus_index.*`, `corpus_index/document_index.jsonl`.
- `answer_guidance`: explain how material should be separated into policy, procedural notes if already present, source registry, retrieval corpus, tools, memory/state, and quality boundaries.
- `risk_flags`: monolithic prompt proposals; unsupported source-of-truth claims; blurred canonical-vs-derivative boundary.
- `optional_notes`: none.

### `survey_writing_prior`

- `route_id`: `survey_writing_prior`
- `trigger_terms`: survey writing resources, literature survey, related work, taxonomy, source cards, claim ledger, broad literature mapping, survey organization.
- `do_not_use_when`: the task is a formal systematic review or scoping review methods, conduct, reporting, checklist, JBI, PRISMA, or PRISMA-ScR question rather than broad survey organization.
- `missing_context_signals`: target survey scope, source collection path, or desired artifact type is unclear.
- `reference_files`: `task-routing.md`, `source-map.md`, `evidence-rules.md`, `source_inventory/coverage_report.md`, `route-source-index.yaml`.
- `lookup_surfaces`: citation-management, openalex-database, file search/RAG, graphify when already available, `source_inventory/local_corpus_index.*`, `corpus_index/sections/by_source/<source_id>.jsonl`.
- `answer_guidance`: describe source registry, taxonomy, source cards, claim ledger, and minimal writing support as knowledge layers, not mandatory outputs.
- `risk_flags`: author-reported claims blurred with agent synthesis; missing citation path for synthesized claims.
- `optional_notes`: `notes/synthesis-writing-note.md` only as background if the user asks how grounded writing should be structured.

### `sr_writing_prior`

- `route_id`: `sr_writing_prior`
- `trigger_terms`: systematic review writing, SR writing, scoping review writing, scoping review conduct, scoping review checklist, PRISMA, PRISMA-S, PRISMA-ScR, Cochrane, JBI, GRADE, AMSTAR 2, ROBIS, PRESS, PROSPERO.
- `do_not_use_when`: the task asks only for a tool feature such as screening UI or project management.
- `missing_context_signals`: review type, writing section, authority source, or corpus path is unclear.
- `reference_files`: `task-routing.md`, `source-map.md`, `evidence-rules.md`, `source_inventory/coverage_report.md`, `route-source-index.yaml`.
- `lookup_surfaces`: literature-review, citation-management, pubmed-database, clinicaltrials-database, openalex-database, `source_inventory/local_corpus_index.*`, `corpus_index/sections/by_source/<source_id>.jsonl`.
- `answer_guidance`: identify authority class, source role, likely evidence need, and provenance boundary.
- `risk_flags`: PROSPERO treated as methodology authority; workflow tools treated as methodology truth; guideline claims made without current authority evidence.
- `optional_notes`: Route formal scoping-review reporting/conduct/checklist/JBI/PRISMA-ScR tasks here. Route only broad literature mapping, taxonomy, or survey organization tasks to `survey_writing_prior`.

### `evidence_grounding`

- `route_id`: `evidence_grounding`
- `trigger_terms`: evidence extraction, source support, claim support, quote, page, span, evidence packet.
- `do_not_use_when`: the user asks for a high-level architecture without evaluating any concrete claim.
- `missing_context_signals`: claim text, candidate sources, corpus scope, or expected confidence level is unclear.
- `reference_files`: `evidence-rules.md`, `source-map.md`, `graphify-navigation.md`, `route-source-index.yaml`.
- `lookup_surfaces`: PDF/text search, file search/RAG, graphify when already available, citation-management, `corpus_index/document_index.jsonl`, `corpus_index/section_index_manifest.jsonl`, `corpus_index/sections/by_source/<source_id>.jsonl`.
- `answer_guidance`: use evidence packet fields and classify support as direct, indirect, conflicting, missing, background, or stale when the task needs claim support.
- `risk_flags`: support inferred from title/abstract alone when the scope does not allow it; missing source path or locator.
- `optional_notes`: `notes/evidence-extraction-note.md` only as a checklist for evidence-sensitive tasks.

### `source_audit`

- `route_id`: `source_audit`
- `trigger_terms`: source audit, citation audit, authority audit, source of truth, registry cleanup, provenance.
- `do_not_use_when`: the task is only to draft prose from already-accepted evidence.
- `missing_context_signals`: source list or registry path, audit question, or authority hierarchy is unclear.
- `reference_files`: `source-map.md`, `source_inventory/coverage_report.md`, `source_inventory/source_registry.yaml`, `source_inventory/local_corpus_index.md`, `route-source-index.yaml`, `evidence-rules.md`, `task-routing.md`.
- `lookup_surfaces`: repo search, citation-management, metadata inspection tools, `source_inventory/source_manifest.jsonl`, `canonical_sources/download_manifest.jsonl`, `corpus_index/document_index.jsonl`.
- `answer_guidance`: classify source role, authority level, freshness, scope, and not-for boundary when relevant.
- `risk_flags`: derivative artifacts promoted to canonical; stale or missing version/date fields ignored.
- `optional_notes`: `notes/source-grounding-audit-note.md` only as background for audit checklists.

### `synthesis_writing`

- `route_id`: `synthesis_writing`
- `trigger_terms`: synthesize, write related work, write survey section, write SR section, compare methods, summarize limitations.
- `do_not_use_when`: evidence packets or source registry are missing and the user asks for grounded writing.
- `missing_context_signals`: target section, audience, corpus scope, or accepted evidence support is unclear.
- `reference_files`: `task-routing.md`, `evidence-rules.md`, `source-map.md`, `source_inventory/coverage_report.md`, `route-source-index.yaml`.
- `lookup_surfaces`: citation-management, scientific-writing, literature-review, `source_inventory/local_corpus_index.*`, `corpus_index/sections/by_source/<source_id>.jsonl`.
- `answer_guidance`: preserve supported/uncertain separation and claim type labels when drafting or evaluating grounded prose.
- `risk_flags`: substantive claims without evidence or agent-inference labels; unresolved gaps hidden in prose.
- `optional_notes`: `notes/synthesis-writing-note.md` only as background if the user asks for writing structure.
