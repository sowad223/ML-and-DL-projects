# Chronic Disease Prediction Web Application

A web-based application to predict chronic disease status using user-provided medical parameters. The application leverages a trained Random Forest Classifier and provides an easy-to-use form for inputting data, with a visually appealing and cheerful interface.

## Features
- User-friendly form interface for data input.
- Side-by-side layout with a bright, jolly design.
- Predicts whether a user has a chronic disease based on the provided medical parameters.
- Displays a detailed result page with the prediction outcome.
- Option to try again and re-enter data.

## Results
![Prediction Result Screenshot](https://github.com/sowad223/ML-and-DL-projects/blob/main/chronic_kidney_disease_prediction/result/Screenshot%202024-12-16%20065811.png?raw=true)

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Model**: Random Forest Classifier (trained and saved using `joblib`)

## Prerequisites
Ensure the following are installed on your system:
- Python (>= 3.7)
- Flask (>= 2.0)
- scikit-learn (>= 0.24)
- joblib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sowad223/chronic-disease-prediction.git
    cd chronic-disease-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the trained model file (`random_forest_model_1.991667.joblib`) is in the project directory.

5. Run the Flask application:
    ```bash
    python app.py
    ```


    ```

## Usage
1. Fill in the form with your medical data, including fields like age, blood pressure, sugar levels, and more.
2. Click the **Predict** button.
3. View the prediction result, which indicates whether a chronic disease is detected.
4. Use the **Try Again** button to reset the form and input new data.

## Project Structure

```plaintext
chronic-disease-prediction/
├── app.py                 # Flask application code
├── random_forest_model_1.991667.joblib  # Pre-trained model file
├── templates/
│   ├── index.html         # Home page with the input form
│   ├── result.html        # Prediction result page
├── static/
│   ├── styles.css         # Styling for the application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
