"""
=============================================================
  PROJECT 1: MULTI-CATEGORY QUIZ GAME
=============================================================

Welcome to your first final project! You're going to build a
fun multi-category quiz game that tests players on Python,
Science, and Pop Culture.

WHAT YOU'LL PRACTICE:
  - Variables, data types (lists, dicts)
  - Loops (for, while)
  - Conditionals (if/elif/else)
  - Functions
  - Random module
  - Score tracking
  - String formatting

REQUIREMENTS:
  1. Create 3 quiz categories: Python, Science, Pop Culture
  2. Each category should have at least 5 questions
  3. Store questions as a list of dicts, each with:
     - "question": the question text
     - "options": list of 4 answer choices (A, B, C, D)
     - "answer": the correct answer letter
  4. Let the player choose a category or play all categories
  5. Randomize question order
  6. Track the score and show results at the end
  7. Show the correct answer when the player gets it wrong
  8. Display final score with percentage

BONUS CHALLENGES:
  - Add a timer for each question
  - Add difficulty levels
  - Save high scores to a file
  - Add a "lifeline" system (50/50, skip)

EXAMPLE OUTPUT:
  =============================
    WELCOME TO THE QUIZ GAME!
  =============================
  Choose a category:
  1. Python
  2. Science
  3. Pop Culture
  4. All Categories
  > 1

  --- Question 1 of 5 ---
  What does 'len()' do in Python?
  A) Calculates length of an object
  B) Returns the last element
  C) Creates a new list
  D) Converts to lowercase

  Your answer (A/B/C/D): A
  Correct! Nice job!

  ...

  ========= RESULTS =========
  You scored 4 out of 5 (80.0%)
  Great work!
  ============================

HINTS:
  - Use random.shuffle() to randomize questions
  - Use input().strip().upper() to clean user input
  - A dict is perfect for mapping category names to question lists

Good luck, and have fun!
=============================================================
"""

import random


# Step 1: Define your questions for each category.
# Each question should be a dict like:
# {
#     "question": "What is ...?",
#     "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
#     "answer": "A"
# }

python_questions = [
    # Add 5 questions about Python here
]

science_questions = [
    # Add 5 questions about Science here
]

pop_culture_questions = [
    # Add 5 questions about Pop Culture here
]


# Step 2: Create a dict mapping category names to question lists
categories = {}


# Step 3: Write a function to display a single question and check the answer
def ask_question(question_dict, question_number):
    """Display a question and return True if answered correctly."""
    # TODO: Print the question and options
    # TODO: Get user input
    # TODO: Check if correct and give feedback
    pass


# Step 4: Write a function to run a quiz on a list of questions
def run_quiz(questions, category_name):
    """Run through all questions, track and return the score."""
    # TODO: Shuffle questions
    # TODO: Loop through and ask each one
    # TODO: Track score
    # TODO: Return score and total
    pass


# Step 5: Write a function to display the final results
def show_results(score, total):
    """Display the final score with percentage and a message."""
    # TODO: Calculate percentage
    # TODO: Print formatted results
    # TODO: Give different messages based on score
    pass


# Step 6: Write the main game function
def main():
    """Main game loop - show menu, run quiz, show results."""
    # TODO: Print welcome banner
    # TODO: Show category menu
    # TODO: Get player choice
    # TODO: Run the quiz
    # TODO: Show results
    # TODO: Ask to play again
    pass


if __name__ == "__main__":
    main()
