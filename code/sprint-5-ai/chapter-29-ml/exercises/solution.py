"""
Chapter 29: Machine Learning — SOLUTION
=========================================

You just built a spam classifier! This is basically what Gmail
does (with way more data and fancier models, but the concept
is identical). You're officially doing AI stuff now!
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- EMAIL DATASET ---
emails = [
    # SPAM (label = 1)
    "FREE MONEY! Click here to claim your prize now!!!",
    "Congratulations! You've won a $1000 gift card. Claim now!",
    "URGENT: Your account will be suspended. Verify immediately!",
    "Buy cheap medications online! Best prices guaranteed!!!",
    "You are selected for a special offer! Act now before it expires!",
    "Make money fast from home! No experience needed! $$$",
    "Limited time offer! Buy one get one free! Click now!",
    "You've inherited $5,000,000 from a distant relative! Reply now!",
    "Hot singles in your area want to meet you tonight!!!",
    "Lose 30 pounds in 30 days! Revolutionary new diet pill!",
    "WINNER! Claim your free iPhone now! Limited supply!",
    "Earn $500/day working from home! No skills required!",
    "Your loan has been pre-approved! Click to claim your money!",
    "DISCOUNT: 90% off luxury watches! Buy now before they're gone!",
    "Secret investment trick the banks don't want you to know!",

    # HAM / not spam (label = 0)
    "Hey, can we meet for coffee tomorrow at 10am?",
    "The project deadline has been moved to next Friday.",
    "Thanks for sending the report. I'll review it tonight.",
    "Don't forget about the team meeting at 3pm today.",
    "I've attached the updated spreadsheet you requested.",
    "Happy birthday! Hope you have a wonderful day!",
    "Can you pick up some milk on your way home?",
    "The code review is done. I left some comments on the PR.",
    "Let's schedule a call to discuss the new requirements.",
    "Your order has been shipped. Expected delivery: Monday.",
    "Great job on the presentation today! Very impressive.",
    "Reminder: dentist appointment on Thursday at 2pm.",
    "I'll be working from home tomorrow. Call if you need me.",
    "The restaurant reservation is confirmed for 7pm Saturday.",
    "Could you review the pull request when you get a chance?",
]

labels = [1]*15 + [0]*15  # 1=spam, 0=ham

print("=" * 60)
print("SPAM CLASSIFIER")
print("=" * 60)
print(f"Dataset: {len(emails)} emails ({sum(labels)} spam, {len(labels) - sum(labels)} ham)")
print()

# TASK 1: Split the data
X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.2, random_state=42
)
print(f"Training set: {len(X_train)} emails")
print(f"Test set:     {len(X_test)} emails")
print()

# TASK 2: Create the pipeline
# TfidfVectorizer converts text → numbers (TF-IDF matrix)
# MultinomialNB is Naive Bayes — great for text classification
spam_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,        # Convert to lowercase
        stop_words="english",  # Remove common words ("the", "is", etc.)
    )),
    ("classifier", MultinomialNB())
])

# TASK 3: Train the model
spam_pipeline.fit(X_train, y_train)
print("Model trained!")

# TASK 4: Make predictions
y_pred = spam_pipeline.predict(X_test)

# TASK 5: Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.1%}")
print(f"({int(accuracy * len(y_test))}/{len(y_test)} correct predictions)")

cm = confusion_matrix(y_test, y_pred)
print(f"\nConfusion Matrix:")
print(f"                Predicted Ham  Predicted Spam")
print(f"  Actually Ham      {cm[0][0]:>4d}           {cm[0][1]:>4d}")
print(f"  Actually Spam     {cm[1][0]:>4d}           {cm[1][1]:>4d}")

print(f"\nClassification Report:")
print(classification_report(y_test, y_pred,
                             target_names=["Ham", "Spam"]))

# TASK 6: Test with custom messages
print("=" * 60)
print("TESTING WITH NEW MESSAGES")
print("=" * 60)

test_messages = [
    "Hey, want to grab lunch today?",
    "FREE BITCOIN! Double your crypto investment NOW!!!",
    "The meeting has been rescheduled to 4pm.",
    "URGENT: Verify your bank account or lose access!!!",
    "Can you send me the project files?",
]

predictions = spam_pipeline.predict(test_messages)

# Also get probability scores (how confident is the model?)
probabilities = spam_pipeline.predict_proba(test_messages)

for msg, pred, probs in zip(test_messages, predictions, probabilities):
    label = "SPAM" if pred == 1 else "HAM"
    confidence = max(probs) * 100
    icon = "[!]" if pred == 1 else "[+]"
    print(f"\n{icon} {label} (confidence: {confidence:.0f}%)")
    print(f"    \"{msg}\"")

# BONUS: Let's see what words the model thinks are most "spammy"
print("\n" + "=" * 60)
print("MOST 'SPAMMY' WORDS (highest spam probability)")
print("=" * 60)

# Get the feature names (words) from TF-IDF
feature_names = spam_pipeline.named_steps["tfidf"].get_feature_names_out()
# Get the log probability of each word given spam class
spam_probs = spam_pipeline.named_steps["classifier"].feature_log_prob_[1]
ham_probs = spam_pipeline.named_steps["classifier"].feature_log_prob_[0]

# Difference in log probs = how much more "spammy" vs "hammy" a word is
spam_indicator = spam_probs - ham_probs
top_spam_indices = np.argsort(spam_indicator)[-10:][::-1]

print("Top 10 spam indicator words:")
for idx in top_spam_indices:
    print(f"  '{feature_names[idx]}' (spam score: {spam_indicator[idx]:.2f})")

print("\nYour spam classifier is ready to protect inboxes!")
