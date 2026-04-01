"""
=============================================================
  PROJECT 3: TO-DO APP (CLI) - SOLUTION
=============================================================
  An OOP-based to-do manager with JSON persistence and
  priority-colored display.

  No external dependencies needed!

  Run:  python solution.py
=============================================================
"""

import json
import os
from datetime import datetime


# ── Priority Display Helpers ────────────────────────────────
# We use simple text indicators since not all terminals
# support color codes. (But we add ANSI colors as a bonus!)

PRIORITY_INDICATORS = {
    "high": "[!!!]",
    "medium": "[!! ]",
    "low": "[!  ]",
}

# ANSI color codes (works on most modern terminals)
COLORS = {
    "high": "\033[91m",     # Red
    "medium": "\033[93m",   # Yellow
    "low": "\033[92m",      # Green
    "done": "\033[90m",     # Gray
    "reset": "\033[0m",     # Reset
}


class Task:
    """Represents a single to-do task."""

    def __init__(self, title, description="", priority="medium"):
        self.id = None  # Set by TodoApp when added
        self.title = title
        self.description = description
        self.priority = priority.lower()
        self.completed = False
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_date": self.created_date,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task instance from a dictionary."""
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
        )
        task.id = data["id"]
        task.completed = data.get("completed", False)
        task.created_date = data.get("created_date", "Unknown")
        return task

    def __str__(self):
        """Formatted string with priority indicator and status."""
        indicator = PRIORITY_INDICATORS.get(self.priority, "[?  ]")
        status = "[DONE]" if self.completed else "[PENDING]"

        # Pick color based on status/priority
        if self.completed:
            color = COLORS["done"]
        else:
            color = COLORS.get(self.priority, "")
        reset = COLORS["reset"]

        lines = [
            f"{color}{self.id:>3}. {indicator} {self.title:<30} {status}{reset}",
        ]
        if self.description:
            lines.append(f"          {self.description}")
        lines.append(f"          Created: {self.created_date}")

        return "\n".join(lines)


class TodoApp:
    """Manages a collection of tasks with CRUD + persistence."""

    DATA_FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_from_file()

    # ── CRUD Operations ─────────────────────────────────────

    def add_task(self, title, description="", priority="medium"):
        """Create a new task and add it to the list."""
        task = Task(title, description, priority)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        self.save_to_file()
        return task

    def complete_task(self, task_id):
        """Mark a task as done. Returns True if found."""
        task = self._find_task(task_id)
        if task:
            task.mark_complete()
            self.save_to_file()
            return True
        return False

    def delete_task(self, task_id):
        """Delete a task by ID. Returns True if found."""
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_file()
            return True
        return False

    def _find_task(self, task_id):
        """Helper to find a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    # ── Display Methods ─────────────────────────────────────

    def list_tasks(self, show_completed=True):
        """Print all tasks (or only pending ones)."""
        if not self.tasks:
            print("\n  No tasks yet! Add one to get started.")
            return

        tasks_to_show = self.tasks
        if not show_completed:
            tasks_to_show = [t for t in self.tasks if not t.completed]

        if not tasks_to_show:
            print("\n  All tasks completed! Nice work!")
            return

        print()
        print("  YOUR TASKS:")
        print(f"  {'─' * 50}")
        for task in tasks_to_show:
            print(task)
            print()
        print(f"  {'─' * 50}")

        # Show summary
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.completed)
        print(f"  Total: {total} | Done: {done} | Pending: {total - done}")

    def filter_by_priority(self, priority):
        """Show only tasks matching the given priority."""
        matching = [t for t in self.tasks if t.priority == priority.lower()]

        if not matching:
            print(f"\n  No {priority} priority tasks found.")
            return

        print(f"\n  {priority.upper()} PRIORITY TASKS:")
        print(f"  {'─' * 50}")
        for task in matching:
            print(task)
            print()
        print(f"  {'─' * 50}")

    # ── Persistence ─────────────────────────────────────────

    def save_to_file(self):
        """Save all tasks to a JSON file."""
        data = {
            "next_id": self.next_id,
            "tasks": [task.to_dict() for task in self.tasks],
        }
        try:
            with open(self.DATA_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_from_file(self):
        """Load tasks from the JSON file."""
        if not os.path.exists(self.DATA_FILE):
            return

        try:
            with open(self.DATA_FILE, "r") as f:
                data = json.load(f)

            self.next_id = data.get("next_id", 1)
            self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load tasks: {e}")
            self.tasks = []


# ── CLI Interface ──────────────────────────────────────────

def get_priority():
    """Ask user to pick a priority level."""
    while True:
        print("  Priority: (h)igh, (m)edium, (l)ow")
        choice = input("  > ").strip().lower()
        if choice in ("h", "high"):
            return "high"
        elif choice in ("m", "medium", ""):
            return "medium"
        elif choice in ("l", "low"):
            return "low"
        print("  Please enter h, m, or l.")


def show_menu():
    """Display the main menu."""
    print()
    print("=" * 36)
    print("         TO-DO APP")
    print("=" * 36)
    print("  1. Add Task")
    print("  2. List All Tasks")
    print("  3. List Pending Only")
    print("  4. Complete Task")
    print("  5. Delete Task")
    print("  6. Filter by Priority")
    print("  7. Exit")
    print()


def main():
    """Main program loop."""
    app = TodoApp()

    print()
    print("*" * 36)
    print("  Welcome to your To-Do App!")
    print("  Stay organized, get stuff done.")
    print("*" * 36)

    while True:
        show_menu()
        choice = input("  Choose an option (1-7): ").strip()

        if choice == "1":
            # Add a new task
            print("\n  --- Add New Task ---")
            title = input("  Title: ").strip()
            if not title:
                print("  Task title cannot be empty!")
                continue
            description = input("  Description (optional): ").strip()
            priority = get_priority()

            task = app.add_task(title, description, priority)
            print(f"\n  Task #{task.id} added!")

        elif choice == "2":
            app.list_tasks(show_completed=True)

        elif choice == "3":
            app.list_tasks(show_completed=False)

        elif choice == "4":
            # Complete a task
            app.list_tasks()
            try:
                task_id = int(input("\n  Enter task ID to complete: ").strip())
                if app.complete_task(task_id):
                    print(f"  Task #{task_id} marked as done!")
                else:
                    print(f"  Task #{task_id} not found.")
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "5":
            # Delete a task
            app.list_tasks()
            try:
                task_id = int(input("\n  Enter task ID to delete: ").strip())
                confirm = input(f"  Delete task #{task_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    if app.delete_task(task_id):
                        print(f"  Task #{task_id} deleted.")
                    else:
                        print(f"  Task #{task_id} not found.")
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "6":
            # Filter by priority
            priority = get_priority()
            app.filter_by_priority(priority)

        elif choice == "7":
            print("\n  Goodbye! Keep crushing those tasks!")
            break

        else:
            print("  Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()
