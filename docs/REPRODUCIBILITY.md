# Reproducibility status

**Confirmed from source files:** notebook JSON is valid; source cells include CNN training/evaluation, model saving, and Grad-CAM; saved outputs report the figures in `reports/RESULTS.md`.

**Not supplied:** 3.10-GB Kaggle dataset; additional custom `new_data`; saved `phase2_model.pt` or `model (16).pt` checkpoints; experiment logs beyond embedded notebook output; exact pip lockfile; a fully specified patient-level split manifest.

**Not rerun:** GPU training, model checkpoint loading, inference, F1/AUC recomputation, visual Grad-CAM generation from the final model. Tests in `.github/workflows/ci.yml` deliberately check notebook structure and dataset-filename helpers only.

### Restoring an experiment

Adapt the original source to the data paths on your own machine, use a clean Python environment with compatible PyTorch/TorchVision builds, train from scratch (or supply **trusted** original checkpoints), and document the version, random seeds, dataset snapshot, split assignments, and metric averaging. A strict replication of the saved results cannot be guaranteed from this archive alone.
