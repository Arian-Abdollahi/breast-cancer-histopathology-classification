# Saved notebook results

The following numbers are transcribed from **saved output cells** of the uploaded notebooks, not newly calculated.

| Source | Metric | Saved output |
| --- | --- | ---: |
| `phase2_version1.ipynb` | Test Precision | 0.9175 |
| `phase2_version1.ipynb` | Test Recall | 0.9175 |
| `phase2_version1.ipynb` | Test F1 Score | **0.9175** |
| `phase2_version1.ipynb` | Test AUC | **0.9678** |
| `phase2_version2.ipynb` | Test F1 Score | **0.9488** |
| `phase2_version2.ipynb` | Test AUC | **0.9850** |

The values are **historical, unverified notebook outputs**. Their reported `F1` may be an averaging variant different from positive-class sensitivity; consult the installed TorchMetrics defaults before interpreting it as medical recall. Sample-level splitting can leak slide/patient information. Version 1 and version 2 also differ in evaluation selection logic. No independent test results or clinical claims are made here.

## Saved visualizations

- [`figures/class_balance_v2.png`](../figures/class_balance_v2.png): class-count chart from the notebook.
- [`figures/train_validation_metrics_v2.png`](../figures/train_validation_metrics_v2.png): original metric history plot.
- [`figures/gradcam_positive_v2.png`](../figures/gradcam_positive_v2.png) and [`figures/gradcam_negative_v2.png`](../figures/gradcam_negative_v2.png): attribution overlays, **not segmentation masks**.

The figures have been extracted byte-for-byte from the uploaded version 2 notebook's embedded PNG outputs.
