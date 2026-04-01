# Project 4: Hangman Game

> **Difficulty:** 2/5 | **Time:** ~1.5 hours | **Skills:** strings, game logic, ASCII art, loops
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-04-hangman/

## What You'll Build

A classic Hangman game in the terminal with word categories, difficulty levels, ASCII art that updates with each wrong guess, and score tracking across rounds. It's polished, fun, and surprisingly satisfying to build.

Here's what it looks like:

```
=== HANGMAN ===

Category: Animals | Difficulty: Medium | Lives: 6

   ------
   |    |
   |    O
   |   /|
   |
   |
  ---

Word: _ _ _ _ _ _ _

Guessed: a, e, r, t
Remaining: 3 lives

Guess a letter: s
Correct! The 's' appears 1 time(s).

Word: _ _ _ s _ e r
```

## Skills You'll Use

- String manipulation and methods (learned in Chapter 2)
- Loops and conditionals (learned in Chapter 3)
- Lists and random selection (learned in Chapter 4)
- Functions and modular design (learned in Chapter 5)
- Sets for tracking guesses (learned in Chapter 4)

## Step-by-Step Build Guide

### Step 1: Define the Word Bank and ASCII Art

Start with the word bank organized by category and difficulty, and the hangman stages as ASCII art strings.

```python
# hangman.py

import random

# Word bank organized by category
WORD_BANK = {
    "Animals": {
        "easy": ["cat", "dog", "bird", "fish", "frog"],
        "medium": ["dolphin", "giraffe", "penguin", "hamster", "lobster"],
        "hard": ["chameleon", "rhinoceros", "hippopotamus", "chinchilla"]
    },
    "Countries": {
        "easy": ["india", "china", "japan", "italy", "spain"],
        "medium": ["germany", "australia", "thailand", "portugal", "morocco"],
        "hard": ["mozambique", "kazakhstan", "afghanistan", "liechtenstein"]
    },
    "Technology": {
        "easy": ["code", "data", "wifi", "byte", "chip"],
        "medium": ["python", "server", "docker", "github", "laptop"],
        "hard": ["kubernetes", "javascript", "blockchain", "tensorflow"]
    }
}

# Each stage is one more body part -- 7 stages (0 = no parts, 6 = full body)
HANGMAN_STAGES = [
    """
   ------
   |    |
   |
   |
   |
   |
  ---""",
    """
   ------
   |    |
   |    O
   |
   |
   |
  ---""",
    """
   ------
   |    |
   |    O
   |    |
   |
   |
  ---""",
    """
   ------
   |    |
   |    O
   |   /|
   |
   |
  ---""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |
   |
  ---""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |   /
   |
  ---""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
   |
  ---"""
]
```

### Step 2: Build the Setup Functions

Let the player choose their category and difficulty before each round.

```python
def choose_category():
    """Let the player choose a word category."""
    categories = list(WORD_BANK.keys())
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Choose a category: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        except ValueError:
            pass
        print(f"Please enter a number between 1 and {len(categories)}.")


def choose_difficulty():
    """Let the player choose difficulty level."""
    print("\nDifficulty:")
    print("  1. Easy   (short words, 8 lives)")
    print("  2. Medium (longer words, 6 lives)")
    print("  3. Hard   (longest words, 5 lives)")

    lives_map = {"1": ("easy", 8), "2": ("medium", 6), "3": ("hard", 5)}

    while True:
        choice = input("Choose difficulty: ").strip()
        if choice in lives_map:
            return lives_map[choice]
        print("Please enter 1, 2, or 3.")


def get_random_word(category, difficulty):
    """Pick a random word from the selected category and difficulty."""
    words = WORD_BANK[category][difficulty]
    return random.choice(words).lower()
```

### Step 3: Create the Display Function

This function renders the current game state: the hangman figure, the partially revealed word, and the guessed letters.

```python
def display_state(word, guessed_letters, wrong_guesses, max_lives,
                  category, difficulty):
    """Display the current game state."""
    # Clear some space
    print("\n" * 2)

    lives_remaining = max_lives - wrong_guesses
    stage_index = min(wrong_guesses, len(HANGMAN_STAGES) - 1)

    # Header
    print(f"Category: {category} | Difficulty: {difficulty.title()} "
          f"| Lives: {max_lives}")

    # Hangman figure
    print(HANGMAN_STAGES[stage_index])

    # Word display (show guessed letters, hide others)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"\nWord: {display_word.strip()}")

    # Guessed letters
    if guessed_letters:
        sorted_guesses = sorted(guessed_letters)
        print(f"\nGuessed: {', '.join(sorted_guesses)}")

    print(f"Remaining: {lives_remaining} lives")

    return lives_remaining
```

### Step 4: Build the Core Game Loop

This is the heart of the game. Each iteration gets a guess, validates it, checks if it's correct, and determines win/loss.

```python
def play_round(category, difficulty, max_lives):
    """Play a single round of hangman. Returns True if player wins."""
    word = get_random_word(category, difficulty)
    guessed_letters = set()
    wrong_guesses = 0

    while True:
        lives = display_state(word, guessed_letters, wrong_guesses,
                              max_lives, category, difficulty)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n  YOU WIN! The word was: {word}")
            return True

        # Check lose condition
        if lives <= 0:
            print(f"\n  GAME OVER! The word was: {word}")
            return False

        # Get player's guess
        while True:
            guess = input("\nGuess a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another.")
                continue
            break

        guessed_letters.add(guess)

        # Check if correct
        if guess in word:
            count = word.count(guess)
            print(f"Correct! The '{guess}' appears {count} time(s).")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
```

### Step 5: Add Score Tracking and the Main Loop

Keep a running score across multiple rounds and display a session summary at the end.

```python
def show_scoreboard(wins, losses):
    """Display the current score."""
    total = wins + losses
    if total == 0:
        return

    win_rate = (wins / total) * 100
    print("\n--- Scoreboard ---")
    print(f"  Wins: {wins}  |  Losses: {losses}  |  "
          f"Win Rate: {win_rate:.0f}%")

    # Visual bar
    bar_width = 20
    filled = int((wins / total) * bar_width) if total > 0 else 0
    bar = "#" * filled + "-" * (bar_width - filled)
    print(f"  [{bar}]")


def main():
    """Main game loop with score tracking."""
    print("=" * 30)
    print("      HANGMAN")
    print("=" * 30)
    print("Guess the word before")
    print("the hangman is complete!")

    wins = 0
    losses = 0

    while True:
        category = choose_category()
        difficulty, max_lives = choose_difficulty()

        won = play_round(category, difficulty, max_lives)

        if won:
            wins += 1
        else:
            losses += 1

        show_scoreboard(wins, losses)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\n--- Final Results ---")
            show_scoreboard(wins, losses)
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Hint system:** Give the player one free hint per round that reveals a random unguessed letter. Deduct half a life as the cost. This requires tracking which letters are still hidden.

2. **Two-player mode:** Let one player enter a custom word (hiding the input with `getpass.getpass()`) and the other player guesses. Add a competitive scoreboard.

3. **Word bank from file:** Move the word bank to an external text file (one word per line, organized by headers like `[Animals:easy]`). Write code to parse this file, making it easy for anyone to add new words without touching the Python code.

## Portfolio Tips

Hangman is a game most people know instantly, which makes it a great demo piece. When presenting this project:

- **GitHub:** Create an animated GIF of gameplay for your README. Tools like `asciinema` can record terminal sessions beautifully.
- **Resume:** "Built a terminal Hangman game with multiple categories, difficulty scaling, ASCII art rendering, and session score tracking in Python."
- **Interview talking point:** Talk about how you used sets to efficiently track guessed letters (O(1) lookup vs. searching a list). Discuss the state machine pattern: every round moves through a clear sequence of states (setup, playing, won/lost).
