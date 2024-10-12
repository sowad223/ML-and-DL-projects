# Brain Tumor Detection

This project implements a deep learning model for brain tumor detection using two architectures: ResNet50 CNN and a hybrid CNN+LSTM model. The goal is to classify brain MRI images into tumor and non-tumor categories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Architectures](#model-architectures)
- [Training the Model](#training-the-model)
- [Evaluation](#evaluation)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sowad223/Brain_tumor_detection.git
   cd Brain_tumor_detection
Usage
### Loading the Model
You can load and use the trained models as follows:
python
from keras.models import load_model
# Load the ResNet50 model
resnet_model = load_model('resnet50_model.h5')
# Load the CNN+LSTM model
cnn_lstm_model = load_model('cnn_lstm_model.h5')
# Make predictions
predictions = resnet_model.predict(X_test)


1. **ResNet50 CNN**: This model uses the ResNet50 architecture as a feature extractor, followed
by fully connected layers for classification.
2. **CNN+LSTM**: This hybrid model combines Convolutional Neural Networks (CNN) for feature
extraction from images with Long Short-Term Memory (LSTM) layers for sequential data processing.


Training the Model
To train the models, follow this structure:
```python
# For ResNet50
resnet_model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
# For CNN+LSTM
cnn_lstm_model.fit(X_train, y_train_encoded, epochs=10, batch_size=32, validation_data=(X_val,
y_val_encoded))


Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
Acknowledgements
- [Keras](https://keras.io/) for the deep learning framework.
- [TensorFlow](https://www.tensorflow.org/) for the underlying libraries.
- The dataset used for training and evaluation
