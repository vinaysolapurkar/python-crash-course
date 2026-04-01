# Sprint 3 Checkpoint: Library Management System

> **Project** | **45-60 min build** | **Starter & Solution: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/sprint-3-project-library/)**

Sprint 3 done. Take a second to appreciate what just happened.

You now think in objects. You look at a problem and you see classes, attributes, methods, relationships. That's a fundamental shift in how you write code - and honestly, in how you *think* about code. Most of the software in the world is built this way, and now you can read it, write it, and reason about it.

Let's prove it by building something real.

## The Project: Library Management System

You're going to build a Library Management System with three core classes - `Book`, `Member`, and `Library` - that handles checkouts, returns, searching, and saves everything to a JSON file so your data survives between runs.

This isn't a toy example. It touches every skill from this sprint:

| Concept | Where You'll Use It |
|-----|----------|
| Classes & `__init__` (Ch. 15) | Every class you build |
| Methods & `self` (Ch. 15) | Every method you write |
| Inheritance (Ch. 16) | `EBook` and `AudioBook` extend `Book` |
| Magic methods (Ch. 17) | `__str__`, `__repr__`, `__len__` on `Library` |
| Encapsulation (Ch. 18) | Protected attributes, controlled access |
| Composition (Ch. 18) | `Library` HAS books and members |
| Polymorphism (Ch. 18) | Different book types, same interface |

Plus file handling and error handling from Sprint 2. See? It all connects.

## Step 1: The Book Class

Start with the foundation. A book has a title, author, ISBN, and availability status.

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self._borrower = None

    def check_out(self, member_name):
        if not self.is_available:
            raise ValueError(f"'{self.title}' is already checked out")
        self.is_available = False
        self._borrower = member_name
        return f"'{self.title}' checked out to {member_name}"

    def return_book(self):
        if self.is_available:
            raise ValueError(f"'{self.title}' wasn't checked out")
        borrower = self._borrower
        self.is_available = True
        self._borrower = None
        return f"'{self.title}' returned by {borrower}"

    def __str__(self):
        status = "Available" if self.is_available else f"Checked out to {self._borrower}"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

    def to_dict(self):
        """Convert to dictionary for JSON saving."""
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_available": self.is_available,
            "borrower": self._borrower,
        }
```

Notice the `to_dict()` method - that's how we'll save to JSON later. Also notice `_borrower` has a single underscore. It's internal data that should only be changed through `check_out()` and `return_book()`. That's encapsulation in action.

## Step 2: Specialized Book Types (Inheritance)

An eBook has a file format. An audiobook has a narrator and duration. Both are still books.

```python
class EBook(Book):
    def __init__(self, title, author, isbn, file_format="PDF"):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        base = super().__str__()
        return f"{base} [EBook: {self.file_format}]"

    def to_dict(self):
        data = super().to_dict()
        data["file_format"] = self.file_format
        return data


class AudioBook(Book):
    def __init__(self, title, author, isbn, narrator, duration_hours):
        super().__init__(title, author, isbn)
        self.narrator = narrator
        self.duration_hours = duration_hours

    def __str__(self):
        base = super().__str__()
        return f"{base} [AudioBook: {self.duration_hours}h, narrated by {self.narrator}]"

    def to_dict(self):
        data = super().to_dict()
        data["narrator"] = self.narrator
        data["duration_hours"] = self.duration_hours
        return data
```

Inheritance at work: `EBook` and `AudioBook` get `check_out()`, `return_book()`, and everything else from `Book` for free. They just add their own special attributes.

## Step 3: The Member Class

A library member can borrow books and has a borrowing history.

```python
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self._max_books = 5

    def borrow(self, book):
        if len(self.borrowed_books) >= self._max_books:
            raise ValueError(f"{self.name} has reached the borrowing limit ({self._max_books})")
        result = book.check_out(self.name)
        self.borrowed_books.append(book.isbn)
        return result

    def return_book(self, book):
        if book.isbn not in self.borrowed_books:
            raise ValueError(f"{self.name} didn't borrow '{book.title}'")
        result = book.return_book()
        self.borrowed_books.remove(book.isbn)
        return result

    def __str__(self):
        count = len(self.borrowed_books)
        return f"Member: {self.name} (ID: {self.member_id}) - {count} book(s) borrowed"

    def __repr__(self):
        return f"Member('{self.name}', '{self.member_id}')"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books,
        }
```

## Step 4: The Library Class (Composition + Magic Methods)

The `Library` class is the heart of the system. It HAS books and HAS members (composition). It supports `len()` and string formatting (magic methods).

```python
import json
from pathlib import Path


class Library:
    def __init__(self, name):
        self.name = name
        self._books = {}       # isbn -> Book
        self._members = {}     # member_id -> Member

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists")
        self._books[book.isbn] = book
        return f"Added: {book.title}"

    def add_member(self, member):
        if member.member_id in self._members:
            raise ValueError(f"Member ID {member.member_id} already exists")
        self._members[member.member_id] = member
        return f"Registered: {member.name}"

    def find_book(self, query):
        """Search by title or author (case-insensitive)."""
        query = query.lower()
        results = []
        for book in self._books.values():
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results

    def checkout_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if not member:
            raise ValueError(f"No member with ID {member_id}")
        book = self._books.get(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")
        return member.borrow(book)

    def return_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if not member:
            raise ValueError(f"No member with ID {member_id}")
        book = self._books.get(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")
        return member.return_book(book)

    def available_books(self):
        return [b for b in self._books.values() if b.is_available]

    # -- Magic methods --

    def __len__(self):
        return len(self._books)

    def __str__(self):
        available = len(self.available_books())
        total = len(self)
        return f"{self.name}: {total} books ({available} available), {len(self._members)} members"

    def __contains__(self, isbn):
        return isbn in self._books

    # -- JSON persistence --

    def save(self, filepath="library_data.json"):
        data = {
            "name": self.name,
            "books": [b.to_dict() for b in self._books.values()],
            "members": [m.to_dict() for m in self._members.values()],
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return f"Library saved to {filepath}"

    @classmethod
    def load(cls, filepath="library_data.json"):
        with open(filepath, "r") as f:
            data = json.load(f)

        library = cls(data["name"])

        # Rebuild books (polymorphism: different types, same loading logic)
        book_classes = {"Book": Book, "EBook": EBook, "AudioBook": AudioBook}
        for book_data in data["books"]:
            book_type = book_data.pop("type", "Book")
            is_available = book_data.pop("is_available")
            borrower = book_data.pop("borrower")
            BookClass = book_classes.get(book_type, Book)
            book = BookClass(**book_data)
            book.is_available = is_available
            book._borrower = borrower
            library.add_book(book)

        # Rebuild members
        for member_data in data["members"]:
            borrowed = member_data.pop("borrowed_books")
            member = Member(**member_data)
            member.borrowed_books = borrowed
            library.add_member(member)

        return library
```

## Step 5: Put It All Together

Here's a script that exercises the entire system:

```python
def main():
    # Create the library
    lib = Library("City Central Library")

    # Add books (polymorphism - different types, same interface)
    lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"))
    lib.add_book(Book("1984", "George Orwell", "978-0451524935"))
    lib.add_book(EBook("Python Crash Course", "Eric Matthes", "978-1718502703", "EPUB"))
    lib.add_book(AudioBook("Dune", "Frank Herbert", "978-0441013593", "Scott Brick", 21.5))

    # Add members
    lib.add_member(Member("Alice", "M001"))
    lib.add_member(Member("Bob", "M002"))

    # Library overview
    print(lib)
    print()

    # Search for books
    results = lib.find_book("python")
    for book in results:
        print(f"  Found: {book}")
    print()

    # Check out some books
    print(lib.checkout_book("M001", "978-0743273565"))
    print(lib.checkout_book("M001", "978-1718502703"))
    print(lib.checkout_book("M002", "978-0441013593"))
    print()

    # Check status
    print(lib)
    print()

    print("Available books:")
    for book in lib.available_books():
        print(f"  {book}")
    print()

    # Return a book
    print(lib.return_book("M001", "978-0743273565"))
    print()

    # Magic method: __contains__
    print(f"Has ISBN 978-0451524935? {'978-0451524935' in lib}")
    print(f"Total books: {len(lib)}")
    print()

    # Save to JSON
    print(lib.save())

    # Load from JSON (proof it works)
    loaded_lib = Library.load()
    print(f"\nLoaded: {loaded_lib}")


if __name__ == "__main__":
    main()
```

Expected output:

```
City Central Library: 4 books (4 available), 2 members

  Found: 'Python Crash Course' by Eric Matthes (ISBN: 978-1718502703) - Available [EBook: EPUB]

'The Great Gatsby' checked out to Alice
'Python Crash Course' checked out to Alice
'Dune' checked out to Bob

City Central Library: 4 books (1 available), 2 members

Available books:
  '1984' by George Orwell (ISBN: 978-0451524935) - Available

'The Great Gatsby' returned by Alice

Has ISBN 978-0451524935? True
Total books: 4

Library saved to library_data.json

Loaded: City Central Library: 4 books (2 available), 2 members
```

## Stretch Goals

Already finished? Try adding:

1. **Due dates.** When a book is checked out, record the date. Add a method to check for overdue books (more than 14 days).

2. **Fines.** Calculate late fees at $0.25 per day. Store the fine on the `Member` object.

3. **Search improvements.** Add search by availability, by type (`EBook` vs `AudioBook`), or by member (show all books a member has borrowed).

4. **A command-line interface.** Use `input()` and a menu loop to let users interact with the library from the terminal. Something like:

```
Welcome to City Central Library!
1. Search for a book
2. Check out a book
3. Return a book
4. View available books
5. Save & quit
```

5. **Exception handling.** Wrap the main flow in try/except blocks so the program doesn't crash on bad input.

## What You Used From This Sprint

Take a look at what you just built:

- **Classes and objects** - `Book`, `Member`, `Library` (Chapter 15)
- **`__init__` and `self`** - everywhere (Chapter 15)
- **Inheritance** - `EBook` and `AudioBook` extending `Book` (Chapter 16)
- **`super()`** - child constructors calling parent setup (Chapter 16)
- **Magic methods** - `__str__`, `__repr__`, `__len__`, `__contains__` (Chapter 17)
- **Encapsulation** - `_borrower`, `_books`, `_members`, `_max_books` (Chapter 18)
- **Composition** - `Library` HAS books and members (Chapter 18)
- **Polymorphism** - `EBook`, `AudioBook`, and `Book` all work the same way (Chapter 18)
- **File handling** - JSON save/load (Sprint 2, Chapter 12)
- **Error handling** - `ValueError` for invalid operations (Sprint 2, Chapter 13)

That's not a toy program. That's a real system with real design patterns. You should feel good about this.

## What's Next

You're past the halfway point of the book. Most people who start learning to code quit before getting here. You didn't. That means something. It means you're the kind of person who pushes through the hard parts, who doesn't quit when `self` is confusing or when inheritance doesn't click on the first try.

Sprint 4 is where things get *really* exciting. You're going to take everything you've built - your Python fundamentals, your OOP skills - and start building things that connect to the real world: APIs, web scraping, databases. The code you write is about to escape your terminal and start talking to the internet.

But first, take a break. Build the library project. Maybe go outside. You've earned it.

See you in Sprint 4.
