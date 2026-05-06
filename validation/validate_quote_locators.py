#!/usr/bin/env python3
"""Validate resolvable source-card quote_or_locator file and line references."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARDS_DIR = ROOT / "references/source_inventory/source_cards_v2"

FILE_REF_RE = re.compile(
    r"(?P<path>(?:references/[A-Za-z0-9_./%+=@~(),-]+|[A-Za-z0-9_.%+=@~(),-]+)"
    r"(?:\.md|\.jsonl)):"
    r"(?P<ranges>\d+(?:-\d+)?(?:\s*(?:,|and)\s*\d+(?:-\d+)?)*)"
)
RANGE_RE = re.compile(r"\d+(?:-\d+)?")


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


def extract_quote_or_locator(keypoint_block: str) -> str | None:
    match = re.search(r"(?m)^\s*quote_or_locator:\s*(.*)$", keypoint_block)
    if not match:
        return None
    return match.group(1).strip().strip('"')


def resolve_locator_path(path_text: str, supporting_paths: list[str]) -> tuple[list[Path], str | None]:
    if "/" in path_text:
        return [ROOT / path_text], None

    matches = [ROOT / supporting_path for supporting_path in supporting_paths if Path(supporting_path).name == path_text]
    if matches:
        return matches, None
    return [], f"basename locator {path_text!r} does not match any supporting_canonical_paths basename"


def parse_ranges(ranges_text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for match in RANGE_RE.finditer(ranges_text):
        raw_range = match.group(0)
        if "-" in raw_range:
            start_text, end_text = raw_range.split("-", 1)
            start = int(start_text)
            end = int(end_text)
        else:
            start = end = int(raw_range)
        ranges.append((start, end))
    return ranges


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def validate_file_ref(
    card_rel: Path,
    keypoint_index: int,
    path_text: str,
    ranges_text: str,
    supporting_paths: list[str],
) -> list[str]:
    errors: list[str] = []
    paths, resolution_error = resolve_locator_path(path_text, supporting_paths)
    if resolution_error:
        return [f"{card_rel}: key point {keypoint_index}: {resolution_error}"]

    ranges = parse_ranges(ranges_text)
    if not ranges:
        errors.append(f"{card_rel}: key point {keypoint_index}: no line ranges parsed for {path_text!r}")

    for path in paths:
        rel_path = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        if not path.exists():
            errors.append(f"{card_rel}: key point {keypoint_index}: locator path does not exist: {rel_path}")
            continue
        if not path.is_file():
            errors.append(f"{card_rel}: key point {keypoint_index}: locator path is not a file: {rel_path}")
            continue

        line_count = count_lines(path)
        for start, end in ranges:
            if start < 1 or end < 1:
                errors.append(f"{card_rel}: key point {keypoint_index}: line ranges must be 1-based: {path_text}:{start}-{end}")
            if start > end:
                errors.append(f"{card_rel}: key point {keypoint_index}: reversed range: {path_text}:{start}-{end}")
            if end > line_count:
                errors.append(
                    f"{card_rel}: key point {keypoint_index}: range {path_text}:{start}-{end} exceeds "
                    f"{rel_path} line count {line_count}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    checked_refs = 0
    skipped_locator_values = 0

    if not CARDS_DIR.exists():
        print(f"quote locator validation: FAIL\n- missing cards directory: {CARDS_DIR.relative_to(ROOT)}")
        return 1

    cards = sorted(
        path
        for path in CARDS_DIR.glob("*.md")
        if path.name != "README.md" and not path.name.startswith("._")
    )

    for card in cards:
        card_rel = card.relative_to(ROOT)
        text = card.read_text(encoding="utf-8")
        keypoint_blocks = extract_keypoint_blocks(text)
        if not keypoint_blocks:
            errors.append(f"{card_rel}: missing key points yaml block")
            continue

        for index, keypoint in enumerate(keypoint_blocks, start=1):
            locator = extract_quote_or_locator(keypoint)
            if locator is None:
                errors.append(f"{card_rel}: key point {index}: missing quote_or_locator")
                continue

            supporting_paths = extract_supporting_paths(keypoint)
            matches = list(FILE_REF_RE.finditer(locator))
            if not matches:
                skipped_locator_values += 1
                continue

            for match in matches:
                checked_refs += 1
                errors.extend(
                    validate_file_ref(
                        card_rel,
                        index,
                        match.group("path"),
                        match.group("ranges"),
                        supporting_paths,
                    )
                )

    if errors:
        print("quote locator validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("quote locator validation: PASS")
    print(f"checked_cards: {len(cards)}")
    print(f"checked_file_refs: {checked_refs}")
    print(f"skipped_unstructured_locators: {skipped_locator_values}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
