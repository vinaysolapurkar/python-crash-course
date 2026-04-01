"""
=============================================================
  PROJECT 1: MULTI-CATEGORY QUIZ GAME - SOLUTION
=============================================================
  A fun multi-category quiz game with scoring and results.
  No external dependencies needed - just pure Python!

  Run:  python solution.py
=============================================================
"""

import random

# ── Question Banks ──────────────────────────────────────────
# Each question is a dict with the question text, four options,
# and the correct answer letter.

python_questions = [
    {
        "question": "What does 'len()' do in Python?",
        "options": [
            "A) Calculates the length of an object",
            "B) Returns the last element",
            "C) Creates a new list",
            "D) Converts to lowercase",
        ],
        "answer": "A",
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": [
            "A) func",
            "B) define",
            "C) def",
            "D) function",
        ],
        "answer": "C",
    },
    {
        "question": "What data type is the result of: 3 / 2?",
        "options": [
            "A) int",
            "B) float",
            "C) str",
            "D) bool",
        ],
        "answer": "B",
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": [
            "A) tuple",
            "B) str",
            "C) int",
            "D) list",
        ],
        "answer": "D",
    },
    {
        "question": "What does 'PEP' stand for in Python?",
        "options": [
            "A) Python Enhancement Proposal",
            "B) Python Execution Plan",
            "C) Programming Extension Package",
            "D) Pretty Easy Python",
        ],
        "answer": "A",
    },
]

science_questions = [
    {
        "question": "What is the chemical symbol for water?",
        "options": [
            "A) O2",
            "B) CO2",
            "C) H2O",
            "D) NaCl",
        ],
        "answer": "C",
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": [
            "A) Venus",
            "B) Mars",
            "C) Jupiter",
            "D) Saturn",
        ],
        "answer": "B",
    },
    {
        "question": "What is the speed of light (approx)?",
        "options": [
            "A) 300,000 km/s",
            "B) 150,000 km/s",
            "C) 1,000,000 km/s",
            "D) 30,000 km/s",
        ],
        "answer": "A",
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": [
            "A) Oxygen",
            "B) Nitrogen",
            "C) Carbon Dioxide",
            "D) Hydrogen",
        ],
        "answer": "C",
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": [
            "A) 186",
            "B) 206",
            "C) 226",
            "D) 256",
        ],
        "answer": "B",
    },
]

pop_culture_questions = [
    {
        "question": "Who directed the movie 'Inception'?",
        "options": [
            "A) Steven Spielberg",
            "B) James Cameron",
            "C) Christopher Nolan",
            "D) Martin Scorsese",
        ],
        "answer": "C",
    },
    {
        "question": "Which band performed 'Bohemian Rhapsody'?",
        "options": [
            "A) The Beatles",
            "B) Led Zeppelin",
            "C) Pink Floyd",
            "D) Queen",
        ],
        "answer": "D",
    },
    {
        "question": "What is the name of Harry Potter's pet owl?",
        "options": [
            "A) Errol",
            "B) Hedwig",
            "C) Scabbers",
            "D) Fawkes",
        ],
        "answer": "B",
    },
    {
        "question": "In 'The Office', what is Michael Scott's catchphrase?",
        "options": [
            "A) 'That's what she said'",
            "B) 'Cool cool cool'",
            "C) 'How you doin?'",
            "D) 'Bazinga'",
        ],
        "answer": "A",
    },
    {
        "question": "Which video game features a character named Mario?",
        "options": [
            "A) Sonic the Hedgehog",
            "B) The Legend of Zelda",
            "C) Super Mario Bros.",
            "D) Pac-Man",
        ],
        "answer": "C",
    },
]

# ── Map category names to their question lists ─────────────
categories = {
    "Python": python_questions,
    "Science": science_questions,
    "Pop Culture": pop_culture_questions,
}


# ── Helper Functions ────────────────────────────────────────

def ask_question(question_dict, question_number, total):
    """
    Display a single question and check the player's answer.
    Returns True if correct, False otherwise.
    """
    print(f"\n--- Question {question_number} of {total} ---")
    print(question_dict["question"])
    print()

    # Print each option
    for option in question_dict["options"]:
        print(f"  {option}")

    print()

    # Get the player's answer (keep asking until valid)
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            break
        print("Please enter A, B, C, or D.")

    # Check if correct
    if answer == question_dict["answer"]:
        print("Correct! Nice job!")
        return True
    else:
        correct = question_dict["answer"]
        # Find the full text of the correct option
        correct_text = [opt for opt in question_dict["options"]
                        if opt.startswith(correct)][0]
        print(f"Wrong! The correct answer was: {correct_text}")
        return False


def run_quiz(questions, category_name):
    """
    Run through all questions in a category.
    Returns (score, total).
    """
    print(f"\n{'=' * 40}")
    print(f"  Category: {category_name}")
    print(f"  {len(questions)} questions")
    print(f"{'=' * 40}")

    # Shuffle so the order is different each time
    shuffled = questions.copy()
    random.shuffle(shuffled)

    score = 0
    total = len(shuffled)

    for i, question in enumerate(shuffled, start=1):
        if ask_question(question, i, total):
            score += 1

    return score, total


def show_results(score, total):
    """Display final results with percentage and a fun message."""
    percentage = (score / total) * 100 if total > 0 else 0

    print()
    print("=" * 40)
    print("          FINAL RESULTS")
    print("=" * 40)
    print(f"  Score: {score} / {total}")
    print(f"  Percentage: {percentage:.1f}%")
    print()

    # Fun messages based on how they did
    if percentage == 100:
        print("  PERFECT SCORE! You're a genius!")
    elif percentage >= 80:
        print("  Great work! You really know your stuff!")
    elif percentage >= 60:
        print("  Not bad! Room for improvement though.")
    elif percentage >= 40:
        print("  Keep studying, you'll get there!")
    else:
        print("  Ouch! Time to hit the books!")

    print("=" * 40)


def show_welcome():
    """Print the welcome banner."""
    print()
    print("=" * 40)
    print("    WELCOME TO THE QUIZ GAME!")
    print("=" * 40)
    print()


def show_menu():
    """Show category options and return the player's choice."""
    print("Choose a category:")
    print("  1. Python")
    print("  2. Science")
    print("  3. Pop Culture")
    print("  4. All Categories (mix it up!)")
    print()

    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return int(choice)
        print("Please enter 1, 2, 3, or 4.")


# ── Main Game Loop ──────────────────────────────────────────

def main():
    """Main game loop: menu -> quiz -> results -> play again?"""
    show_welcome()

    while True:
        choice = show_menu()

        # Build the question list based on choice
        if choice == 1:
            questions = python_questions
            name = "Python"
        elif choice == 2:
            questions = science_questions
            name = "Science"
        elif choice == 3:
            questions = pop_culture_questions
            name = "Pop Culture"
        else:
            # Combine all categories for the ultimate challenge
            questions = python_questions + science_questions + pop_culture_questions
            name = "All Categories"

        # Run the quiz and show results
        score, total = run_quiz(questions, name)
        show_results(score, total)

        # Play again?
        print()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! See you next time!")
            break
        print()


if __name__ == "__main__":
    main()
