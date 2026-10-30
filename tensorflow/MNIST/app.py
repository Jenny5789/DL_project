import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from utils import preprocess_image, postprocess

app = Flask(__name__)
MODEL_PATH = os.environ.get("MODEL_PATH", "model.keras")
print(f"Loading model from {MODEL_PATH} ...")
model = tf.keras.models.load_model(MODEL_PATH)
_ = model.predict(np.zeros((1, 28, 28, 1), dtype=np.float32), verbose=0)

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400
    arr = preprocess_image(request.files["file"])
    pred = model.predict(arr, verbose=0)
    return jsonify(postprocess(pred[0]))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
