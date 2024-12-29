# Email Spam Classification Models

This repository contains machine learning models for classifying emails as spam or not spam. The project utilizes the [Email Spam Classification Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) and implements various machine learning algorithms for predictive analysis.

## Project Structure

- **Dataset**: The dataset used for this project is a CSV file containing email text and labels indicating whether the email is spam or not.
- **Models**: The repository contains implementations of 10 machine learning models, each in separate `.ipynb` files.
- **Evaluation**: Models are evaluated using accuracy as the primary metric.

## Models Implemented

1. Decision Tree Classifier
2. Random Forest Classifier
3. Naive Bayes Classifier
4. Logistic Regression
5. K-Nearest Neighbors (KNN)
6. Support Vector Machine (SVM)
7. Gradient Boosting Classifier
8. AdaBoost Classifier
9. Multi-Layer Perceptron (MLP) Classifier
10. Bagging Classifier

## Dataset

The dataset consists of:
- **EmailText**: The email content.
- **Prediction**: The target variable, indicating whether an email is spam (`1`) or not spam (`0`).

Dataset Source: [Kaggle - Email Spam Classification Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv)

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Jupyter Notebook or JupyterLab
- Required libraries: `numpy`, `pandas`, `scikit-learn`

Install the dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/sowad223/email_spam_classification
   ```





## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.


## Acknowledgements

- [Kaggle](https://www.kaggle.com) for providing the dataset.
- [scikit-learn](https://scikit-learn.org) for the machine learning tools used in this project.

