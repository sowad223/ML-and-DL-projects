import os
import zipfile
from flask import Flask, request, render_template, redirect, url_for
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


app = Flask(__name__)

# Define paths
model_path = "D:\Brain_Tumar_ Classification\segnet_model.h5" # Update with your model path
uploads_dir = 'D:\\Brain_Tumar_ Classification\\uploads'
users_dir = 'D:\\Brain_Tumar_ Classification\\user_uploads'  # Directory for user uploads


model = load_model(model_path)


class_names = {
    0: 'glioma_tumor',
    1: 'meningioma_tumor',
    2: 'no_tumor',
    3: 'pituitary_tumor'
}


if not os.path.exists(users_dir):
    os.makedirs(users_dir)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400


    user_folder = os.path.join(users_dir, file.filename.split('.')[0])
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)


    file_path = os.path.join(user_folder, file.filename)
    file.save(file_path)


    img = image.load_img(file_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)


    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_names[predicted_class]


    class_folder = os.path.join(user_folder, predicted_class_name)
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)


    os.rename(file_path, os.path.join(class_folder, file.filename))


    uploaded_count = len(os.listdir(user_folder))

    return f'Uploaded {file.filename} categorized as {predicted_class_name}. Total images uploaded: {uploaded_count}'

if __name__ == '__main__':
    app.run(debug=True)
