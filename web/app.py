from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
from PIL import Image
import io

app = Flask(__name__)
app.config['TEST_IMAGES_FOLDER'] = 'static/test_images/'

# Load the trained model
model_path = os.path.join('saved_models', 'last.keras')
model = load_model(model_path)

def prepare_image(image, target_size):
    # Preprocess the image
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize to match the training data
    return image

@app.route("/", methods=["GET"])
def index():
    # List images in the test_images directory
    test_images = {}
    for subdir, _, files in os.walk(app.config['TEST_IMAGES_FOLDER']):
        folder = os.path.relpath(subdir, app.config['TEST_IMAGES_FOLDER'])
        if folder == '.':
            folder = ''
        test_images[folder] = [file for file in files if file.lower().endswith(('png', 'jpg', 'jpeg'))]
    return render_template("index.html", test_images=test_images)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if 'file' in request.files:
            file = request.files['file']
            image = Image.open(io.BytesIO(file.read())).convert('L')
        else:
            filename = request.form.get('filename')
            folder = request.form.get('folder', '')
            filepath = os.path.join(app.config['TEST_IMAGES_FOLDER'], folder, filename)
            image = load_img(filepath, color_mode='grayscale', target_size=(100, 100))

        image = prepare_image(image, target_size=(100, 100))

        # Make prediction
        prediction = model.predict(image).flatten()
        prediction = (prediction > 0.5).astype(int)
        label = "PNEUMONIA" if prediction == 1 else "NORMAL"

        return jsonify({"label": label})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
