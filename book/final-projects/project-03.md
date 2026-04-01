# Project 3: To-Do App (CLI)

> **Difficulty:** 2/5 | **Time:** ~2 hours | **Skills:** OOP, CRUD, JSON persistence
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-03-todo-app/

## What You'll Build

A full-featured command-line to-do application built with object-oriented programming. You'll create a `Task` class, implement all four CRUD operations (Create, Read, Update, Delete), add priority levels and filtering, and persist everything to a JSON file.

Here's what it looks like when running:

```
=== TO-DO APP ===

1. Add Task       4. Complete Task
2. View Tasks     5. Delete Task
3. Edit Task      6. Exit

Choice: 2

-- Your Tasks --
  ID  Priority  Status      Task                    Due Date
  1   [!!!]     [ ]         Buy groceries           2026-04-05
  2   [!! ]     [x]         Finish Python project   2026-04-01
  3   [!  ]     [ ]         Call dentist             2026-04-10

Showing 3 task(s). Filter: all
```

## Skills You'll Use

- Classes and OOP (learned in Chapter 9)
- JSON file I/O (learned in Chapter 7)
- List comprehensions (learned in Chapter 4)
- Error handling (learned in Chapter 8)
- String formatting (learned in Chapter 2)
- Functions and program design (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Define the Task Class

This is the core of your application. Each task is an object with properties like title, priority, completion status, and a due date. We include methods to convert the task to and from a dictionary for JSON storage.

```python
# todo_app.py

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


class Task:
    """Represents a single to-do task."""

    # Class variable to track the next available ID
    _next_id = 1

    def __init__(self, title, priority="medium", due_date=None,
                 completed=False, task_id=None):
        if task_id is not None:
            self.id = task_id
            # Keep _next_id ahead of any loaded IDs
            Task._next_id = max(Task._next_id, task_id + 1)
        else:
            self.id = Task._next_id
            Task._next_id += 1

        self.title = title
        self.priority = priority  # "high", "medium", "low"
        self.due_date = due_date  # "YYYY-MM-DD" string or None
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        """Convert task to a dictionary for JSON storage."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary (loaded from JSON)."""
        task = cls(
            title=data["title"],
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date"),
            completed=data.get("completed", False),
            task_id=data["id"]
        )
        task.created_at = data.get("created_at", "Unknown")
        return task

    def priority_display(self):
        """Return a visual priority indicator."""
        indicators = {"high": "[!!!]", "medium": "[!! ]", "low": "[!  ]"}
        return indicators.get(self.priority, "[?  ]")

    def status_display(self):
        """Return a checkbox-style status."""
        return "[x]" if self.completed else "[ ]"

    def __str__(self):
        status = self.status_display()
        priority = self.priority_display()
        due = self.due_date or "No date"
        return (f"  {self.id:<4}{priority:<10}{status:<12}"
                f"{self.title:<24}{due}")
```

### Step 2: Build the TaskManager Class

The `TaskManager` handles the collection of tasks, including loading, saving, and all CRUD operations. This keeps your data management logic organized in one place.

```python
class TaskManager:
    """Manages a collection of tasks with CRUD operations."""

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if not os.path.exists(self.data_file):
            self.tasks = []
            return

        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load tasks ({e}). Starting fresh.")
            self.tasks = []

    def save_tasks(self):
        """Save all tasks to the JSON file."""
        data = [task.to_dict() for task in self.tasks]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def add_task(self, title, priority="medium", due_date=None):
        """Create and add a new task."""
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_task(self, task_id):
        """Find a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, **kwargs):
        """Update task properties."""
        task = self.get_task(task_id)
        if task is None:
            return None

        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

        self.save_tasks()
        return task

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False

    def complete_task(self, task_id):
        """Mark a task as completed."""
        return self.update_task(task_id, completed=True)

    def get_filtered(self, filter_type="all"):
        """Return tasks filtered by status or priority."""
        if filter_type == "active":
            return [t for t in self.tasks if not t.completed]
        elif filter_type == "completed":
            return [t for t in self.tasks if t.completed]
        elif filter_type == "high":
            return [t for t in self.tasks if t.priority == "high"]
        return self.tasks

    def get_sorted(self, tasks=None, sort_by="priority"):
        """Sort tasks by priority or due date."""
        if tasks is None:
            tasks = self.tasks

        if sort_by == "priority":
            order = {"high": 0, "medium": 1, "low": 2}
            return sorted(tasks, key=lambda t: order.get(t.priority, 1))
        elif sort_by == "due_date":
            return sorted(tasks,
                          key=lambda t: t.due_date or "9999-12-31")
        elif sort_by == "id":
            return sorted(tasks, key=lambda t: t.id)
        return tasks
```

### Step 3: Build the User Interface Functions

Now create the interactive functions that collect user input and call the TaskManager methods.

```python
def get_priority():
    """Ask the user to choose a priority level."""
    print("  Priority: 1=High, 2=Medium, 3=Low")
    mapping = {"1": "high", "2": "medium", "3": "low"}
    while True:
        choice = input("  Choose (1/2/3): ").strip()
        if choice in mapping:
            return mapping[choice]
        print("  Please enter 1, 2, or 3.")


def get_due_date():
    """Ask the user for an optional due date."""
    while True:
        date_str = input("  Due date (YYYY-MM-DD, or press Enter to skip): ").strip()
        if not date_str:
            return None
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("  Invalid date format. Use YYYY-MM-DD.")


def get_task_id(prompt="Task ID: "):
    """Get a valid task ID from the user."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Please enter a number.")


def display_tasks(tasks, filter_name="all"):
    """Display tasks in a formatted table."""
    if not tasks:
        print("\n  No tasks found.")
        return

    print(f"\n  {'ID':<4}{'Priority':<10}{'Status':<12}"
          f"{'Task':<24}{'Due Date'}")
    print("  " + "-" * 64)
    for task in tasks:
        print(task)
    print(f"\n  Showing {len(tasks)} task(s). Filter: {filter_name}")
```

### Step 4: Implement Each Menu Action

```python
def add_task_ui(manager):
    """Interactive UI for adding a task."""
    print("\n-- Add Task --")
    title = input("  Task title: ").strip()
    if not title:
        print("  Title cannot be empty.")
        return

    priority = get_priority()
    due_date = get_due_date()

    task = manager.add_task(title, priority, due_date)
    print(f"\n  Added task #{task.id}: {task.title}")


def view_tasks_ui(manager):
    """Interactive UI for viewing tasks with filter/sort options."""
    print("\n-- Your Tasks --")
    print("  Filter: 1=All  2=Active  3=Completed  4=High Priority")
    choice = input("  Choose (or Enter for all): ").strip()

    filter_map = {"1": "all", "2": "active", "3": "completed", "4": "high"}
    filter_type = filter_map.get(choice, "all")

    tasks = manager.get_filtered(filter_type)
    tasks = manager.get_sorted(tasks, sort_by="priority")
    display_tasks(tasks, filter_type)


def edit_task_ui(manager):
    """Interactive UI for editing a task."""
    print("\n-- Edit Task --")
    display_tasks(manager.tasks)
    task_id = get_task_id("\n  Task ID to edit: ")

    task = manager.get_task(task_id)
    if not task:
        print(f"  Task #{task_id} not found.")
        return

    print(f"  Editing: {task.title}")
    new_title = input(f"  New title (Enter to keep '{task.title}'): ").strip()
    if new_title:
        manager.update_task(task_id, title=new_title)

    change_priority = input("  Change priority? (y/n): ").strip().lower()
    if change_priority == "y":
        new_priority = get_priority()
        manager.update_task(task_id, priority=new_priority)

    change_date = input("  Change due date? (y/n): ").strip().lower()
    if change_date == "y":
        new_date = get_due_date()
        manager.update_task(task_id, due_date=new_date)

    print("  Task updated!")


def complete_task_ui(manager):
    """Interactive UI for completing a task."""
    print("\n-- Complete Task --")
    active = [t for t in manager.tasks if not t.completed]
    display_tasks(active, "active")

    if not active:
        return

    task_id = get_task_id("\n  Task ID to complete: ")
    result = manager.complete_task(task_id)
    if result:
        print(f"  Task #{task_id} marked as complete!")
    else:
        print(f"  Task #{task_id} not found.")


def delete_task_ui(manager):
    """Interactive UI for deleting a task."""
    print("\n-- Delete Task --")
    display_tasks(manager.tasks)

    if not manager.tasks:
        return

    task_id = get_task_id("\n  Task ID to delete: ")
    task = manager.get_task(task_id)
    if not task:
        print(f"  Task #{task_id} not found.")
        return

    confirm = input(f"  Delete '{task.title}'? (y/n): ").strip().lower()
    if confirm == "y":
        manager.delete_task(task_id)
        print("  Task deleted.")
    else:
        print("  Cancelled.")
```

### Step 5: Build the Main Menu

```python
def main():
    """Main application loop."""
    print("=" * 35)
    print("       TO-DO APP")
    print("=" * 35)

    manager = TaskManager()
    print(f"Loaded {len(manager.tasks)} task(s).")

    while True:
        print("\n1. Add Task       4. Complete Task")
        print("2. View Tasks     5. Delete Task")
        print("3. Edit Task      6. Exit")

        choice = input("\nChoice: ").strip()

        actions = {
            "1": lambda: add_task_ui(manager),
            "2": lambda: view_tasks_ui(manager),
            "3": lambda: edit_task_ui(manager),
            "4": lambda: complete_task_ui(manager),
            "5": lambda: delete_task_ui(manager),
        }

        if choice == "6":
            print("\nGoodbye! Stay productive.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Subtasks:** Add the ability to create subtasks under a parent task. A parent task automatically completes when all its subtasks are done. This will stretch your OOP skills with composition.

2. **Color-coded output:** Use ANSI escape codes to make high-priority tasks appear in red, completed tasks in green, and overdue tasks flash a warning. (Search for "ANSI color codes Python" to learn how.)

3. **Undo/Redo:** Implement an undo stack that lets the user reverse their last action. Every time a task is added, deleted, or modified, push the previous state onto the stack.

## Portfolio Tips

This project demonstrates OOP, data persistence, and clean architecture - three things every employer cares about. When presenting it:

- **GitHub:** Structure your repo cleanly. Put the code in a `/src` folder, include sample data, and write a README that shows the app in action.
- **Resume:** "Built an OOP-based CLI task manager with CRUD operations, JSON persistence, and priority-based filtering using Python."
- **Interview talking point:** Explain your class design decisions. Why did you separate `Task` from `TaskManager`? How does `to_dict` / `from_dict` enable persistence? This shows you think about software architecture, not just "making it work."
