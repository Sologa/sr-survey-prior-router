# Retrieval Adapter Notes

The retrieval layer is backend-neutral. Do not bind the staged knowledge router to `llm-wiki-compiler`, file search, custom RAG, graphify, MCP, or any single implementation.

## Conceptual Flow

```text
query_intent -> corpus_scope -> retrieval_backend -> evidence_packet -> canonical_verification
```

For the local canonical corpus, use this lookup ladder before opening full text:

```text
route-registry -> route-source-index -> local_corpus_index -> document_index -> sections/by_source/<source_id> -> selected canonical Markdown/raw source
```

When graphify navigation is available, insert it only after route and source-scope selection:

```text
route-registry -> route-source-index -> local_corpus_index/source cards -> graphify navigation -> document_index/section locator -> selected canonical Markdown/raw source
```

Use `graphify-navigation.md` for graph-specific rules. Graph results are locators and relationship leads; important claims still need canonical verification.

## Useful Fields

- `query_intent`: what the user needs, such as definition, authority check, claim support, comparison, limitation, or source discovery.
- `corpus_scope`: allowed source set, review id, source registry subset, paper collection, guideline family, or tool registry slice.
- `retrieval_backend`: the concrete lookup method used for this run.
- `evidence_packet`: source-grounded packet following `evidence-rules.md`.
- `canonical_verification`: whether the returned evidence was checked against the canonical source or only a derivative.

## Good Retrieval Results Expose

- source identifier and source path.
- chunk/span/page or equivalent locator.
- document ID and section ID when the local corpus index supplied them.
- whether the result is canonical or derivative.
- date/version metadata when available.
- query used or enough parameters to reproduce the lookup.

## Upgrade Signals

Consider a compiled wiki, file search, custom RAG, or MCP resource layer when:

- routes repeatedly need cross-document lookup.
- source cards no longer locate evidence quickly.
- evidence coverage failures come from search/discovery rather than missing sources.
- citation tracing becomes too expensive by manual path inspection.
- the same corpus must serve multiple knowledge routes.

Consider graphify specifically when:

- source cards and route indexes repeatedly produce too many candidates.
- cross-document concept neighborhoods are useful before opening source text.
- an existing graph can answer a relationship/path question inside a small token budget.
- graph traversal can produce source/document/section candidates that are then verified canonically.

Do not upgrade only because the number of reference files grew. Upgrade when retrieval behavior is the bottleneck.
