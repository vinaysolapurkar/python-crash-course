"""
Chapter 11 Exercise: Random Quote Generator
============================================
Build a program that:
  1. Loads quotes from quotes.json
  2. Displays a random quote with the current timestamp
  3. Loops until the user types 'quit'

Modules you'll need:
  - json (to load the quotes file)
  - random (to pick a random quote)
  - datetime (to show the current time)
  - os.path (to find the quotes file)

HINTS:
  - Use os.path.dirname(__file__) to get the folder this script is in
  - Use os.path.join() to build the path to quotes.json
  - Use json.load() (not json.loads!) to read from a file
  - Use random.choice() to pick a random quote
  - Use datetime.now().strftime() to format the timestamp
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
        list: List of quote dictionaries
    """
    # TODO: Open the file and use json.load() to read it
    # HINT:
    #   with open(filepath, "r") as f:
    #       quotes = json.load(f)
    #   return quotes
    pass


def display_quote(quote):
    """
    Display a quote with a timestamp.

    Parameters:
        quote (dict): A dictionary with 'quote' and 'author' keys
    """
    # TODO: Get the current time and format it nicely
    # TODO: Print the quote in a nice format, like:
    #   [2:30 PM] "The quote text here" -- Author Name
    pass


def main():
    """Run the random quote generator."""
    print("=== RANDOM QUOTE GENERATOR ===")
    print("Press Enter for a new quote, or type 'quit' to exit.\n")

    # TODO: Build the path to quotes.json (it's in the same folder as this file)
    # HINT: script_dir = os.path.dirname(os.path.abspath(__file__))
    #        filepath = os.path.join(script_dir, "quotes.json")

    # TODO: Load the quotes

    # TODO: Loop: display a random quote, then wait for input
    # If user types 'quit', break out of the loop
    pass


if __name__ == "__main__":
    main()
