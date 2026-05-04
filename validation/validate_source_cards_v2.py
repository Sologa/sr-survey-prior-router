#!/usr/bin/env python3
"""Validate source_cards_v2 metadata and evidence boundaries."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARDS_DIR = ROOT / "references/source_inventory/source_cards_v2"

REQUIRED_METADATA_FIELDS = [
    "source_id",
    "source_family",
    "canonical_paths",
    "canonical_urls",
    "authority_level",
    "version_or_access_date",
    "applies_to",
    "not_for",
    "route_relevance",
    "freshness_risk",
    "reuse_or_license_risk",
    "qa_status",
    "last_reviewed",
]

REQUIRED_SECTIONS = [
    "## Key points",
    "## Operational rules",
    "## Common misuses",
    "## Evidence limits",
    "## Verification paths",
    "## Unresolved gaps",
]

FORBIDDEN_DIRECT_EVIDENCE_PATH_PARTS = [
    "references/source_inventory/source_cards",
    "references/corpus_index/",
    "references/graphify",
    "graphify-out/",
    "references/source_inventory/source_manifest.jsonl",
    "references/source_inventory/source_registry.yaml",
    "references/canonical_sources/download_manifest.jsonl",
    "validation/",
]

BLOCKED_OR_LOCATOR_AUTHORITY_LEVELS = {
    "blocked_inventory_target",
    "bad_capture_do_not_use",
    "locator_only",
}

IGNORED_METADATA_DIRS = {".git", ".omx"}


def load_source_ids() -> set[str]:
    manifest = ROOT / "references/source_inventory/source_manifest.jsonl"
    source_ids: set[str] = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        source_ids.add(json.loads(line)["source_id"])
    return source_ids


def load_route_ids() -> set[str]:
    registry = ROOT / "references/route-registry.md"
    text = registry.read_text(encoding="utf-8")
    return set(re.findall(r"^### `([^`]+)`", text, flags=re.MULTILINE))


def first_fenced_block(text: str) -> str | None:
    match = re.search(r"```yaml\n(.*?)\n```", text, flags=re.DOTALL)
    if not match:
        return None
    return match.group(1)


def parse_simple_yaml_block(block: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                data[current_key] = []
            data[current_key].append(line[4:].strip().strip('"'))
            continue
        match = re.match(r"^([A-Za-z0-9_]+):(?:\s*(.*))?$", line)
        if not match:
            current_key = None
            continue
        key, raw_value = match.groups()
        current_key = key
        value = (raw_value or "").strip()
        if value == "[]":
            data[key] = []
        elif value:
            data[key] = value.strip('"')
        else:
            data[key] = []
    return data


def extract_keypoint_blocks(text: str) -> list[str]:
    keypoints_match = re.search(r"## Key points\n\n```yaml\n(.*?)\n```", text, flags=re.DOTALL)
    if not keypoints_match:
        return []
    block = keypoints_match.group(1)
    parts = re.split(r"(?m)^- claim: ", block)
    return [part for part in parts[1:] if part.strip()]


def extract_supporting_paths(keypoint_block: str) -> list[str]:
    paths: list[str] = []
    in_paths = False
    for line in keypoint_block.splitlines():
        stripped = line.strip()
        if stripped == "supporting_canonical_paths:":
            in_paths = True
            continue
        if in_paths and stripped.startswith("- "):
            paths.append(stripped[2:].strip())
            continue
        if in_paths and stripped and not stripped.startswith("- "):
            in_paths = False
    return paths


def main() -> int:
    errors: list[str] = []

    if not CARDS_DIR.exists():
        errors.append(f"missing cards directory: {CARDS_DIR.relative_to(ROOT)}")
    readme = CARDS_DIR / "README.md"
    if not readme.exists():
        errors.append("missing source_cards_v2/README.md")

    source_ids = load_source_ids()
    route_ids = load_route_ids()
    cards = sorted(path for path in CARDS_DIR.glob("*.md") if path.name != "README.md")

    for card in cards:
        rel = card.relative_to(ROOT)
        text = card.read_text(encoding="utf-8")
        metadata_block = first_fenced_block(text)
        if metadata_block is None:
            errors.append(f"{rel}: missing fenced yaml metadata block")
            continue
        metadata = parse_simple_yaml_block(metadata_block)

        source_id = metadata.get("source_id")
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{rel}: missing source_id")
            continue
        if card.stem != source_id:
            errors.append(f"{rel}: filename does not match source_id {source_id!r}")
        if source_id not in source_ids:
            errors.append(f"{rel}: source_id not found in source_manifest.jsonl")

        authority_level = metadata.get("authority_level")
        allow_missing_canonical_paths = authority_level in BLOCKED_OR_LOCATOR_AUTHORITY_LEVELS

        for field in REQUIRED_METADATA_FIELDS:
            if field == "canonical_paths" and allow_missing_canonical_paths:
                continue
            value = metadata.get(field)
            if value in (None, "", []):
                errors.append(f"{rel}: missing or empty metadata field {field}")

        canonical_paths = metadata.get("canonical_paths", [])
        if not isinstance(canonical_paths, list):
            errors.append(f"{rel}: canonical_paths is not a list")
            canonical_paths = []
        if not canonical_paths and not allow_missing_canonical_paths:
            errors.append(f"{rel}: canonical_paths is empty for authority_level {authority_level!r}")
        for path_text in canonical_paths:
            path = ROOT / path_text
            if not path.exists():
                errors.append(f"{rel}: canonical path does not exist: {path_text}")

        route_relevance = metadata.get("route_relevance", [])
        if not isinstance(route_relevance, list):
            errors.append(f"{rel}: route_relevance is not a list")
            route_relevance = []
        for route_id in route_relevance:
            if route_id not in route_ids:
                errors.append(f"{rel}: unknown route_relevance value: {route_id}")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{rel}: missing section {section}")

        keypoint_blocks = extract_keypoint_blocks(text)
        if not keypoint_blocks:
            errors.append(f"{rel}: missing required key points yaml block")
        for index, keypoint in enumerate(keypoint_blocks, start=1):
            if "support_type:" not in keypoint:
                errors.append(f"{rel}: key point {index} missing support_type")
            if "verification_note:" not in keypoint:
                errors.append(f"{rel}: key point {index} missing verification_note")
            paths = extract_supporting_paths(keypoint)
            if not paths:
                errors.append(f"{rel}: key point {index} missing supporting_canonical_paths")
            support_match = re.search(r"support_type:\s*([A-Za-z_]+)", keypoint)
            support_type = support_match.group(1) if support_match else ""
            if support_type in {"direct", "indirect"}:
                for path_text in paths:
                    if any(part in path_text for part in FORBIDDEN_DIRECT_EVIDENCE_PATH_PARTS):
                        errors.append(
                            f"{rel}: key point {index} uses derivative path as {support_type} evidence: {path_text}"
                        )
                    if not (ROOT / path_text).exists():
                        errors.append(f"{rel}: key point {index} supporting path does not exist: {path_text}")

    generated_metadata = sorted(
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("._*")
        if not (IGNORED_METADATA_DIRS & set(path.relative_to(ROOT).parts))
    )
    if generated_metadata:
        errors.append(f"pack contains macOS metadata files: {generated_metadata}")

    if errors:
        print("source_cards_v2 validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("source_cards_v2 validation: PASS")
    print(f"checked_cards: {len(cards)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
