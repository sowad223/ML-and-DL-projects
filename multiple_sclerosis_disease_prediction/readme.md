# Multiple Sclerosis Disease Prediction: CIS to MS Conversion

## Overview

This project aims to predict the conversion of Clinically Isolated Syndrome (CIS) to Multiple Sclerosis (MS) using machine learning techniques. The dataset used in this study was collected as part of a prospective cohort study conducted in Mexican mestizo patients newly diagnosed with CIS at the National Institute of Neurology and Neurosurgery (NINN) in Mexico City, Mexico, between 2006 and 2010. The objective is to identify predictive factors and early markers that can help in understanding the likelihood of conversion from CIS to MS.

Multiple Sclerosis (MS) is a chronic autoimmune disease affecting the central nervous system, causing a wide range of symptoms, from muscle weakness to cognitive and psychiatric problems. Early identification of factors that predict the conversion from CIS to MS is critical for timely interventions and improving patient outcomes.

## Dataset

The dataset for this project contains clinical and diagnostic features, collected from patients diagnosed with CIS, to help predict the transition to MS.

### Citation

- **Reference**:  
  Pineda, Benjamin; Flores Rivera, Jose De Jesus (2023), “Conversion predictors of Clinically Isolated Syndrome to Multiple Sclerosis in Mexican patients: a prospective study.”, Mendeley Data, V1, doi: [10.17632/8wk5hjx7x2.1](https://doi.org/10.17632/8wk5hjx7x2.1)

- **License**: CC BY 4.0

### Dataset Columns:
- **ID**: Patient identifier (int)
- **Age**: Age of the patient (in years)
- **Schooling**: Time the patient spent in school (in years)
- **Gender**: 1=male, 2=female
- **Breastfeeding**: 1=yes, 2=no, 3=unknown
- **Varicella**: 1=positive, 2=negative, 3=unknown (Chickenpox history)
- **Initial_Symptoms**: 
  - 1=visual, 2=sensory, 3=motor, 4=other, 5=visual and sensory, 
  - 6=visual and motor, 7=visual and others, 8=sensory and motor, 
  - 9=sensory and other, 10=motor and other, 11=Visual, sensory and motor,
  - 12=visual, sensory and other, 13=Visual, motor and other, 
  - 14=Sensory, motor and other, 15=visual, sensory, motor and other
- **Mono_or_Polysymptomatic**: 1=monosymptomatic, 2=polysymptomatic, 3=unknown
- **Oligoclonal_Bands**: 0=negative, 1=positive, 2=unknown
- **LLSSEP**: 0=negative, 1=positive (Lower Limb Somatosensory Evoked Potential)
- **ULSSEP**: 0=negative, 1=positive (Upper Limb Somatosensory Evoked Potential)
- **VEP**: 0=negative, 1=positive (Visual Evoked Potential)
- **BAEP**: 0=negative, 1=positive (Brainstem Auditory Evoked Potential)
- **Periventricular_MRI**: 0=negative, 1=positive
- **Cortical_MRI**: 0=negative, 1=positive
- **Infratentorial_MRI**: 0=negative, 1=positive
- **Spinal_Cord_MRI**: 0=negative, 1=positive
- **Initial_EDSS**: Expanded Disability Status Scale at diagnosis (higher indicates more disability)
- **Final_EDSS**: Expanded Disability Status Scale at follow-up
- **Group**: 
  - 1=CDMS (Clinically Definite Multiple Sclerosis)
  - 2=non-CDMS (non-MS)

### Medical Terminology:
- **Oligoclonal Bands (OCBs)**: Bands of immunoglobulins in the cerebrospinal fluid, which are used in the diagnosis of MS.
- **VEP**: Visual evoked potential, used to detect damage to the visual pathway, including the optic nerve.
- **BAEP**: Brainstem auditory evoked potentials, a diagnostic test for auditory processing.
- **SSEP**: Somatosensory evoked potentials, used to evaluate sensory pathway dysfunction.

## Objective

The main objective of this project is to predict the conversion from Clinically Isolated Syndrome (CIS) to Multiple Sclerosis (MS). By analyzing a set of clinical features, we aim to identify early indicators of MS that may help clinicians make timely interventions.

### Possible Use Cases:
- Identifying key predictive factors for MS conversion.
- Classifying patients into two groups: CDMS (Multiple Sclerosis) or non-CDMS.
- Assisting doctors in decision-making regarding follow-up treatments.

## Models

Various machine learning algorithms are used to predict the conversion from CIS to MS, including but not limited to:

- **Logistic Regression**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Support Vector Machine (SVM)**
- **K-Nearest Neighbors (KNN)**
- **Gradient Boosting Classifier**
- **XGBoost**
- **Naive Bayes Classifier**
- **MLP Neural Network**
- **Ridge Classifier**
- **Bagging Classifier**
- **HistGradientBoosting Classifier**

Each model is trained on the dataset and evaluated using metrics like accuracy, precision, recall, and F1-score. The goal is to select the best model for predicting MS.

## Workflow

1. **Data Preprocessing**: 
   - Clean the dataset by handling missing values and encoding categorical variables.
   - Normalize or standardize numerical variables where applicable (e.g., SVM, KNN).

2. **Model Training**:
   - Split the dataset into training and testing sets (typically a 70-30 split).
   - Train each model and tune hyperparameters using techniques like GridSearchCV or RandomizedSearchCV.

3. **Model Evaluation**:
   - Evaluate the performance of each model using a variety of metrics including accuracy, precision, recall, F1-score, and confusion matrix.
   - Use ROC-AUC for binary classification evaluation.

4. **Model Comparison**:
   - Compare models and select the one with the best performance metrics for clinical use.

## Requirements

To run this project, ensure you have the necessary libraries installed:

```bash
pip install pandas scikit-learn xgboost matplotlib seaborn
**Mendeley Datasets:** https://data.mendeley.com/datasets/8wk5hjx7x2/1
