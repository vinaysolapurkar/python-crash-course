# Sprint 2 Checkpoint: Expense Tracker

> **Sprint 2 Project** | **Estimated Time: 45-60 minutes** | **Skills: Chapters 9-14**

Sprint 2 complete. You're officially not a beginner anymore.

Think about where you were six chapters ago. You could make lists and loop through them. Now? You can organize data with dictionaries, write reusable functions, import powerful libraries, save data to files, handle errors gracefully, and write one-liners that would make a senior developer nod approvingly.

That's a serious level-up. Time to prove it.

## What You're Building

An **Expense Tracker** that runs in the terminal. It lets you add expenses, view them by category, see spending summaries, and - here's the important part - it saves everything to a CSV file so your data survives between sessions.

This isn't a toy. This is a tool you could actually use. (Or at least show off in an interview.)

### Features

- Add an expense (amount, category, description, auto-dated)
- View all expenses
- View expenses filtered by category
- See a spending summary (total per category + grand total)
- Data persists in a CSV file
- Crash-proof user input (no more explosions when someone types "banana" for the amount)

### Skills You'll Use

| Feature | Chapter |
|-----|-----|
| Storing expense data as dictionaries | Chapter 9 - Dictionaries |
| Organizing code into reusable functions | Chapter 10 - Functions |
| Using `csv`, `datetime`, and `os` modules | Chapter 11 - Modules |
| Reading/writing CSV files | Chapter 12 - File Handling |
| Input validation and error handling | Chapter 13 - Error Handling |
| Sorting and filtering with lambda | Chapter 14 - Lambda & Friends |

## Step-by-Step Build Guide

### Step 1: Set Up the Foundation

Create a file called `expense_tracker.py`. Start with your imports and constants.

```python
import csv
import os
from datetime import datetime

EXPENSE_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]
```

### Step 2: Write the Load Function

This function reads existing expenses from the CSV file. If the file doesn't exist yet, it returns an empty list.

```python
def load_expenses():
    """Load expenses from CSV file. Returns a list of dictionaries."""
    if not os.path.exists(EXPENSE_FILE):
        return []

    expenses = []
    try:
        with open(EXPENSE_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except (FileNotFoundError, csv.Error) as e:
        print(f"Error loading expenses: {e}")
        return []

    return expenses
```

Notice how we convert the amount back to a float. CSV files store everything as strings, so we need to convert numeric data back when reading.

### Step 3: Write the Save Function

This function writes all expenses to the CSV file.

```python
def save_expenses(expenses):
    """Save all expenses to CSV file."""
    fieldnames = ["date", "category", "amount", "description"]
    try:
        with open(EXPENSE_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
    except IOError as e:
        print(f"Error saving expenses: {e}")
```

### Step 4: Write the Input Helper

Remember the crash-proof input pattern from Chapter 13? Let's make a reusable version.

```python
def get_amount(prompt):
    """Get a valid positive number from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("That's not a valid number. Try again.")


def get_category():
    """Let the user pick a category from the list."""
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Pick a category (number): "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print(f"Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("That's not a valid number. Try again.")
```

### Step 5: Add an Expense

```python
def add_expense(expenses):
    """Add a new expense to the list."""
    print("\n-- Add Expense --")

    amount = get_amount("Amount: $")
    category = get_category()
    description = input("Description (optional): ").strip() or "No description"
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nAdded: ${amount:.2f} for {category} - {description}")
```

### Step 6: View Expenses

```python
def view_all_expenses(expenses):
    """Display all expenses in a formatted table."""
    if not expenses:
        print("\nNo expenses recorded yet. Start spending! (Responsibly.)")
        return

    print(f"\n{'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 55)

    for e in expenses:
        print(f"{e['date']:<12} {e['category']:<15} ${e['amount']:>9.2f} {e['description']}")

    total = sum(e["amount"] for e in expenses)
    print("-" * 55)
    print(f"{'TOTAL':<27} ${total:>9.2f}")


def view_by_category(expenses):
    """View expenses filtered by category."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    category = get_category()
    filtered = list(filter(lambda e: e["category"] == category, expenses))

    if not filtered:
        print(f"\nNo expenses in {category}.")
        return

    print(f"\n-- {category} Expenses --")
    for e in filtered:
        print(f"  {e['date']} - ${e['amount']:.2f} - {e['description']}")

    total = sum(e["amount"] for e in filtered)
    print(f"\n  Total {category}: ${total:.2f}")
```

### Step 7: Spending Summary

```python
def spending_summary(expenses):
    """Show total spending per category."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n-- Spending Summary --")

    # Group expenses by category
    category_totals = {}
    for e in expenses:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]

    # Sort by amount (highest first)
    sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

    grand_total = sum(category_totals.values())

    for cat, total in sorted_cats:
        percentage = (total / grand_total) * 100
        bar = "#" * int(percentage / 2)
        print(f"  {cat:<15} ${total:>9.2f} ({percentage:>5.1f}%) {bar}")

    print(f"\n  {'Grand Total':<15} ${grand_total:>9.2f}")
```

### Step 8: The Main Menu

```python
def main():
    """Main application loop."""
    expenses = load_expenses()
    print("=" * 40)
    print("   EXPENSE TRACKER")
    print("=" * 40)

    while True:
        print("\n-- Menu --")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Spending Summary")
        print("5. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            spending_summary(expenses)
        elif choice == "5":
            print("\nGoodbye! Stay on budget!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
```

### Step 9: Run It!

Save the file and run it:

```bash
python expense_tracker.py
```

Try adding a few expenses, viewing them, checking the summary. Close the program and run it again - your expenses are still there because they're saved to `expenses.csv`.

## Challenge Upgrades

If you breezed through the basic version, try these enhancements:

1. **Delete an expense** - Show numbered expenses and let the user pick one to remove
2. **Monthly report** - Filter expenses by month and show monthly totals
3. **Budget limits** - Set a budget per category and warn when approaching the limit
4. **Export summary** - Save the spending summary to a separate text file
5. **JSON storage** - Replace CSV with JSON for more flexible data storage

## The Full Code

The complete, working expense tracker is available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/sprint-2-checkpoint-expense-tracker/`

The repo includes:
- `expense_tracker.py` - The complete solution
- `expense_tracker_starter.py` - A skeleton with function signatures and comments
- `sample_expenses.csv` - Sample data to test with

## What's Next: Sprint 3

You've just built a real application. It has a menu system, file persistence, error handling, and organized code. That's not a tutorial exercise - that's a project.

Sprint 3 is where things get *really* interesting. You're going to learn **Object-Oriented Programming** - the paradigm that powers everything from video games to web apps to AI systems. You'll learn about classes, objects, inheritance, and all the patterns that make large-scale software possible.

You'll build a **Library Management System** that puts all of it together.

But first, take a break. You earned it. Go outside, touch grass, tell someone you're now an intermediate Python developer. Because you are.

See you in Sprint 3.
