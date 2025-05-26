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

![U-Net Architecture](https://miro.medium.com/max/1400/1*f7YOaE4TWubwaFF7Z1fzNw.png)

### Key Components:
- **Encoder Path**: 4 downsampling blocks with max pooling
- **Decoder Path**: 3 upsampling blocks with skip connections
- **Bottleneck**: High-level feature extraction
- **Output**: Single channel segmentation mask

## Dataset Structure⚙️

Task09_Spleen/
├── imagesTr/       # Training images (.nii or .nii.gz)
├── labelsTr/       # Training labels
├── imagesTs/       # Test images (optional)
└── labelsTs/       # Test labels (optional)

