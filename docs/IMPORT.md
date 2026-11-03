# Finish importing the Phase 2 breast histopathology project

**Status: awaiting one ZIP upload on the `import/phase2-complete` branch.**

All project code and figures are in the prepared `breast-cancer-histopathology-classification-git-ready.zip` archive, verified locally as 27 files (SHA256: `8522679fd0d2a2d7bb94b4e8a4ebe732010a33210a7d9a5bc0b8dbb7860d195f`).

## Upload through GitHub

1. Download the Git-ready ZIP from the ChatGPT conversation (not the originals-backup ZIP and not the Git bundle).
2. Open the [import branch](https://github.com/Arian-Abdollahi/breast-cancer-histopathology-classification/tree/import/phase2-complete).
3. Choose **Add file → Upload files**.
4. Upload **the ZIP itself** to the root of this branch; do not unzip it or modify its bytes. The filename can be anything ending in `.zip`, provided there is only one root-level ZIP file.
5. Choose **Commit directly to the `import/phase2-complete` branch** and click **Commit changes**.
6. Open [GitHub Actions](https://github.com/Arian-Abdollahi/breast-cancer-histopathology-classification/actions) and inspect the **Import verified Phase 2 archive** workflow. It checks the ZIP SHA256, extracts all 27 files, runs notebook structure checks and utility tests, removes the ZIP, and pushes the complete project to the same branch.
7. Inspect the [Pull Request](https://github.com/Arian-Abdollahi/breast-cancer-histopathology-classification/pulls) and any required Actions approval before merging into `main`.

## Scientific and data caveats

This is **binary IDC-positive/IDC-negative histopathology patch classification**, not pixel-level tumor segmentation. Grad-CAM maps are model explanations, not ground-truth segmentation masks.

The original Phase 2 assignment requested Keras, whereas the preserved notebooks use PyTorch. The saved notebook metrics are historical outputs; model training and medical performance were not independently re-run. The dataset and model weights were not part of the uploaded files and are intentionally excluded.

**No patient data or clinical dataset should be uploaded into this Git repository.** Consult `docs/REVIEW.md` after the import for leakage and reproducibility caveats.
