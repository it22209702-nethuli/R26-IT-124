from flask import Flask, request, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

classes = ["Fresh", "Early", "Moderate", "Spoiled"]

@app.route("/", methods=["GET"])
def home():
    return "Pineapple Freshness Detection Backend Running"

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)

    # Temporary mock prediction
    prediction = random.choice(classes)

    confidence = round(random.uniform(0.75, 0.96), 2)

    result = {
        "filename": image.filename,
        "freshness": prediction,
        "confidence": confidence,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)