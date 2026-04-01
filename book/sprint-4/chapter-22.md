# Chapter 22: Databases with Python -- Storing Data for Real

> **Sprint 4, Chapter 22** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Every app you've ever used has a database behind it. Instagram stores your photos and likes. Spotify stores your playlists and listening history. Amazon stores your orders, payment info, and that wish list you've been building since 2015. Even the simplest to-do app needs to remember your tasks after you close it.

Up until now, we've been saving data to text files, CSV files, and JSON files. That works for small projects, but it falls apart fast. Try searching a million-row CSV file. Try making sure two users don't edit the same file at the same time. Try updating one field without rewriting the entire file.

Databases solve all of these problems. And Python comes with one built in.

## The Spreadsheet Analogy

CSV files are like spreadsheets. Databases are like spreadsheets with superpowers -- they can search millions of rows in milliseconds, enforce rules about what data is allowed, handle multiple users at once, and never lose your data if the power goes out.

Think of a database as a collection of spreadsheets (called **tables**), where each spreadsheet has defined columns (called **fields** or **columns**) and each row is a record. The difference is that databases have a powerful query language called **SQL** that lets you ask complex questions about your data instantly.

## SQLite: A Database in Your Pocket

There are many database systems -- PostgreSQL, MySQL, MongoDB, Oracle. They all require installing and running a separate server. Except one.

**SQLite** is a database that lives in a single file. No server needed. No installation. No configuration. And it's **built into Python**. Just `import sqlite3` and go.

Don't let the simplicity fool you -- SQLite handles databases up to 281 terabytes. It's used in every iPhone, every Android phone, every Chrome browser, and every Firefox browser. It's the most widely deployed database engine in the world.

```python
import sqlite3

# Create a database (or open it if it already exists)
conn = sqlite3.connect("my_app.db")

# Create a cursor (this is how you send SQL commands)
cursor = conn.cursor()

print("Database created!")

# Always close when done
conn.close()
```

That's it. You now have a database. The file `my_app.db` was created in your current directory.

## Creating Tables

Before you can store data, you need to create a **table** -- the structure that defines what your data looks like:

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()  # Save changes to disk
conn.close()
```

Let's decode that SQL:

| Part | Meaning |
|---|---|
| `CREATE TABLE IF NOT EXISTS` | Make a table (don't crash if it already exists) |
| `id INTEGER PRIMARY KEY AUTOINCREMENT` | Auto-numbering ID column (1, 2, 3...) |
| `name TEXT NOT NULL` | Text column, required (can't be empty) |
| `email TEXT UNIQUE NOT NULL` | Text column, required, must be unique |
| `age INTEGER` | Number column, optional |
| `DEFAULT CURRENT_TIMESTAMP` | Auto-fill with current date/time |

> **Don't Panic:** SQL looks like a foreign language at first, but it reads almost like English. "CREATE a TABLE called users with these columns." Once you see a few examples, you'll pick up the pattern fast.

## CRUD Operations: The Four Things You Do with Data

Every database interaction boils down to four operations. Developers call them **CRUD**:

- **C**reate (INSERT)
- **R**ead (SELECT)
- **U**pdate (UPDATE)
- **D**elete (DELETE)

Let's go through each one.

### Create: INSERT

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Insert a single record
cursor.execute("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", ("Alice", "alice@email.com", 28))

# Insert multiple records
users = [
    ("Bob", "bob@email.com", 34),
    ("Charlie", "charlie@email.com", 22),
    ("Diana", "diana@email.com", 31),
]
cursor.executemany("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", users)

conn.commit()
print(f"Inserted {cursor.rowcount} users")

conn.close()
```

See those `?` marks? Those are **placeholders**. This is critically important, so let's talk about it.

### NEVER Use f-strings in SQL (Security Warning)

This is one of the most important things in this entire book:

```python
# NEVER DO THIS -- SQL injection vulnerability!
name = input("Enter name: ")
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

# What if someone types: ' OR '1'='1
# The query becomes: SELECT * FROM users WHERE name = '' OR '1'='1'
# That returns EVERY user in the database!

# Or worse: '; DROP TABLE users; --
# That DELETES your entire table!
```

This is called **SQL injection**, and it's one of the most common security vulnerabilities in web applications. The fix is simple -- always use parameterized queries:

```python
# ALWAYS DO THIS -- safe!
name = input("Enter name: ")
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

The `?` placeholder tells SQLite to treat the value as data, not as SQL code. Problem solved. No exceptions. **Always use `?` placeholders.**

> **Wait, What?** "Is SQL injection really that dangerous?" Yes. In 2017, Equifax suffered a breach that exposed 147 million people's personal data due to a vulnerability that could have been prevented with parameterized queries. This isn't theoretical.

### Read: SELECT

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Get all users
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
for user in all_users:
    print(user)
# (1, 'Alice', 'alice@email.com', 28, '2024-01-15 10:30:00')
# (2, 'Bob', 'bob@email.com', 34, '2024-01-15 10:30:00')
# ...

# Get specific columns
cursor.execute("SELECT name, email FROM users")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

# Filter with WHERE
cursor.execute("SELECT * FROM users WHERE age > ?", (25,))
older_users = cursor.fetchall()

# Get just one record
cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@email.com",))
alice = cursor.fetchone()
print(alice)  # (1, 'Alice', 'alice@email.com', 28, '2024-01-15 10:30:00')

# Sort results
cursor.execute("SELECT * FROM users ORDER BY age DESC")

# Limit results
cursor.execute("SELECT * FROM users LIMIT 5")

conn.close()
```

Key fetch methods:
- `fetchone()` -- get the next single row (or `None` if no more rows)
- `fetchall()` -- get all remaining rows as a list of tuples
- `fetchmany(n)` -- get the next `n` rows

### Getting Named Columns with Row Factory

Tuples are fine, but accessing columns by index (`row[0]`, `row[1]`) is error-prone. Use `Row` factory to access columns by name:

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
conn.row_factory = sqlite3.Row  # Enable named access

cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
user = cursor.fetchone()

# Now you can use column names!
print(user["name"])    # Alice
print(user["email"])   # alice@email.com
print(user["age"])     # 28

conn.close()
```

Much better than remembering that name is index 1 and email is index 2.

### Update: UPDATE

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Update one user's age
cursor.execute("""
    UPDATE users SET age = ? WHERE email = ?
""", (29, "alice@email.com"))

# Update multiple fields
cursor.execute("""
    UPDATE users SET name = ?, age = ? WHERE id = ?
""", ("Alicia", 29, 1))

conn.commit()
print(f"Updated {cursor.rowcount} rows")

conn.close()
```

Always include a `WHERE` clause in your `UPDATE` statements. Without it, you'll update **every** row in the table. Ask me how I know.

### Delete: DELETE

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Delete a specific user
cursor.execute("DELETE FROM users WHERE id = ?", (3,))

conn.commit()
print(f"Deleted {cursor.rowcount} rows")

conn.close()
```

Same warning as `UPDATE` -- always use `WHERE`. `DELETE FROM users` without a `WHERE` clause deletes everything. Every row. Gone. No undo.

## Context Managers: The Right Way

Manually calling `conn.close()` is fragile -- if an error happens before that line, the connection stays open. Use a context manager instead:

```python
import sqlite3

def get_all_users():
    with sqlite3.connect("my_app.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY name")
        return [dict(row) for row in cursor.fetchall()]

# The connection auto-commits on success and auto-closes when done
users = get_all_users()
for user in users:
    print(user)
```

The `with` statement ensures the connection is properly handled -- it commits on success and rolls back on error.

> **Remember When?** We used context managers for file handling in Sprint 2 -- `with open("file.txt") as f:`. Same pattern here. Python loves context managers because they guarantee cleanup.

## Building a Complete Database Module

Let's build something real. Here's a clean database module for managing tasks:

```python
import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"

def get_connection():
    """Get a database connection with row factory."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Create the tasks table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'medium',
                completed INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

def add_task(title, description="", priority="medium"):
    """Add a new task."""
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (title, description, priority)
        )
        return cursor.lastrowid

def get_all_tasks(show_completed=False):
    """Get all tasks, optionally including completed ones."""
    with get_connection() as conn:
        if show_completed:
            query = "SELECT * FROM tasks ORDER BY created_at DESC"
            rows = conn.execute(query).fetchall()
        else:
            query = "SELECT * FROM tasks WHERE completed = 0 ORDER BY priority, created_at DESC"
            rows = conn.execute(query).fetchall()
        return [dict(row) for row in rows]

def complete_task(task_id):
    """Mark a task as completed."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
        return cursor.rowcount > 0

def delete_task(task_id):
    """Delete a task."""
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        return cursor.rowcount > 0

# Usage
if __name__ == "__main__":
    create_tables()
    
    # Add some tasks
    add_task("Learn SQLite", "Chapter 22 of Python Crash Course", "high")
    add_task("Build a project", "Sprint 4 checkpoint", "medium")
    add_task("Take a break", "You've earned it", "low")
    
    # List tasks
    print("Open tasks:")
    for task in get_all_tasks():
        print(f"  [{task['id']}] {task['title']} ({task['priority']})")
    
    # Complete a task
    complete_task(1)
    
    print("\nAfter completing task 1:")
    for task in get_all_tasks():
        print(f"  [{task['id']}] {task['title']} ({task['priority']})")
```

This is a pattern you'll use over and over: one function per operation, each with its own connection, each using parameterized queries.

## Brief ORM Intro: SQLAlchemy

Writing raw SQL is fine for learning and small projects, but bigger projects use an **ORM** (Object-Relational Mapper). An ORM lets you interact with your database using Python objects instead of SQL strings.

The most popular Python ORM is **SQLAlchemy**. Here's what the same task code looks like:

```python
# This is just a preview -- don't worry about memorizing this
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(String, default="medium")
    completed = Column(Boolean, default=False)

engine = create_engine("sqlite:///tasks.db")
Base.metadata.create_all(engine)

# Adding a task becomes:
with Session(engine) as session:
    task = Task(title="Learn SQLAlchemy", priority="high")
    session.add(task)
    session.commit()

# Querying becomes:
with Session(engine) as session:
    open_tasks = session.query(Task).filter_by(completed=False).all()
    for task in open_tasks:
        print(task.title)
```

See how you work with `Task` objects instead of writing SQL? That's the appeal of ORMs. You'll use them extensively in web development (Django has its own ORM, Flask uses SQLAlchemy).

For now, focus on raw SQL with `sqlite3`. Understanding SQL directly makes you a better developer, and the ORM will make more sense later.

## Your Turn: Convert Expense Tracker to SQLite

> **Remember When?** The expense tracker from Sprint 2 used CSV files. Let's upgrade it to a real database.

**Challenge:** Build an expense tracker with SQLite that can:

1. Create an `expenses` table (id, amount, category, description, date)
2. Add expenses
3. List all expenses
4. Show totals by category
5. Delete expenses

Here's the schema to get you started:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")
```

And here's the category summary query (a taste of SQL's power):

```python
cursor.execute("""
    SELECT category, 
           COUNT(*) as count, 
           SUM(amount) as total,
           AVG(amount) as average
    FROM expenses 
    GROUP BY category 
    ORDER BY total DESC
""")
```

Try doing *that* with a CSV file.

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-22-databases/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-22-databases/)

## TL;DR

| Concept | What It Does |
|---|---|
| SQLite | File-based database, built into Python |
| `sqlite3.connect("file.db")` | Create/open a database |
| `cursor.execute(sql, params)` | Run a SQL command with safe parameters |
| `?` placeholders | Prevent SQL injection (ALWAYS use these) |
| `fetchone()` / `fetchall()` | Get query results |
| `conn.commit()` | Save changes to disk |
| `conn.row_factory = sqlite3.Row` | Access columns by name instead of index |
| `with sqlite3.connect() as conn:` | Auto-commit and auto-close |
| CRUD | Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE) |

**The one-sentence version:** Use `sqlite3` to store data in a real database file, always use `?` placeholders to prevent SQL injection, and use context managers for clean connections.

Next up: Web Scraping -- where we teach Python to read websites and extract data.
