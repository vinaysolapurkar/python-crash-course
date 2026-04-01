"""
Chapter 12 Exercise: Diary App
===============================
Build a personal diary app that saves entries to a file!

Features:
  1. Write a new diary entry (with automatic timestamp)
  2. Read all diary entries
  3. Quit

Your diary file should look something like:
  --- Entry: March 15, 2025 at 03:45 PM ---
  Today I learned about file handling in Python. Mind = blown.

  --- Entry: March 16, 2025 at 10:22 AM ---
  I built a diary app! I'm basically a software engineer now.

HINTS:
  - Use "a" mode to append entries (don't overwrite old ones!)
  - Use datetime.now().strftime() for timestamps
  - Use "r" mode to read all entries back
  - Use os.path.exists() to check if diary.txt exists yet
"""

from datetime import datetime
import os


# Path to the diary file (same folder as this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIARY_FILE = os.path.join(SCRIPT_DIR, "diary.txt")


def write_entry():
    """Write a new diary entry with a timestamp."""
    # TODO: Ask the user for their diary entry (use input())
    # TODO: Get the current timestamp using datetime.now().strftime()
    # TODO: Open the diary file in APPEND mode ("a")
    # TODO: Write the timestamp header and the entry text
    # HINT:
    #   with open(DIARY_FILE, "a") as f:
    #       f.write(f"--- Entry: {timestamp} ---\n")
    #       f.write(f"{entry}\n\n")
    pass


def read_entries():
    """Read and display all diary entries."""
    # TODO: Check if the diary file exists (os.path.exists)
    # TODO: If it doesn't exist, tell the user there are no entries yet
    # TODO: If it does exist, read and print all contents
    # HINT:
    #   with open(DIARY_FILE, "r") as f:
    #       print(f.read())
    pass


def main():
    """Run the diary app."""
    print("=== MY PERSONAL DIARY ===")
    print("Your thoughts are safe here (well, in a .txt file).\n")

    while True:
        print("1. Write a new entry")
        print("2. Read all entries")
        print("3. Quit")

        choice = input("\nPick an option (1-3): ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye! Keep writing -- future you will thank present you.")
            break
        else:
            print("Invalid choice! Please pick 1, 2, or 3.")


if __name__ == "__main__":
    main()
