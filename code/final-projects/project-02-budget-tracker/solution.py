"""
=============================================================
  PROJECT 2: PERSONAL BUDGET TRACKER - SOLUTION
=============================================================
  A CLI budget tracker with CSV persistence, monthly
  summaries, and budget warnings.

  No external dependencies - just Python's standard library!

  Run:  python solution.py
=============================================================
"""

import csv
import os
from datetime import date, datetime

# ── Configuration ───────────────────────────────────────────
DATA_FILE = "budget_data.csv"
BUDGET_FILE = "budget_settings.txt"

INCOME_CATEGORIES = ["Salary", "Freelance", "Investments", "Other"]
EXPENSE_CATEGORIES = [
    "Food", "Transport", "Housing", "Entertainment",
    "Shopping", "Bills", "Health", "Other",
]

CSV_HEADERS = ["date", "type", "category", "amount", "description"]


# ── File I/O Functions ─────────────────────────────────────

def load_transactions():
    """Load all transactions from the CSV file."""
    transactions = []

    if not os.path.exists(DATA_FILE):
        return transactions

    try:
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except (FileNotFoundError, csv.Error) as e:
        print(f"Warning: Could not load data file: {e}")

    return transactions


def save_transaction(transaction):
    """Append a single transaction to the CSV file."""
    file_exists = os.path.exists(DATA_FILE)

    try:
        with open(DATA_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)

            # Write headers if the file is brand new
            if not file_exists:
                writer.writeheader()

            writer.writerow(transaction)
    except IOError as e:
        print(f"Error saving transaction: {e}")


def load_budget():
    """Load the monthly budget from the settings file."""
    if not os.path.exists(BUDGET_FILE):
        return None
    try:
        with open(BUDGET_FILE, "r") as f:
            return float(f.read().strip())
    except (ValueError, IOError):
        return None


def save_budget(amount):
    """Save the monthly budget to the settings file."""
    try:
        with open(BUDGET_FILE, "w") as f:
            f.write(str(amount))
    except IOError as e:
        print(f"Error saving budget: {e}")


# ── Input Helpers ──────────────────────────────────────────

def get_amount(prompt="Amount: $"):
    """Safely get a positive dollar amount from the user."""
    while True:
        try:
            raw = input(prompt).strip().replace("$", "").replace(",", "")
            amount = float(raw)
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("That's not a valid number. Try again.")


def get_category(category_list):
    """Let the user pick from a list of categories."""
    print("Categories:")
    for i, cat in enumerate(category_list, 1):
        print(f"  {i}. {cat}")

    while True:
        choice = input("Choose a category (number or name): ").strip()

        # Try by number
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(category_list):
                return category_list[idx]
        except ValueError:
            pass

        # Try by name (case-insensitive)
        for cat in category_list:
            if choice.lower() == cat.lower():
                return cat

        print(f"Invalid choice. Please pick 1-{len(category_list)}.")


# ── Core Features ──────────────────────────────────────────

def add_income():
    """Record a new income entry."""
    print("\n--- Add Income ---")
    category = get_category(INCOME_CATEGORIES)
    amount = get_amount()
    description = input("Description: ").strip() or "No description"

    transaction = {
        "date": date.today().isoformat(),
        "type": "income",
        "category": category,
        "amount": amount,
        "description": description,
    }

    save_transaction(transaction)
    print(f"\nAdded! Income of ${amount:,.2f} ({category}) recorded.")


def add_expense():
    """Record a new expense entry."""
    print("\n--- Add Expense ---")
    category = get_category(EXPENSE_CATEGORIES)
    amount = get_amount()
    description = input("Description: ").strip() or "No description"

    transaction = {
        "date": date.today().isoformat(),
        "type": "expense",
        "category": category,
        "amount": amount,
        "description": description,
    }

    save_transaction(transaction)
    print(f"\nAdded! Expense of ${amount:,.2f} ({category}) recorded.")


def view_summary():
    """Show a monthly summary of income, expenses, and balance."""
    transactions = load_transactions()

    if not transactions:
        print("\nNo transactions yet. Start adding some!")
        return

    # Default to current month
    today = date.today()
    print(f"\nShow summary for which month? (default: {today.strftime('%Y-%m')})")
    month_input = input("Enter YYYY-MM or press Enter: ").strip()

    if month_input:
        try:
            target = datetime.strptime(month_input, "%Y-%m")
            year, month = target.year, target.month
        except ValueError:
            print("Invalid format. Showing current month.")
            year, month = today.year, today.month
    else:
        year, month = today.year, today.month

    # Filter transactions for the target month
    monthly = []
    for t in transactions:
        try:
            t_date = datetime.strptime(t["date"], "%Y-%m-%d")
            if t_date.year == year and t_date.month == month:
                monthly.append(t)
        except ValueError:
            continue

    # Calculate totals
    total_income = sum(t["amount"] for t in monthly if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in monthly if t["type"] == "expense")
    balance = total_income - total_expenses

    month_name = date(year, month, 1).strftime("%B %Y")

    print()
    print("=" * 40)
    print(f"  MONTHLY SUMMARY: {month_name}")
    print("=" * 40)
    print(f"  Total Income:    ${total_income:>10,.2f}")
    print(f"  Total Expenses:  ${total_expenses:>10,.2f}")
    print(f"  {'─' * 34}")

    # Color the balance (positive = good, negative = bad)
    if balance >= 0:
        print(f"  Balance:         ${balance:>10,.2f}")
    else:
        print(f"  Balance:        -${abs(balance):>10,.2f}  !!!")

    # Check against budget
    budget = load_budget()
    if budget is not None:
        remaining = budget - total_expenses
        print()
        print(f"  Monthly Budget:  ${budget:>10,.2f}")
        if remaining >= 0:
            print(f"  Remaining:       ${remaining:>10,.2f}")
            print(f"  Status: Within budget")
        else:
            print(f"  Over Budget By: -${abs(remaining):>10,.2f}")
            print(f"  Status: OVER BUDGET! Cut back!")

    print("=" * 40)
    print(f"  Transactions this month: {len(monthly)}")


def view_by_category():
    """Show a breakdown of spending/income by category."""
    transactions = load_transactions()

    if not transactions:
        print("\nNo transactions yet!")
        return

    # Group by type and category
    income_totals = {}
    expense_totals = {}

    for t in transactions:
        cat = t["category"]
        amount = t["amount"]
        if t["type"] == "income":
            income_totals[cat] = income_totals.get(cat, 0) + amount
        else:
            expense_totals[cat] = expense_totals.get(cat, 0) + amount

    print()
    print("=" * 40)
    print("  CATEGORY REPORT")
    print("=" * 40)

    if income_totals:
        print("\n  INCOME:")
        print(f"  {'Category':<16} {'Amount':>12}")
        print(f"  {'─' * 28}")
        for cat, total in sorted(income_totals.items(),
                                 key=lambda x: x[1], reverse=True):
            print(f"  {cat:<16} ${total:>10,.2f}")
        print(f"  {'─' * 28}")
        grand = sum(income_totals.values())
        print(f"  {'TOTAL':<16} ${grand:>10,.2f}")

    if expense_totals:
        print("\n  EXPENSES:")
        print(f"  {'Category':<16} {'Amount':>12}")
        print(f"  {'─' * 28}")
        for cat, total in sorted(expense_totals.items(),
                                 key=lambda x: x[1], reverse=True):
            print(f"  {cat:<16} ${total:>10,.2f}")
        print(f"  {'─' * 28}")
        grand = sum(expense_totals.values())
        print(f"  {'TOTAL':<16} ${grand:>10,.2f}")

    print()
    print("=" * 40)


def set_monthly_budget():
    """Set or update the monthly expense budget."""
    current = load_budget()
    if current is not None:
        print(f"\nCurrent monthly budget: ${current:,.2f}")
    else:
        print("\nNo budget set yet.")

    amount = get_amount("Enter new monthly budget: $")
    save_budget(amount)
    print(f"Budget set to ${amount:,.2f} per month.")


# ── Main Menu ──────────────────────────────────────────────

def show_menu():
    """Display the main menu."""
    print()
    print("=" * 36)
    print("  PERSONAL BUDGET TRACKER")
    print("=" * 36)
    print("  1. Add Income")
    print("  2. Add Expense")
    print("  3. View Monthly Summary")
    print("  4. View by Category")
    print("  5. Set Monthly Budget")
    print("  6. Exit")
    print()


def main():
    """Main program loop."""
    print()
    print("*" * 36)
    print("  Welcome to Budget Tracker!")
    print("  Your finances, under control.")
    print("*" * 36)

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            set_monthly_budget()
        elif choice == "6":
            print("\nGoodbye! Keep tracking those dollars!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
