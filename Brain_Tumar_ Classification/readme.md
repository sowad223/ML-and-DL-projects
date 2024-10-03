# Brain Tumor Classification
**DATASET:** https://www.kaggle.com/code/shivamagarwal29/brain-tumor-classification
## Overview

This project aims to classify brain tumor images using deep learning techniques. Four different models have been implemented, including SegNet, DeepLab, Fully Convolutional Network (FCN), and Convolutional Neural Network (CNN). Each model is designed to effectively handle the classification task of brain tumor images into four categories:

- **Glioma Tumor**
- **Meningioma Tumor**
- **No Tumor**
- **Pituitary Tumor**

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- TensorFlow
- Keras
- NumPy
- Matplotlib
- OpenCV
- scikit-learn

## Installation

You can install the required packages using pip:

```bash
pip install tensorflow keras numpy matplotlib opencv-python scikit-learn
```

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sowad223/ML-and-DL-projects.git
   cd ML-and-DL-projects/Brain_Tumor_Classification
   ```

   ```

   This will handle the loading of data, training the models, and making predictions.

2. **Predicting Tumor Types**:
   
   To make predictions using the trained models, update the path in the script to point to the images you want to classify. The script will automatically handle image loading and display the predicted class.

## Directory Structure

```
ML-and-DL-projects/
│
├── Brain_Tumor_Classification/
│   └── brain_tumor_classification-4models.ipynb  # Main code file
│
├── data/
│   ├── train/                         # Training dataset
│   └── test/                          # Testing dataset
│
├── requirements.txt                   # List of required packages
└── README.md                          # Project documentation
```

## Acknowledgments

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [OpenCV](https://opencv.org/)
- [Matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)



## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



MIT License

Copyright (c) [2024] [Sowad Rahman]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
