# Data and labels

## Source

- Named dataset: **Breast Histopathology Images** from Kaggle (`paultimothymooney/breast-histopathology-images`).
- Original filenames typically end with `_class0.png` or `_class1.png` and include a numeric patient identifier and image-tile coordinates.
- In this project, `0` means **IDC-negative image patch** and `1` means **IDC-positive image patch**. These are patch-level labels, **not lesion masks or full-patient diagnoses**.
- Notebooks additionally reference custom `new_data` and a separately stored checkpoint. Neither was supplied in the project files.

## Preparation

1. Download the data from Kaggle under its published terms; do not commit raw medical images or access credentials.
2. Place the data in an ignored local `data/` directory.
3. Use `python scripts/audit_dataset.py data/IDC_regular_ps50_idx5` to inspect class and patient counts.
4. Split **by patient ID**, not by individual image patch, to avoid adjacent tiles from the same tissue slide entering both training and test sets.
5. Fit any normalization/calibration only on training data, then apply identical transforms to validation and test data.
6. Report patch-level and, if applicable, patient-level metrics separately, with class balance and confidence intervals.

The **original notebooks use stratified patch-level `train_test_split`**, not patient-group splits. Their historical saved test results may therefore be optimistic. This package deliberately preserves original code and records the limitation; it does not silently relabel the results as patient-independent.

The included dataset-auditing script uses filenames only, and does not inspect medical imagery or produce diagnostic predictions.
