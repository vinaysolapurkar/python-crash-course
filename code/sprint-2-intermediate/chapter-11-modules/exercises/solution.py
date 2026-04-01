"""
Chapter 11 Exercise SOLUTION: Random Quote Generator
=====================================================
A complete quote generator that loads from JSON, displays
random quotes with timestamps, and tracks your session.
Fortune cookie meets terminal!
"""

import json
import random
from datetime import datetime
import os


def load_quotes(filepath):
    """
    Load quotes from a JSON file.

    Parameters:
        filepath (str): Path to the quotes.json file

    Returns:
        list: List of quote dictionaries, or empty list on error
    """
    # Check if the file exists before trying to open it
    if not os.path.exists(filepath):
        print(f"  Error: Could not find '{filepath}'")
        print("  Make sure quotes.json is in the same folder as this script!")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        quotes = json.load(f)

    return quotes


def display_quote(quote):
    """
    Display a quote with a pretty timestamp and formatting.

    Parameters:
        quote (dict): A dictionary with 'quote' and 'author' keys
    """
    # Get current time formatted nicely
    timestamp = datetime.now().strftime("%I:%M:%S %p")

    # Display with some flair
    print(f"\n  [{timestamp}]")
    print(f'  "{quote["quote"]}"')
    print(f"    -- {quote['author']}")


def display_stats(total_shown, session_start):
    """Show session statistics -- because data is fun!"""
    duration = datetime.now() - session_start
    minutes = duration.total_seconds() / 60

    print(f"\n  --- Session Stats ---")
    print(f"  Quotes shown: {total_shown}")
    print(f"  Session time: {minutes:.1f} minutes")
    print(f"  Started at: {session_start.strftime('%I:%M %p')}")
    print(f"  Ended at: {datetime.now().strftime('%I:%M %p')}")


def main():
    """Run the random quote generator."""
    print("=" * 50)
    print("    RANDOM QUOTE GENERATOR")
    print("    'Wisdom at the press of Enter'")
    print("=" * 50)

    # Build the path to quotes.json (same folder as this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "quotes.json")

    # Load the quotes
    quotes = load_quotes(filepath)
    if not quotes:
        print("\nNo quotes loaded. Exiting. :(")
        return

    print(f"\nLoaded {len(quotes)} quotes. Let's get inspired!")
    print("Press Enter for a quote, or type 'quit' to exit.\n")

    # Track session stats
    session_start = datetime.now()
    quotes_shown = 0
    shown_indices = set()  # Track which quotes we've shown to avoid repeats

    while True:
        user_input = input(">> ").strip().lower()

        if user_input == "quit":
            break

        # Pick a random quote
        # Try to avoid repeats until we've shown them all
        if len(shown_indices) >= len(quotes):
            print("  (You've seen all quotes! Shuffling for Round 2...)")
            shown_indices.clear()

        # Pick one we haven't shown yet
        idx = random.randint(0, len(quotes) - 1)
        while idx in shown_indices:
            idx = random.randint(0, len(quotes) - 1)

        shown_indices.add(idx)
        quotes_shown += 1

        display_quote(quotes[idx])
        print()  # Breathing room

    # Session wrap-up
    if quotes_shown > 0:
        display_stats(quotes_shown, session_start)

    print("\n  Stay curious, keep coding, and remember:")
    print('  "Talk is cheap. Show me the code." -- Linus Torvalds')
    print("  Goodbye!\n")


if __name__ == "__main__":
    main()
