
## Overview
This project implements a U-Net-based deep learning model for brain tumor segmentation using the BraTS 2020 dataset. The model segments tumor regions from multi-modal MRI scans (T1, T1ce, T2, FLAIR) and includes Grad-CAM for visualizing important regions in the predictions. The project is part of the CSE427 Lab Project and is designed to run on Kaggle with GPU support.
Features

U-Net Model: A convolutional neural network with encoder-decoder architecture for semantic segmentation.
Custom Metrics: Dice Coefficient, IoU, and F1 Score to evaluate segmentation performance.
Grad-CAM Visualization: Heatmaps to highlight regions contributing to predictions.
Training and Evaluation: 10 epochs of training with validation, saving the best model based on validation loss.
Results Visualization: Plots of loss, Dice, IoU, and F1 scores, along with prediction visualizations.

## Dataset

BraTS 2020: Multi-modal MRI scans stored in .h5 files, with 4 input channels and segmentation masks.
Preprocessing: Images and masks resized to 128x128, normalized, and converted to PyTorch tensors.
Split: 80% training, 20% validation.

## Requirements

Python 3.8+
PyTorch
NumPy
scikit-learn
scikit-image
h5py
Matplotlib
Kaggle environment with GPU (recommended)

## Installation

Clone the repository: 

git clone https://github.com/sowad223/ML-and-DL-projects.git



## Install dependencies:

pip install torch numpy scikit-learn scikit-image h5py matplotlib


Download the BraTS 2020 dataset and place it in the appropriate directory (e.g., /kaggle/input/brats2020-training-data/).

Usage

Run the main script to train the model and generate results:python main.py


## The script will:
Train the U-Net model for 10 epochs.
Save the best model (model-unet.best.pth) and final model (final_model_unet.pth).
Save training history (training_history.json).
Generate metric plots (loss_plot.png, dice_plot.png, etc.).
Produce prediction visualizations with Grad-CAM (visualization_1.png, etc.).


View results in the cse427_results directory:ML-and-DL-projects/CSE427_LAB_PROJECT/cse427_results



## Results

Metrics: Training and validation loss, Dice, IoU, and F1 scores are plotted and saved.
Visualizations: Input images, true masks, predicted masks, and Grad-CAM overlays are generated for sample predictions.
Output Files:
model-unet.best.pth: Best model based on validation loss.
final_model_unet.pth: Final trained model.
training_history.json: Training and validation metrics.
*_plot.png: Plots for loss, Dice, IoU, and F1.
visualization_*.png: Prediction and Grad-CAM visualizations.


Results are available at: cse427_results

Training Metrics
The following plots show the training and validation metrics over 10 epochs:

Loss Plot:

Dice Coefficient Plot:

IoU Plot:

F1 Score Plot:


Sample Predictions
The following image shows a sample prediction, including the input MRI (channel 0), true mask, predicted mask, and Grad-CAM overlay:



Notes

Ensure the BraTS 2020 dataset is accessible in the specified path.
The script checks for GPU availability and uses mixed precision training for efficiency.
Grad-CAM is applied to the dec1 layer; modify the layer name in GradCAM for other layers.
For improved performance, consider increasing epochs, adding data augmentation, or using additional loss functions.

## License
This project is licensed under the MIT License.
## Acknowledgments

BraTS 2020 dataset providers.
Kaggle for providing the computational environment.
PyTorch and open-source libraries used in the project.


