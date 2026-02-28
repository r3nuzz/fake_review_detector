from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")   # Serve the frontend

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review = data.get("review", "")

    if not review.strip():
        return jsonify({"error": "Review cannot be empty"}), 400

    # Vectorize input
    vec = vectorizer.transform([review])

    # Predict
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    return jsonify({
        "label": "Genuine" if pred == 1 else "Fake",
        "confidence": float(max(prob))
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)