# Heart Disease Prediction Using Machine Learning

## Overview

This project aims to predict the presence or absence of heart disease based on various health-related attributes using multiple machine learning algorithms. The dataset includes information such as age, sex, cholesterol levels, blood pressure, and more. Several classification models are employed to determine the best-performing algorithm for predicting heart disease.

## Dataset

The dataset used in this project contains several health-related attributes and the target variable `Heart Disease`, which indicates whether the person has heart disease or not.

### Data Columns:
1. **Age**: Age of the individual.
2. **Sex**: Gender of the individual (1 = male, 0 = female).
3. **Chest pain type**: Type of chest pain (4 types).
4. **BP (Blood Pressure)**: Blood pressure levels.
5. **Cholesterol**: Cholesterol level.
6. **FBS over 120**: Fasting blood sugar greater than 120 mg/dl (1 = true, 0 = false).
7. **EKG results**: Electrocardiographic results.
8. **Max HR**: Maximum heart rate achieved during exercise.
9. **Exercise angina**: Whether the person experiences exercise-induced angina (1 = yes, 0 = no).
10. **ST depression**: Depression induced by exercise relative to rest.
11. **Slope of ST**: Slope of the peak exercise ST segment.
12. **Number of vessels fluro**: Number of vessels colored by fluoroscopy.
13. **Thallium**: Type of thallium used in test (3 levels).
14. **Heart Disease**: Target variable indicating the presence (Presence) or absence (Absence) of heart disease.

### Sample Data:
| Age | Sex | Chest pain type | BP  | Cholesterol | FBS over 120 | EKG results | Max HR | Exercise angina | ST depression | Slope of ST | Number of vessels fluro | Thallium | Heart Disease |
|-----|-----|-----------------|-----|-------------|--------------|-------------|--------|-----------------|---------------|-------------|-------------------------|----------|---------------|
| 70  | 1   | 4               | 130 | 322         | 0            | 2           | 109    | 0               | 2.4           | 2           | 3                       | 3        | Presence      |
| 67  | 0   | 3               | 115 | 564         | 0            | 2           | 160    | 0               | 1.6           | 2           | 0                       | 7        | Absence       |
| 57  | 1   | 2               | 124 | 261         | 0            | 0           | 141    | 0               | 0.3           | 1           | 0                       | 7        | Presence      |
| 64  | 1   | 4               | 128 | 263         | 0            | 0           | 105    | 1               | 0.2           | 2           | 1                       | 7        | Absence       |
| 74  | 0   | 2               | 120 | 269         | 0            | 2           | 121    | 1               | 0.2           | 1           | 1                       | 3        | Absence       |

## Models

This project includes the implementation of various machine learning algorithms for classification tasks. Below are the models used in this project:

### 1. **Logistic Regression**
   - A statistical model that is commonly used for binary classification tasks.
   
### 2. **Decision Tree Classifier**
   - A model that uses a tree-like graph of decisions and their possible consequences.

### 3. **Random Forest Classifier**
   - An ensemble method that creates a forest of decision trees and outputs the majority prediction.

### 4. **Support Vector Machine (SVM)**
   - A supervised learning model that finds the hyperplane that best divides the data.

### 5. **K-Nearest Neighbors (KNN)**
   - A classification algorithm that assigns the class of a data point based on the majority class of its nearest neighbors.

### 6. **Gradient Boosting Classifier**
   - An ensemble learning method that builds models sequentially, with each model correcting the errors of its predecessor.

### 7. **XGBoost**
   - A powerful and efficient gradient boosting library optimized for performance and scalability.

### 8. **AdaBoost Classifier**
   - An ensemble method that combines weak learners to create a strong learner.

### 9. **Naive Bayes Classifier**
   - A probabilistic classifier based on Bayes' Theorem, assuming independence between features.

### 10. **MLP Neural Network**
   - A neural network model used for classification, consisting of layers of neurons connected by weights.

### 11. **Ridge Classifier**
   - A linear model that combines Ridge regression with classification.

### 12. **Bagging Classifier**
   - An ensemble method that trains multiple classifiers on different subsets of the data and aggregates their predictions.

### 13. **HistGradientBoosting Classifier**
   - A variant of gradient boosting optimized for large datasets and high performance.

### 14. **Linear SVC**
   - A Support Vector Classifier that uses a linear kernel for classification.

### 15. **Extra Trees Classifier**
   - An ensemble method similar to Random Forest, but it builds trees using random splits for both features and data samples.

## Project Workflow

1. **Data Preprocessing**: 
   - Data cleaning: Handle missing values, encoding categorical variables.
   - Feature scaling: Standardize numeric features.

2. **Model Training**:
   - Split the data into training and testing sets.
   - Train multiple models on the training set.

3. **Model Evaluation**:
   - Evaluate models using various metrics (accuracy, precision, recall, F1-score, confusion matrix, etc.).
   - Use cross-validation to avoid overfitting.

4. **Model Comparison**:
   - Compare the performance of different models and select the best one based on evaluation metrics.

## Evaluation Metrics

The models are evaluated using the following metrics:
- **Accuracy**: Proportion of correct predictions out of all predictions.
- **Precision**: Proportion of positive predictions that are actually positive.
- **Recall**: Proportion of actual positives that are correctly predicted.
- **F1-Score**: Harmonic mean of precision and recall.
- **Confusion Matrix**: A table used to describe the performance of a classification model.
- **ROC-AUC**: The Area Under the Receiver Operating Characteristic Curve, used for binary classification.

## Installation

To run this project, make sure you have Python 3.x installed and the following libraries:

```bash
pip install pandas scikit-learn matplotlib xgboost
