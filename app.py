# app.py
# -----------------------------
# Step 2: Flask web app for digit recognition
# It loads model.pkl and predicts drawn digits from a simple HTML canvas.

from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from PIL import Image
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get image data from frontend
    data = request.form["image"]
    # Remove prefix "data:image/png;base64,"
    data = data.split(",")[1]
    # Decode base64 string to bytes
    image = Image.open(io.BytesIO(base64.b64decode(data))).convert("L").resize((8, 8))
    
    # Convert to numpy array and scale
    img_array = np.array(image)
    img_array = (16 - (img_array / 16)).flatten().reshape(1, -1)

    # Predict digit
    prediction = model.predict(img_array)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
