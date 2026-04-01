"""
Chapter 12 Exercise SOLUTION: Diary App
=========================================
A fully working diary app with timestamps, entry counting,
and even word counts. Dear Diary, Python is awesome.
"""

from datetime import datetime
import os


# Path to the diary file (same folder as this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIARY_FILE = os.path.join(SCRIPT_DIR, "diary.txt")


def show_menu():
    """Display the diary menu."""
    print("\n" + "=" * 40)
    print("       MY PERSONAL DIARY")
    print("=" * 40)
    print("  1. Write a new entry")
    print("  2. Read all entries")
    print("  3. Diary stats")
    print("  4. Quit")
    print("=" * 40)


def write_entry():
    """Write a new diary entry with a pretty timestamp."""
    print("\n  What's on your mind? (Press Enter twice to finish)")

    # Collect multi-line input (keep reading until empty line)
    lines = []
    while True:
        line = input("  > ")
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("  Empty entry -- nothing saved. Writer's block happens!")
        return

    entry_text = "\n  ".join(lines)

    # Generate timestamp
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Append to diary file
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"--- Entry: {timestamp} ---\n")
        f.write(f"  {entry_text}\n\n")

    print(f"\n  Entry saved! ({len(lines)} line(s), {sum(len(l) for l in lines)} chars)")
    print("  Your thoughts are now immortalized in diary.txt.")


def read_entries():
    """Read and display all diary entries."""
    if not os.path.exists(DIARY_FILE):
        print("\n  No diary entries yet! Start writing to create your diary.")
        return

    # Check if file is empty
    if os.path.getsize(DIARY_FILE) == 0:
        print("\n  Diary file exists but is empty. Time to write something!")
        return

    print("\n  " + "-" * 40)
    print("  YOUR DIARY ENTRIES")
    print("  " + "-" * 40)

    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print(content)
    print("  " + "-" * 40)
    print("  (End of diary)")


def diary_stats():
    """Show some fun stats about your diary. Data nerds rejoice!"""
    if not os.path.exists(DIARY_FILE):
        print("\n  No diary to analyze! Write some entries first.")
        return

    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

    # Count entries (lines that start with "--- Entry:")
    entry_count = sum(1 for line in lines if line.startswith("--- Entry:"))

    # Count words (rough estimate)
    words = content.split()
    word_count = len(words)

    # File size
    file_size = os.path.getsize(DIARY_FILE)

    print(f"\n  --- Diary Stats ---")
    print(f"  Total entries: {entry_count}")
    print(f"  Total words: {word_count}")
    print(f"  Total lines: {len(lines)}")
    print(f"  File size: {file_size} bytes")

    if entry_count > 0:
        avg_words = word_count // entry_count
        print(f"  Avg words/entry: ~{avg_words}")

    # Fun commentary based on entry count
    if entry_count == 0:
        print("  Verdict: Your diary is emptier than a Monday morning inbox.")
    elif entry_count < 5:
        print("  Verdict: A fledgling diarist! Keep it up!")
    elif entry_count < 20:
        print("  Verdict: Getting serious! You're a regular Anne Frank.")
    else:
        print("  Verdict: Prolific writer! Publishing deal incoming?")


def main():
    """Run the diary app."""
    print("\n  Welcome to your Personal Diary!")
    print("  'A place where your thoughts roam free (in plaintext)'")

    while True:
        show_menu()
        choice = input("  Pick an option (1-4): ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            diary_stats()
        elif choice == "4":
            print("\n  Goodbye! Remember: the pen is mightier than the sword,")
            print("  but Python is mightier than the pen. See you tomorrow!")
            break
        else:
            print("  Invalid choice. Pick 1-4, not the meaning of life.")


if __name__ == "__main__":
    main()
