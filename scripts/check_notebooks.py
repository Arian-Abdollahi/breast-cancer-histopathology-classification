"""Lightweight standard-library checks; no dataset, GPU or model required."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ('phase2_version1.ipynb', 'phase2_version2.ipynb')


def validate(path: Path):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    if notebook.get('nbformat') != 4:
        raise ValueError(f'{path.name}: expected notebook format 4')
    cells = notebook.get('cells')
    if not isinstance(cells, list) or len(cells) < 20:
        raise ValueError(f'{path.name}: missing source cells')
    if any(not isinstance(c.get('source'), list) for c in cells):
        raise ValueError(f'{path.name}: invalid cell source structure')
    if any(c.get('cell_type') == 'code' and c.get('outputs') for c in cells):
        raise ValueError(f'{path.name}: committed notebook should not contain embedded outputs')
    source = '\n'.join(''.join(c.get('source', [])) for c in cells)
    if 'class CNN(' not in source or 'GradCAM' not in source:
        raise ValueError(f'{path.name}: expected original model and heatmap source')
    return len(cells)


def main():
    for name in NOTEBOOKS:
        count = validate(ROOT / 'notebooks' / name)
        print(f'{name}: {count} source cells; structure OK')
    print('Notebook integrity checks passed. Model execution not tested.')


if __name__ == '__main__':
    main()
