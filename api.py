from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
from predict import process_image
from ultralytics import YOLO
import supervision as sv

# Initialize Flask app
app = Flask(__name__)

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
    image_bytes = encoded_image.tobytes()
    
    # Return the processed image
    return image_bytes, 200, {'Content-Type': 'image/jpeg'}

# Route to render the HTML template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)