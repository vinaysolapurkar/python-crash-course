"""
CHECKPOINT: Library Management System
=======================================

Congratulations on finishing Sprint 3! Time to put it all together.

Build a Library Management System using everything you've learned:
  - Classes & Objects (Chapter 15)
  - Inheritance (Chapter 16) — not required but you could use it
  - Magic Methods (Chapter 17) — __str__, __repr__, __len__, etc.
  - Design Principles (Chapter 18) — clean code, single responsibility

Requirements:

1. Book class:
   - Attributes: title, author, isbn, available (bool, default True)
   - Magic methods: __str__, __repr__, __eq__ (compare by ISBN)
   - Method: info() — returns a formatted string

2. Member class:
   - Attributes: name, member_id, borrowed_books (list of ISBNs)
   - Methods: borrow(isbn), return_book(isbn)
   - Magic methods: __str__, __repr__

3. Library class:
   - Attributes: name, books (dict of isbn→Book), members (dict of id→Member)
   - Methods:
     - add_book(book) — add a Book to the library
     - register_member(member) — add a Member
     - borrow_book(member_id, isbn) — handle borrowing logic
     - return_book(member_id, isbn) — handle returning logic
     - search(query) — search books by title or author
     - list_available() — show all available books
     - list_borrowed() — show all borrowed books
     - save(filename) — save library state to JSON
     - load(filename) — load library state from JSON
   - Magic methods: __str__, __len__ (number of books)

4. Main menu (text-based):
   - Display options: add book, register member, borrow, return,
     search, list books, save, load, quit
   - Loop until user quits

Bonus:
   - Add a due date system (books due in 14 days)
   - Track borrowing history
   - Add late fee calculation

Starter code below — fill in the classes and menu!
"""

import json
from datetime import datetime


class Book:
    """A library book."""

    def __init__(self, title, author, isbn, available=True):
        # TODO: Set attributes
        pass

    def __str__(self):
        # TODO: Return a nice display string
        # Example: "'The Hobbit' by J.R.R. Tolkien (ISBN: 978-0-547-92822-7) [Available]"
        pass

    def __repr__(self):
        # TODO: Return a developer-friendly string
        pass

    def __eq__(self, other):
        # TODO: Books are equal if they have the same ISBN
        pass

    def to_dict(self):
        """Convert to dictionary for JSON saving."""
        # TODO: Return a dict with all attributes
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Book from a dictionary (for JSON loading)."""
        # TODO: Return Book(**data)
        pass


class Member:
    """A library member."""

    def __init__(self, name, member_id, borrowed_books=None):
        # TODO: Set attributes (be careful with mutable default!)
        pass

    def __str__(self):
        # TODO: Return member info string
        pass

    def __repr__(self):
        pass

    def to_dict(self):
        """Convert to dictionary for JSON saving."""
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Member from a dictionary."""
        pass


class Library:
    """The library that manages books and members."""

    def __init__(self, name):
        # TODO: Set name, books (dict), members (dict)
        pass

    def add_book(self, book):
        """Add a book to the library."""
        # TODO: Add book to self.books using ISBN as key
        pass

    def register_member(self, member):
        """Register a new member."""
        # TODO: Add member to self.members using member_id as key
        pass

    def borrow_book(self, member_id, isbn):
        """Handle the borrowing process."""
        # TODO: Check member exists, book exists, book available
        # TODO: Mark book unavailable, add ISBN to member's borrowed list
        pass

    def return_book(self, member_id, isbn):
        """Handle the return process."""
        # TODO: Check member exists, book exists
        # TODO: Mark book available, remove ISBN from member's borrowed list
        pass

    def search(self, query):
        """Search books by title or author (case insensitive)."""
        # TODO: Return list of matching books
        pass

    def list_available(self):
        """Return list of available books."""
        # TODO
        pass

    def list_borrowed(self):
        """Return list of borrowed books."""
        # TODO
        pass

    def save(self, filename="library_data.json"):
        """Save library state to JSON file."""
        # TODO: Convert books and members to dicts, save as JSON
        pass

    def load(self, filename="library_data.json"):
        """Load library state from JSON file."""
        # TODO: Read JSON, create Book and Member objects
        pass

    def __str__(self):
        # TODO
        pass

    def __len__(self):
        # TODO: Return total number of books
        pass


def main():
    """Main menu for the library system."""
    library = Library("Pythonville Public Library")

    # TODO: Add some sample books to get started
    # TODO: Create the menu loop

    while True:
        print(f"\n{'=' * 45}")
        print(f"  {library}")
        print(f"{'=' * 45}")
        print("  1. Add a book")
        print("  2. Register a member")
        print("  3. Borrow a book")
        print("  4. Return a book")
        print("  5. Search books")
        print("  6. List available books")
        print("  7. List borrowed books")
        print("  8. Save library")
        print("  9. Load library")
        print("  0. Quit")
        print(f"{'=' * 45}")

        choice = input("\nChoose an option: ").strip()

        if choice == "0":
            # TODO: Maybe auto-save?
            print("Thanks for visiting the library! 📚")
            break
        # TODO: Handle each menu option
        else:
            print("Invalid option. Try again!")


if __name__ == "__main__":
    main()
