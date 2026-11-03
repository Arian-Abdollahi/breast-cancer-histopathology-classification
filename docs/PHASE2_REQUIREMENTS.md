# Phase 2 requirement mapping

Source: the Persian assignment in `references/CI_CNN_Project_Fall_2024_v2.pdf`, especially **pages 4-8**.

| Assignment requirement | Evidence in uploaded notebooks | Assessment |
| --- | --- | --- |
| Acquire and preprocess histopathology data; train/validation/test split | Kaggle download cells, PIL/torchvision transforms, `train_test_split` | Implemented as **patch-level split**; patient leakage is possible |
| Assess class imbalance | Class distribution counts and plots | Included |
| Build convolutional classifier with F1 above 90% on test set | Residual CNN and saved test outputs 0.9175 / 0.9488 | Historical saved result only; not reproduced |
| Graph loss, accuracy, precision, recall by epoch | Training history lists and plotting cells | Included in source; outputs not rerun |
| Discuss test precision, recall, F1 and AUC | v1 printed all four; v2 printed F1 and AUC | Partly covered; v2 lacks printed test precision/recall |
| Display final model with Keras `plot_model` | PyTorch `nn.Sequential` model; v1 contains `torchsummary` cell | **Not met as written** |
| Grad-CAM heatmaps for positive and negative samples (optional) | Grad-CAM cells and saved example images | Present as explanatory heatmaps, **not segmentation** |
| Use Keras API, BatchNorm + ReLU, no pretrained model | PyTorch from-scratch model with BatchNorm + ReLU | **Architecture follows part of the intent, but Keras requirement not met** |
| Save best checkpoint by validation loss | `torch.save` on improved validation loss | Implemented differently from `tf.keras.callbacks.ModelCheckpoint` |
| GPU training and appropriate batches | CUDA detection and batch size 32 | GPU-dependent setup present; a new run has not been verified |

Nothing in Phase 2 requests pixel-wise tumor annotations, mask labels, U-Net, Dice/IoU segmentation, or a trained segmentation decoder. The uploaded notebooks do not implement these tasks.
