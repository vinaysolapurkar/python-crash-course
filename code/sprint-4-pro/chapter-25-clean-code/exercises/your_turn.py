"""
Chapter 25 Exercise: Add Type Hints to the Expense Tracker
============================================================

Take the expense tracker functions below (simplified from Chapter 22)
and add proper type hints to EVERYTHING:
  - Function parameters
  - Return types
  - Variable annotations where helpful
  - Use Optional, Union, list, dict as needed

Also:
  - Fix any PEP 8 issues you spot
  - Rename any poorly-named variables
  - Add or improve docstrings

When done, run mypy on this file:
  mypy your_turn.py

Aim for ZERO mypy errors!

Starter code (intentionally missing type hints and has some style issues):
"""

# TODO: Add proper imports for type hints
# from typing import ...


# TODO: Add type hints to this class and all its methods
class Expense:
    """Represents a single expense."""

    def __init__(self, desc, amt, cat, date):
        # TODO: Add type annotations
        self.description = desc
        self.amount = amt
        self.category = cat
        self.date = date

    def to_dict(self):
        # TODO: Add return type hint
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        # TODO: Add parameter and return type hints
        return cls(
            desc=data["description"],
            amt=data["amount"],
            cat=data["category"],
            date=data["date"],
        )

    def __str__(self):
        return f"{self.date} | {self.description} | ${self.amount:.2f} [{self.category}]"


# TODO: Add type hints to all functions below

def add_expense(expenses, desc, amt, cat, date):
    """Add a new expense to the list."""
    # TODO: What types should these be?
    e = Expense(desc, amt, cat, date)
    expenses.append(e)
    return e


def get_total(expenses):
    """Calculate total of all expenses."""
    # TODO: Add type hints
    return sum(e.amount for e in expenses)


def get_by_category(expenses, cat):
    """Filter expenses by category."""
    # TODO: Add type hints
    return [e for e in expenses if e.category.lower() == cat.lower()]


def get_summary(expenses):
    """Get spending summary grouped by category."""
    # TODO: Add type hints
    summary = {}
    for e in expenses:
        c = e.category
        if c not in summary:
            summary[c] = {"count": 0, "total": 0.0}
        summary[c]["count"] += 1
        summary[c]["total"] += e.amount
    return summary


def find_expense(expenses, query):
    """Search expenses by description. Returns matches or empty list."""
    # TODO: Add type hints
    q = query.lower()
    return [e for e in expenses if q in e.description.lower()]


def remove_expense(expenses, idx):
    """Remove expense at index. Returns the removed expense or None."""
    # TODO: Add type hints (note: this can return None!)
    if 0 <= idx < len(expenses):
        return expenses.pop(idx)
    return None


def format_currency(amt):
    """Format a number as currency string."""
    # TODO: Add type hints
    return f"${amt:,.2f}"


def save_expenses(expenses, filename):
    """Save expenses to a JSON file."""
    # TODO: Add type hints
    import json
    data = [e.to_dict() for e in expenses]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_expenses(filename):
    """Load expenses from a JSON file. Returns list or empty list if file not found."""
    # TODO: Add type hints
    import json
    import os
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
    return [Expense.from_dict(d) for d in data]


# ----- Test your type hints -----
# After adding all type hints, run:
#   mypy your_turn.py
#   (aim for 0 errors!)

if __name__ == "__main__":
    expenses = []
    add_expense(expenses, "Coffee", 4.50, "food", "2024-01-15")
    add_expense(expenses, "Bus ticket", 2.50, "transport", "2024-01-15")
    add_expense(expenses, "Lunch", 12.99, "food", "2024-01-15")

    print("Expenses:")
    for e in expenses:
        print(f"  {e}")

    print(f"\nTotal: {format_currency(get_total(expenses))}")
    print(f"\nFood expenses: {get_by_category(expenses, 'food')}")
    print(f"\nSummary: {get_summary(expenses)}")
