# Spleen Segmentation with U-Net 🏥

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.8%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A U-Net implementation for automated spleen segmentation from CT scans, trained on the [Medical Segmentation Decathlon - Task09_Spleen](https://decathlon-10.grand-challenge.org/) dataset.

## Features ✨

- Complete U-Net implementation with skip connections
- Multi-channel input using adjacent CT slices
- Combined BCE + Dice loss for better segmentation
- Comprehensive evaluation metrics
- Visualization tools for samples and predictions
- NIfTI file support for medical imaging

## Model Architecture 🧠

![Enhanced Unet Architecture ](https://github.com/sowad223/ML-and-DL-projects/blob/main/CSE463/CSE463_PROJECT/archi.jpg)

### Key Components:
- **Encoder Path**: 4 downsampling blocks with max pooling
- **Decoder Path**: 3 upsampling blocks with skip connections
- **Bottleneck**: High-level feature extraction
- **Output**: Single channel segmentation mask

## Dataset Structure⚙️



1. **Training Set (required)**
   - `imagesTr/`: Directory containing 3D CT volumes
     - File format: `.nii` or `.nii.gz`
     - Shape: (Width, Height, Slices)
     - Values: Hounsfield Units (HU)
   - `labelsTr/`: Directory containing segmentation masks
     - Binary masks (0: background, 1: spleen)
     - Must have exact same filenames as corresponding images

2. **Test Set (optional)**
   - `imagesTs/`: For final evaluation/prediction
   - `labelsTs/`: Only needed if you want to evaluate test performance

### Important Notes:

- Files must be **paired** (image and label with identical names)
- Supported formats: `.nii` or compressed `.nii.gz`
- The loader automatically:
  - Applies CT windowing (-100 to 400 HU)
  - Normalizes to [0,1] range
  - Uses adjacent slices for 3-channel input
  - Filters out slices without spleen tissue during training

## Results:

![metrics distribution](https://github.com/sowad223/ML-and-DL-projects/blob/main/CSE463/CSE463_PROJECT/output/metrics_distribution.png)

## Vizualization:
![metrics distribution](https://github.com/sowad223/ML-and-DL-projects/blob/main/CSE463/CSE463_PROJECT/output/sample_0_0%20(3).png)
