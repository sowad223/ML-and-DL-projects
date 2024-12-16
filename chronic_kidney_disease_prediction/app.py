from flask import Flask, render_template, request
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained Random Forest model
model = load('random_forest_model_1.991667.joblib')

# Preprocessing function
def preprocess_input(data):
    # Replace missing values for numerical columns with a default value (e.g., mean)
    numerical_defaults = {
        'age': 40.0, 'bp': 70.0, 'sg': 1.015, 'al': 0.0, 'su': 0.0,
        'bgr': 120.0, 'bu': 20.0, 'sc': 1.0, 'sod': 135.0, 'pot': 4.5,
        'hemo': 13.5, 'pcv': 40, 'wc': 8000, 'rc': 4.5
    }
    for key, default in numerical_defaults.items():
        if pd.isna(data[key]):
            data[key] = default

    # Replace missing values for categorical columns with 'notpresent' or default
    categorical_defaults = {
        'rbc': 'normal', 'pc': 'normal', 'pcc': 'notpresent', 'ba': 'notpresent',
        'htn': 'no', 'dm': 'no', 'cad': 'no', 'appet': 'good', 'pe': 'no', 'ane': 'no'
    }
    for key, default in categorical_defaults.items():
        if pd.isna(data[key]):
            data[key] = default

    # Encode categorical variables
    categorical_mappings = {
        'rbc': {'normal': 0, 'abnormal': 1},
        'pc': {'normal': 0, 'abnormal': 1},
        'pcc': {'notpresent': 0, 'present': 1},
        'ba': {'notpresent': 0, 'present': 1},
        'htn': {'no': 0, 'yes': 1},
        'dm': {'no': 0, 'yes': 1},
        'cad': {'no': 0, 'yes': 1},
        'appet': {'good': 0, 'poor': 1},
        'pe': {'no': 0, 'yes': 1},
        'ane': {'no': 0, 'yes': 1}
    }
    for key, mapping in categorical_mappings.items():
        data[key] = mapping[data[key]]

    # Return processed data (include 'id' but exclude it in the model input)
    return [data[key] for key in [
        'id', 'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr',
        'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm',
        'cad', 'appet', 'pe', 'ane'
    ]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve form data
            input_data = {
                'id': request.form.get('id'),  # Retain ID for reference
                'age': float(request.form.get('age')),
                'bp': float(request.form.get('bp')),
                'sg': float(request.form.get('sg')),
                'al': float(request.form.get('al')),
                'su': float(request.form.get('su')),
                'rbc': request.form.get('rbc'),
                'pc': request.form.get('pc'),
                'pcc': request.form.get('pcc'),
                'ba': request.form.get('ba'),
                'bgr': float(request.form.get('bgr')),
                'bu': float(request.form.get('bu')),
                'sc': float(request.form.get('sc')),
                'sod': float(request.form.get('sod')),
                'pot': float(request.form.get('pot')),
                'hemo': float(request.form.get('hemo')),
                'pcv': int(request.form.get('pcv')),
                'wc': int(request.form.get('wc')),
                'rc': float(request.form.get('rc')),
                'htn': request.form.get('htn'),
                'dm': request.form.get('dm'),
                'cad': request.form.get('cad'),
                'appet': request.form.get('appet'),
                'pe': request.form.get('pe'),
                'ane': request.form.get('ane')
            }

            # Preprocess input data
            processed_data = preprocess_input(input_data)

        except Exception as e:
            return render_template('result.html', prediction=f"Invalid input. Error: {str(e)}")

        # Convert to numpy array and reshape (exclude 'id')
        input_array = np.array(processed_data[1:]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)

        # Interpret prediction
        result = "Chronic Disease Detected" if prediction[0] == 1 else "No Chronic Disease Detected"

        # Return the result, including the ID for reference
        return render_template('result.html', prediction=f"ID: {input_data['id']} - {result}")

if __name__ == '__main__':
    app.run(debug=True)
