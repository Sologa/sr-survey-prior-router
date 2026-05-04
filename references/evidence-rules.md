# Evidence Rules

Evidence packets connect claims to sources. Grounded SR/survey claims, source audits, and synthesis writing usually need this kind of source trace.

## Typical Evidence Packet Fields

Useful evidence packets include:

- `source_id`: stable source key from the source registry or manifest.
- `doc_id`: stable document key from `corpus_index/document_index.jsonl` when local corpus evidence is used.
- `section_id`: section/page locator from `corpus_index/sections/by_source/<source_id>.jsonl` when available.
- `source_path`: local path, URL, DOI, or registry pointer.
- `section`: source section, table, figure, abstract, methods, or metadata field.
- `span_or_page`: page, paragraph, line range, chunk id, or text span when available.
- `quote_or_summary`: short quote when allowed, otherwise a concise source-faithful summary.
- `support_type`: `direct`, `indirect`, `conflicting`, `missing`, `background`, or `stale`.
- `confidence`: `high`, `medium`, or `low`, based on source authority and span specificity.
- `freshness`: version/date check, such as `current_checked`, `dated_source`, `unknown_date`, or `likely_stale`.

## Claim Type Labels

SR and survey writing should label claim origin when the distinction matters:

- `reported_by_authors`: the source authors state the claim.
- `guideline_requirement`: a guideline or method authority requires or recommends it.
- `tool_capability`: a software/tool claims or demonstrates the capability.
- `agent_inference`: the agent synthesized or inferred the claim from evidence.

## Source Support Rules

- Use `direct` only when the cited span states the claim without material inference.
- Use `indirect` when multiple source facts are combined.
- Use `conflicting` when credible sources disagree or the same source has tension.
- Use `missing` when no adequate source was found in the consulted corpus.
- Use `stale` freshness when version-sensitive guidance was not checked against a current source.
- For local corpus evidence, an index row is only a locator. Verify the claim against the selected `canonical_sources/md/<source_id>/...` file or raw source before marking support as `direct`.
- Rows marked `blocked`, `bad_capture`, or `no_local_docs` cannot support `direct` local evidence; use `missing`, `background`, or a locator-only status until usable source content is captured.
- Rows or documents with `content_quality: entry_point_stub`, `evidence_use: locator_only`, or `conversion_depth` containing `stub` are locator-only by default. Mark support as `direct` only after selecting a non-stub local document or current official source span that states the claim.

## SR/Synthesis Guardrails

- PRISMA, PRISMA-S, PRISMA-P, Cochrane, JBI, Campbell, GRADE, GRADE-CERQual, AMSTAR 2, ROBIS, and PRESS are authority candidates, but each claim still needs a versioned source.
- PROSPERO is a registry, not a methodology authority.
- EQUATOR PRISMA is a registry/update locator; use primary PRISMA source rows for PRISMA method or reporting claims.
- RevMan, Covidence, Rayyan, ASReview, EPPI-Reviewer, DistillerSR, and SRDR+ are workflow/tool sources, not methodology truth sources.
- Source cards, source cards v2, corpus indexes, compiled wiki pages, RAG snippets, and previous chat summaries are derivative aids; verify important claims against canonical sources.
