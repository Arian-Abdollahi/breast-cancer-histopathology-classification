# Technical review and limitations

This report describes the **supplied source**, not a newly performed experiment.

1. **Task semantics:** The notebooks output image-level IDC class logits and Grad-CAM overlays. They are not tumor segmentation systems; no masks, Dice, IoU or pixel-wise training targets appear in the source.
2. **Patient leakage:** The original `train_test_split(df, stratify=df['target'])` separates individual patches, not patients. Related patches from a patient can occur in multiple splits. Evaluation should be repeated with patient-group separation.
3. **Non-comparable results:** Version 1 constructs `df_test_new` by combining test and validation, while version 2 uses only test samples before filtering. Both later construct a test DataLoader, so reported F1/AUC values are not a controlled head-to-head comparison.
4. **External state:** `/content` and `/content/drive` mounts, a second `new_data` image collection, a checkpoint named `phase2_model.pt`, and temporary weight files are referenced but not included. Model execution cannot be claimed reproducible from the two notebooks alone.
5. **Framework mismatch:** The course PDF requires Keras, Batch Normalization and ReLU; source uses PyTorch, with BN/ReLU in its convolution blocks. No Keras `plot_model` appears.
6. **Metric definitions:** For a clinical research task, explain whether precision/recall/F1 are micro, macro or positive-class scores, report TP/FP/TN/FN, and use patient-safe test sets. The notebooks' saved metrics do not establish clinical sensitivity.
7. **Grad-CAM caution:** A heatmap is an attribution visualization, **not a localization ground truth**. Its output must not be described as segmented tumor boundaries.
8. **Code issues:** The source uses legacy backward hooks in Grad-CAM and unguarded `cam / cam.max()` normalization. Some cells depend on execution order and existing global variables; they may fail from a clean kernel.
9. **Checkpoint safety:** `torch.load` can deserialize unsafe Python objects. Load only checkpoints from trusted sources and follow the security guidance for your PyTorch version.
10. **Ethics and reuse:** No trained weights, raw clinical data, or independent validation are provided. Avoid representing outputs as medical advice or patient-level cancer diagnoses.

## Suggested next research iteration

Separate patients into train/validation/test splits; record fixed random seeds and metrics definitions; use a modern checkpoint format; package preprocessing and model construction; rerun benchmark metrics with confidence intervals. If **true segmentation** is required, obtain pixel-wise tumor masks and develop a separate segmentation model (for example U-Net) evaluated by Dice and IoU, instead of rebranding Grad-CAM classification overlays.
