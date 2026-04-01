"""
=============================================================
  PROJECT 9: ML PREDICTION APP
=============================================================

Build a machine learning prediction service! You'll train
a model on synthetic house price data and serve predictions
through a Flask API.

WHAT YOU'LL PRACTICE:
  - Machine learning with scikit-learn
  - Generating synthetic training data
  - Model training and evaluation
  - Saving/loading models with joblib
  - Serving predictions via a REST API
  - Data validation

DEPENDENCIES:
  pip install flask scikit-learn pandas numpy joblib

REQUIREMENTS:
  1. Generate synthetic house price data with features:
     - sqft (square footage)
     - bedrooms
     - bathrooms
     - age (years old)
  2. Train a regression model (e.g., RandomForest)
  3. Evaluate with R-squared score and MAE
  4. Save the trained model with joblib
  5. Create a Flask API:
     POST /predict - accepts features, returns prediction
     GET  /model-info - returns model metadata
  6. Include example requests in comments

TESTING:
  # Train the model first, then start the API:
  python solution.py

  # Make a prediction:
  curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"sqft":2000,"bedrooms":3,"bathrooms":2,"age":10}'

  # Get model info:
  curl http://localhost:5000/model-info

EXAMPLE OUTPUT:
  Training model on 1000 samples...
  Model R-squared: 0.94
  Mean Absolute Error: $12,345
  Model saved to house_model.joblib

  API running at http://localhost:5000
  POST /predict with JSON body to get predictions

HINTS:
  - numpy.random for generating synthetic data
  - Use a formula: price = base + sqft*150 + bedrooms*10000 + ...
  - Add some random noise for realism
  - sklearn.ensemble.RandomForestRegressor works well
  - joblib.dump(model, 'file.joblib') to save
  - joblib.load('file.joblib') to load

Good luck!
=============================================================
"""

import os

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


MODEL_FILE = "house_model.joblib"
FEATURES = ["sqft", "bedrooms", "bathrooms", "age"]


def generate_data(n_samples=1000):
    """Generate synthetic house price data."""
    # TODO: Create random features
    # TODO: Calculate price using a formula + noise
    # TODO: Return a DataFrame
    pass


def train_model(df):
    """Train a model and return it with evaluation metrics."""
    # TODO: Split features (X) and target (y)
    # TODO: Train/test split
    # TODO: Train RandomForestRegressor
    # TODO: Evaluate (R2 score, MAE)
    # TODO: Return model and metrics
    pass


def save_model(model, metrics):
    """Save the trained model to a file."""
    # TODO: Use joblib.dump()
    pass


def load_model():
    """Load a saved model."""
    # TODO: Use joblib.load()
    pass


# ── Flask API ──────────────────────────────────────────────

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    """Make a price prediction for given house features."""
    # TODO: Get JSON data from request
    # TODO: Validate that all features are present
    # TODO: Load model and make prediction
    # TODO: Return prediction as JSON
    pass


@app.route("/model-info", methods=["GET"])
def model_info():
    """Return information about the trained model."""
    # TODO: Return model type, features, etc.
    pass


def main():
    """Train model (if needed) and start the API."""
    # TODO: Generate data
    # TODO: Train model
    # TODO: Save model
    # TODO: Start Flask app
    pass


if __name__ == "__main__":
    main()
