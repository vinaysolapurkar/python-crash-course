"""
=============================================================
  PROJECT 4: HANGMAN GAME - SOLUTION
=============================================================
  Classic Hangman with ASCII art, difficulty levels, and
  score tracking across games.

  No external dependencies needed!

  Run:  python solution.py
=============================================================
"""

import random

# ── ASCII Art Stages ────────────────────────────────────────
# 7 stages (0 = no wrong guesses, 6 = game over)

HANGMAN_STAGES = [
    # 0: Empty gallows
    """
     ┌───┐
     │   │
     │
     │
     │
     │
    ═══════
    """,
    # 1: Head
    """
     ┌───┐
     │   │
     │   O
     │
     │
     │
    ═══════
    """,
    # 2: Body
    """
     ┌───┐
     │   │
     │   O
     │   │
     │
     │
    ═══════
    """,
    # 3: Left arm
    """
     ┌───┐
     │   │
     │   O
     │  /│
     │
     │
    ═══════
    """,
    # 4: Both arms
    r"""
     ┌───┐
     │   │
     │   O
     │  /│\
     │
     │
    ═══════
    """,
    # 5: Left leg
    """
     ┌───┐
     │   │
     │   O
     │  /│\\
     │  /
     │
    ═══════
    """,
    # 6: Both legs (game over!)
    """
     ┌───┐
     │   │
     │   O
     │  /│\\
     │  / \\
     │
    ═══════
    """,
]

MAX_WRONG = len(HANGMAN_STAGES) - 1  # 6 wrong guesses allowed

# ── Word Lists ──────────────────────────────────────────────

WORDS = {
    "easy": [
        "cat", "dog", "sun", "hat", "cup",
        "run", "red", "big", "map", "box",
        "fly", "pen", "bus", "jam", "kit",
    ],
    "medium": [
        "python", "coding", "planet", "garden", "bridge",
        "rocket", "banana", "castle", "dragon", "forest",
        "puzzle", "silver", "turtle", "wonder", "breeze",
    ],
    "hard": [
        "algorithm", "beautiful", "challenge", "debugging",
        "exception", "framework", "gymnasium", "hypnotize",
        "interface", "juxtapose", "knowledge", "labyrinth",
        "microchip", "nightmare", "otherwise",
    ],
}


# ── Game Functions ──────────────────────────────────────────

def choose_difficulty():
    """Ask the player to pick a difficulty. Returns the word list."""
    while True:
        choice = input("  Difficulty: (e)asy, (m)edium, (h)ard? ").strip().lower()
        if choice in ("e", "easy"):
            print("  Easy mode - short words!")
            return WORDS["easy"], "Easy"
        elif choice in ("m", "medium"):
            print("  Medium mode - let's go!")
            return WORDS["medium"], "Medium"
        elif choice in ("h", "hard"):
            print("  Hard mode - good luck!")
            return WORDS["hard"], "Hard"
        else:
            print("  Please enter e, m, or h.")


def display_game_state(word, guessed_letters, wrong_guesses):
    """Display the full game state: hangman art, word, and info."""
    # Show the hangman
    print(HANGMAN_STAGES[wrong_guesses])

    # Show the word with blanks
    display_word = " ".join(
        c.upper() if c in guessed_letters else "_"
        for c in word
    )
    print(f"  Word: {display_word}")

    # Show guessed letters
    if guessed_letters:
        sorted_guessed = sorted(guessed_letters)
        print(f"  Guessed: {', '.join(g.upper() for g in sorted_guessed)}")

    # Show remaining wrong guesses
    remaining = MAX_WRONG - wrong_guesses
    print(f"  Remaining guesses: {remaining}")
    print()


def check_win(word, guessed_letters):
    """Return True if every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


def get_guess(guessed_letters):
    """Get a valid letter guess from the player."""
    while True:
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("  Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("  That's not a letter! Try again.")
            continue

        if guess in guessed_letters:
            print(f"  You already guessed '{guess.upper()}'! Try another.")
            continue

        return guess


def play_round(word):
    """
    Play one round of Hangman.
    Returns True if the player won, False if they lost.
    """
    guessed_letters = set()
    wrong_guesses = 0

    print(f"\n  The word has {len(word)} letters. Good luck!\n")

    while wrong_guesses < MAX_WRONG:
        display_game_state(word, guessed_letters, wrong_guesses)

        # Check for win before asking for next guess
        if check_win(word, guessed_letters):
            print(f"  YOU WIN! The word was {word.upper()}!")
            return True

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"  Correct! '{guess.upper()}' is in the word!")

            # Check win right after a correct guess
            if check_win(word, guessed_letters):
                display_game_state(word, guessed_letters, wrong_guesses)
                print(f"  YOU WIN! The word was {word.upper()}!")
                return True
        else:
            wrong_guesses += 1
            remaining = MAX_WRONG - wrong_guesses
            print(f"  Wrong! '{guess.upper()}' is not in the word. "
                  f"({remaining} guesses left)")

    # Out of guesses - show final state
    display_game_state(word, guessed_letters, wrong_guesses)
    print(f"  GAME OVER! The word was {word.upper()}.")
    return False


# ── Main Game Loop ──────────────────────────────────────────

def main():
    """Main game with score tracking and replay."""
    print()
    print("=" * 34)
    print("        H A N G M A N")
    print("=" * 34)
    print("  Guess the word before the")
    print("  hangman is complete!")
    print("=" * 34)

    wins = 0
    losses = 0

    while True:
        print()
        word_list, difficulty = choose_difficulty()
        word = random.choice(word_list)

        if play_round(word):
            wins += 1
        else:
            losses += 1

        # Show running score
        print()
        print(f"  ── Score: Wins {wins} | Losses {losses} ──")

        # Play again?
        print()
        again = input("  Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print()
            print("=" * 34)
            print("  FINAL SCORE")
            print(f"  Wins: {wins} | Losses: {losses}")
            if wins + losses > 0:
                rate = wins / (wins + losses) * 100
                print(f"  Win rate: {rate:.0f}%")
            print("  Thanks for playing!")
            print("=" * 34)
            break


if __name__ == "__main__":
    main()
