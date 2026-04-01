"""
Chapter 22 Exercise SOLUTION: SQLite Expense Tracker
=====================================================
Track your spending with a database that remembers everything.
Your wallet might cry, but at least you'll know why.

Run it: python solution.py
"""

import sqlite3
import os
from datetime import datetime

DB_FILE = "expenses.db"


def get_connection():
    """Get a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """Create the expenses table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL DEFAULT 'other',
                date TEXT NOT NULL
            )
        """)
    print("  Database ready!")


def add_expense(description, amount, category):
    """Add a new expense to the database."""
    date = datetime.now().strftime("%Y-%m-%d")
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)",
            (description, amount, category.lower(), date),
        )
    print(f"  Added: {description} — ${amount:.2f} [{category}] on {date}")


def view_all_expenses():
    """Display all expenses in a table format."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM expenses ORDER BY date DESC, id DESC"
        ).fetchall()

    if not rows:
        print("\n  No expenses recorded yet. Your wallet is safe... for now.")
        return

    print(f"\n  {'ID':<5} {'Date':<12} {'Description':<25} {'Category':<15} {'Amount':>10}")
    print(f"  {'-'*5} {'-'*12} {'-'*25} {'-'*15} {'-'*10}")
    for row in rows:
        print(f"  {row['id']:<5} {row['date']:<12} "
              f"{row['description'][:24]:<25} {row['category']:<15} "
              f"${row['amount']:>9.2f}")
    print(f"  {'-'*67}")
    print(f"  {'Total:':<58} ${sum(r['amount'] for r in rows):>9.2f}")


def view_by_category(category):
    """Display expenses for a specific category."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM expenses WHERE category = ? ORDER BY date DESC",
            (category.lower(),),
        ).fetchall()

    if not rows:
        print(f"\n  No expenses in '{category}'. Either you're frugal or forgetful!")
        return

    total = sum(r["amount"] for r in rows)
    print(f"\n  Expenses in '{category}' ({len(rows)} items, ${total:.2f} total):")
    print(f"  {'-'*60}")
    for row in rows:
        print(f"  {row['date']} — {row['description']:<25} ${row['amount']:>9.2f}")


def get_total():
    """Get the grand total of all expenses."""
    with get_connection() as conn:
        result = conn.execute("SELECT SUM(amount) as total FROM expenses").fetchone()
    total = result["total"] or 0
    print(f"\n  Total expenses: ${total:.2f}")

    if total > 1000:
        print("  Whoa, big spender! Maybe time for a budget review? 💸")
    elif total > 500:
        print("  Getting up there. Keep an eye on it!")
    elif total > 0:
        print("  Looking reasonable! Keep it up!")
    return total


def get_total_by_category():
    """Get totals grouped by category."""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT category,
                   COUNT(*) as count,
                   SUM(amount) as total,
                   AVG(amount) as average,
                   MIN(amount) as min_amount,
                   MAX(amount) as max_amount
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
        """).fetchall()

    if not rows:
        print("\n  No expenses to analyze.")
        return

    grand_total = sum(r["total"] for r in rows)

    print(f"\n  {'Category':<15} {'Count':<8} {'Total':>10} {'Avg':>10} {'% of Total':>10}")
    print(f"  {'-'*15} {'-'*8} {'-'*10} {'-'*10} {'-'*10}")
    for row in rows:
        pct = (row["total"] / grand_total * 100) if grand_total > 0 else 0
        print(f"  {row['category']:<15} {row['count']:<8} "
              f"${row['total']:>9.2f} ${row['average']:>9.2f} {pct:>9.1f}%")
    print(f"  {'-'*53}")
    print(f"  {'TOTAL':<23} ${grand_total:>9.2f}")


def delete_expense(expense_id):
    """Delete an expense by its ID."""
    with get_connection() as conn:
        # First check if it exists
        row = conn.execute(
            "SELECT * FROM expenses WHERE id = ?", (expense_id,)
        ).fetchone()

        if not row:
            print(f"\n  Expense #{expense_id} not found!")
            return False

        print(f"\n  Deleting: {row['description']} — ${row['amount']:.2f} "
              f"[{row['category']}] on {row['date']}")

        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        print("  Deleted successfully!")
        return True


def search_expenses(query):
    """Search expenses by description (fuzzy match)."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM expenses WHERE description LIKE ? ORDER BY date DESC",
            (f"%{query}%",),
        ).fetchall()

    if not rows:
        print(f"\n  No expenses matching '{query}'.")
        return

    print(f"\n  Search results for '{query}' ({len(rows)} found):")
    print(f"  {'-'*60}")
    for row in rows:
        print(f"  [{row['id']}] {row['date']} — {row['description']:<25} "
              f"${row['amount']:>9.2f} [{row['category']}]")


def add_sample_data():
    """Add some sample expenses for testing."""
    samples = [
        ("Morning coffee", 4.50, "food"),
        ("Uber to work", 12.00, "transport"),
        ("Lunch - sushi", 15.99, "food"),
        ("Netflix subscription", 15.99, "entertainment"),
        ("Groceries", 67.43, "food"),
        ("Gas", 45.00, "transport"),
        ("Python book", 39.99, "education"),
        ("Movie tickets", 24.00, "entertainment"),
        ("Electricity bill", 85.00, "utilities"),
        ("Gym membership", 30.00, "health"),
        ("Dinner out", 42.50, "food"),
        ("Bus pass", 60.00, "transport"),
    ]
    for desc, amount, cat in samples:
        add_expense(desc, amount, cat)


def get_categories():
    """Get list of all categories used."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT DISTINCT category FROM expenses ORDER BY category"
        ).fetchall()
    return [r["category"] for r in rows]


def main():
    """Main menu for the expense tracker."""
    create_table()

    # Check if database is empty and offer sample data
    with get_connection() as conn:
        count = conn.execute("SELECT COUNT(*) FROM expenses").fetchone()[0]

    if count == 0:
        print("\n  Database is empty.")
        add_samples = input("  Load sample data? (y/n): ").strip().lower()
        if add_samples == "y":
            add_sample_data()

    while True:
        print(f"\n{'=' * 45}")
        print("  EXPENSE TRACKER (SQLite Edition)")
        print(f"{'=' * 45}")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. View by category")
        print("  4. Total expenses")
        print("  5. Totals by category")
        print("  6. Search expenses")
        print("  7. Delete expense")
        print("  0. Quit")
        print(f"{'=' * 45}")

        choice = input("\n  Choose: ").strip()

        if choice == "1":
            print("\n  --- Add Expense ---")
            desc = input("  Description: ").strip()
            if not desc:
                print("  Description is required!")
                continue

            try:
                amount = float(input("  Amount ($): ").strip())
                if amount <= 0:
                    print("  Amount must be positive!")
                    continue
            except ValueError:
                print("  Invalid amount!")
                continue

            categories = get_categories()
            if categories:
                print(f"  Existing categories: {', '.join(categories)}")
            category = input("  Category: ").strip() or "other"

            add_expense(desc, amount, category)

        elif choice == "2":
            view_all_expenses()

        elif choice == "3":
            categories = get_categories()
            if categories:
                print(f"\n  Available categories: {', '.join(categories)}")
            category = input("  Category to view: ").strip()
            if category:
                view_by_category(category)

        elif choice == "4":
            get_total()

        elif choice == "5":
            get_total_by_category()

        elif choice == "6":
            query = input("\n  Search term: ").strip()
            if query:
                search_expenses(query)

        elif choice == "7":
            view_all_expenses()
            try:
                expense_id = int(input("\n  Expense ID to delete: ").strip())
                confirm = input("  Are you sure? (y/n): ").strip().lower()
                if confirm == "y":
                    delete_expense(expense_id)
            except ValueError:
                print("  Invalid ID!")

        elif choice == "0":
            print("\n  Your expenses are safely stored in the database.")
            print("  They'll be here when you come back! Goodbye!")
            break

        else:
            print("  Invalid option! Choose 0-7.")


if __name__ == "__main__":
    main()
