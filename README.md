# Quantum-Enabled Digital Image Watermarking Using TF-QKD and Siamese ConvNeXt

Code for the manuscript "Quantum-Enabled Digital Image Watermarking Using TF-QKD and Siamese ConvNeXt for Robust Authentication and Tamper Detection".

## Contents
- `TFQKD_Watermarking_Pipeline.ipynb` – complete pipeline (Phases 0–7), run top to bottom.
- `watermarks/watermark_binary.png` – main watermark (eagle silhouette, derived from a public Wikimedia Commons file).
- `watermarks/watermark_binary_cameraman.png` – cameraman watermark.

## Dataset
CASIA 2.0 is not included. Download it and place it in `data/CASIA2/`.

## Folder layout
    TFQKD_Watermarking_Pipeline.ipynb
    watermarks/
    data/CASIA2/        (you add this)
    outputs/            (created by the notebook)

## How to run
1. Install the requirements: numpy, scipy, pandas, scikit-image, scikit-learn, opencv-python, Pillow, matplotlib, tqdm, cryptography, psutil, thop, torch, torchvision.
2. Place CASIA 2.0 in `data/CASIA2/`.
3. Open the notebook and run all cells in order, starting with the CONFIG cell.
   Phase 0 (data preparation and Siamese training) runs automatically on the first run.

All paths are relative to the folder that contains the notebook. The embedding constants are set in the CONFIG cell (T0 = 28.0, margin = 15.0, cap = 18.0, R = 3).
