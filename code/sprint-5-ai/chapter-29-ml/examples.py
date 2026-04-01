"""
Chapter 29: Machine Learning 101 — Teaching Computers to Learn
================================================================

Machine Learning is NOT magic. It's just math that finds patterns.

Here's the simplest way to think about it:
  - Regular programming: You write RULES, computer follows them.
  - Machine learning: You give DATA, computer DISCOVERS the rules.

Example:
  Regular: "If email contains 'FREE MONEY', it's spam"
  ML: "Here are 10,000 emails labeled spam/not-spam. Figure it out."

The ML workflow is always the same:
  1. Get data
  2. Split into training set and test set
  3. Train a model on the training data
  4. Test it on the test data (data it's never seen!)
  5. Evaluate how well it did

Let's do this! You're building AI now — that's not normal beginner stuff!
"""

import numpy as np

# scikit-learn is THE machine learning library for Python
# It's like a toolbox full of pre-built ML algorithms
try:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import (mean_squared_error, r2_score,
                                  accuracy_score, confusion_matrix,
                                  classification_report)
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    print("scikit-learn not installed! Run: pip install scikit-learn")
    print("This chapter requires sklearn. Examples shown but won't execute.\n")


# ============================================================
# 1. THE TRAIN/TEST SPLIT CONCEPT
# ============================================================
# Imagine studying for a test. You practice with old exams
# (training data), then take the real exam (test data).
# If you only test yourself on questions you've already seen,
# you don't really know if you learned anything.
#
# Same with ML! We HIDE some data from the model during training,
# then see if it can correctly predict the hidden data.

print("=" * 60)
print("CONCEPT: Train/Test Split")
print("=" * 60)
print("""
  All your data: [||||||||||||||||||||||||||||||||||||||||]
                  ^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^
                  Training data (80%)       Test data (20%)

  Training: Model learns patterns from this data
  Testing:  Model proves it learned (not memorized!) on NEW data
""")


# ============================================================
# 2. LINEAR REGRESSION — Predicting Numbers
# ============================================================
# Linear regression finds the best straight line through your data.
# Think of it as drawing a line of best fit — remember that from
# math class? Same thing, but the computer does it.
#
# Use case: "Given a house's size, predict its price."

if HAS_SKLEARN:
    print("=" * 60)
    print("LINEAR REGRESSION — Predicting House Prices")
    print("=" * 60)

    # Create synthetic housing data
    # (We're making our own data because the real Boston dataset
    #  has been deprecated for ethical reasons)
    np.random.seed(42)
    n_houses = 200

    # Features (inputs) — things we know about each house
    size_sqft = np.random.uniform(800, 3500, n_houses)
    bedrooms = np.random.randint(1, 6, n_houses)
    age_years = np.random.uniform(0, 50, n_houses)

    # Price (target) — what we want to predict
    # Formula: price is mostly driven by size + bedrooms - age + noise
    price = (size_sqft * 150                      # $150 per sqft
             + bedrooms * 20000                     # $20k per bedroom
             - age_years * 1000                     # Loses $1k per year of age
             + np.random.normal(0, 25000, n_houses))  # Random noise (real life!)

    # Combine features into a 2D array (sklearn expects this shape)
    X = np.column_stack([size_sqft, bedrooms, age_years])
    y = price

    print(f"Dataset: {n_houses} houses")
    print(f"Features: size (sqft), bedrooms, age (years)")
    print(f"Target: price ($)")
    print(f"X shape: {X.shape}, y shape: {y.shape}")
    print()

    # --- STEP 1: Split data into training and test sets ---
    # test_size=0.2 means 20% for testing, 80% for training
    # random_state is like a seed — makes it reproducible
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training set: {X_train.shape[0]} houses")
    print(f"Test set:     {X_test.shape[0]} houses")
    print()

    # --- STEP 2: Create and train the model ---
    model = LinearRegression()
    model.fit(X_train, y_train)  # This is where the learning happens!
    # .fit() finds the best line through the training data

    # What did it learn? Let's look at the coefficients
    features = ["Size (sqft)", "Bedrooms", "Age (years)"]
    print("What the model learned:")
    for name, coef in zip(features, model.coef_):
        print(f"  {name}: ${coef:,.0f} per unit")
    print(f"  Base price (intercept): ${model.intercept_:,.0f}")
    print()

    # --- STEP 3: Make predictions on the test set ---
    y_pred = model.predict(X_test)

    # --- STEP 4: Evaluate the model ---
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("Model performance on TEST data:")
    print(f"  RMSE: ${rmse:,.0f}")  # Average prediction error
    print(f"  R-squared: {r2:.3f}")  # 1.0 = perfect, 0.0 = random
    print()

    # Let's predict a specific house!
    new_house = np.array([[2000, 3, 10]])  # 2000 sqft, 3 bed, 10 yrs old
    predicted_price = model.predict(new_house)[0]
    print(f"Prediction for a 2000 sqft, 3 bedroom, 10 year old house:")
    print(f"  Estimated price: ${predicted_price:,.0f}")
    print()

    # Let's see some actual vs predicted
    print("Sample predictions vs actual:")
    print(f"  {'Actual':>12s}  {'Predicted':>12s}  {'Error':>10s}")
    for actual, pred in zip(y_test[:5], y_pred[:5]):
        error = pred - actual
        print(f"  ${actual:>10,.0f}  ${pred:>10,.0f}  ${error:>+9,.0f}")
    print()


# ============================================================
# 3. DECISION TREE CLASSIFIER — Predicting Categories
# ============================================================
# Classification = predicting a CATEGORY (spam/not-spam, cat/dog)
# A Decision Tree is like a flowchart of yes/no questions.
#
# "Is the email longer than 100 words?"
#   → Yes: "Does it contain 'unsubscribe'?"
#     → Yes: "Probably not spam"
#     → No: "Check for 'FREE'..."
#   → No: ...
#
# The tree learns WHICH questions to ask from the data!

if HAS_SKLEARN:
    print("=" * 60)
    print("DECISION TREE — Will They Buy Premium?")
    print("=" * 60)

    # Synthetic data: predicting if a user will upgrade to premium
    np.random.seed(42)
    n_users = 300

    # Features
    age = np.random.randint(18, 65, n_users)
    usage_hours = np.random.uniform(0, 50, n_users)  # Hours per week
    num_features_used = np.random.randint(1, 20, n_users)

    # Target: 1 = will buy premium, 0 = won't
    # Logic: older users who use the app a lot and use many features
    # are more likely to buy premium
    buy_probability = (
        (usage_hours / 50) * 0.4
        + (num_features_used / 20) * 0.4
        + (age / 65) * 0.2
    )
    will_buy = (buy_probability + np.random.normal(0, 0.15, n_users) > 0.5).astype(int)

    X = np.column_stack([age, usage_hours, num_features_used])
    y = will_buy

    print(f"Dataset: {n_users} users")
    print(f"Features: age, usage_hours, features_used")
    print(f"Target: will buy premium (0=No, 1=Yes)")
    print(f"Class balance: {np.sum(y==1)} buyers, {np.sum(y==0)} non-buyers")
    print()

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    tree = DecisionTreeClassifier(max_depth=4, random_state=42)
    # max_depth=4 prevents the tree from getting too complex (overfitting)
    tree.fit(X_train, y_train)

    # Predict
    y_pred = tree.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.1%}")
    print(f"(The model got {accuracy:.1%} of its predictions right!)\n")

    # Confusion Matrix — the report card for classifiers
    # It shows: what did the model get right and wrong?
    #
    #                  Predicted No    Predicted Yes
    # Actually No      True Negative   False Positive  (said yes, was no)
    # Actually Yes     False Negative  True Positive   (said no, was yes)

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(f"  (Read as: rows = actual, columns = predicted)")
    print(f"                Predicted No  Predicted Yes")
    print(f"  Actually No      {cm[0][0]:>4d}          {cm[0][1]:>4d}")
    print(f"  Actually Yes     {cm[1][0]:>4d}          {cm[1][1]:>4d}")
    print()

    # Classification report — precision, recall, f1-score
    print("Classification Report:")
    print(classification_report(y_test, y_pred,
                                 target_names=["Won't Buy", "Will Buy"]))

    # Feature importance — which features matter most?
    print("Feature importance (which features matter most):")
    feature_names = ["Age", "Usage Hours", "Features Used"]
    for name, importance in zip(feature_names, tree.feature_importances_):
        bar = "#" * int(importance * 40)
        print(f"  {name:15s} {importance:.3f} {bar}")
    print()


# ============================================================
# 4. KEY ML CONCEPTS SUMMARY
# ============================================================
print("=" * 60)
print("KEY ML CONCEPTS")
print("=" * 60)
print("""
TYPES OF ML:
  Supervised Learning: You give labeled data (input → output)
    - Regression: Predict a NUMBER (price, temperature, score)
    - Classification: Predict a CATEGORY (spam/ham, cat/dog)

  Unsupervised Learning: No labels, find patterns
    - Clustering: Group similar things together
    - (We'll keep it simple and focus on supervised for now!)

THE SKLEARN WORKFLOW (memorize this!):
  1. from sklearn.xxx import ModelName
  2. model = ModelName()
  3. model.fit(X_train, y_train)      # Train
  4. predictions = model.predict(X_test)  # Predict
  5. score = metric(y_test, predictions)  # Evaluate

COMMON PITFALLS:
  - Overfitting: Model memorizes training data but fails on new data
    (Like memorizing answers instead of learning the subject)
  - Underfitting: Model is too simple to capture patterns
    (Like trying to predict house prices using only the house color)
  - Data leakage: Accidentally including test data in training
    (Like peeking at the answer key before the exam)

EVALUATION METRICS:
  Regression:
    - RMSE: Average prediction error (lower = better)
    - R-squared: How much variance explained (closer to 1 = better)
  Classification:
    - Accuracy: % of correct predictions
    - Precision: Of all "yes" predictions, how many were actually yes?
    - Recall: Of all actual "yes"es, how many did we catch?
    - F1 Score: Balance between precision and recall
""")


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 29 RECAP")
print("=" * 60)
print("""
You just built TWO machine learning models! Seriously, that's awesome.

1. Linear Regression: Predict numbers from features
2. Decision Tree: Predict categories from features
3. Train/Test Split: Always evaluate on unseen data
4. Confusion Matrix: See exactly what went right and wrong
5. Feature Importance: Know which inputs matter most

The sklearn workflow is always the same:
  model = SomeModel()
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)

Next up: AI APIs and LLMs — talking to ChatGPT from your code!
""")
