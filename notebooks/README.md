# Notebook provenance

The two files in this folder preserve the **source cells** of the supplied notebooks. Their execution counts, image outputs, and heavyweight saved widget states were removed to make Git diffs useful and avoid including sample tissue imagery directly inside notebooks.

- `phase2_version1.ipynb`: 63 source cells
- `phase2_version2.ipynb`: 64 source cells

The unmodified original `.ipynb` files, with saved outputs, are kept separately in the **source-backup ZIP** supplied alongside this repository bundle. The original checksums are recorded in `docs/PROVENANCE.json`.

These are archival research notebooks, not a clean end-to-end CLI. Several cells depend on Kaggle credentials, Google Drive mounts, additional datasets, checkpoints, and absolute Colab filesystem paths. They must be adapted before execution. Do not run cells that move or delete your files without inspecting them first.
