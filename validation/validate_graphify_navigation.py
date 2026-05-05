#!/usr/bin/env python3
"""Validate that graphify remains a scoped optional locator backend."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from networkx.readwrite import json_graph


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "references/graphify-navigation.md",
    ".graphifyignore",
    "scripts/build_graphify_index_graph.py",
]

GENERATED_GRAPH_FILES = [
    "graphify-out/graph.json",
    "graphify-out/GRAPH_REPORT.md",
    "graphify-out/manifest.json",
]

FORBIDDEN_GRAPH_OUTPUT_PATTERNS = [
    "references/canonical_sources/raw/",
    "references/canonical_sources/md/",
    "references/corpus_index/sections/by_source/",
    "refs_old/",
    "upstream_repo/",
]

IGNORED_METADATA_DIRS = {".git", ".omx"}
IGNORED_METADATA_FILES = {"._.omx"}

REQUIRED_PHRASES = {
    "SKILL.md": [
        "references/graphify-navigation.md",
        "graph output is never canonical evidence",
        "Do not bulk-load `references/canonical_sources/raw/`",
    ],
    "references/graphify-navigation.md": [
        "Graphify output is a locator and triage artifact, not evidence.",
        "The default graph scope is the router and index surface",
        "references/canonical_sources/raw/",
        "references/canonical_sources/md/",
        "references/corpus_index/sections/by_source/",
        "canonical_verification: false",
        "evidence_use: locator",
        "python3 scripts/build_graphify_index_graph.py",
        "Do not graphify the full canonical corpus by default.",
    ],
    "scripts/build_graphify_index_graph.py": [
        "router_index_graph",
        "canonical_verification_required",
        "FORBIDDEN_OUTPUT_PATTERNS",
    ],
    "references/retrieval-adapter-notes.md": [
        "graphify navigation",
        "Graph results are locators",
    ],
    "references/route-registry.md": [
        "graphify-navigation.md",
        "graph results as locators, not evidence",
    ],
    "references/route-source-index.yaml": [
        "optional_navigation_backends:",
        "graphify:",
        "evidence_rule: graph output is locator-only",
    ],
    "references/source-map.md": [
        "graphify-navigation.md",
        "optional rebuildable graph navigation output",
    ],
    ".graphifyignore": [
        "references/canonical_sources/raw/",
        "references/canonical_sources/md/",
        "references/corpus_index/sections/by_source/",
        "graphify-out/",
    ],
    ".gitignore": [
        "/graphify-out/",
        "/.graphify_*",
    ],
}

GENERATED_REQUIRED_PHRASES = {
    "graphify-out/GRAPH_REPORT.md": [
        "Graphify Index Graph Report",
        "It intentionally does not read or embed canonical fulltext Markdown/raw files.",
        "Graph edges are navigation leads, not evidence.",
    ],
}


def should_ignore_generated_metadata(path: Path) -> bool:
    rel_parts = path.relative_to(ROOT).parts
    return bool(IGNORED_METADATA_DIRS & set(rel_parts)) or path.name in IGNORED_METADATA_FILES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-generated",
        action="store_true",
        help="fail if ignored rebuildable graphify-out artifacts are absent",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing file for phrase check: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel}: missing phrase {phrase!r}")

    generated_paths = [ROOT / rel for rel in GENERATED_GRAPH_FILES]
    generated_present = [path for path in generated_paths if path.exists()]
    generated_missing = [
        rel for rel, path in zip(GENERATED_GRAPH_FILES, generated_paths, strict=True) if not path.exists()
    ]
    generated_complete = len(generated_present) == len(generated_paths)

    if args.require_generated and generated_missing:
        for rel in generated_missing:
            errors.append(f"missing generated graphify artifact: {rel}")
    elif generated_present and not generated_complete:
        for rel in generated_missing:
            errors.append(f"incomplete generated graphify artifact set; missing: {rel}")

    if generated_complete:
        for rel, phrases in GENERATED_REQUIRED_PHRASES.items():
            path = ROOT / rel
            text = path.read_text(encoding="utf-8")
            for phrase in phrases:
                if phrase not in text:
                    errors.append(f"{rel}: missing phrase {phrase!r}")

    generated_metadata = sorted(
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("._*")
        if not should_ignore_generated_metadata(path)
    )
    if generated_metadata:
        errors.append(f"pack contains macOS metadata files: {generated_metadata}")

    for rel in GENERATED_GRAPH_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_GRAPH_OUTPUT_PATTERNS:
            if pattern in text:
                errors.append(f"{rel}: contains forbidden full-corpus path reference {pattern!r}")

    graph_path = ROOT / "graphify-out/graph.json"
    manifest_path = ROOT / "graphify-out/manifest.json"
    if generated_complete and graph_path.exists():
        try:
            graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
            graph = json_graph.node_link_graph(graph_data, edges="links")
            node_kinds = {data.get("node_kind") for _, data in graph.nodes(data=True)}
            required_kinds = {"route", "family", "source", "document_locator", "section_index_locator"}
            missing_kinds = sorted(required_kinds - node_kinds)
            if missing_kinds:
                errors.append(f"graphify-out/graph.json: missing node kinds {missing_kinds}")
            if graph.number_of_nodes() < 300:
                errors.append(f"graphify-out/graph.json: too few nodes: {graph.number_of_nodes()}")
            if graph.number_of_edges() < 1000:
                errors.append(f"graphify-out/graph.json: too few edges: {graph.number_of_edges()}")
        except Exception as exc:
            errors.append(f"graphify-out/graph.json: could not load graph: {exc}")

    if generated_complete and manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("scope") != "router_index_graph":
                errors.append("graphify-out/manifest.json: scope is not router_index_graph")
            if manifest.get("evidence_use") != "locator_only":
                errors.append("graphify-out/manifest.json: evidence_use is not locator_only")
            if manifest.get("canonical_verification_required") is not True:
                errors.append("graphify-out/manifest.json: canonical_verification_required is not true")
        except Exception as exc:
            errors.append(f"graphify-out/manifest.json: could not load manifest: {exc}")

    if errors:
        print("graphify navigation validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("graphify navigation validation: PASS")
    print(f"checked_root: {ROOT}")
    if generated_complete:
        print("generated_graph: present")
    else:
        print("generated_graph: absent_optional_rebuildable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
