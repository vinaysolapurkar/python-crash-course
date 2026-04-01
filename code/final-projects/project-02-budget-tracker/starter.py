"""
=============================================================
  PROJECT 2: PERSONAL BUDGET TRACKER
=============================================================

Build a command-line budget tracker that helps you manage
your money! It saves everything to a CSV file so your data
persists between sessions.

WHAT YOU'LL PRACTICE:
  - File I/O (reading/writing CSV files)
  - Functions and code organization
  - Error handling (try/except)
  - Working with dates
  - String formatting for reports
  - Data aggregation

REQUIREMENTS:
  1. Add income entries (amount, category, description)
  2. Add expense entries (amount, category, description)
  3. Save all transactions to a CSV file
  4. Load transactions when the program starts
  5. Show a monthly summary (total income, expenses, balance)
  6. Set a monthly budget and warn when overspending
  7. Generate a formatted report by category
  8. Handle invalid inputs gracefully (don't crash!)

CATEGORIES:
  Income:  Salary, Freelance, Investments, Other
  Expense: Food, Transport, Housing, Entertainment,
           Shopping, Bills, Health, Other

EXAMPLE OUTPUT:
  ====================================
    PERSONAL BUDGET TRACKER
  ====================================
  1. Add Income
  2. Add Expense
  3. View Summary
  4. View by Category
  5. Set Monthly Budget
  6. Exit

  > 1
  Category (Salary/Freelance/Investments/Other): Salary
  Amount: $3500
  Description: March paycheck
  Added! Income of $3,500.00 recorded.

  > 3
  ========= MONTHLY SUMMARY =========
  Period: March 2026

  Total Income:    $3,500.00
  Total Expenses:  $1,245.80
  ─────────────────────────────
  Balance:         $2,254.20

  Budget: $2,000.00
  Remaining: $754.20
  Status: Within budget

HINTS:
  - Use the csv module for reading/writing
  - Use datetime.date.today() for dates
  - Store amounts as floats, format with f"{amount:,.2f}"
  - Use try/except around float() conversions
  - A list of dicts works great for transactions

Good luck!
=============================================================
"""

import csv
import os
from datetime import date, datetime


# File to store transactions
DATA_FILE = "budget_data.csv"

# Valid categories
INCOME_CATEGORIES = ["Salary", "Freelance", "Investments", "Other"]
EXPENSE_CATEGORIES = ["Food", "Transport", "Housing", "Entertainment",
                      "Shopping", "Bills", "Health", "Other"]


def load_transactions():
    """Load transactions from the CSV file. Return a list of dicts."""
    # TODO: Read from DATA_FILE
    # TODO: Handle the case where the file doesn't exist yet
    # TODO: Return list of transaction dicts
    pass


def save_transaction(transaction):
    """Append a single transaction to the CSV file."""
    # TODO: Open file in append mode
    # TODO: Write the transaction as a CSV row
    # TODO: Create headers if file is new
    pass


def add_income():
    """Prompt user for income details and save it."""
    # TODO: Ask for category, amount, description
    # TODO: Validate inputs
    # TODO: Save the transaction
    pass


def add_expense():
    """Prompt user for expense details and save it."""
    # TODO: Ask for category, amount, description
    # TODO: Validate inputs
    # TODO: Save the transaction
    pass


def get_monthly_summary(year=None, month=None):
    """Calculate and display monthly summary."""
    # TODO: Filter transactions for the given month
    # TODO: Calculate total income and expenses
    # TODO: Show balance
    # TODO: Compare against budget if set
    pass


def get_category_report():
    """Show spending/income breakdown by category."""
    # TODO: Group transactions by category
    # TODO: Show totals for each category
    # TODO: Format as a nice table
    pass


def set_budget():
    """Let the user set a monthly budget."""
    # TODO: Ask for budget amount
    # TODO: Save it (you could use a separate file or variable)
    pass


def main():
    """Main menu loop."""
    # TODO: Print welcome banner
    # TODO: Show menu options
    # TODO: Handle user choice
    # TODO: Loop until exit
    pass


if __name__ == "__main__":
    main()
