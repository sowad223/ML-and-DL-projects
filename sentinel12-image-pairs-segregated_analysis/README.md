
# Image Classification using Pre-trained Models

This repository provides a solution for training image classification models using four pre-trained models: **VGG16**, **ResNet50**, **EfficientNetB0**, and **InceptionV3**. These models are applied to a custom dataset organized in a directory format, and the models are fine-tuned for a multi-class classification task.

## Models Used
1. **VGG16**: A 16-layer deep Convolutional Neural Network, pre-trained on the ImageNet dataset.
2. **ResNet50**: A 50-layer deep Residual Neural Network, known for its skip connections that allow for deeper networks.
3. **EfficientNetB0**: A highly efficient model, which balances network depth, width, and resolution.
4. **InceptionV3**: A sophisticated architecture designed to capture features using multiple filter sizes within a single layer.

## Dataset Structure
The dataset should be structured in the following format:

```
dataset/
    class1/
        img1.jpg
        img2.jpg
        ...
    class2/
        img1.jpg
        img2.jpg
        ...
    ...
```

- The `dataset/` directory should contain subdirectories for each class. Inside each class directory, place the respective images.
- The script will automatically split 80% of the images for training and 20% for validation.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install tensorflow keras
```

## Model Training and Evaluation

Each model is trained and evaluated using a similar process. Follow the steps below to train and evaluate the models.

### 1. VGG16 Model

To train and evaluate the **VGG16** model:

```python
# Load and compile the VGG16 model
vgg16_base = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
vgg16_model = build_model(vgg16_base)

# Train the model
vgg16_model.fit(train_generator, validation_data=validation_generator, epochs=10)

# Evaluate the model
vgg16_eval = vgg16_model.evaluate(validation_generator)
print(f"VGG16 Evaluation - Loss: {vgg16_eval[0]}, Accuracy: {vgg16_eval[1]}")
```

### 2. ResNet50 Model

To train and evaluate the **ResNet50** model:

```python
# Load and compile the ResNet50 model
resnet50_base = ResNet50(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
resnet50_model = build_model(resnet50_base)

# Train the model
resnet50_model.fit(train_generator, validation_data=validation_generator, epochs=10)

# Evaluate the model
resnet50_eval = resnet50_model.evaluate(validation_generator)
print(f"ResNet50 Evaluation - Loss: {resnet50_eval[0]}, Accuracy: {resnet50_eval[1]}")
```

### 3. EfficientNetB0 Model

To train and evaluate the **EfficientNetB0** model:

```python
# Load and compile the EfficientNetB0 model
efficientnet_base = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
efficientnet_model = build_model(efficientnet_base)

# Train the model
efficientnet_model.fit(train_generator, validation_data=validation_generator, epochs=10)

# Evaluate the model
efficientnet_eval = efficientnet_model.evaluate(validation_generator)
print(f"EfficientNetB0 Evaluation - Loss: {efficientnet_eval[0]}, Accuracy: {efficientnet_eval[1]}")
```

### 4. InceptionV3 Model

To train and evaluate the **InceptionV3** model:

```python
# Load and compile the InceptionV3 model
inceptionv3_base = InceptionV3(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
inceptionv3_model = build_model(inceptionv3_base)

# Train the model
inceptionv3_model.fit(train_generator, validation_data=validation_generator, epochs=10)

# Evaluate the model
inceptionv3_eval = inceptionv3_model.evaluate(validation_generator)
print(f"InceptionV3 Evaluation - Loss: {inceptionv3_eval[0]}, Accuracy: {inceptionv3_eval[1]}")
```

## Training Parameters
- **Batch size**: 32 (can be adjusted for larger datasets or smaller GPUs)
- **Image size**: 224x224 pixels (required input size for all models)
- **Learning rate**: 0.0001 (can be fine-tuned as needed)
- **Optimizer**: Adam
- **Loss function**: Categorical Crossentropy (for multi-class classification)

## Evaluation
The evaluation is done using the validation set split during the data preprocessing phase. The evaluation metrics include:
- **Loss**: The categorical cross-entropy loss function.
- **Accuracy**: The accuracy of the model on the validation set.

## Customization

You can modify the following parameters based on your specific requirements:
- **Number of epochs**: Increase or decrease depending on the size of the dataset.
- **Learning rate**: Tune this hyperparameter to improve training performance.
- **Data Augmentation**: Add more augmentations in the `ImageDataGenerator` to improve model generalization.

## License
This project is licensed under the MIT License.


**The project still is'nt completed the val loss is too much because i couldn't train it for my GPU.**
