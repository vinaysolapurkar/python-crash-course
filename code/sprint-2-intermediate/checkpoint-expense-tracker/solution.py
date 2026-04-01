"""
CHECKPOINT PROJECT SOLUTION: Expense Tracker
==============================================
A complete, polished expense tracker that brings together
everything from Sprint 2. This is what a real mini-app looks like!

Features:
  - Add expenses with categories and auto-timestamps
  - Persistent storage via CSV (your data survives restarts!)
  - View all expenses in a formatted table
  - Filter by category
  - Summary stats with per-category bar chart
  - Bulletproof error handling throughout

Modules used: csv, os, datetime, functools.reduce, map, filter
Concepts: dicts, functions, file I/O, error handling, lambdas
"""

import csv
import os
from datetime import datetime
from functools import reduce

# =============================================================================
# CONFIGURATION
# =============================================================================

# Path for the CSV file (same folder as this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "expenses.csv")

# Available categories -- pick from these when adding expenses
CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]

# CSV column headers
FIELDNAMES = ["date", "amount", "category", "description"]

# Our in-memory expense list (loaded from CSV on startup)
expenses = []


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_float(prompt, min_val=None, max_val=None):
    """Safely get a float from the user. Retry until valid."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "quit":
            return None
        try:
            value = float(user_input)
        except ValueError:
            print(f"  '{user_input}' is not a valid number. Try again!")
            continue
        if min_val is not None and value < min_val:
            print(f"  Must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Must be at most {max_val}.")
            continue
        return value


def get_int(prompt, min_val=None, max_val=None):
    """Safely get an integer from the user. Retry until valid."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "quit":
            return None
        try:
            value = int(user_input)
        except ValueError:
            print(f"  '{user_input}' is not a valid whole number. Try again!")
            continue
        if min_val is not None and value < min_val:
            print(f"  Must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Must be at most {max_val}.")
            continue
        return value


def pick_category():
    """Display category menu and return the chosen category string."""
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    choice = get_int("  Pick a category (1-6): ", min_val=1, max_val=len(CATEGORIES))
    if choice is None:
        return None
    return CATEGORIES[choice - 1]


# =============================================================================
# FILE I/O -- Save and Load from CSV
# =============================================================================

def load_expenses():
    """
    Load expenses from the CSV file.
    Returns a list of expense dicts, or empty list if file doesn't exist.
    """
    if not os.path.exists(CSV_FILE):
        return []

    loaded = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert amount from string back to float
                row["amount"] = float(row["amount"])
                loaded.append(row)
    except (csv.Error, ValueError, KeyError) as e:
        print(f"  Warning: Error reading CSV file: {e}")
        print("  Starting with empty expense list.")
        return []

    return loaded


def save_expenses():
    """Save all expenses to the CSV file."""
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except IOError as e:
        print(f"  Error saving to CSV: {e}")
        return False


# =============================================================================
# CORE FEATURES
# =============================================================================

def add_expense():
    """Add a new expense with full input validation."""
    print("\n  --- Add New Expense ---")

    # Get amount
    amount = get_float("  Amount: $", min_val=0.01, max_val=999999.99)
    if amount is None:
        print("  Cancelled.")
        return

    # Get category
    category = pick_category()
    if category is None:
        print("  Cancelled.")
        return

    # Get description
    description = input("  Description: ").strip()
    if not description:
        description = f"{category} expense"  # Default if they skip it

    # Auto-generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Create expense dict and add to list
    expense = {
        "date": timestamp,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

    # Save immediately (so data persists even if program crashes)
    if save_expenses():
        print(f"\n  Added: ${amount:.2f} for {category} -- '{description}'")
        print(f"  Recorded at {timestamp}. Your wallet felt that one.")
    else:
        print("  Expense added to memory but could not save to file.")


def view_all():
    """Display all expenses in a nicely formatted table."""
    if not expenses:
        print("\n  No expenses recorded yet! Your wallet is breathing easy.")
        return

    print(f"\n  {'#':>3}  {'Date':<17} {'Amount':>9}  {'Category':<15} {'Description'}")
    print("  " + "-" * 70)

    for i, exp in enumerate(expenses, 1):
        print(
            f"  {i:>3}  "
            f"{exp['date']:<17} "
            f"${exp['amount']:>8.2f}  "
            f"{exp['category']:<15} "
            f"{exp['description']}"
        )

    # Total at the bottom
    total = sum(exp["amount"] for exp in expenses)
    print("  " + "-" * 70)
    print(f"  {'TOTAL':>3}  {'':<17} ${total:>8.2f}")
    print(f"\n  {len(expenses)} expense(s) recorded.")


def view_by_category():
    """Filter and display expenses for a chosen category."""
    if not expenses:
        print("\n  No expenses to filter! Add some first.")
        return

    # Pick a category
    category = pick_category()
    if category is None:
        return

    # Use filter() to get matching expenses -- Chapter 14 in action!
    filtered = list(filter(
        lambda exp: exp["category"] == category,
        expenses
    ))

    if not filtered:
        print(f"\n  No expenses in '{category}'. That category is living rent-free!")
        return

    # Display filtered results
    print(f"\n  --- {category} Expenses ({len(filtered)} found) ---")
    print(f"  {'#':>3}  {'Date':<17} {'Amount':>9}  {'Description'}")
    print("  " + "-" * 55)

    for i, exp in enumerate(filtered, 1):
        print(f"  {i:>3}  {exp['date']:<17} ${exp['amount']:>8.2f}  {exp['description']}")

    # Category total using reduce -- because we can!
    cat_total = reduce(lambda acc, exp: acc + exp["amount"], filtered, 0)
    print("  " + "-" * 55)
    print(f"  {'':>3}  {'SUBTOTAL':<17} ${cat_total:>8.2f}")


def show_summary():
    """Show summary statistics with per-category breakdown and bar chart."""
    if not expenses:
        print("\n  No expenses to summarize! Add some spending first.")
        return

    print("\n" + "=" * 55)
    print("          EXPENSE SUMMARY")
    print("=" * 55)

    # --- Overall Stats (using reduce) ---
    total = reduce(lambda acc, exp: acc + exp["amount"], expenses, 0)
    average = total / len(expenses)

    # Find highest and lowest expense using reduce
    highest = reduce(
        lambda a, b: a if a["amount"] > b["amount"] else b,
        expenses
    )
    lowest = reduce(
        lambda a, b: a if a["amount"] < b["amount"] else b,
        expenses
    )

    print(f"\n  Total expenses:     {len(expenses)}")
    print(f"  Total spending:     ${total:>10.2f}")
    print(f"  Average per expense: ${average:>9.2f}")
    print(f"  Biggest expense:    ${highest['amount']:>10.2f} ({highest['description']})")
    print(f"  Smallest expense:   ${lowest['amount']:>10.2f} ({lowest['description']})")

    # --- Per-Category Breakdown ---
    print(f"\n  --- By Category ---")
    print(f"  {'Category':<15} {'Count':>5} {'Total':>10} {'Avg':>9}  {'Chart'}")
    print("  " + "-" * 65)

    # Calculate per-category stats using map and filter
    cat_stats = []
    for cat in CATEGORIES:
        # Filter expenses for this category
        cat_expenses = list(filter(lambda e: e["category"] == cat, expenses))
        if cat_expenses:
            cat_total = reduce(lambda a, e: a + e["amount"], cat_expenses, 0)
            cat_avg = cat_total / len(cat_expenses)
            cat_stats.append({
                "category": cat,
                "count": len(cat_expenses),
                "total": cat_total,
                "avg": cat_avg
            })

    # Sort by total (highest first)
    cat_stats.sort(key=lambda c: c["total"], reverse=True)

    # Find max total for bar chart scaling
    max_total = max(c["total"] for c in cat_stats) if cat_stats else 1

    for cs in cat_stats:
        # Create a proportional bar chart
        bar_length = int((cs["total"] / max_total) * 20)
        bar = "#" * bar_length

        # Calculate percentage of total
        pct = (cs["total"] / total) * 100

        print(
            f"  {cs['category']:<15} "
            f"{cs['count']:>5} "
            f"${cs['total']:>9.2f} "
            f"${cs['avg']:>8.2f}  "
            f"{bar} {pct:.0f}%"
        )

    # Categories with no expenses
    empty_cats = [cat for cat in CATEGORIES
                  if not any(e["category"] == cat for e in expenses)]
    if empty_cats:
        print(f"\n  No spending in: {', '.join(empty_cats)}")

    print("=" * 55)

    # Fun commentary based on spending
    if total > 1000:
        print("  Your wallet is crying. Maybe rethink some of these?")
    elif total > 500:
        print("  Moderate spending. Not bad, not great. The financial middle child.")
    elif total > 100:
        print("  Reasonable spending! Your budget approves.")
    else:
        print("  Very frugal! Are you saving up for something big?")


# =============================================================================
# MAIN MENU & PROGRAM LOOP
# =============================================================================

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("      EXPENSE TRACKER v1.0")
    print("=" * 35)
    print("  1. Add expense")
    print("  2. View all expenses")
    print("  3. View by category")
    print("  4. Summary & stats")
    print("  5. Quit")
    print("=" * 35)


def main():
    """Main program loop -- the conductor of the orchestra."""
    global expenses

    print("\n  Welcome to Expense Tracker v1.0!")
    print("  'Track every penny, even the ones in the couch cushions.'\n")

    # Load existing expenses from CSV
    expenses = load_expenses()
    if expenses:
        total = sum(e["amount"] for e in expenses)
        print(f"  Loaded {len(expenses)} expenses (${total:.2f} total) from file.")
    else:
        print("  No existing expenses found. Starting fresh!")
        print("  (Expenses will be saved to expenses.csv)")

    while True:
        show_menu()

        try:
            choice = input("  Pick an option (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\n\n  Interrupted! Saving and exiting...")
            save_expenses()
            break

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            # Save one final time before exiting
            save_expenses()
            print("\n  All expenses saved to expenses.csv!")
            print("  Thanks for tracking your spending.")
            print("  Remember: a budget is telling your money where to go")
            print("  instead of wondering where it went.")
            print("  Goodbye!\n")
            break
        else:
            print("  Invalid choice! Please pick a number from 1 to 5.")


if __name__ == "__main__":
    main()
