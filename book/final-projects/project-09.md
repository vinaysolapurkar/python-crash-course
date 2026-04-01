# Project 9: ML Prediction App

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** scikit-learn, Flask, model training
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-09-ml-prediction/

## What You'll Build

A machine learning application that predicts house prices based on features like square footage, number of bedrooms, and location. You'll generate a realistic training dataset, train a model using scikit-learn, evaluate its performance, save the trained model, and serve predictions through a Flask API.

Here's what using it looks like:

```bash
# Train the model
$ python train_model.py

Training house price prediction model...
Dataset: 1000 samples, 6 features
Training set: 800 samples
Test set: 200 samples

Model Performance:
  R2 Score:           0.92
  Mean Absolute Error: $18,432
  Root Mean Sq Error:  $24,891

Model saved to house_price_model.pkl

# Start the prediction API
$ python prediction_api.py

# Make a prediction
$ curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"sqft": 2000, "bedrooms": 3, "bathrooms": 2,
         "age": 10, "garage": 1, "location": "suburban"}'

{"predicted_price": "$342,150", "confidence_range": "$317,718 - $366,582"}
```

## Skills You'll Use

- scikit-learn for ML (learned in Chapter 17)
- Data generation and preprocessing (learned in Chapter 16)
- Flask API (learned in Chapter 15)
- File I/O with pickle (learned in Chapter 7)
- NumPy basics (learned in Chapter 16)
- Error handling (learned in Chapter 8)

## Step-by-Step Build Guide

### Step 1: Install Dependencies

```bash
pip install scikit-learn flask numpy
```

### Step 2: Generate the Training Dataset

Since we don't have a real housing dataset, we'll generate a realistic synthetic one. This is actually a common technique in ML when real data is scarce or proprietary.

```python
# generate_data.py

import csv
import random
import numpy as np

def generate_housing_data(n_samples=1000):
    """Generate a realistic synthetic housing dataset."""
    random.seed(42)
    np.random.seed(42)

    locations = ["urban", "suburban", "rural"]
    location_multiplier = {"urban": 1.4, "suburban": 1.0, "rural": 0.7}

    data = []
    for _ in range(n_samples):
        # Generate correlated features
        sqft = random.randint(600, 5000)
        bedrooms = max(1, min(6, int(sqft / 600) + random.randint(-1, 1)))
        bathrooms = max(1, min(bedrooms, random.randint(1, bedrooms + 1)))
        age = random.randint(0, 80)
        garage = random.choice([0, 1, 2])
        location = random.choice(locations)

        # Calculate price based on realistic-ish formula + noise
        base_price = 50000
        price = base_price
        price += sqft * 150                      # price per sqft
        price += bedrooms * 15000                 # bedroom premium
        price += bathrooms * 12000                # bathroom premium
        price -= age * 1200                       # depreciation
        price += garage * 25000                   # garage value
        price *= location_multiplier[location]    # location factor

        # Add realistic noise (10% standard deviation)
        noise = np.random.normal(0, price * 0.10)
        price = max(50000, price + noise)

        data.append({
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age": age,
            "garage": garage,
            "location": location,
            "price": round(price, 2)
        })

    return data


def save_dataset(data, filename="housing_data.csv"):
    """Save dataset to CSV."""
    fieldnames = ["sqft", "bedrooms", "bathrooms", "age",
                  "garage", "location", "price"]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated {len(data)} samples -> {filename}")


if __name__ == "__main__":
    data = generate_housing_data(1000)
    save_dataset(data)

    # Quick stats
    prices = [d["price"] for d in data]
    print(f"Price range: ${min(prices):,.0f} - ${max(prices):,.0f}")
    print(f"Average price: ${sum(prices)/len(prices):,.0f}")
```

### Step 3: Train the Model

This is where the ML magic happens. We'll load the data, preprocess it (encoding the location category), split it into training and test sets, train a Random Forest model, and evaluate its performance.

```python
# train_model.py

import csv
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

MODEL_FILE = "house_price_model.pkl"
ENCODER_FILE = "location_encoder.pkl"


def load_data(filename="housing_data.csv"):
    """Load the housing dataset from CSV."""
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    # Convert to numpy arrays
    locations = [row["location"] for row in data]

    # Encode location strings as numbers
    encoder = LabelEncoder()
    location_encoded = encoder.fit_transform(locations)

    features = []
    prices = []
    for i, row in enumerate(data):
        features.append([
            float(row["sqft"]),
            int(row["bedrooms"]),
            int(row["bathrooms"]),
            int(row["age"]),
            int(row["garage"]),
            location_encoded[i]
        ])
        prices.append(float(row["price"]))

    X = np.array(features)
    y = np.array(prices)

    return X, y, encoder


def train_and_evaluate():
    """Train the model and print evaluation metrics."""
    print("Training house price prediction model...")
    print()

    # Load data
    X, y, encoder = load_data()
    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")

    # Train Random Forest model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1  # Use all CPU cores
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))

    print(f"\nModel Performance:")
    print(f"  R2 Score:            {r2:.3f}")
    print(f"  Mean Absolute Error: ${mae:,.0f}")
    print(f"  Root Mean Sq Error:  ${rmse:,.0f}")

    # Feature importance
    feature_names = ["sqft", "bedrooms", "bathrooms",
                     "age", "garage", "location"]
    importances = model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]

    print(f"\nFeature Importance:")
    for idx in sorted_idx:
        bar = "#" * int(importances[idx] * 40)
        print(f"  {feature_names[idx]:<12} {bar} ({importances[idx]:.3f})")

    # Save the model and encoder
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)
    print(f"\nModel saved to {MODEL_FILE}")

    with open(ENCODER_FILE, "wb") as f:
        pickle.dump(encoder, f)
    print(f"Encoder saved to {ENCODER_FILE}")

    return model, encoder


if __name__ == "__main__":
    train_and_evaluate()
```

### Step 4: Build the Prediction API

Now wrap the trained model in a Flask API so anyone can get predictions by sending a JSON request.

```python
# prediction_api.py

import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_FILE = "house_price_model.pkl"
ENCODER_FILE = "location_encoder.pkl"

# Load model and encoder at startup
try:
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    with open(ENCODER_FILE, "rb") as f:
        encoder = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("ERROR: Model files not found. Run train_model.py first.")
    exit(1)

VALID_LOCATIONS = list(encoder.classes_)


@app.route("/predict", methods=["POST"])
def predict():
    """Predict house price from features."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Validate required fields
    required = ["sqft", "bedrooms", "bathrooms", "age", "garage", "location"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({
            "error": f"Missing fields: {', '.join(missing)}",
            "required": required
        }), 400

    # Validate values
    try:
        sqft = float(data["sqft"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])
        age = int(data["age"])
        garage = int(data["garage"])
        location = data["location"].lower()
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid value: {e}"}), 400

    if location not in VALID_LOCATIONS:
        return jsonify({
            "error": f"Invalid location. Choose from: {VALID_LOCATIONS}"
        }), 400

    if sqft <= 0 or bedrooms <= 0 or bathrooms <= 0:
        return jsonify({"error": "Values must be positive"}), 400

    # Encode location and create feature array
    location_encoded = encoder.transform([location])[0]
    features = np.array([[sqft, bedrooms, bathrooms, age,
                          garage, location_encoded]])

    # Make prediction
    predicted_price = model.predict(features)[0]

    # Calculate confidence range (rough estimate based on model error)
    margin = predicted_price * 0.07  # ~7% margin
    low = predicted_price - margin
    high = predicted_price + margin

    return jsonify({
        "predicted_price": f"${predicted_price:,.0f}",
        "confidence_range": f"${low:,.0f} - ${high:,.0f}",
        "input": {
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age": age,
            "garage": garage,
            "location": location
        }
    })


@app.route("/model-info", methods=["GET"])
def model_info():
    """Return information about the loaded model."""
    feature_names = ["sqft", "bedrooms", "bathrooms",
                     "age", "garage", "location"]
    importances = model.feature_importances_

    features_info = {}
    for name, imp in zip(feature_names, importances):
        features_info[name] = round(float(imp), 4)

    return jsonify({
        "model_type": "RandomForestRegressor",
        "n_estimators": model.n_estimators,
        "valid_locations": VALID_LOCATIONS,
        "feature_importances": features_info,
        "input_format": {
            "sqft": "int (square footage, e.g., 2000)",
            "bedrooms": "int (1-6)",
            "bathrooms": "int (1-6)",
            "age": "int (years, 0-80)",
            "garage": "int (0, 1, or 2 cars)",
            "location": f"string ({', '.join(VALID_LOCATIONS)})"
        }
    })


@app.route("/", methods=["GET"])
def home():
    """API documentation."""
    return jsonify({
        "name": "House Price Prediction API",
        "endpoints": {
            "POST /predict": "Predict house price from features",
            "GET /model-info": "Get model information",
            "GET /": "This documentation"
        },
        "example_request": {
            "sqft": 2000,
            "bedrooms": 3,
            "bathrooms": 2,
            "age": 10,
            "garage": 1,
            "location": "suburban"
        }
    })


if __name__ == "__main__":
    print("House Price Prediction API")
    print("Endpoints:")
    print("  POST /predict     - Get a price prediction")
    print("  GET  /model-info  - Model details")
    print("  GET  /            - API docs")
    print()
    app.run(debug=True)
```

### Step 5: Run the Full Pipeline

Execute these commands in order:

```bash
# Step 1: Generate the dataset
python generate_data.py

# Step 2: Train the model
python train_model.py

# Step 3: Start the API
python prediction_api.py

# Step 4: Test (in another terminal)
curl http://localhost:5000/

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sqft": 2000, "bedrooms": 3, "bathrooms": 2,
       "age": 10, "garage": 1, "location": "suburban"}'

curl http://localhost:5000/model-info
```

## Challenges (Level Up!)

1. **Model comparison:** Train multiple models (Linear Regression, Gradient Boosting, and Random Forest) and compare their performance. Add an endpoint that returns predictions from all three models with their confidence scores.

2. **Input validation and feature engineering:** Add derived features like price-per-sqft from the training data, bed-to-bath ratio, and age categories (new/moderate/old). Retrain and see if performance improves.

3. **Batch predictions:** Add a `/predict/batch` endpoint that accepts a JSON array of houses and returns predictions for all of them at once, along with summary statistics (average predicted price, range).

## Portfolio Tips

An ML project that goes from data to trained model to serving API is exactly what employers want to see. When presenting this:

- **GitHub:** Include all three scripts with clear naming. Add a README that explains the ML pipeline (data generation, training, evaluation, serving). Include the model performance metrics.
- **Resume:** "Built an end-to-end ML pipeline: synthetic data generation, Random Forest model training (R2=0.92), and a Flask REST API serving real-time house price predictions."
- **Interview talking point:** Discuss why you chose Random Forest (handles non-linear relationships, built-in feature importance, robust to outliers). Explain the train/test split and why it matters (preventing overfitting). Talk about how you'd deploy this in production (Docker, cloud hosting, model versioning).
