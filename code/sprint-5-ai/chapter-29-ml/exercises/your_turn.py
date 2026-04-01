"""
Chapter 29: Machine Learning — YOUR TURN!
===========================================

Time to build your first text classifier! You're going to build
a SPAM DETECTOR using real ML techniques:

  1. TF-IDF: Convert text into numbers (because ML only understands numbers)
  2. Naive Bayes: A simple but powerful algorithm for text classification
  3. Pipeline: Chain TF-IDF + Naive Bayes into one neat workflow

TF-IDF stands for "Term Frequency - Inverse Document Frequency"
In plain English: "How important is this word to this specific document?"
  - "the" appears everywhere → low TF-IDF (not important)
  - "FREE" appears mostly in spam → high TF-IDF (very important!)

Naive Bayes is like a really smart probability calculator:
  "Given these words, what's the probability this is spam?"

TASKS:
1. Create the email dataset (provided below)
2. Split into training and test sets (80/20)
3. Create a TF-IDF + Naive Bayes pipeline
4. Train the model
5. Evaluate with accuracy and confusion matrix
6. Test with your own custom messages!
"""

# Uncomment and complete each section!

# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- EMAIL DATASET ---
# Real spam detection uses millions of emails. We'll use a small sample
# to demonstrate the concept. In production, you'd use a MUCH larger dataset.

emails = [
    # SPAM emails (label = 1)
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

    # HAM (not spam) emails (label = 0)
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

labels = [1]*15 + [0]*15  # 1=spam, 0=ham (not spam)

# TODO 1: Split the data into training and test sets
# Hint: train_test_split(emails, labels, test_size=0.2, random_state=42)


# TODO 2: Create a Pipeline with TF-IDF and Naive Bayes
# A Pipeline chains multiple steps together:
#   Pipeline([
#       ("tfidf", TfidfVectorizer()),
#       ("classifier", MultinomialNB())
#   ])


# TODO 3: Train the model
# Hint: pipeline.fit(X_train, y_train)


# TODO 4: Make predictions on the test set
# Hint: pipeline.predict(X_test)


# TODO 5: Evaluate the model
# Print: accuracy, confusion matrix, classification report


# TODO 6: Test with your own messages!
# Create a list of new messages and predict if they're spam or not
test_messages = [
    "Hey, want to grab lunch today?",
    "FREE BITCOIN! Double your crypto investment NOW!!!",
    "The meeting has been rescheduled to 4pm.",
    "URGENT: Verify your bank account or lose access!!!",
    "Can you send me the project files?",
]

# Predict each message and print the result
# Hint: pipeline.predict(test_messages)
