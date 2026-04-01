"""
=============================================================
  PROJECT 9: ML PREDICTION APP - SOLUTION
=============================================================
  A machine learning house price predictor with a Flask API.
  Generates synthetic data, trains a model, and serves
  predictions via REST endpoints.

  Dependencies:
    pip install flask scikit-learn pandas numpy joblib

  Run:  python solution.py

  ── TESTING ────────────────────────────────────────────────

  # Predict a house price:
  curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"sqft":2000,"bedrooms":3,"bathrooms":2,"age":10}'

  # Predict with different features:
  curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"sqft":3500,"bedrooms":5,"bathrooms":3,"age":2}'

  # Get model info:
  curl http://localhost:5000/model-info

=============================================================
"""

import os
import sys

try:
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, r2_score
    import joblib
    from flask import Flask, request, jsonify
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install flask scikit-learn pandas numpy joblib")
    exit(1)

# ── Configuration ──────────────────────────────────────────
MODEL_FILE = "house_model.joblib"
METADATA_FILE = "model_metadata.joblib"
FEATURES = ["sqft", "bedrooms", "bathrooms", "age"]
N_SAMPLES = 1000

app = Flask(__name__)


# ── Data Generation ────────────────────────────────────────

def generate_data(n_samples=N_SAMPLES):
    """
    Generate synthetic house price data.

    The pricing formula tries to mimic real-world patterns:
    - Bigger houses cost more (price per sqft)
    - More bedrooms and bathrooms add value
    - Newer houses cost more (age reduces price)
    - Random noise simulates market variation
    """
    np.random.seed(42)  # For reproducible results

    # Generate features with realistic distributions
    sqft = np.random.randint(600, 5000, n_samples)
    bedrooms = np.random.randint(1, 6, n_samples)
    bathrooms = np.random.randint(1, 4, n_samples)
    age = np.random.randint(0, 80, n_samples)

    # Calculate price with a realistic-ish formula
    price = (
        50_000                          # Base price
        + sqft * 150                    # $150 per sqft
        + bedrooms * 15_000             # $15k per bedroom
        + bathrooms * 20_000            # $20k per bathroom
        - age * 1_500                   # $1.5k less per year of age
        + np.random.normal(0, 25_000, n_samples)  # Market noise
    )

    # Make sure no negative prices
    price = np.maximum(price, 50_000)

    df = pd.DataFrame({
        "sqft": sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "price": price.astype(int),
    })

    return df


# ── Model Training ─────────────────────────────────────────

def train_model(df):
    """
    Train a RandomForest model on the house data.
    Returns the model and evaluation metrics.
    """
    X = df[FEATURES]
    y = df["price"]

    # Split into training and test sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"  Training set: {len(X_train)} samples")
    print(f"  Test set:     {len(X_test)} samples")

    # Train a Random Forest Regressor
    model = RandomForestRegressor(
        n_estimators=100,    # 100 trees in the forest
        max_depth=15,        # Limit tree depth to prevent overfitting
        random_state=42,
        n_jobs=-1,           # Use all CPU cores
    )

    print("  Training RandomForest model...")
    model.fit(X_train, y_train)

    # Evaluate on the test set
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    metrics = {
        "r2_score": round(r2, 4),
        "mae": round(mae, 2),
        "training_samples": len(X_train),
        "test_samples": len(X_test),
        "model_type": "RandomForestRegressor",
        "n_estimators": 100,
        "features": FEATURES,
    }

    # Show feature importance
    importances = model.feature_importances_
    print("\n  Feature Importance:")
    for feature, importance in sorted(
        zip(FEATURES, importances), key=lambda x: x[1], reverse=True
    ):
        bar = "█" * int(importance * 40)
        print(f"    {feature:<12} {bar} {importance:.3f}")

    return model, metrics


def save_model(model, metrics):
    """Save the trained model and metadata to disk."""
    joblib.dump(model, MODEL_FILE)
    joblib.dump(metrics, METADATA_FILE)
    print(f"\n  Model saved to {MODEL_FILE}")
    print(f"  Metadata saved to {METADATA_FILE}")


def load_model():
    """Load the trained model from disk."""
    if not os.path.exists(MODEL_FILE):
        return None, None

    model = joblib.load(MODEL_FILE)
    metadata = joblib.load(METADATA_FILE) if os.path.exists(METADATA_FILE) else {}
    return model, metadata


# ── Flask API ──────────────────────────────────────────────

@app.route("/")
def index():
    """Welcome page with API docs."""
    return jsonify({
        "message": "House Price Prediction API",
        "endpoints": {
            "POST /predict": "Predict house price",
            "GET /model-info": "Get model metadata",
        },
        "example_request": {
            "url": "POST /predict",
            "body": {"sqft": 2000, "bedrooms": 3, "bathrooms": 2, "age": 10},
        },
    })


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict house price from features.

    Expected JSON body:
    {
        "sqft": 2000,
        "bedrooms": 3,
        "bathrooms": 2,
        "age": 10
    }
    """
    model, _ = load_model()
    if model is None:
        return jsonify({"error": "Model not trained yet. Run the script first."}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Validate that all required features are present
    missing = [f for f in FEATURES if f not in data]
    if missing:
        return jsonify({
            "error": f"Missing features: {missing}",
            "required": FEATURES,
        }), 400

    # Validate that values are numbers
    try:
        feature_values = [float(data[f]) for f in FEATURES]
    except (ValueError, TypeError):
        return jsonify({"error": "All feature values must be numbers"}), 400

    # Basic sanity checks
    if data["sqft"] <= 0 or data["bedrooms"] <= 0 or data["bathrooms"] <= 0:
        return jsonify({"error": "sqft, bedrooms, and bathrooms must be positive"}), 400

    if data["age"] < 0:
        return jsonify({"error": "age cannot be negative"}), 400

    # Make prediction
    input_array = np.array([feature_values])
    prediction = model.predict(input_array)[0]

    return jsonify({
        "predicted_price": round(prediction, 2),
        "formatted_price": f"${prediction:,.0f}",
        "input_features": {f: data[f] for f in FEATURES},
        "note": "This is a prediction based on synthetic data for learning purposes.",
    })


@app.route("/model-info", methods=["GET"])
def model_info():
    """Return metadata about the trained model."""
    _, metadata = load_model()
    if metadata is None:
        return jsonify({"error": "No model metadata available."}), 500

    return jsonify({
        "model": metadata,
        "status": "Model is loaded and ready for predictions.",
    })


# ── Main ───────────────────────────────────────────────────

def main():
    """Generate data, train model, and start the API server."""
    print()
    print("=" * 50)
    print("  HOUSE PRICE PREDICTION ML APP")
    print("=" * 50)

    # Step 1: Generate synthetic data
    print("\n  Step 1: Generating synthetic data...")
    df = generate_data()
    print(f"  Generated {len(df)} house records")
    print(f"\n  Sample data:")
    print(df.head().to_string(index=False))
    print(f"\n  Price range: ${df['price'].min():,.0f} - ${df['price'].max():,.0f}")
    print(f"  Average price: ${df['price'].mean():,.0f}")

    # Step 2: Train the model
    print("\n  Step 2: Training the model...")
    model, metrics = train_model(df)
    print(f"\n  Model Performance:")
    print(f"    R-squared score: {metrics['r2_score']}")
    print(f"    Mean Absolute Error: ${metrics['mae']:,.0f}")

    # Step 3: Save the model
    print("\n  Step 3: Saving the model...")
    save_model(model, metrics)

    # Step 4: Make a sample prediction
    print("\n  Step 4: Sample prediction...")
    sample = {"sqft": 2000, "bedrooms": 3, "bathrooms": 2, "age": 10}
    sample_array = np.array([[sample[f] for f in FEATURES]])
    price = model.predict(sample_array)[0]
    print(f"    Input: {sample}")
    print(f"    Predicted price: ${price:,.0f}")

    # Step 5: Start the API
    print()
    print("=" * 50)
    print("  API SERVER STARTING")
    print("=" * 50)
    print("  Try these commands in another terminal:")
    print()
    print('  curl http://localhost:5000/model-info')
    print()
    print('  curl -X POST http://localhost:5000/predict \\')
    print('    -H "Content-Type: application/json" \\')
    print('    -d \'{"sqft":2000,"bedrooms":3,"bathrooms":2,"age":10}\'')
    print()
    print("=" * 50)

    app.run(debug=False, port=5000)


if __name__ == "__main__":
    main()
