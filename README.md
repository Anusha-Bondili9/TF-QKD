# TF-QKD: Quantum-Enabled Image Watermarking with Siamese ConvNeXt

Code for the manuscript "Quantum-Enabled Digital Image Watermarking Using TF-QKD and Siamese ConvNeXt for Robust Authentication and Tamper Detection".

The pipeline covers: a simulated TF-QKD-inspired key generation (QBER check, Cascade-style reconciliation, Toeplitz privacy amplification), AES-256-GCM encryption of a binary watermark, key-driven DCT block selection, Siamese ConvNeXt-guided adaptive embedding, watermark extraction, attack simulation, and tamper detection and localization.

## Note on the key
The TF-QKD stage is a simulation. With `KEY_MODE = "reproducible"` the key is generated from a fixed seed, so it is a test key only. Set `KEY_MODE = "fresh"` for a new random key.

## Requirements
Python 3 with: numpy, pandas, scipy, scikit-learn, scikit-image, opencv-python, Pillow, matplotlib, tqdm, psutil, thop, cryptography, torch, torchvision.

    pip install numpy pandas scipy scikit-learn scikit-image opencv-python pillow matplotlib tqdm psutil thop cryptography torch torchvision

## Data
Download the CASIA 2.0 image tampering dataset and place it in `data/CASIA2/`. The dataset is not included in this repository and has its own licence.

## Folder layout
    Complete_Pipeline.ipynb   the pipeline notebook (run from this folder)
    watermarks/               the binary watermark images
    data/CASIA2/              dataset (you add this)
    outputs/                  created automatically; all results are written here

## How to run
Open `Complete_Pipeline.ipynb` and run the cells from the top. All paths are set in the CONFIG cell and are relative to the notebook's folder.

## Citation
Please cite the manuscript above.

## License
Add a LICENSE file (for example MIT) and state it here.
