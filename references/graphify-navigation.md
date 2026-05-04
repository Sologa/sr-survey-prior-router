# Graphify Navigation

Graphify is an optional navigation backend for this staged router. It helps
agents find likely source IDs, document IDs, section IDs, and concept
neighborhoods without bulk-loading the canonical corpus.

Graphify output is a locator and triage artifact, not evidence. It does not
change the router's authority model.

## When It Is Worth Using

Use graphify when navigation, not source truth, is the bottleneck:

- the route and source indexes produce too many candidate sources.
- repeated tasks need cross-source concept or source-family lookup.
- the user asks how prepared resources connect across routes.
- graph traversal can reduce the number of source cards, index rows, or section
  locators that must be opened manually.

Do not build or consult a graph only because the corpus is large. Use it when it
reduces repeated lookup work.

## Default Scope

The default graph scope is the router and index surface, not the full backing
corpus. Run graphify from the skill root only after checking `.graphifyignore`.

Default included surface:

- `SKILL.md`
- `references/route-registry.md`
- `references/task-routing.md`
- `references/source-map.md`
- `references/retrieval-adapter-notes.md`
- `references/route-source-index.yaml`
- `references/source_inventory/source_registry.yaml`
- `references/source_inventory/local_corpus_index.md`
- `references/source_inventory/source_cards/*.md`
- `references/corpus_index/document_index.jsonl`
- `references/corpus_index/section_index_manifest.jsonl`

Default excluded surface:

- `references/canonical_sources/raw/`
- `references/canonical_sources/md/`
- `references/corpus_index/sections/by_source/`
- `graphify-out/`
- macOS AppleDouble metadata files

Selected section indexes may be graphed later only through an explicit scoped
run, after a route has already selected those sources.

## Query Ladder

Use graphify only after route selection:

```text
route-registry -> route-source-index -> local_corpus_index/source cards -> optional graphify query -> document/section locator -> selected canonical Markdown/raw source
```

If the graph is missing or stale, fall back to the normal route/index ladder.

## Acceptable Backends

Build or refresh the default index-scope graph from the skill root:

```sh
python3 scripts/build_graphify_index_graph.py
```

When `graphify-out/graph.json` exists, use one of these access modes:

```sh
graphify query "<question>" --graph graphify-out/graph.json --budget 1200
python3 -m graphify.serve graphify-out/graph.json
```

Depending on the installed graphify version, the MCP server may expose tools
such as `query_graph`, `get_node`, `get_neighbors`, `get_community`,
`god_nodes`, `graph_stats`, and `shortest_path`. Some graphify skill variants
also document `path` or `explain` CLI helpers; check `graphify --help` before
using those commands in this staged pack.

Do not run graphify install commands, hooks, watch mode, `add`, or `save-result`
from this staged pack unless the user explicitly asks to mutate runtime state.

## Result Contract

Convert graph output into a route-local locator before using it:

- `route_id`
- `query_intent`
- `corpus_scope`
- `retrieval_backend: graphify`
- `graph_path`
- `query`
- `traversal`
- `budget`
- `candidate_node_ids`
- `candidate_source_ids`
- `candidate_document_ids`
- `candidate_section_ids`
- `edge_confidence`
- `canonical_verification: false`
- `evidence_use: locator`

Only after this conversion should the agent open a selected section index or
canonical Markdown/raw source.

## Evidence Boundary

Graph nodes, graph edges, `GRAPH_REPORT.md`, source cards, and index rows are
derivative artifacts. They can support navigation decisions, but not
substantive claims.

For substantive claims:

1. Use graphify only to identify candidate sources or sections.
2. Open the selected section locator.
3. Open the selected canonical Markdown/raw source.
4. Build an evidence packet following `evidence-rules.md`.

Edges labeled `EXTRACTED`, `INFERRED`, or `AMBIGUOUS` are graph metadata.
`INFERRED` and `AMBIGUOUS` edges are investigation leads only. Even `EXTRACTED`
graph edges need canonical verification before they support a claim.

## Freshness Rules

Treat `graphify-out/` as rebuildable local output. A graph is stale when any of
these change:

- route definitions.
- source registry or source cards.
- local corpus indexes.
- section indexes included in an explicit graph scope.
- canonical source files used by an explicitly approved full-canonical graph.

If graph freshness is unclear, report that graph navigation was unavailable and
continue with the normal route/index ladder.

## Anti-Patterns

- Do not graphify the full canonical corpus by default.
- Do not bulk-load `references/canonical_sources/md/` because graphify returned
  broad or uncertain results.
- Do not treat `GRAPH_REPORT.md` as a methodology authority.
- Do not install graphify hooks or mutate runtime config from this staged pack.
- Do not use graphify to bypass blocked, missing, stale, or out-of-scope source
  records.
