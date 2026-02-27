# 📌 Project Documentation

# Fake Review Detection System for E-Commerce

---

# 1️⃣ Project Overview

Fake reviews mislead customers and damage trust in online marketplaces.
This project builds a Machine Learning-based system that detects whether a product review is:

* ✅ Genuine
* ❌ Fake

The system uses Natural Language Processing (NLP) techniques and a Logistic Regression classifier to analyze review text and predict authenticity.

---

# 2️⃣ Technology Stack

## 🧠 Machine Learning Stack

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

## 🌐 Backend

* Flask (Python Web Framework)
* Flask-CORS
* Pickle (Model serialization)

## 🎨 Frontend

* HTML
* CSS
* JavaScript
* Chart.js (for live graphs)

---

# 3️⃣ System Architecture

```
User Input (Review Text)
        ↓
Frontend (HTML + JS)
        ↓
Flask API (Backend)
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression Model
        ↓
Prediction + Confidence
        ↓
Frontend Dashboard (Chart + Progress Bar)
```

---

# 4️⃣ Working of the System

## Step 1: Data Collection

The dataset contains:

* Review text
* Rating
* Label (0 = Fake, 1 = Genuine)

Example:

| Text               | Rating | Label |
| ------------------ | ------ | ----- |
| "Amazing product!" | 5      | 1     |
| "Fake seller scam" | 1      | 0     |

---

## Step 2: Text Preprocessing

The review text is converted into string format and cleaned.

Common preprocessing steps:

* Lowercasing
* Removing stopwords (like “the”, “is”, “and”)
* Tokenization (handled by TF-IDF)

---

## Step 3: Feature Extraction (TF-IDF)

TF-IDF converts text into numerical vectors.

### Why TF-IDF?

* Assigns higher weight to important words
* Reduces importance of common words
* Works efficiently for text classification

Example:

Input:

```
"This product is amazing"
```

Output:

```
[0.0, 0.34, 0.89, 0.0, ...]
```

Now text becomes mathematical data.

---

## Step 4: Model Training (Logistic Regression)

We use:

```
LogisticRegression()
```

### Why Logistic Regression?

* Works well for binary classification
* Fast and lightweight
* Good performance for text data
* Easy to interpret

The model learns patterns like:

* Words such as “scam”, “fake”, “waste” → often fake
* Words such as “excellent”, “quality” → often genuine

---

## Step 5: Model Evaluation

The dataset is split:

* 80% Training
* 20% Testing

We evaluate using:

* Precision
* Recall
* F1-score
* Accuracy

---

## Step 6: Model Saving

After training:

```
model.pkl
vectorizer.pkl
```

These files are loaded in the backend for real-time prediction.

---

# 5️⃣ Backend Working (Flask API)

Flask provides an API endpoint:

```
POST /predict
```

### Process:

1. Receives review text
2. Converts text using TF-IDF
3. Passes vector to Logistic Regression
4. Returns:

```json
{
  "label": "Fake",
  "confidence": 0.87
}
```

---

# 6️⃣ Frontend Working

The frontend:

* Accepts user review
* Sends request to Flask API
* Displays:

  * Prediction (Fake / Genuine)
  * Confidence percentage
  * Animated progress bar
  * Live pie chart (Fake vs Genuine count)

---

# 7️⃣ Data Visualization (Interactive Features)

We implemented:

### 📊 Live Pie Chart

Using Chart.js to show:

* Total fake reviews detected
* Total genuine reviews detected

### 📈 Confidence Progress Bar

Visually represents model certainty.

These features improve:

* User interaction
* Visual understanding
* Hackathon presentation quality

---

# 8️⃣ Why This Model is Suitable

✔ Lightweight
✔ Fast prediction
✔ Easy to deploy
✔ Good accuracy on text classification
✔ Interpretable
✔ Works well for hackathon-scale datasets

---

# 9️⃣ Advantages of the System

* Helps customers avoid misleading products
* Helps small businesses maintain credibility
* Fast real-time analysis
* Easy to scale
* Simple deployment

---

# 🔟 Future Enhancements

Possible upgrades:

* Deep Learning (LSTM)
* Transformer-based model (BERT)
* Bulk review analysis
* User trust scoring
* Chrome extension
* Review sentiment analysis
* Fake reviewer behavior detection

---

# 1️⃣1️⃣ Conclusion

This project successfully implements a Machine Learning pipeline using TF-IDF and Logistic Regression to detect fake reviews.

It combines:

* NLP
* Backend API
* Interactive Frontend
* Data Visualization

The system is efficient, scalable, and suitable for real-world e-commerce platforms.

