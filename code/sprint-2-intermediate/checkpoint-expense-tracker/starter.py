"""
CHECKPOINT PROJECT: Expense Tracker
====================================
Congratulations on finishing Sprint 2! Time to put it ALL together.

Build a complete expense tracker that uses everything you've learned:
  - Dictionaries (Chapter 9)   -> store expense data
  - Functions (Chapter 10)     -> organize your code
  - Modules (Chapter 11)       -> csv, datetime, os
  - File Handling (Chapter 12) -> save/load expenses to CSV
  - Error Handling (Chapter 13)-> handle all bad input
  - Functional Tools (Ch 14)   -> map, filter, reduce for summaries

FEATURES TO BUILD:
  1. Add an expense (amount, category, description, auto-timestamp)
  2. View all expenses (formatted table)
  3. View expenses by category (using filter)
  4. Summary statistics (total, average, per-category breakdown with bar chart)
  5. Save to / Load from CSV file (persistent data!)
  6. Menu loop with error handling throughout

CATEGORIES: Food, Transport, Entertainment, Shopping, Bills, Other

DATA FORMAT (each expense is a dict):
  {
      "date": "2025-03-15 14:30",
      "amount": 12.50,
      "category": "Food",
      "description": "Lunch at Chipotle"
  }

CSV FORMAT:
  date,amount,category,description
  2025-03-15 14:30,12.50,Food,Lunch at Chipotle

STARTER STRUCTURE (fill in the functions!):
"""

import csv
import os
from datetime import datetime
from functools import reduce

# Path for the CSV file (same folder as this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "expenses.csv")

# Available categories
CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]

# Our in-memory expense list
expenses = []


def load_expenses():
    """Load expenses from the CSV file into the expenses list."""
    # TODO: Check if CSV file exists
    # TODO: Use csv.DictReader to load rows
    # TODO: Convert amount from string to float
    # TODO: Return the list of expense dicts
    pass


def save_expenses():
    """Save all expenses to the CSV file."""
    # TODO: Use csv.DictWriter to write all expenses
    # TODO: Include header row: date, amount, category, description
    pass


def add_expense():
    """Add a new expense with input validation."""
    # TODO: Ask for amount (validate: must be positive number)
    # TODO: Show category menu and ask for choice (validate: must be 1-6)
    # TODO: Ask for description
    # TODO: Auto-generate timestamp with datetime.now()
    # TODO: Create expense dict and append to expenses list
    # TODO: Save to CSV
    pass


def view_all():
    """Display all expenses in a formatted table."""
    # TODO: If no expenses, print a message
    # TODO: Print a nice table with columns: #, Date, Amount, Category, Description
    # TODO: Print total at the bottom
    pass


def view_by_category():
    """Filter and display expenses for a specific category."""
    # TODO: Show category menu
    # TODO: Use filter() to get expenses matching the chosen category
    # TODO: Display filtered results
    pass


def show_summary():
    """Show summary statistics using reduce and map."""
    # TODO: Total spending (use reduce)
    # TODO: Average per expense
    # TODO: Per-category breakdown with totals
    # TODO: Simple bar chart using # characters
    pass


def show_menu():
    """Display the main menu."""
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View by category")
    print("4. Summary & stats")
    print("5. Quit")
    print("===========================")


def main():
    """Main program loop."""
    global expenses

    print("Welcome to the Expense Tracker!")
    print("Your wallet's new best friend (or worst enemy).\n")

    # Load existing expenses
    # TODO: expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Pick an option (1-5): ").strip()

        # TODO: Route to the correct function based on choice
        # TODO: Handle invalid input
        # TODO: On quit, save and say goodbye
        pass


if __name__ == "__main__":
    main()
