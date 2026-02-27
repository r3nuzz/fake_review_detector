from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("../model/model.pkl", "rb"))
vectorizer = pickle.load(open("../model/vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review = data.get("review", "")

    if not review.strip():
        return jsonify({"error": "Review cannot be empty"}), 400

    vec = vectorizer.transform([review])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    return jsonify({
        "label": "Genuine" if pred == 1 else "Fake",
        "confidence": float(max(prob))
    })

if __name__ == "__main__":
    app.run(debug=True)