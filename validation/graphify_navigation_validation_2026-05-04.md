# Graphify Navigation Validation

Date: 2026-05-04

Scope: validate the staged addition of a graphify-backed lazy navigation
contract and the generated index-scope graph for `sr-survey-prior-router`.

## Decision

Worth doing as a staged optional locator with a real index-scope graph.

The value is not that graphify becomes a new source of truth. The value is that
the generated graph can narrow candidate route, source, document, and section
neighborhoods before the agent opens canonical source text.

## Implemented Surface

- `references/graphify-navigation.md`: optional graphify use, scope, query
  ladder, result contract, evidence boundary, freshness rules, and
  anti-patterns.
- `SKILL.md`: route-first navigation now allows graphify only after route
  selection and keeps graph output non-canonical.
- `references/retrieval-adapter-notes.md`: graphify is documented as an
  optional backend-neutral navigation layer.
- `references/route-registry.md`: graphify navigation is referenced for routes
  where knowledge architecture or evidence narrowing may need relationship
  lookup.
- `references/route-source-index.yaml`: records graphify under optional
  navigation backends.
- `references/source-map.md`: lists the graphify navigation contract and
  rebuildable `graphify-out/` boundary.
- `.graphifyignore` and `.gitignore`: keep the full canonical backing corpus,
  split section indexes, and generated graphify output out of the default
  graph/navigation surface.
- `scripts/build_graphify_index_graph.py`: reproducibly builds the default
  graphify-compatible graph from route/source/index metadata without reading or
  embedding canonical fulltext paths.
- `graphify-out/graph.json`: generated graphify-compatible node-link graph.
- `graphify-out/GRAPH_REPORT.md`: generated report for graph scope, summary,
  core nodes, communities, and evidence boundary.
- `graphify-out/manifest.json`: generated build manifest with input checksums
  and graph counts.
- `graphify-out/graph.html`: generated local interactive visualization.
- `validation/validate_graphify_navigation.py`: deterministic contract checks.

## Validation Invariants

- Graphify is optional and must not be required for normal route lookup.
- The default graph scope is the index/router surface, not the full canonical
  corpus.
- `references/canonical_sources/raw/`, `references/canonical_sources/md/`, and
  all split `references/corpus_index/sections/by_source/` files stay excluded
  from default graphify runs.
- Graph output, `GRAPH_REPORT.md`, source cards, and indexes are locator-only.
- Substantive claims still require selected canonical Markdown/raw spans and
  evidence packets.
- `EXTRACTED`, `INFERRED`, and `AMBIGUOUS` graph edges are graph metadata, not
  claim support by themselves.
- The staged pack does not install graphify hooks, activate runtime config, or
  mutate `AGENTS.md`.

## Checks To Run

```sh
cd docs/agent_capability_packs/sr-survey-prior-router
python3 -m pip install -r requirements.txt
python3 scripts/build_graphify_index_graph.py
python3 validation/validate_graphify_navigation.py
```

Optional graphify smoke check from the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
from graphify.detect import detect
root = Path("docs/agent_capability_packs/sr-survey-prior-router")
result = detect(root)
files = [f for values in result["files"].values() for f in values]
assert result["graphifyignore_patterns"] > 0
assert not any("canonical_sources/raw" in f for f in files)
assert not any("canonical_sources/md" in f for f in files)
assert not any("corpus_index/sections/by_source" in f for f in files)
print(result["total_files"], result["total_words"], result["graphifyignore_patterns"])
PY
```

## Current Results

Generated graph:

```json
{
  "nodes": 363,
  "edges": 1336,
  "communities": 44,
  "scope": "router_index_graph"
}
```

Graphify detect smoke check:

```json
{
  "total_files": 24,
  "total_words": 11127,
  "graphifyignore_patterns": 8,
  "graphify_out_hits": 0,
  "canonical_raw_hits": 0,
  "canonical_md_hits": 0,
  "section_by_source_hits": 0
}
```

Generated output scope check:

```sh
rg -n "references/canonical_sources/(raw|md)/|references/corpus_index/sections/by_source/|refs_old/|upstream_repo/" graphify-out
```

Result: no matches in `graphify-out/`.

Graphify query smoke check:

```sh
graphify query "PRISMA checklist systematic review reporting" --graph graphify-out/graph.json --budget 900
```

Result: returned route/source neighborhoods including `sr_writing_prior`,
`evidence_grounding`, `synthesis_writing`, `prisma_2020`, `cochrane_handbook`,
and `sr_reporting_and_conduct`, using only router/index source files as graph
source locations.

## Residual Risk

This validates graph existence, scope, queryability, and safety boundaries. It
does not make graph nodes or edges evidentiary. Representative substantive
claims still need a follow-up validation that selects a graph candidate, opens
the corresponding document/section locator, and verifies the claim against the
canonical Markdown/raw source.
