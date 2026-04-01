"""
=============================================================
  PROJECT 4: HANGMAN GAME
=============================================================

Build the classic Hangman word-guessing game with ASCII art!
The player tries to guess a word letter by letter before
the hangman is fully drawn.

WHAT YOU'LL PRACTICE:
  - String manipulation
  - Sets (for tracking guessed letters)
  - Game loop logic
  - ASCII art
  - Functions
  - Random selection
  - While loops with conditions

REQUIREMENTS:
  1. Word list organized by difficulty (easy/medium/hard)
  2. ASCII art hangman that builds up with wrong guesses
     (7 stages: empty, head, body, left arm, right arm,
      left leg, right leg)
  3. Track guessed and remaining letters
  4. Win/lose detection
  5. Play again loop
  6. Score tracking across multiple games

EXAMPLE OUTPUT:
  =============================
    HANGMAN
  =============================
  Difficulty: (e)asy, (m)edium, (h)ard? m

     ┌───┐
     │   │
     │   O
     │  /│
     │
     │
    ═══════

  Word: _ Y _ _ O N
  Guessed: A, E, I, X
  Remaining: 3 guesses

  Enter a letter: T
  Correct!

  ...

  You WIN! The word was PYTHON!
  Score: Wins 3 | Losses 1

HINTS:
  - Use a set for guessed letters (fast lookup)
  - The display word can be built with a list comprehension:
    " ".join(c if c in guessed else "_" for c in word)
  - Use a list of multiline strings for hangman stages
  - random.choice() picks a random word

Good luck!
=============================================================
"""

import random


# Step 1: Define the ASCII art stages (7 stages, from
# empty gallows to fully drawn hangman)
HANGMAN_STAGES = [
    # Stage 0: empty gallows
    # Stage 1: head
    # Stage 2: body
    # Stage 3: left arm
    # Stage 4: both arms
    # Stage 5: left leg
    # Stage 6: both legs (dead!)
    # TODO: Create each stage as a multiline string
]


# Step 2: Create word lists by difficulty
WORDS = {
    "easy": [],    # 3-4 letter words
    "medium": [],  # 5-6 letter words
    "hard": [],    # 7+ letter words
}


def choose_difficulty():
    """Let the player pick easy, medium, or hard."""
    # TODO: Ask for difficulty, return the chosen word list
    pass


def display_game_state(word, guessed_letters, wrong_guesses):
    """Show the hangman, word progress, and guessed letters."""
    # TODO: Print the current hangman stage
    # TODO: Show the word with blanks for unguessed letters
    # TODO: Show all guessed letters
    # TODO: Show remaining guesses
    pass


def check_win(word, guessed_letters):
    """Return True if all letters in the word have been guessed."""
    # TODO: Check if every letter in word is in guessed_letters
    pass


def play_round(word):
    """Play one round of hangman. Return True if won."""
    # TODO: Initialize guessed letters set and wrong guess count
    # TODO: Game loop: show state, get guess, update
    # TODO: Return True/False for win/loss
    pass


def main():
    """Main game loop with score tracking."""
    # TODO: Welcome message
    # TODO: Score tracking (wins, losses)
    # TODO: Difficulty selection
    # TODO: Play round
    # TODO: Play again loop
    pass


if __name__ == "__main__":
    main()
