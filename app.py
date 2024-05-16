from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cv2
import numpy as np
import pybase64
from predict import process_image
from ultralytics import YOLO
import supervision as sv

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize the YOLOv8 model
MODEL_PATH = "best.pt"
model = YOLO(MODEL_PATH)

# API route to receive an image and process it
@app.route('/process_image', methods=['POST'])
def process_image_api():
    # Check if an image file is provided in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    # Read the image file from the request
    image_file = request.files['file']

    # Convert the image file to a NumPy array
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Process the image using the YOLOv8 model
    processed_image = process_image(image, model)

    # Convert the processed image to bytes
    _, encoded_image = cv2.imencode('.jpg', processed_image)
    cv2.imwrite('test.jpg', encoded_image)
    image_bytes = encoded_image.tobytes()

    # Encode image bytes to base64
    # image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    base64_data = pybase64.b64encode(image_bytes).decode('utf-8')
    f64_decode = f'data:image/png;base64,{base64_data}'  # Add the data URI heade
    # with open('imagebase64.txt', 'w') as file:
    #     file.write(image_base64)
    # Return the processed image as base64 string
    return jsonify({'image': f64_decode}), 200

# Route to render the HTML template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)

