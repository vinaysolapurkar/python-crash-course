# Project 1: The Quiz Game

> **Difficulty:** 1/5 | **Time:** ~1 hour | **Skills:** variables, loops, conditions, lists, input
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-01-quiz-game/

## What You'll Build

A terminal-based quiz game with three categories (Science, History, and Geography), five questions each, score tracking, and a results summary at the end. When running, the player picks a category, answers multiple-choice questions, gets instant feedback on each answer, and sees a final scorecard showing how they did.

It looks like this when running:

```
=== THE QUIZ GAME ===

Choose a category:
1. Science
2. History
3. Geography
4. All Categories

Your choice: 1

--- Science ---

Q1: What planet is known as the Red Planet?
  a) Venus
  b) Mars
  c) Jupiter
  d) Saturn
Your answer: b
Correct!

...

=== RESULTS ===
You scored 4/5 (80%)
Rating: Great job!
```

## Skills You'll Use

- Variables and data types (learned in Chapter 2)
- Lists and dictionaries (learned in Chapter 4)
- Conditional statements (learned in Chapter 3)
- Loops (learned in Chapter 3)
- User input and string methods (learned in Chapter 2)
- Functions (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Set Up the Question Data

The foundation of any quiz game is its questions. We'll store them as a list of dictionaries -- each dictionary holds the question text, the answer choices, and the correct answer.

```python
# quiz_game.py

# Each question is a dictionary with question text, options, and correct answer
science_questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["a) Oxygen", "b) Nitrogen", "c) Carbon Dioxide", "d) Hydrogen"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) O2", "b) CO2", "c) NaCl", "d) H2O"],
        "answer": "d"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["a) 106", "b) 206", "c) 306", "d) 156"],
        "answer": "b"
    },
    {
        "question": "What force keeps us on the ground?",
        "options": ["a) Magnetism", "b) Friction", "c) Gravity", "d) Inertia"],
        "answer": "c"
    }
]

history_questions = [
    {
        "question": "In what year did World War II end?",
        "options": ["a) 1943", "b) 1944", "c) 1945", "d) 1946"],
        "answer": "c"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["a) John Adams", "b) Thomas Jefferson",
                    "c) Benjamin Franklin", "d) George Washington"],
        "answer": "d"
    },
    {
        "question": "The ancient city of Rome is in which modern country?",
        "options": ["a) Greece", "b) Italy", "c) Spain", "d) Turkey"],
        "answer": "b"
    },
    {
        "question": "Who wrote the Declaration of Independence?",
        "options": ["a) George Washington", "b) Benjamin Franklin",
                    "c) Thomas Jefferson", "d) John Adams"],
        "answer": "c"
    },
    {
        "question": "The Great Wall was built primarily to protect which country?",
        "options": ["a) Japan", "b) India", "c) China", "d) Mongolia"],
        "answer": "c"
    }
]

geography_questions = [
    {
        "question": "What is the largest continent by area?",
        "options": ["a) Africa", "b) North America", "c) Europe", "d) Asia"],
        "answer": "d"
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["a) Amazon", "b) Nile", "c) Mississippi", "d) Yangtze"],
        "answer": "b"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["a) Monaco", "b) Nauru", "c) Vatican City", "d) San Marino"],
        "answer": "c"
    },
    {
        "question": "Mount Everest is located in which mountain range?",
        "options": ["a) Andes", "b) Alps", "c) Rockies", "d) Himalayas"],
        "answer": "d"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["a) Atlantic", "b) Indian", "c) Pacific", "d) Arctic"],
        "answer": "c"
    }
]
```

### Step 2: Build the Category Selection

Now let's write a function that lets the player choose what they want to be quizzed on. We use a dictionary to map choices to question lists.

```python
def choose_category():
    """Let the player pick a quiz category."""
    categories = {
        "1": ("Science", science_questions),
        "2": ("History", history_questions),
        "3": ("Geography", geography_questions),
        "4": ("All Categories",
              science_questions + history_questions + geography_questions)
    }

    print("\nChoose a category:")
    print("1. Science")
    print("2. History")
    print("3. Geography")
    print("4. All Categories")

    while True:
        choice = input("\nYour choice: ").strip()
        if choice in categories:
            name, questions = categories[choice]
            print(f"\n--- {name} ---")
            return name, questions
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
```

### Step 3: Create the Quiz Runner

This function takes a list of questions, presents them one at a time, validates the player's input, and tracks the score.

```python
def run_quiz(questions):
    """Run through questions and return the score."""
    score = 0
    total = len(questions)
    results = []  # Track each answer for the summary

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        # Get valid input
        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in ["a", "b", "c", "d"]:
                break
            print("Please enter a, b, c, or d.")

        # Check the answer
        if answer == q["answer"]:
            print("Correct!")
            score += 1
            results.append((q["question"], True))
        else:
            correct_letter = q["answer"]
            # Find the full text of the correct answer
            correct_text = [opt for opt in q["options"]
                           if opt.startswith(correct_letter)][0]
            print(f"Wrong! The correct answer was: {correct_text}")
            results.append((q["question"], False))

    return score, total, results
```

### Step 4: Build the Results Summary

After the quiz, show a detailed breakdown. A nice touch is giving the player a rating based on their percentage.

```python
def show_results(score, total, results, category_name):
    """Display the final results summary."""
    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print(f"  RESULTS - {category_name}")
    print("=" * 40)
    print(f"\n  You scored {score}/{total} ({percentage:.0f}%)")

    # Give a rating
    if percentage == 100:
        rating = "Perfect score! You're a genius!"
    elif percentage >= 80:
        rating = "Great job! Really impressive!"
    elif percentage >= 60:
        rating = "Good effort! Keep studying!"
    elif percentage >= 40:
        rating = "Not bad, but there's room to grow."
    else:
        rating = "Keep learning -- you'll get there!"

    print(f"  Rating: {rating}")

    # Show question-by-question breakdown
    print(f"\n  Breakdown:")
    for question, correct in results:
        status = "+" if correct else "X"
        # Truncate long questions for clean display
        short_q = question if len(question) <= 45 else question[:42] + "..."
        print(f"    [{status}] {short_q}")

    print("\n" + "=" * 40)
```

### Step 5: Add the Play Again Loop

Wrap everything in a main function with a loop so the player can keep playing.

```python
def main():
    """Main game loop."""
    print("=" * 40)
    print("       THE QUIZ GAME")
    print("=" * 40)
    print("Test your knowledge across 3 categories!")

    while True:
        category_name, questions = choose_category()
        score, total, results = run_quiz(questions)
        show_results(score, total, results, category_name)

        # Ask to play again
        print()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! See you next time.")
            break


if __name__ == "__main__":
    main()
```

### Step 6: Run and Test

Save your file as `quiz_game.py` and run it:

```
python quiz_game.py
```

Test each category, try invalid inputs (like entering "z" when it expects a-d), and make sure the score tallies correctly. Try the "All Categories" option to confirm questions from all three sets appear.

## Challenges (Level Up!)

1. **Randomize questions:** Import the `random` module and use `random.shuffle(questions)` to present questions in a different order each time. This makes the game replayable.

2. **Add a timer:** Use `time.time()` to track how long the player takes per question and display the total time in the results. Bonus: give a speed bonus for fast answers.

3. **High score persistence:** Save the top 5 scores to a text file so they persist between sessions. Display a "New High Score!" message when the player beats an existing record.

## Portfolio Tips

This is your "Hello World on steroids" -- it shows you can structure data, handle user input, and build a complete program with a clear beginning, middle, and end. When presenting this project:

- **GitHub:** Include a clear README with a screenshot of the game running in the terminal. Mention the categories and how to add new questions.
- **Resume:** "Built a terminal-based quiz game with multiple categories, input validation, and score tracking using Python."
- **Interview talking point:** Discuss how you structured the question data (list of dictionaries) and why that choice made the code easy to extend with new categories.
