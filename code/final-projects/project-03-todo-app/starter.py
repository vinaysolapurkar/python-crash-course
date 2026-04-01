"""
=============================================================
  PROJECT 3: TO-DO APP (CLI)
=============================================================

Build a full-featured to-do app using Object-Oriented
Programming! This project teaches you how to structure code
with classes and persist data to JSON files.

WHAT YOU'LL PRACTICE:
  - Classes and objects (OOP)
  - CRUD operations (Create, Read, Update, Delete)
  - File persistence with JSON
  - Date/time handling
  - List filtering and sorting
  - String formatting

REQUIREMENTS:
  1. Task class with attributes:
     - title, description, priority (high/medium/low)
     - completed (bool), created_date
  2. TodoApp class with methods:
     - add_task(), complete_task(), delete_task()
     - list_tasks(), filter_by_priority()
     - save_to_file(), load_from_file()
  3. JSON file persistence (tasks survive restarts)
  4. Priority display with visual indicators
  5. Menu-driven CLI interface

EXAMPLE OUTPUT:
  ====================================
    TO-DO APP
  ====================================
  1. Add Task
  2. List All Tasks
  3. Complete Task
  4. Delete Task
  5. Filter by Priority
  6. Exit

  > 2

  YOUR TASKS:
  ──────────────────────────────────
  1. [!!!] Buy groceries            [PENDING]
     Get milk, eggs, bread
     Created: 2026-03-28

  2. [!! ] Finish homework          [DONE]
     Math chapter 5
     Created: 2026-03-27

  3. [!  ] Clean room               [PENDING]
     Vacuum and dust
     Created: 2026-03-29
  ──────────────────────────────────

HINTS:
  - Use __str__ or __repr__ for nice Task display
  - json module can't serialize datetime directly -
    convert to string first!
  - Use a list inside TodoApp to hold Task objects
  - Each task could have an auto-incrementing ID

Good luck!
=============================================================
"""

import json
import os
from datetime import datetime


class Task:
    """Represents a single to-do task."""

    def __init__(self, title, description="", priority="medium"):
        # TODO: Initialize all attributes
        # - title, description, priority
        # - completed (default False)
        # - created_date (use datetime.now())
        # - id (you'll set this from TodoApp)
        pass

    def mark_complete(self):
        """Mark this task as completed."""
        # TODO: Set completed to True
        pass

    def to_dict(self):
        """Convert task to a dictionary for JSON saving."""
        # TODO: Return a dict with all attributes
        # Remember: datetime needs to be converted to string!
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary (loaded from JSON)."""
        # TODO: Create and return a Task from the dict data
        pass

    def __str__(self):
        """Nice string representation of the task."""
        # TODO: Return a formatted string showing the task
        pass


class TodoApp:
    """Manages a collection of tasks."""

    DATA_FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        # TODO: Load existing tasks from file
        pass

    def add_task(self, title, description="", priority="medium"):
        """Create and add a new task."""
        # TODO: Create task, assign ID, add to list, save
        pass

    def complete_task(self, task_id):
        """Mark a task as completed by its ID."""
        # TODO: Find task by ID and mark complete
        pass

    def delete_task(self, task_id):
        """Remove a task by its ID."""
        # TODO: Find and remove the task, save
        pass

    def list_tasks(self, show_completed=True):
        """Display all tasks."""
        # TODO: Print all tasks nicely formatted
        pass

    def filter_by_priority(self, priority):
        """Show only tasks with a given priority."""
        # TODO: Filter and display matching tasks
        pass

    def save_to_file(self):
        """Save all tasks to a JSON file."""
        # TODO: Convert tasks to dicts, write to JSON
        pass

    def load_from_file(self):
        """Load tasks from the JSON file."""
        # TODO: Read JSON, convert to Task objects
        pass


def main():
    """Main menu loop."""
    # TODO: Create TodoApp instance
    # TODO: Show menu, handle choices
    # TODO: Loop until exit
    pass


if __name__ == "__main__":
    main()
