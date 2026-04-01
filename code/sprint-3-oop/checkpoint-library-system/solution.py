"""
CHECKPOINT SOLUTION: Library Management System
================================================
A fully-featured library system using OOP principles from Sprint 3!

Features:
  - Book, Member, Library classes with magic methods
  - Borrow/return with validation
  - Search by title or author
  - JSON persistence (save/load)
  - Text-based menu interface

Run it: python solution.py
"""

import json
import os
from datetime import datetime, timedelta


class Book:
    """
    A library book. Each book is identified by its ISBN.
    Think of it like a Social Security number, but for books.
    """

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) [{status}]"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.available})"

    def __eq__(self, other):
        """Two books are the same if they share an ISBN."""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return NotImplemented

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Book from a dictionary (deserialization)."""
        return cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            available=data.get("available", True),
        )


class Member:
    """
    A library member. Can borrow books and (hopefully) return them.
    """

    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        # Avoid mutable default argument trap!
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __str__(self):
        book_count = len(self.borrowed_books)
        return f"{self.name} (ID: {self.member_id}) — {book_count} book(s) borrowed"

    def __repr__(self):
        return f"Member('{self.name}', '{self.member_id}', {self.borrowed_books})"

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Member from a dictionary."""
        return cls(
            name=data["name"],
            member_id=data["member_id"],
            borrowed_books=data.get("borrowed_books", []),
        )


class Library:
    """
    The Library — manages books and members.
    Single Responsibility: Book handles book data, Member handles member data,
    Library handles the interactions between them.
    """

    def __init__(self, name):
        self.name = name
        self.books = {}      # isbn → Book
        self.members = {}    # member_id → Member

    def add_book(self, book):
        """Add a book to the library collection."""
        if book.isbn in self.books:
            print(f"  Book with ISBN {book.isbn} already exists!")
            return False
        self.books[book.isbn] = book
        print(f"  Added: {book}")
        return True

    def register_member(self, member):
        """Register a new library member."""
        if member.member_id in self.members:
            print(f"  Member ID {member.member_id} already registered!")
            return False
        self.members[member.member_id] = member
        print(f"  Registered: {member}")
        return True

    def borrow_book(self, member_id, isbn):
        """
        Handle the borrowing process.
        Checks: member exists, book exists, book is available.
        """
        # Check member exists
        if member_id not in self.members:
            print(f"  Member ID '{member_id}' not found. Register first!")
            return False

        # Check book exists
        if isbn not in self.books:
            print(f"  Book ISBN '{isbn}' not found in library.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        # Check book is available
        if not book.available:
            print(f"  Sorry, '{book.title}' is currently borrowed by someone else.")
            return False

        # Check member hasn't exceeded limit (let's say 5 books max)
        if len(member.borrowed_books) >= 5:
            print(f"  {member.name} has reached the borrowing limit (5 books)!")
            return False

        # All good — process the borrow
        book.available = False
        member.borrowed_books.append(isbn)
        print(f"  {member.name} borrowed '{book.title}'. Enjoy the read!")
        return True

    def return_book(self, member_id, isbn):
        """Handle the return process."""
        if member_id not in self.members:
            print(f"  Member ID '{member_id}' not found.")
            return False

        if isbn not in self.books:
            print(f"  Book ISBN '{isbn}' not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if isbn not in member.borrowed_books:
            print(f"  {member.name} didn't borrow '{book.title}'.")
            return False

        # Process the return
        book.available = True
        member.borrowed_books.remove(isbn)
        print(f"  {member.name} returned '{book.title}'. Thanks!")
        return True

    def search(self, query):
        """Search books by title or author (case insensitive)."""
        query_lower = query.lower()
        results = [
            book for book in self.books.values()
            if query_lower in book.title.lower() or query_lower in book.author.lower()
        ]
        return results

    def list_available(self):
        """Return list of available books."""
        return [book for book in self.books.values() if book.available]

    def list_borrowed(self):
        """Return list of currently borrowed books."""
        return [book for book in self.books.values() if not book.available]

    def save(self, filename="library_data.json"):
        """Save library state to a JSON file."""
        data = {
            "name": self.name,
            "books": [book.to_dict() for book in self.books.values()],
            "members": [member.to_dict() for member in self.members.values()],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  Library saved to '{filename}'!")

    def load(self, filename="library_data.json"):
        """Load library state from a JSON file."""
        if not os.path.exists(filename):
            print(f"  File '{filename}' not found. Starting fresh!")
            return False

        with open(filename, "r") as f:
            data = json.load(f)

        self.name = data.get("name", self.name)
        self.books = {}
        self.members = {}

        for book_data in data.get("books", []):
            book = Book.from_dict(book_data)
            self.books[book.isbn] = book

        for member_data in data.get("members", []):
            member = Member.from_dict(member_data)
            self.members[member.member_id] = member

        print(f"  Loaded {len(self.books)} books and {len(self.members)} members!")
        return True

    def __str__(self):
        available = len(self.list_available())
        total = len(self.books)
        return f"{self.name} — {total} books ({available} available), {len(self.members)} members"

    def __len__(self):
        return len(self.books)

    def __contains__(self, isbn):
        """Allows: 'ISBN-123' in library"""
        return isbn in self.books


def get_sample_books():
    """Returns a list of sample books to populate the library."""
    return [
        Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0-345-39180-3"),
        Book("1984", "George Orwell", "978-0-451-52493-5"),
        Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5"),
        Book("Pride and Prejudice", "Jane Austen", "978-0-14-143951-8"),
        Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "978-0-590-35340-3"),
        Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0-618-64015-7"),
        Book("Dune", "Frank Herbert", "978-0-441-17271-9"),
        Book("Python Crash Course", "Eric Matthes", "978-1-718-50227-8"),
    ]


def display_books(books, label="Books"):
    """Helper to display a list of books nicely."""
    if not books:
        print(f"\n  No {label.lower()} found.")
        return
    print(f"\n  {label} ({len(books)}):")
    print(f"  {'─' * 60}")
    for i, book in enumerate(books, 1):
        print(f"  {i}. {book}")
    print(f"  {'─' * 60}")


def main():
    """Main menu for the library system."""
    library = Library("Pythonville Public Library")

    # Try to load saved data, otherwise use sample books
    if not library.load():
        print("\n  Loading sample books...")
        for book in get_sample_books():
            library.add_book(book)
        # Add a sample member
        library.register_member(Member("Alice Johnson", "M001"))
        library.register_member(Member("Bob Smith", "M002"))

    while True:
        print(f"\n{'=' * 55}")
        print(f"  {library}")
        print(f"{'=' * 55}")
        print("  1. Add a book")
        print("  2. Register a member")
        print("  3. Borrow a book")
        print("  4. Return a book")
        print("  5. Search books")
        print("  6. List available books")
        print("  7. List borrowed books")
        print("  8. List all members")
        print("  9. Save library")
        print("  0. Quit")
        print(f"{'=' * 55}")

        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            # Add a book
            print("\n  --- Add a New Book ---")
            title = input("  Title: ").strip()
            author = input("  Author: ").strip()
            isbn = input("  ISBN: ").strip()
            if title and author and isbn:
                library.add_book(Book(title, author, isbn))
            else:
                print("  All fields are required!")

        elif choice == "2":
            # Register a member
            print("\n  --- Register a New Member ---")
            name = input("  Name: ").strip()
            member_id = input("  Member ID: ").strip()
            if name and member_id:
                library.register_member(Member(name, member_id))
            else:
                print("  Both name and member ID are required!")

        elif choice == "3":
            # Borrow a book
            print("\n  --- Borrow a Book ---")
            display_books(library.list_available(), "Available Books")
            member_id = input("\n  Your Member ID: ").strip()
            isbn = input("  Book ISBN to borrow: ").strip()
            if member_id and isbn:
                library.borrow_book(member_id, isbn)
            else:
                print("  Both member ID and ISBN are required!")

        elif choice == "4":
            # Return a book
            print("\n  --- Return a Book ---")
            display_books(library.list_borrowed(), "Currently Borrowed")
            member_id = input("\n  Your Member ID: ").strip()
            isbn = input("  Book ISBN to return: ").strip()
            if member_id and isbn:
                library.return_book(member_id, isbn)
            else:
                print("  Both member ID and ISBN are required!")

        elif choice == "5":
            # Search
            print("\n  --- Search Books ---")
            query = input("  Search (title or author): ").strip()
            if query:
                results = library.search(query)
                display_books(results, f"Results for '{query}'")
            else:
                print("  Enter a search term!")

        elif choice == "6":
            # Available books
            display_books(library.list_available(), "Available Books")

        elif choice == "7":
            # Borrowed books
            display_books(library.list_borrowed(), "Borrowed Books")

        elif choice == "8":
            # List members
            if library.members:
                print(f"\n  Members ({len(library.members)}):")
                print(f"  {'─' * 50}")
                for member in library.members.values():
                    print(f"  - {member}")
                    if member.borrowed_books:
                        for isbn in member.borrowed_books:
                            book = library.books.get(isbn)
                            if book:
                                print(f"      Borrowed: '{book.title}'")
                print(f"  {'─' * 50}")
            else:
                print("\n  No members registered yet.")

        elif choice == "9":
            # Save
            library.save()

        elif choice == "0":
            # Quit
            save_choice = input("\n  Save before quitting? (y/n): ").strip().lower()
            if save_choice == "y":
                library.save()
            print("\n  Thanks for visiting the library! 📚 Happy reading!")
            break

        else:
            print("  Invalid option. Please choose 0-9.")


if __name__ == "__main__":
    main()
