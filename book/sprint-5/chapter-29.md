# Chapter 29: Machine Learning 101: Teaching Computers to Learn

> **Sprint 5, Chapter 29** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-29-machine-learning/)**

Teaching ML is like teaching a toddler. You show them examples: "This is a cat. This is a dog. This is a cat." Eventually, they figure out the pattern themselves. You never explicitly explain whiskers or floppy ears - they just *get it* after seeing enough examples. Machine learning works the same way. You give a computer enough data, and it figures out the rules on its own.

You're building machine learning models now. Most people who start coding never get here. Take a second to appreciate that.

## What You'll Learn
- What machine learning actually is (cutting through the hype)
- Three types: supervised, unsupervised, reinforcement
- The scikit-learn workflow: load, split, train, predict, evaluate
- Your first model: predicting house prices
- Train/test split and why it matters
- Measuring how good your model is
- Decision trees: 20 questions, but for data

## Why Should I Care?

Netflix recommends your next binge. Gmail catches spam before you see it. Spotify knows you'll love that song you've never heard. Your phone unlocks with your face. Doctors catch cancer earlier. Self-driving cars navigate streets. All of this is machine learning.

And the code is literally 5 lines. Seriously. I'll show you.

## What ML Is and Isn't

**Machine learning IS:**
- A way to find patterns in data
- Software that improves with more data (instead of more rules)
- Prediction based on past examples

**Machine learning IS NOT:**
- Magic
- Artificial consciousness
- A replacement for understanding your problem
- Always the right tool (sometimes an `if` statement is all you need)

Think of it this way: traditional programming is "here are the rules, apply them to data." Machine learning is "here's the data, figure out the rules."

```
Traditional:  Rules + Data -> Answers
ML:           Data + Answers -> Rules
```

## The Three Types of ML

### 1. Supervised Learning: "Learning with Answers"
You give the computer examples WITH the correct answers. It learns the pattern.
- "Here are 10,000 emails labeled spam or not-spam. Learn to tell the difference."
- "Here are 50,000 house prices with their features. Learn to predict prices."

### 2. Unsupervised Learning: "Finding Patterns"
You give the computer data WITHOUT answers. It finds structure on its own.
- "Here are 100,000 customers. Group them into clusters."
- "Find the weirdos in this data." (Anomaly detection)

### 3. Reinforcement Learning: "Trial and Error"
The computer tries stuff and gets rewards or penalties. Like training a dog with treats.
- Game-playing AI (AlphaGo, chess engines)
- Robot navigation
- Self-driving cars

We'll focus on **supervised learning** because it's the most common, the most practical, and the easiest to start with.

## Installing scikit-learn

```bash
pip install scikit-learn
```

scikit-learn (often imported as `sklearn`) is the most popular ML library in Python. It has a clean, consistent API: every model works the same way. Learn one, you've learned them all.

## The Scikit-Learn Workflow

Every single machine learning project follows this same flow:

```
1. Load your data
2. Split into training and testing sets
3. Choose a model
4. Train the model (fit)
5. Make predictions (predict)
6. Evaluate how good it is
```

That's it. Six steps. Let's do them.

## Your First Model: House Price Prediction

Let's predict house prices based on features like size, bedrooms, and age. This is a **regression** problem - predicting a number.

### Step 1: Load the Data

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Create a sample dataset
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "size_sqft": np.random.randint(800, 4000, n),
    "bedrooms": np.random.randint(1, 6, n),
    "age_years": np.random.randint(0, 50, n),
    "distance_downtown": np.random.uniform(0.5, 20, n).round(1)
})

# Price formula with some noise (this is what the model will try to learn)
data["price"] = (
    data["size_sqft"] * 150 +
    data["bedrooms"] * 20000 -
    data["age_years"] * 1500 -
    data["distance_downtown"] * 5000 +
    np.random.normal(0, 15000, n)  # Random noise
).round(-3)  # Round to nearest thousand

print(data.head())
#    size_sqft  bedrooms  age_years  distance_downtown    price
# 0       2937         2        42                3.2  362000.0
# 1       2235         4        18               16.5  288000.0
# ...

print(data.shape)  # (200, 5)
```

### Step 2: Split Into Features and Target

```python
# Features (X) = what the model sees
# Target (y) = what the model predicts
X = data[["size_sqft", "bedrooms", "age_years", "distance_downtown"]]
y = data["price"]

print(f"Features shape: {X.shape}")  # (200, 4)
print(f"Target shape: {y.shape}")    # (200,)
```

### Step 3: Train/Test Split

This is crucial. You split your data into two parts:
- **Training set** (80%): The model studies this. It's like homework.
- **Test set** (20%): You check the model on data it's never seen. It's the exam.

If you test on the same data you trained on, it's like giving someone the answer key before the test. Of course they'll do well. But can they actually think?

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape[0]} houses")  # 160 houses
print(f"Test set: {X_test.shape[0]} houses")        # 40 houses
```

### Step 4: Train the Model

```python
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained!")
```

That's it. Two lines. `LinearRegression()` creates the model. `.fit()` trains it. The model just learned the relationship between house features and prices by studying 160 examples.

> **Remember When?** Remember functions from Chapter 10? `model.fit()` and `model.predict()` are just method calls. You've been using `.append()` on lists, `.get()` on dictionaries, `.format()` on strings. This is the same thing. You've been ready for this.

### Step 5: Make Predictions

```python
predictions = model.predict(X_test)

# Compare predictions to actual prices
comparison = pd.DataFrame({
    "Actual": y_test.values[:5],
    "Predicted": predictions[:5].round(),
    "Difference": (y_test.values[:5] - predictions[:5]).round()
})
print(comparison)
#      Actual  Predicted  Difference
# 0  362000.0   358421.0      3579.0
# 1  154000.0   162893.0     -8893.0
# 2  483000.0   471205.0     11795.0
# 3  295000.0   301442.0     -6442.0
# 4  198000.0   205118.0     -7118.0
```

The predictions are close. Not perfect - there's noise in the data - but the model learned the general pattern.

### Step 6: Evaluate

```python
# Mean Absolute Error: on average, how far off are we?
mae = mean_absolute_error(y_test, predictions)
print(f"Average error: ${mae:,.0f}")  # Average error: $11,847

# R-squared: how much of the price variation does our model explain?
r2 = r2_score(y_test, predictions)
print(f"R-squared: {r2:.3f}")  # R-squared: 0.972

# What the model learned (coefficients)
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: ${coef:,.0f} per unit")
# size_sqft: $150 per unit
# bedrooms: $20,142 per unit
# age_years: -$1,489 per unit
# distance_downtown: -$5,021 per unit
```

An R-squared of 0.972 means the model explains 97.2% of the variation in prices. The coefficients show what the model learned: bigger houses cost more ($150 per sq ft), more bedrooms add value ($20K each), older houses cost less, and farther from downtown costs less. The model figured this out by itself just by looking at examples.

### The Whole Thing in One Block

Here's the entire ML pipeline - load to evaluate:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load data
X = data[["size_sqft", "bedrooms", "age_years", "distance_downtown"]]
y = data["price"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3-4. Create and train
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)

# 6. Evaluate
print(f"MAE: ${mean_absolute_error(y_test, predictions):,.0f}")
print(f"R2: {r2_score(y_test, predictions):.3f}")
```

Five lines of actual ML code (steps 3-6). Everything else is just loading and preparing data. I told you it was five lines.

## Accuracy, Precision, Recall: How Good Is Your Model?

For **regression** (predicting numbers), we use:
- **MAE** (Mean Absolute Error): Average distance between prediction and reality
- **R-squared**: How much of the variation the model explains (1.0 = perfect)

For **classification** (predicting categories), we use:

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

# After making predictions on a classification problem:
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions)
# recall = recall_score(y_test, predictions)
```

- **Accuracy**: What percentage of predictions were correct? "Of 100 emails, I got 95 right."
- **Precision**: When I said "spam," how often was I right? "Of the 20 I called spam, 18 actually were."
- **Recall**: Of all the actual spam, how much did I catch? "There were 25 spam emails, and I caught 18."

Think of it as a doctor checking for a disease:
- **Precision**: "When I say you're sick, I'm usually right." (Avoids false alarms)
- **Recall**: "If you're sick, I'll catch it." (Doesn't miss cases)

You want both to be high. In medicine, recall matters more (don't miss a diagnosis). In spam filtering, precision matters more (don't send real emails to spam).

## Decision Trees: 20 Questions for Data

Linear regression predicts numbers. But what if you want to predict categories? Like "spam or not spam?" or "will this customer churn?" That's **classification**.

Decision trees work exactly like the game 20 Questions. "Is the email from a known contact? Yes. Does it contain the word 'lottery'? No. Does it have attachments? Yes..." The tree keeps asking questions until it reaches a conclusion.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

# Create sample data: predict if someone will buy a product
np.random.seed(42)
n = 300

data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "income": np.random.randint(20000, 120000, n),
    "visits_per_month": np.random.randint(0, 30, n),
    "time_on_site_min": np.random.uniform(0.5, 45, n).round(1)
})

# Create target: bought or not (1 = yes, 0 = no)
buy_probability = (
    (data["income"] > 50000).astype(int) * 0.3 +
    (data["visits_per_month"] > 10).astype(int) * 0.3 +
    (data["time_on_site_min"] > 15).astype(int) * 0.3 +
    np.random.uniform(0, 0.3, n)
)
data["bought"] = (buy_probability > 0.5).astype(int)

print(f"Buyers: {data['bought'].sum()} / {len(data)}")

# Split
X = data[["age", "income", "visits_per_month", "time_on_site_min"]]
y = data["bought"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)

# Predict
predictions = tree.predict(X_test)

# Evaluate
print(f"\nAccuracy: {accuracy_score(y_test, predictions):.1%}")
print(f"\nDetailed Report:")
print(classification_report(y_test, predictions, target_names=["Didn't Buy", "Bought"]))
```

Output:

```
Accuracy: 86.7%

Detailed Report:
              precision    recall  f1-score   support
 Didn't Buy       0.83      0.80      0.82        25
     Bought       0.89      0.91      0.90        35
   accuracy                           0.87        60
```

86.7% accuracy. The model learned who's likely to buy a product just from age, income, visits, and time on site.

### Seeing What the Tree Learned

```python
# Feature importance - which features matter most?
importances = pd.Series(tree.feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False))
# time_on_site_min     0.38
# visits_per_month     0.27
# income               0.25
# age                  0.10
```

Time on site is the most important predictor. Makes sense - people who spend more time browsing are more likely to buy.

```python
# Visualize the tree (optional but cool)
from sklearn.tree import export_text

tree_rules = export_text(tree, feature_names=list(X.columns))
print(tree_rules)
# |-- time_on_site_min <= 15.35
# |   |-- visits_per_month <= 10.50
# |   |   |-- income <= 49721.50
# |   |   |   |-- class: 0
# |   |   |-- income > 49721.50
# |   |   |   |-- class: 0
# |   |-- visits_per_month > 10.50
# |   |   |-- ...
```

You can literally read the decision logic. "If time on site is less than 15 minutes AND visits are less than 11 AND income is under $50K, predict they won't buy." This interpretability is why decision trees are so popular in business.

## Trying Different Models

The beauty of scikit-learn is that every model has the exact same interface. Swap in a different model and the rest of your code stays identical:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"{name}: {acc:.1%}")

# Decision Tree:        86.7%
# Random Forest:        90.0%
# Logistic Regression:  85.0%
# K-Nearest Neighbors:  83.3%
```

Same three lines for every model: `.fit()`, `.predict()`, evaluate. Random Forest wins here because it's like a committee of decision trees voting together. But the point is: **you can swap models like swapping batteries.** Learn the scikit-learn API once, use any model.

> **Don't Panic:** Machine learning sounds like sci-fi. But the code is literally the same pattern every time: create model, `.fit(X_train, y_train)`, `.predict(X_test)`, check accuracy. The math inside the models is complex. The code to use them is not. You don't need to understand how an engine works to drive a car.

## Your Turn: Spam Classifier

Build a spam classifier. Create `spam_classifier.py`:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create sample email data
np.random.seed(42)
n = 500

data = pd.DataFrame({
    "word_count": np.random.randint(5, 500, n),
    "contains_free": np.random.choice([0, 1], n, p=[0.7, 0.3]),
    "contains_winner": np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "num_exclamation": np.random.randint(0, 20, n),
    "num_links": np.random.randint(0, 10, n),
    "from_contact": np.random.choice([0, 1], n, p=[0.4, 0.6]),
    "has_unsubscribe": np.random.choice([0, 1], n, p=[0.6, 0.4])
})

# Create target: is_spam
spam_score = (
    data["contains_free"] * 2 +
    data["contains_winner"] * 3 +
    data["num_exclamation"] * 0.2 +
    data["num_links"] * 0.3 -
    data["from_contact"] * 2 -
    (data["word_count"] > 50).astype(int) * 0.5 +
    np.random.normal(0, 1, n)
)
data["is_spam"] = (spam_score > 2).astype(int)

# 1. Split features (X) and target (y)

# 2. Do a train/test split (80/20)

# 3. Train a DecisionTreeClassifier

# 4. Print accuracy

# 5. Print the full classification report

# 6. Which features are most important for detecting spam?

# 7. BONUS: Try a RandomForestClassifier. Is it better?
```

Expected results:
- Decision Tree accuracy: around 85-90%
- Random Forest accuracy: around 88-93%
- Top spam indicators: "contains_winner", "contains_free", "from_contact" (negative)

## TL;DR

- Machine learning = computers learning patterns from data instead of following explicit rules
- **Supervised learning**: give it examples with answers; it learns to predict on new data
- The scikit-learn workflow: load data, split (train/test), create model, `.fit()`, `.predict()`, evaluate
- **Train/test split** prevents overfitting - always test on data the model hasn't seen
- **Linear Regression** predicts numbers; **Decision Trees** and others predict categories
- **Accuracy** = percentage correct; **Precision** = "when I said yes, was I right?"; **Recall** = "of all the yeses, did I catch them?"
- **Feature importance** tells you which inputs matter most
- scikit-learn's API is consistent: every model uses `.fit()` and `.predict()` - learn one, know them all
- The ML code itself is 5 lines. The hard part is preparing good data and choosing what to predict
- You just built machine learning models. You. This chapter. Right now. Let that sink in.
