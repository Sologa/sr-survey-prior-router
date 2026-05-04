#!/usr/bin/env python3
"""Build a scoped graphify graph for the sr-survey-prior-router indexes.

The graph intentionally covers the router/index surface only. It does not read
canonical fulltext Markdown/raw files and does not embed canonical file paths in
graph output. Use the graph as a locator, then verify claims against selected
canonical sources through the normal route/index ladder.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import networkx as nx
import yaml
from graphify.analyze import god_nodes, surprising_connections
from graphify.cluster import cluster, score_all
from graphify.export import to_html, to_json


SKILL_ROOT_MARKER = "SKILL.md"
DEFAULT_OUTPUT_DIR = "graphify-out"

FORBIDDEN_OUTPUT_PATTERNS = (
    "references/canonical_sources/raw/",
    "references/canonical_sources/md/",
    "references/corpus_index/sections/by_source/",
    "refs_old/",
    "upstream_repo/",
)

CORE_INPUTS = (
    "SKILL.md",
    "scripts/build_graphify_index_graph.py",
    "references/route-registry.md",
    "references/task-routing.md",
    "references/source-map.md",
    "references/retrieval-adapter-notes.md",
    "references/graphify-navigation.md",
    "references/route-source-index.yaml",
    "references/source_inventory/source_registry.yaml",
    "references/source_inventory/source_manifest.jsonl",
    "references/source_inventory/local_corpus_index.json",
    "references/source_inventory/local_corpus_index.md",
    "references/corpus_index/document_index.jsonl",
    "references/corpus_index/section_index_manifest.jsonl",
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{lineno}: invalid JSONL row: {exc}") from exc
    return rows


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data or {}


def relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def add_node(G: nx.Graph, node_id: str, **attrs: Any) -> None:
    base = {
        "label": node_id,
        "file_type": "document",
        "source_file": "",
        "scope": "router_index_graph",
    }
    base.update({k: v for k, v in attrs.items() if v is not None})
    G.add_node(node_id, **base)


def add_edge(
    G: nx.Graph,
    source: str,
    target: str,
    relation: str,
    *,
    confidence: str = "EXTRACTED",
    source_file: str = "",
    note: str = "",
) -> None:
    if source not in G or target not in G:
        return
    G.add_edge(
        source,
        target,
        relation=relation,
        confidence=confidence,
        source_file=source_file,
        _src=source,
        _tgt=target,
        note=note,
    )


def add_artifacts(G: nx.Graph, root: Path) -> dict[str, str]:
    artifacts = {
        "artifact:skill": "SKILL.md",
        "artifact:route_registry": "references/route-registry.md",
        "artifact:task_routing": "references/task-routing.md",
        "artifact:source_map": "references/source-map.md",
        "artifact:retrieval_adapter": "references/retrieval-adapter-notes.md",
        "artifact:graphify_navigation": "references/graphify-navigation.md",
        "artifact:route_source_index": "references/route-source-index.yaml",
        "artifact:source_registry": "references/source_inventory/source_registry.yaml",
        "artifact:source_manifest": "references/source_inventory/source_manifest.jsonl",
        "artifact:local_corpus_index": "references/source_inventory/local_corpus_index.json",
        "artifact:document_index": "references/corpus_index/document_index.jsonl",
        "artifact:section_index_manifest": "references/corpus_index/section_index_manifest.jsonl",
    }
    for node_id, file_path in artifacts.items():
        path = root / file_path
        add_node(
            G,
            node_id,
            label=file_path,
            node_kind="artifact",
            file_type="document",
            source_file=file_path,
            exists=path.exists(),
        )
    return artifacts


def build_graph(root: Path) -> tuple[nx.Graph, dict[str, Any]]:
    route_index_path = root / "references/route-source-index.yaml"
    source_registry_path = root / "references/source_inventory/source_registry.yaml"
    source_manifest_path = root / "references/source_inventory/source_manifest.jsonl"
    local_corpus_path = root / "references/source_inventory/local_corpus_index.json"
    doc_index_path = root / "references/corpus_index/document_index.jsonl"
    section_manifest_path = root / "references/corpus_index/section_index_manifest.jsonl"

    route_index = read_yaml(route_index_path)
    source_registry = read_yaml(source_registry_path)
    source_manifest_rows = read_jsonl(source_manifest_path)
    document_rows = read_jsonl(doc_index_path)
    section_rows = read_jsonl(section_manifest_path)
    local_corpus = json.loads(local_corpus_path.read_text(encoding="utf-8")) if local_corpus_path.exists() else {}

    G = nx.Graph()
    artifact_nodes = add_artifacts(G, root)

    concept_nodes = {
        "concept:lazy_loading": "Lazy-loaded knowledge access",
        "concept:locator_only": "Graph output is locator-only",
        "concept:canonical_verification": "Canonical source verification",
        "concept:evidence_boundary": "Derivative artifacts are not evidence",
        "concept:index_scope_graph": "Index-scope graph",
    }
    for node_id, label in concept_nodes.items():
        add_node(
            G,
            node_id,
            label=label,
            node_kind="concept",
            file_type="document",
            source_file="references/graphify-navigation.md",
        )

    add_edge(G, "artifact:skill", "concept:lazy_loading", "requires", source_file="SKILL.md")
    add_edge(
        G,
        "artifact:graphify_navigation",
        "concept:locator_only",
        "defines",
        source_file="references/graphify-navigation.md",
    )
    add_edge(
        G,
        "artifact:graphify_navigation",
        "concept:index_scope_graph",
        "defines_default_scope",
        source_file="references/graphify-navigation.md",
    )
    add_edge(
        G,
        "concept:locator_only",
        "concept:canonical_verification",
        "must_be_followed_by",
        source_file="references/graphify-navigation.md",
    )
    add_edge(
        G,
        "concept:evidence_boundary",
        "concept:canonical_verification",
        "requires",
        source_file="references/evidence-rules.md",
    )

    families = source_registry.get("families", {})
    family_to_sources: dict[str, list[str]] = {}
    source_to_family: dict[str, str] = {}
    for family_id, family_data in families.items():
        add_node(
            G,
            f"family:{family_id}",
            label=family_id,
            node_kind="family",
            file_type="document",
            source_file="references/source_inventory/source_registry.yaml",
            authority_type=family_data.get("authority_type"),
            coverage_state=family_data.get("coverage_state"),
            canonicality=family_data.get("canonicality"),
            scope_summary=family_data.get("scope"),
        )
        source_ids = family_data.get("source_ids", []) or []
        family_to_sources[family_id] = list(source_ids)
        for source_id in source_ids:
            source_to_family[source_id] = family_id
        card_ref = family_data.get("source_card_ref")
        if card_ref:
            card_node = f"source_card:{Path(card_ref).stem}"
            card_path = f"references/source_inventory/{card_ref}"
            add_node(
                G,
                card_node,
                label=card_ref,
                node_kind="source_card",
                file_type="document",
                source_file=card_path,
            )
            add_edge(
                G,
                card_node,
                f"family:{family_id}",
                "summarizes_family",
                source_file="references/source_inventory/source_registry.yaml",
            )

    manifest_by_source = {row.get("source_id"): row for row in source_manifest_rows if row.get("source_id")}
    local_by_source = local_corpus if isinstance(local_corpus, dict) else {}
    all_source_ids = set(source_to_family) | set(manifest_by_source) | set(local_by_source)

    for source_id in sorted(all_source_ids):
        manifest = manifest_by_source.get(source_id, {})
        local = local_by_source.get(source_id, {})
        family = manifest.get("family") or local.get("family") or source_to_family.get(source_id)
        add_node(
            G,
            f"source:{source_id}",
            label=f"{source_id}: {manifest.get('title') or local.get('title') or source_id}",
            node_kind="source",
            file_type="document",
            source_file="references/source_inventory/source_manifest.jsonl",
            source_id=source_id,
            family=family,
            title=manifest.get("title") or local.get("title"),
            authority_class=manifest.get("authority_class") or local.get("authority_class"),
            source_type=manifest.get("source_type"),
            status=local.get("status") or manifest.get("local_bundle_status"),
            validation_status=manifest.get("validation_status"),
            local_docs_count=local.get("local_docs_count"),
            md_docs_count=local.get("md_docs_count"),
            canonical_url=manifest.get("canonical_url") or local.get("canonical_url"),
            locator_rule="resolve document/section paths through corpus indexes; graph output intentionally omits canonical paths",
        )
        if family:
            add_edge(
                G,
                f"family:{family}",
                f"source:{source_id}",
                "contains_source",
                source_file="references/source_inventory/source_registry.yaml",
            )

    routes = (route_index.get("routes") or {})
    for route_id, route_data in routes.items():
        add_node(
            G,
            f"route:{route_id}",
            label=route_id,
            node_kind="route",
            file_type="document",
            source_file="references/route-source-index.yaml",
            evidence_gate=route_data.get("evidence_gate"),
        )
        add_edge(
            G,
            "artifact:route_source_index",
            f"route:{route_id}",
            "declares_route",
            source_file="references/route-source-index.yaml",
        )
        add_edge(
            G,
            f"route:{route_id}",
            "concept:locator_only",
            "may_use_graphify_as",
            source_file="references/route-source-index.yaml",
        )
        for family_id in route_data.get("primary_families", []) or []:
            add_edge(
                G,
                f"route:{route_id}",
                f"family:{family_id}",
                "uses_family",
                source_file="references/route-source-index.yaml",
            )
        for source_id in route_data.get("priority_source_ids", []) or []:
            add_edge(
                G,
                f"route:{route_id}",
                f"source:{source_id}",
                "prioritizes_source",
                source_file="references/route-source-index.yaml",
            )
        for card in route_data.get("default_source_cards", []) or []:
            card_node = f"source_card:{Path(card).stem}"
            if card_node not in G:
                add_node(
                    G,
                    card_node,
                    label=card,
                    node_kind="source_card",
                    file_type="document",
                    source_file=f"references/{card}",
                )
            add_edge(
                G,
                f"route:{route_id}",
                card_node,
                "loads_source_card",
                source_file="references/route-source-index.yaml",
            )

    docs_by_source: dict[str, list[str]] = defaultdict(list)
    route_source_from_docs: set[tuple[str, str]] = set()
    for row in document_rows:
        doc_id = row.get("doc_id")
        source_id = row.get("source_id")
        if not doc_id or not source_id:
            continue
        node_id = f"doc:{doc_id}"
        add_node(
            G,
            node_id,
            label=f"{source_id} / {row.get('label') or doc_id}",
            node_kind="document_locator",
            file_type="document",
            source_file="references/corpus_index/document_index.jsonl",
            doc_id=doc_id,
            source_id=source_id,
            family=row.get("family"),
            status=row.get("status"),
            load_class=row.get("load_class"),
            authority_class=row.get("authority_class"),
            heading_count=row.get("heading_count"),
            line_count=row.get("line_count"),
            bytes=row.get("bytes"),
            page_count_guess=row.get("page_count_guess"),
            route_tags=row.get("route_tags", []),
            locator_rule="open document_index.jsonl row, then selected canonical source; path omitted from graph",
        )
        add_edge(
            G,
            f"source:{source_id}",
            node_id,
            "has_document_locator",
            source_file="references/corpus_index/document_index.jsonl",
        )
        docs_by_source[source_id].append(doc_id)
        for route_id in row.get("route_tags", []) or []:
            route_source_from_docs.add((route_id, source_id))
            add_edge(
                G,
                f"route:{route_id}",
                node_id,
                "has_route_document_locator",
                source_file="references/corpus_index/document_index.jsonl",
            )

    for route_id, source_id in sorted(route_source_from_docs):
        add_edge(
            G,
            f"route:{route_id}",
            f"source:{source_id}",
            "has_available_source_for_route",
            source_file="references/corpus_index/document_index.jsonl",
        )

    for row in section_rows:
        source_id = row.get("source_id")
        if not source_id:
            continue
        node_id = f"section_index:{source_id}"
        add_node(
            G,
            node_id,
            label=f"{source_id} section index ({row.get('section_count', 0)} sections)",
            node_kind="section_index_locator",
            file_type="document",
            source_file="references/corpus_index/section_index_manifest.jsonl",
            source_id=source_id,
            family=row.get("family"),
            section_count=row.get("section_count"),
            bytes=row.get("bytes"),
            locator_rule="resolve source_id through section_index_manifest; graph omits by_source path",
        )
        add_edge(
            G,
            f"source:{source_id}",
            node_id,
            "has_section_index_locator",
            source_file="references/corpus_index/section_index_manifest.jsonl",
        )

    add_edge(
        G,
        "artifact:retrieval_adapter",
        "artifact:graphify_navigation",
        "defines_optional_backend",
        source_file="references/retrieval-adapter-notes.md",
    )
    add_edge(
        G,
        "artifact:source_map",
        "artifact:graphify_navigation",
        "documents_rebuildable_output",
        source_file="references/source-map.md",
    )
    add_edge(
        G,
        "artifact:document_index",
        "concept:canonical_verification",
        "precedes",
        source_file="references/corpus_index/document_index.jsonl",
    )
    add_edge(
        G,
        "artifact:section_index_manifest",
        "concept:canonical_verification",
        "precedes",
        source_file="references/corpus_index/section_index_manifest.jsonl",
    )

    stats = {
        "source_manifest_rows": len(source_manifest_rows),
        "document_rows": len(document_rows),
        "section_index_rows": len(section_rows),
        "families": len(families),
        "routes": len(routes),
        "sources": len(all_source_ids),
        "documents_by_source": {k: len(v) for k, v in sorted(docs_by_source.items())},
    }
    return G, stats


def community_labels(G: nx.Graph, communities: dict[int, list[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    for cid, nodes in communities.items():
        kinds = Counter(G.nodes[n].get("node_kind", "node") for n in nodes)
        families = Counter(G.nodes[n].get("family") for n in nodes if G.nodes[n].get("family"))
        routes = [G.nodes[n].get("label", n) for n in nodes if G.nodes[n].get("node_kind") == "route"]
        if routes:
            labels[cid] = f"route: {routes[0]}"
        elif families:
            labels[cid] = f"family: {families.most_common(1)[0][0]}"
        elif kinds:
            labels[cid] = kinds.most_common(1)[0][0].replace("_", " ")
        else:
            labels[cid] = f"Community {cid}"
    return labels


def write_manifest(root: Path, out_dir: Path, stats: dict[str, Any], G: nx.Graph) -> None:
    input_files = []
    for rel in CORE_INPUTS:
        path = root / rel
        if path.exists():
            input_files.append({"path": rel, "sha256": sha256_file(path), "bytes": path.stat().st_size})
    card_dir = root / "references/source_inventory/source_cards"
    for path in sorted(card_dir.glob("*.md")):
        input_files.append(
            {"path": relpath(path, root), "sha256": sha256_file(path), "bytes": path.stat().st_size}
        )

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "scripts/build_graphify_index_graph.py",
        "scope": "router_index_graph",
        "evidence_use": "locator_only",
        "canonical_verification_required": True,
        "excluded_surface": "canonical fulltext, split section rows, archived refs, and upstream metadata copies",
        "graph": {
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "connected_components": nx.number_connected_components(G),
        },
        "inputs": input_files,
        "input_stats": stats,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_report(
    root: Path,
    out_dir: Path,
    G: nx.Graph,
    communities: dict[int, list[str]],
    labels: dict[int, str],
    stats: dict[str, Any],
) -> None:
    cohesion = score_all(G, communities)
    confidence = Counter(data.get("confidence", "EXTRACTED") for _, _, data in G.edges(data=True))
    node_kinds = Counter(data.get("node_kind", "node") for _, data in G.nodes(data=True))
    top_nodes = god_nodes(G, top_n=12)
    surprises = surprising_connections(G, communities, top_n=8)

    lines = [
        "# Graphify Index Graph Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "## Scope",
        "",
        "This is a graphify-compatible index graph for `sr-survey-prior-router`.",
        "It covers route definitions, source families, source records, document locators,",
        "section-index locators, source cards, and the graphify navigation contract.",
        "",
        "It intentionally does not read or embed canonical fulltext Markdown/raw files.",
        "Use this graph to find candidate route/source/document/section IDs, then verify",
        "substantive claims through the selected canonical source.",
        "",
        "## Summary",
        "",
        f"- Nodes: {G.number_of_nodes()}",
        f"- Edges: {G.number_of_edges()}",
        f"- Communities: {len(communities)}",
        f"- Connected components: {nx.number_connected_components(G)}",
        f"- Confidence: {dict(sorted(confidence.items()))}",
        f"- Node kinds: {dict(sorted(node_kinds.items()))}",
        f"- Routes: {stats['routes']}",
        f"- Families: {stats['families']}",
        f"- Sources: {stats['sources']}",
        f"- Document locator rows: {stats['document_rows']}",
        f"- Section-index locator rows: {stats['section_index_rows']}",
        "",
        "## Query Examples",
        "",
        "```sh",
        "graphify query \"PRISMA checklist systematic review reporting\" --graph graphify-out/graph.json --budget 1200",
        "graphify query \"survey writing taxonomy synthesis\" --graph graphify-out/graph.json --budget 1200",
        "graphify query \"OpenAI Codex skill lazy loading\" --graph graphify-out/graph.json --budget 1200",
        "```",
        "",
        "## Core Nodes",
        "",
    ]
    for i, node in enumerate(top_nodes, 1):
        lines.append(f"{i}. `{node['label']}` - {node['edges']} edges")

    lines += ["", "## Communities", ""]
    for cid, nodes in communities.items():
        display = [G.nodes[n].get("label", n) for n in nodes[:10]]
        suffix = f" (+{len(nodes) - 10} more)" if len(nodes) > 10 else ""
        lines.append(f"### Community {cid}: {labels.get(cid, f'Community {cid}')}")
        lines.append(f"- Nodes: {len(nodes)}")
        lines.append(f"- Cohesion: {cohesion.get(cid, 0.0)}")
        lines.append(f"- Sample: {', '.join(f'`{item}`' for item in display)}{suffix}")
        lines.append("")

    lines += ["## Surprising Cross-File Connections", ""]
    if surprises:
        for item in surprises:
            lines.append(
                f"- `{item['source']}` --{item.get('relation', 'related_to')}--> "
                f"`{item['target']}` [{item.get('confidence', 'EXTRACTED')}]"
            )
            if item.get("why"):
                lines.append(f"  - Why: {item['why']}")
    else:
        lines.append("- None detected by graphify's cross-file heuristic.")

    lines += [
        "",
        "## Evidence Boundary",
        "",
        "- `graph.json`, `graph.html`, this report, source cards, and index rows are derivative artifacts.",
        "- Graph edges are navigation leads, not evidence.",
        "- Important claims must be verified against a selected canonical Markdown/raw source.",
        "",
        "## Rebuild",
        "",
        "```sh",
        "python3 scripts/build_graphify_index_graph.py",
        "python3 validation/validate_graphify_navigation.py",
        "```",
        "",
    ]
    (out_dir / "GRAPH_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def assert_output_is_scoped(out_dir: Path) -> None:
    for path in (out_dir / "graph.json", out_dir / "manifest.json", out_dir / "GRAPH_REPORT.md"):
        text = path.read_text(encoding="utf-8")
        hits = [pattern for pattern in FORBIDDEN_OUTPUT_PATTERNS if pattern in text]
        if hits:
            raise ValueError(f"{path} contains forbidden full-corpus path references: {hits}")


def remove_generated_metadata(out_dir: Path) -> int:
    removed = 0
    for path in out_dir.glob("._*"):
        path.unlink()
        removed += 1
    return removed


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="sr-survey-prior-router skill root")
    parser.add_argument("--out", default=DEFAULT_OUTPUT_DIR, help="output directory under root")
    parser.add_argument("--no-html", action="store_true", help="skip graph.html export")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = Path(args.root).resolve()
    if not (root / SKILL_ROOT_MARKER).exists():
        print(f"error: {root} does not look like the skill root; missing {SKILL_ROOT_MARKER}", file=sys.stderr)
        return 2

    out_dir = root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    G, stats = build_graph(root)
    communities = cluster(G)
    labels = community_labels(G, communities)

    to_json(G, communities, str(out_dir / "graph.json"))
    if not args.no_html:
        to_html(G, communities, str(out_dir / "graph.html"), community_labels=labels)
    write_manifest(root, out_dir, stats, G)
    write_report(root, out_dir, G, communities, labels, stats)
    metadata_removed = remove_generated_metadata(out_dir)
    assert_output_is_scoped(out_dir)

    print(
        json.dumps(
            {
                "graph_path": str(out_dir / "graph.json"),
                "report_path": str(out_dir / "GRAPH_REPORT.md"),
                "nodes": G.number_of_nodes(),
                "edges": G.number_of_edges(),
                "communities": len(communities),
                "scope": "router_index_graph",
                "metadata_removed": metadata_removed,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
