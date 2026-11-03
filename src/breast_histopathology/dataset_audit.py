"""Filename-only IDC patch audit helpers. These do not inspect medical images."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

# Typical public dataset filename: 9345_idx5_x2001_y151_class1.png
PATCH_PATTERN = re.compile(
    r"^(?P<patient>\d+)_idx\d+_x-?\d+_y-?\d+_class(?P<label>[01])\.png$",
    flags=re.IGNORECASE,
)


def parse_patch_filename(path: str | Path) -> tuple[str, int] | None:
    """Return (patient_id, label), or None for nonmatching names."""
    match = PATCH_PATTERN.match(Path(path).name)
    if match is None:
        return None
    return match.group("patient"), int(match.group("label"))


def count_patches(paths: list[str | Path]) -> dict:
    """Count patch-level labels and unique patients without opening image files."""
    by_label = Counter()
    by_patient: dict[str, Counter] = defaultdict(Counter)
    skipped = 0
    for path in paths:
        parsed = parse_patch_filename(path)
        if parsed is None:
            skipped += 1
            continue
        patient, label = parsed
        by_label[label] += 1
        by_patient[patient][label] += 1
    return {
        "matched_patches": sum(by_label.values()),
        "positive_patches": by_label[1],
        "negative_patches": by_label[0],
        "unique_patients": len(by_patient),
        "unmatched_files": skipped,
    }


def patient_overlap(split_to_paths: dict[str, list[str | Path]]) -> dict[str, list[str]]:
    """Return patient IDs found in >1 split. Used to detect patch-level leakage."""
    patient_splits: dict[str, set[str]] = defaultdict(set)
    for split, paths in split_to_paths.items():
        for path in paths:
            parsed = parse_patch_filename(path)
            if parsed is not None:
                patient_splits[parsed[0]].add(split)
    return {patient: sorted(splits) for patient, splits in patient_splits.items() if len(splits) > 1}
