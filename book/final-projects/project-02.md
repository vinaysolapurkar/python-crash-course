# Project 2: Personal Budget Tracker

> **Difficulty:** 2/5 | **Time:** ~1.5 hours | **Skills:** file I/O, functions, error handling, CSV
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-02-budget-tracker/

## What You'll Build

A command-line budget tracker that lets you log income and expenses with categories, view monthly reports, and persist all data to a CSV file. Every time you open the app, your previous transactions are right where you left them.

Here's what it looks like:

```
=== PERSONAL BUDGET TRACKER ===

1. Add Income
2. Add Expense
3. View Summary
4. View Monthly Report
5. Search Transactions
6. Exit

Choice: 3

-- Financial Summary --
Total Income:   $3,250.00
Total Expenses: $1,847.50
Balance:        $1,402.50

Top Expense Categories:
  Rent:       $1,200.00 (64.9%)
  Groceries:    $347.50 (18.8%)
  Transport:    $300.00 (16.2%)
```

## Skills You'll Use

- Functions and program structure (learned in Chapter 5)
- File I/O and CSV module (learned in Chapter 7)
- Error handling with try/except (learned in Chapter 8)
- String formatting and f-strings (learned in Chapter 2)
- Dictionaries for aggregation (learned in Chapter 4)
- The `datetime` module (learned in Chapter 6)

## Step-by-Step Build Guide

### Step 1: Project Setup and Imports

Create the file and import everything you'll need. The `csv` and `datetime` modules are built into Python - no installs required.

```python
# budget_tracker.py

import csv
import os
from datetime import datetime

DATA_FILE = "budget_data.csv"
```

### Step 2: Build the CSV Persistence Layer

These two functions handle saving and loading data. If the CSV file doesn't exist yet, we create it with headers.

```python
def load_transactions():
    """Load all transactions from the CSV file."""
    transactions = []
    if not os.path.exists(DATA_FILE):
        return transactions

    try:
        with open(DATA_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except (csv.Error, ValueError) as e:
        print(f"Warning: Error reading data file: {e}")
        print("Starting with empty transaction list.")

    return transactions


def save_transactions(transactions):
    """Save all transactions to the CSV file."""
    fieldnames = ["date", "type", "category", "description", "amount"]

    try:
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except IOError as e:
        print(f"Error saving data: {e}")
```

### Step 3: Add Transaction Input Functions

These functions collect transaction details from the user with proper input validation. Notice how we validate the amount to ensure it's a positive number.

```python
INCOME_CATEGORIES = ["Salary", "Freelance", "Investment", "Gift", "Other"]
EXPENSE_CATEGORIES = ["Rent", "Groceries", "Transport", "Utilities",
                      "Entertainment", "Healthcare", "Education", "Other"]


def get_amount(prompt="Amount: $"):
    """Get a valid positive dollar amount from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g., 42.50).")


def choose_category(categories):
    """Let the user pick from a list of categories."""
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Choose category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Please enter a valid number.")


def add_transaction(transactions, trans_type):
    """Add an income or expense transaction."""
    print(f"\n-- Add {trans_type} --")

    if trans_type == "Income":
        category = choose_category(INCOME_CATEGORIES)
    else:
        category = choose_category(EXPENSE_CATEGORIES)

    amount = get_amount()
    description = input("Description (optional): ").strip() or "No description"
    date_str = datetime.now().strftime("%Y-%m-%d")

    transaction = {
        "date": date_str,
        "type": trans_type,
        "category": category,
        "description": description,
        "amount": amount
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print(f"\n  Added: {trans_type} - {category} - ${amount:,.2f}")
    print(f"  Saved to {DATA_FILE}")
```

### Step 4: Build the Summary View

This function aggregates all transactions to show totals, balance, and a breakdown of spending by category.

```python
def view_summary(transactions):
    """Display overall financial summary."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    total_income = sum(t["amount"] for t in transactions
                       if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions
                         if t["type"] == "Expense")
    balance = total_income - total_expenses

    print("\n-- Financial Summary --")
    print(f"  Total Income:   ${total_income:>10,.2f}")
    print(f"  Total Expenses: ${total_expenses:>10,.2f}")
    print(f"  Balance:        ${balance:>10,.2f}")

    if balance < 0:
        print("  ** Warning: You're spending more than you earn! **")

    # Category breakdown for expenses
    expense_by_category = {}
    for t in transactions:
        if t["type"] == "Expense":
            cat = t["category"]
            expense_by_category[cat] = expense_by_category.get(cat, 0) + t["amount"]

    if expense_by_category:
        print("\n  Top Expense Categories:")
        sorted_cats = sorted(expense_by_category.items(),
                             key=lambda x: x[1], reverse=True)
        for cat, amount in sorted_cats:
            pct = (amount / total_expenses * 100) if total_expenses > 0 else 0
            print(f"    {cat:<15} ${amount:>8,.2f} ({pct:.1f}%)")
```

### Step 5: Add Monthly Reports

Filter transactions by month and year to show period-specific breakdowns.

```python
def view_monthly_report(transactions):
    """Show a report for a specific month."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    # Get available months
    months = set()
    for t in transactions:
        month_key = t["date"][:7]  # "YYYY-MM"
        months.add(month_key)

    sorted_months = sorted(months, reverse=True)
    print("\nAvailable months:")
    for i, m in enumerate(sorted_months, 1):
        print(f"  {i}. {m}")

    while True:
        try:
            choice = int(input("Choose month number: "))
            if 1 <= choice <= len(sorted_months):
                selected = sorted_months[choice - 1]
                break
            print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    # Filter transactions for selected month
    monthly = [t for t in transactions if t["date"].startswith(selected)]

    income = sum(t["amount"] for t in monthly if t["type"] == "Income")
    expenses = sum(t["amount"] for t in monthly if t["type"] == "Expense")

    print(f"\n-- Report for {selected} --")
    print(f"  Income:   ${income:>10,.2f}")
    print(f"  Expenses: ${expenses:>10,.2f}")
    print(f"  Net:      ${income - expenses:>10,.2f}")

    print(f"\n  Transactions:")
    for t in monthly:
        sign = "+" if t["type"] == "Income" else "-"
        print(f"    {t['date']}  {sign}${t['amount']:>8,.2f}  "
              f"{t['category']:<12} {t['description']}")


def search_transactions(transactions):
    """Search transactions by keyword."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    keyword = input("\nSearch keyword: ").strip().lower()
    if not keyword:
        print("No keyword entered.")
        return

    matches = [t for t in transactions
               if keyword in t["category"].lower()
               or keyword in t["description"].lower()]

    if not matches:
        print(f"No transactions matching '{keyword}'.")
        return

    print(f"\n  Found {len(matches)} transaction(s):")
    total = 0
    for t in matches:
        sign = "+" if t["type"] == "Income" else "-"
        print(f"    {t['date']}  {sign}${t['amount']:>8,.2f}  "
              f"{t['category']:<12} {t['description']}")
        if t["type"] == "Income":
            total += t["amount"]
        else:
            total -= t["amount"]
    print(f"  Net total: ${total:,.2f}")
```

### Step 6: Wire Up the Main Menu

Connect everything with a main menu loop that loads data on start and keeps running until the user exits.

```python
def main():
    """Main application loop."""
    print("=" * 40)
    print("   PERSONAL BUDGET TRACKER")
    print("=" * 40)

    transactions = load_transactions()
    print(f"Loaded {len(transactions)} existing transaction(s).")

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Monthly Report")
        print("5. Search Transactions")
        print("6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_transaction(transactions, "Income")
        elif choice == "2":
            add_transaction(transactions, "Expense")
        elif choice == "3":
            view_summary(transactions)
        elif choice == "4":
            view_monthly_report(transactions)
        elif choice == "5":
            search_transactions(transactions)
        elif choice == "6":
            print("\nGoodbye! Keep tracking those finances.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Budget limits:** Let the user set monthly spending limits per category. When they add an expense that pushes a category over its limit, display a warning. Store limits in a separate CSV or JSON file.

2. **Export to formatted report:** Generate a nicely formatted text file report that summarizes a month's finances - something you could print or email to yourself.

3. **Recurring transactions:** Add support for recurring monthly transactions (like rent or salary) that auto-populate when you start a new month.

## Portfolio Tips

A budget tracker shows you understand data persistence, input validation, and practical problem-solving. When presenting this project:

- **GitHub:** Include sample CSV data so reviewers can see the app in action immediately. Add screenshots of the summary and monthly report output.
- **Resume:** "Developed a CLI budget tracker with CSV persistence, category-based analytics, and monthly reporting using Python."
- **Interview talking point:** Discuss your choice of CSV format for storage (human-readable, easily opened in Excel) and how you handled edge cases like empty files and invalid input. Mention how you'd evolve it - perhaps adding a SQLite database if the data grew large.
