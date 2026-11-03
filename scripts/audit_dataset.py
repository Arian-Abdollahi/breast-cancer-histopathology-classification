"""Summarize public IDC filename labels/patients without reading image pixels."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from breast_histopathology.dataset_audit import count_patches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='Extracted IDC image directory')
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error(f'Directory not found: {args.directory}')
    files = sorted(args.directory.rglob('*.png'))
    print(json.dumps(count_patches(files), indent=2))
    if not files:
        raise SystemExit('No PNG files found')


if __name__ == '__main__':
    main()
