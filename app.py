from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cv2
import numpy as np
import pybase64
from predict import process_image
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)

MODEL_PATH = "best.pt"
model = YOLO(MODEL_PATH)

@app.route('/process_image', methods=['POST'])
def process_image_api():
    if 'file' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['file']
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    processed_image = process_image(image, model)

    _, encoded_image = cv2.imencode('.jpg', processed_image)
    image_bytes = encoded_image.tobytes()
    base64_data = pybase64.b64encode(image_bytes).decode('utf-8')
    f64_decode = f'data:image/png;base64,{base64_data}'
    return jsonify({'image': f64_decode}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
