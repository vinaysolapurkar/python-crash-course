"""
Chapter 25 Exercise SOLUTION: Type-Hinted Expense Tracker
==========================================================
Every function is annotated, every variable is typed,
and mypy gives us a clean bill of health. Code hygiene at its finest!

Run type checking: mypy solution.py
"""

import json
import os
from typing import Optional, Union


class Expense:
    """Represents a single expense with description, amount, category, and date."""

    def __init__(
        self,
        description: str,
        amount: float,
        category: str,
        date: str,
    ) -> None:
        self.description: str = description
        self.amount: float = round(amount, 2)
        self.category: str = category.lower()
        self.date: str = date  # format: "YYYY-MM-DD"

    def to_dict(self) -> dict[str, Union[str, float]]:
        """Convert expense to a dictionary for JSON serialization."""
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Union[str, float]]) -> "Expense":
        """Create an Expense from a dictionary (deserialization)."""
        return cls(
            description=str(data["description"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            date=str(data["date"]),
        )

    def __str__(self) -> str:
        return (
            f"{self.date} | {self.description:<25} | "
            f"${self.amount:>8.2f} [{self.category}]"
        )

    def __repr__(self) -> str:
        return (
            f"Expense('{self.description}', {self.amount}, "
            f"'{self.category}', '{self.date}')"
        )


def add_expense(
    expenses: list[Expense],
    description: str,
    amount: float,
    category: str,
    date: str,
) -> Expense:
    """
    Add a new expense to the list.

    Args:
        expenses: The list to append to.
        description: What the expense was for.
        amount: How much was spent.
        category: Spending category (food, transport, etc.).
        date: Date string in YYYY-MM-DD format.

    Returns:
        The newly created Expense object.
    """
    expense = Expense(description, amount, category, date)
    expenses.append(expense)
    return expense


def get_total(expenses: list[Expense]) -> float:
    """
    Calculate the total of all expenses.

    Args:
        expenses: List of expenses to sum.

    Returns:
        Total amount as a float.
    """
    return round(sum(expense.amount for expense in expenses), 2)


def get_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    """
    Filter expenses by category (case insensitive).

    Args:
        expenses: List of all expenses.
        category: Category to filter by.

    Returns:
        List of matching expenses.
    """
    category_lower: str = category.lower()
    return [
        expense for expense in expenses
        if expense.category == category_lower
    ]


def get_summary(expenses: list[Expense]) -> dict[str, dict[str, Union[int, float]]]:
    """
    Get spending summary grouped by category.

    Args:
        expenses: List of all expenses.

    Returns:
        Dict mapping category name to {"count": int, "total": float}.
    """
    summary: dict[str, dict[str, Union[int, float]]] = {}

    for expense in expenses:
        category: str = expense.category
        if category not in summary:
            summary[category] = {"count": 0, "total": 0.0}
        summary[category]["count"] = int(summary[category]["count"]) + 1
        summary[category]["total"] = float(summary[category]["total"]) + expense.amount

    # Round totals
    for category_data in summary.values():
        category_data["total"] = round(float(category_data["total"]), 2)

    return summary


def find_expense(expenses: list[Expense], query: str) -> list[Expense]:
    """
    Search expenses by description (case insensitive).

    Args:
        expenses: List to search through.
        query: Search string to match.

    Returns:
        List of matching expenses.
    """
    query_lower: str = query.lower()
    return [
        expense for expense in expenses
        if query_lower in expense.description.lower()
    ]


def remove_expense(expenses: list[Expense], index: int) -> Optional[Expense]:
    """
    Remove expense at the given index.

    Args:
        expenses: List to remove from.
        index: Index of the expense to remove.

    Returns:
        The removed Expense, or None if index is out of bounds.
    """
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    return None


def format_currency(amount: float) -> str:
    """
    Format a number as a USD currency string.

    Args:
        amount: The number to format.

    Returns:
        Formatted string like "$1,234.56".
    """
    return f"${amount:,.2f}"


def save_expenses(expenses: list[Expense], filename: str) -> None:
    """
    Save expenses to a JSON file.

    Args:
        expenses: List of expenses to save.
        filename: Path to the output JSON file.
    """
    data: list[dict[str, Union[str, float]]] = [
        expense.to_dict() for expense in expenses
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_expenses(filename: str) -> list[Expense]:
    """
    Load expenses from a JSON file.

    Args:
        filename: Path to the JSON file.

    Returns:
        List of Expense objects, or empty list if file not found.
    """
    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as file:
        data: list[dict[str, Union[str, float]]] = json.load(file)

    return [Expense.from_dict(item) for item in data]


def display_expenses(expenses: list[Expense], title: str = "Expenses") -> None:
    """Display a list of expenses in a formatted table."""
    if not expenses:
        print(f"\n  No {title.lower()} found.")
        return

    total: float = get_total(expenses)
    print(f"\n  {title} ({len(expenses)} items):")
    print(f"  {'─' * 60}")
    for expense in expenses:
        print(f"  {expense}")
    print(f"  {'─' * 60}")
    print(f"  Total: {format_currency(total)}")


def display_summary(expenses: list[Expense]) -> None:
    """Display spending summary by category."""
    summary: dict[str, dict[str, Union[int, float]]] = get_summary(expenses)

    if not summary:
        print("\n  No expenses to summarize.")
        return

    grand_total: float = get_total(expenses)

    print(f"\n  {'Category':<15} {'Count':>6} {'Total':>12} {'% of Total':>10}")
    print(f"  {'─' * 15} {'─' * 6} {'─' * 12} {'─' * 10}")

    for category, data in sorted(summary.items()):
        count: int = int(data["count"])
        total: float = float(data["total"])
        percentage: float = (total / grand_total * 100) if grand_total > 0 else 0

        print(
            f"  {category:<15} {count:>6} "
            f"{format_currency(total):>12} {percentage:>9.1f}%"
        )

    print(f"  {'─' * 43}")
    print(f"  {'TOTAL':<22} {format_currency(grand_total):>12}")


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  TYPE-HINTED EXPENSE TRACKER")
    print("=" * 55)

    # Create expenses
    expenses: list[Expense] = []
    add_expense(expenses, "Morning coffee", 4.50, "food", "2024-01-15")
    add_expense(expenses, "Bus ticket", 2.50, "transport", "2024-01-15")
    add_expense(expenses, "Lunch - sushi", 15.99, "food", "2024-01-15")
    add_expense(expenses, "Python book", 39.99, "education", "2024-01-15")
    add_expense(expenses, "Movie night", 24.00, "entertainment", "2024-01-16")
    add_expense(expenses, "Groceries", 67.43, "food", "2024-01-16")
    add_expense(expenses, "Uber ride", 18.50, "transport", "2024-01-16")
    add_expense(expenses, "Gym membership", 30.00, "health", "2024-01-17")

    # Display all
    display_expenses(expenses, "All Expenses")

    # Summary
    display_summary(expenses)

    # Filter by category
    food_expenses: list[Expense] = get_by_category(expenses, "food")
    display_expenses(food_expenses, "Food Expenses")

    # Search
    search_results: list[Expense] = find_expense(expenses, "coffee")
    display_expenses(search_results, "Search: 'coffee'")

    # Remove an expense
    removed: Optional[Expense] = remove_expense(expenses, 0)
    if removed:
        print(f"\n  Removed: {removed}")

    # Save and load
    save_expenses(expenses, "test_expenses.json")
    loaded: list[Expense] = load_expenses("test_expenses.json")
    print(f"\n  Saved and loaded {len(loaded)} expenses successfully!")

    # Clean up test file
    if os.path.exists("test_expenses.json"):
        os.remove("test_expenses.json")

    print(f"""
\n  Type Hint Summary:
  ─────────────────────
  Functions annotated:  10+
  Classes annotated:    1
  Return types:         All specified
  Parameter types:      All specified
  Optional used:        remove_expense (can return None)
  Union used:           dict values (str | float | int)

  Run 'mypy solution.py' to verify — should be 0 errors!
""")
