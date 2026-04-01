"""
Chapter 22 Exercise: SQLite Expense Tracker
=============================================

Convert the expense tracker concept to use a SQLite database!
No more losing data when the program ends.

Requirements:

1. Create an 'expenses' table with columns:
   - id (auto-increment primary key)
   - description (text, required)
   - amount (real, required)
   - category (text — "food", "transport", "entertainment", etc.)
   - date (text — store as "YYYY-MM-DD")

2. Implement these functions:
   - add_expense(description, amount, category)
   - view_all_expenses()
   - view_by_category(category)
   - get_total()
   - get_total_by_category()
   - delete_expense(expense_id)
   - search_expenses(query)

3. Build a menu-driven interface

Bonus:
   - Monthly summary
   - Export to CSV
   - Budget warnings per category

Starter code below:
"""

import sqlite3
import os
from datetime import datetime

DB_FILE = "expenses.db"


def create_table():
    """Create the expenses table if it doesn't exist."""
    # TODO: Connect to DB_FILE and create the table
    # Hint: Use CREATE TABLE IF NOT EXISTS
    pass


def add_expense(description, amount, category):
    """Add a new expense to the database."""
    # TODO: Insert a new expense with today's date
    # Hint: datetime.now().strftime("%Y-%m-%d") for today's date
    pass


def view_all_expenses():
    """Display all expenses."""
    # TODO: SELECT all expenses, ordered by date (newest first)
    # TODO: Display in a nice table format
    pass


def view_by_category(category):
    """Display expenses filtered by category."""
    # TODO: SELECT expenses WHERE category matches
    pass


def get_total():
    """Get the total of all expenses."""
    # TODO: Use SELECT SUM(amount) FROM expenses
    pass


def get_total_by_category():
    """Get totals grouped by category."""
    # TODO: Use GROUP BY category
    pass


def delete_expense(expense_id):
    """Delete an expense by its ID."""
    # TODO: DELETE FROM expenses WHERE id = ?
    pass


def search_expenses(query):
    """Search expenses by description."""
    # TODO: Use LIKE for fuzzy matching
    pass


def main():
    """Main menu for the expense tracker."""
    create_table()

    while True:
        print(f"\n{'=' * 40}")
        print("  EXPENSE TRACKER (SQLite Edition)")
        print(f"{'=' * 40}")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. View by category")
        print("  4. Total expenses")
        print("  5. Totals by category")
        print("  6. Search expenses")
        print("  7. Delete expense")
        print("  0. Quit")
        print(f"{'=' * 40}")

        choice = input("\n  Choose: ").strip()

        if choice == "0":
            print("  Goodbye! Your expenses are saved.")
            break
        # TODO: Handle each menu option
        else:
            print("  Invalid option!")


if __name__ == "__main__":
    main()
