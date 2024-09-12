
# Transfer Learning and Custom Models for Fish Species Classification

This repository contains 10 Jupyter notebooks that demonstrate transfer learning and custom model approaches for fish species classification using the Fish Dataset from Kaggle. Each notebook includes the steps to download the dataset, extract it, and apply various pre-trained models for transfer learning as well as custom CNN and CNN + LSTM hybrid models.

## Models Covered

1. **VGG16**: A convolutional neural network that is 16 layers deep. We fine-tune the model using transfer learning.
2. **VGG19**: A variant of VGG16 but with 19 layers. Another transfer learning approach.
3. **ResNet50**: A deep residual network with 50 layers. We fine-tune the last few layers.
4. **ResNet101**: A deeper residual network with 101 layers, applied via transfer learning.
5. **ResNet152**: The deepest of the ResNet architectures used, with 152 layers.
6. **InceptionV3**: An efficient model that uses inception modules to capture complex features.
7. **Xception**: An extension of the Inception architecture, using depthwise separable convolutions.
8. **MobileNet**: A lightweight, efficient model suitable for mobile and edge devices.
9. **Custom CNN**: A fully custom convolutional neural network built from scratch for fish classification.
10. **Hybrid CNN + LSTM**: A combination of CNN for feature extraction and LSTM for sequential data processing (useful if you have a sequence of images, e.g., in video data).

## Dataset

All models are trained using the [Fish Dataset](https://www.kaggle.com/datasets/markdaniellampa/fish-dataset), which consists of images of different fish species. The dataset is automatically downloaded and extracted in each notebook.

## Steps in Each Notebook

Each notebook follows these steps:

1. **Dataset Download & Extraction**: The Fish Dataset is downloaded from Kaggle, and the ZIP file is extracted.
2. **Data Preprocessing**: The dataset is preprocessed using `ImageDataGenerator` to augment and normalize the images.
3. **Model Definition**: Each notebook includes the specific model (either a pre-trained model for transfer learning or a custom model).
4. **Training**: The model is trained for 10 epochs using the fish dataset.
5. **Result Visualization**: After training, the training and validation accuracy and loss curves are plotted.
6. **Evaluation**: The model is evaluated on the test dataset, and test accuracy is reported.

## Usage

To run the notebooks, follow these steps:

1. Download or clone the repository.
2. Ensure you have the `kaggle.json` API key file for Kaggle access. You will be prompted to upload this file in each notebook.
3. Open any of the Jupyter notebooks.
4. Run each cell to download the dataset, preprocess the data, and train the model.
5. Visualize the results after training is complete.

## Models Overview

| Model         | Description                                                          |
|---------------|----------------------------------------------------------------------|
| VGG16         | 16-layer deep convolutional network with transfer learning.          |
| VGG19         | 19-layer deep convolutional network with transfer learning.          |
| ResNet50      | Residual network with 50 layers using transfer learning.             |
| ResNet101     | Residual network with 101 layers for deeper feature extraction.      |
| ResNet152     | Deeper residual network with 152 layers using transfer learning.      |
| InceptionV3   | Efficient model with inception modules for feature extraction.       |
| Xception      | Depthwise separable convolutions based on Inception architecture.    |
| MobileNet     | Lightweight model for efficient computation on mobile/edge devices.  |
| Custom CNN    | Custom convolutional neural network built from scratch.              |
| CNN + LSTM    | Hybrid model with CNN for spatial feature extraction and LSTM for temporal sequence processing. |

## Requirements

- Python 3.x
- TensorFlow 2.x
- Keras
- Matplotlib
- Kaggle API (for dataset download)
- Jupyter Notebook

You can install the required packages using the following command:

```bash
pip install tensorflow keras matplotlib kaggle
```

## License

This repository is licensed under the MIT License.

