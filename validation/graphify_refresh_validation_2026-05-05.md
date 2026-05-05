# Graphify Refresh Validation

Date: 2026-05-05

Scope: `docs/agent_capability_packs/sr-survey-prior-router`.

## Command

Run from the pack root:

```sh
python3 scripts/build_graphify_index_graph.py
python3 validation/validate_graphify_navigation.py
```

## Result

`scripts/build_graphify_index_graph.py` regenerated:

- `graphify-out/graph.json`
- `graphify-out/graph.html`
- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/manifest.json`

Builder output:

```json
{
  "nodes": 376,
  "edges": 1390,
  "communities": 46,
  "scope": "router_index_graph",
  "metadata_removed": 4
}
```

`validation/validate_graphify_navigation.py` passed.

## Freshness Checks

The refreshed `graphify-out/manifest.json` records:

```json
{
  "generated_at_utc": "2026-05-05T09:36:27+00:00",
  "scope": "router_index_graph",
  "evidence_use": "locator_only",
  "canonical_verification_required": true,
  "graph": {
    "connected_components": 7,
    "edges": 1390,
    "nodes": 376
  },
  "input_stats": {
    "source_manifest_rows": 65,
    "document_rows": 212,
    "section_index_rows": 65,
    "sources": 65,
    "routes": 6,
    "families": 6
  }
}
```

The post-refresh subagent verifier confirmed that current graph node counts align
with `document_index.jsonl` and `section_index_manifest.jsonl`: 212 document
locator nodes, 65 section-index locator nodes, 65 source nodes, 6 route nodes,
6 family nodes, 12 artifact nodes, 5 concept nodes, and 5 source-card nodes.

## Evidence Boundary

The graph remains a locator-only artifact:

- `scope=router_index_graph`
- `evidence_use=locator_only`
- `canonical_verification_required=true`
- Graph outputs do not contain `references/canonical_sources/raw/`.
- Graph outputs do not contain `references/canonical_sources/md/`.
- Graph outputs do not contain `references/corpus_index/sections/by_source/`.

This preserves the intended route-first, lazy-load behavior: graphify may help
identify candidate route/source/document/section IDs, but substantive claims
still require selected canonical Markdown/raw verification through
`references/evidence-rules.md`.
