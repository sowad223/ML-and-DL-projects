# Fracture Multi-Region X-Ray Dataset

This repository is designed to assist in the exploration and training of machine learning models using the **Fracture Multi-Region X-Ray Dataset** from Kaggle. The dataset contains X-ray images of bone fractures, organized into binary classification tasks for detecting fractures.

## Dataset Overview

- **Source**: [Kaggle - Fracture Multi-Region X-Ray Data](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)
- **Purpose**: Binary classification to detect the presence or absence of bone fractures.
- **Structure**:
  - **Train**: Contains images for training the model.
  - **Validation**: Used to validate model performance during training.
  - **Test**: Separate data to evaluate the model.

### Directory Structure
```
Bone_Fracture_Binary_Classification/
├── train/
│   ├── Fracture/
│   ├── Normal/
├── val/
│   ├── Fracture/
│   ├── Normal/
├── test/
    ├── Fracture/
    ├── Normal/
```

### Image Details
- **Format**: JPEG
- **Channels**: Grayscale
- **Size**: Various resolutions, resized to 224x224 during preprocessing.

---

## Preprocessing Pipeline

1. **Grayscale Conversion**:
   - All images are converted to grayscale (single channel).
2. **Resizing**:
   - Images are resized to `224x224` for uniformity.
3. **Normalization**:
   - Standardized to zero mean and unit variance.
4. **Data Augmentation** (Training Only):
   - Random flips, rotations, and zooms to improve generalization.

---

## Model Architecture

We use a hybrid convolutional neural network (CNN) for feature extraction and binary classification. The architecture includes:

1. **Convolutional Layers**:
   - 4 blocks with increasing filters (64, 128, 256, 512).
   - Batch normalization and max pooling for stability and dimensionality reduction.
2. **Dense Layers**:
   - Fully connected layers for classification.
   - Dropout for regularization.
3. **Output Layer**:
   - Sigmoid activation for binary classification.

### Hyperparameters
- Optimizer: Adam (learning rate = 0.0001)
- Loss Function: Binary Cross-Entropy
- Metrics: Accuracy, Precision, Recall

---

## Training Configuration

1. **Early Stopping**:
   - Monitors validation loss and stops training if no improvement after 5 epochs.
2. **Epochs**:
   - Maximum of 50 epochs.
3. **Batch Size**:
   - 32 samples per batch.
4. **Callbacks**:
   - Early stopping to prevent overfitting.

---

## Evaluation Metrics

- **Accuracy**: Percentage of correctly classified samples.
- **Precision**: True positives / (True positives + False positives).
- **Recall**: True positives / (True positives + False negatives).

---

## How to Use

### Prerequisites
1. Install TensorFlow and other dependencies:
   ```bash
   pip install tensorflow matplotlib
   ```

2. Download and extract the dataset from Kaggle.

### Running the Model

1. Preprocess the dataset and create training, validation, and test sets.
2. Train the model using the provided Python code.
3. Evaluate the model on the test set.

### Visualizing Results
- Use the provided plotting functions to visualize:
  - Training and validation accuracy.
  - Training and validation loss.

---

## Notes
- Ensure all images in the dataset are valid and properly formatted.
- If using GPUs, verify TensorFlow is configured for GPU acceleration.
- Consider using transfer learning with pre-trained models (e.g., ResNet, DenseNet) for better performance.

---

## References
- Kaggle Dataset: [Fracture Multi-Region X-Ray Data](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)
- TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)

---

## Author
Developed by Ahsan Mahbub, utilizing state-of-the-art techniques for medical image analysis and classification.

**More models on this going to be added like qnn,qnn+transfer learning etc.**
