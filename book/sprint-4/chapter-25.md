# Chapter 25: Type Hints, Linting & Clean Code

> **Sprint 4, Chapter 25** | **Estimated Time: 15-20 minutes** | **Difficulty: Advanced**

## Why Should I Care?

You can write Python that works but is impossible to read. You can write functions where nobody - including you in two weeks - knows what types the parameters should be. You can write code that's inconsistently formatted, full of unused imports, and structured like a bowl of spaghetti.

And it'll still run. Python doesn't care.

But your teammates care. Your future self cares. The hiring manager reviewing your GitHub portfolio cares. Code readability, team collaboration, catching bugs early, and getting hired - clean code matters for all of these.

This chapter gives you the tools that professional developers use to write code that's not just correct, but *clear*.

## The Kitchen Analogy

Writing clean code is like keeping a clean kitchen. You CAN cook in a messy kitchen. The food tastes the same. But everything takes longer - you can't find the spatula, the cutting board is buried under dishes, and you accidentally grab the sugar instead of the salt.

A clean kitchen means you cook faster, make fewer mistakes, and other people can jump in and help.

Clean code is the same. Variables have clear names. Functions do one thing. Types are documented. Formatting is consistent. Anyone can read it, understand it, and modify it.

## Type Hints: Helping Your Future Self

Python is dynamically typed - you don't have to declare what type a variable is. That's great for quick scripts. But in larger projects, it becomes a problem:

```python
# What does this function expect? What does it return?
def process(data, flag):
    ...
```

Is `data` a string? A list? A dictionary? Is `flag` a boolean? An integer? A string? You'd have to read the entire function to find out.

**Type hints** fix this:

```python
def process(data: list[str], flag: bool) -> dict[str, int]:
    ...
```

Now you know instantly: `data` is a list of strings, `flag` is a boolean, and it returns a dictionary mapping strings to integers. No guessing.

### Basic Type Hints

```python
# Variable annotations
name: str = "Alice"
age: int = 28
price: float = 19.99
active: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_valid(email: str) -> bool:
    return "@" in email
```

The syntax is simple: `variable: type` for variables, `parameter: type` for function parameters, and `-> type` for return values.

### Collection Types

```python
# Lists, dicts, sets, tuples
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def count_words(text: str) -> dict[str, int]:
    words = text.split()
    return {word: words.count(word) for word in set(words)}

def unique_names(names: list[str]) -> set[str]:
    return set(names)

def get_point() -> tuple[float, float]:
    return (3.14, 2.71)
```

### Optional and Union Types

```python
from typing import Optional

# This parameter might be None
def find_user(user_id: int) -> Optional[dict]:
    """Returns user dict or None if not found."""
    # ...
    return None

# A parameter that accepts multiple types (Python 3.10+)
def display(value: str | int) -> str:
    return str(value)

# For older Python versions
from typing import Union
def display(value: Union[str, int]) -> str:
    return str(value)
```

### Type Hints for Complex Functions

```python
from typing import Callable, Any

# Function that takes a callback
def retry(func: Callable, max_attempts: int = 3) -> Any:
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception:
            if attempt == max_attempts - 1:
                raise

# Function with default values
def create_user(
    name: str,
    email: str,
    age: int = 0,
    active: bool = True
) -> dict[str, Any]:
    return {
        "name": name,
        "email": email,
        "age": age,
        "active": active
    }
```

### Important: Type Hints Don't Enforce Anything

Here's the thing - Python **ignores** type hints at runtime. They're documentation, not enforcement:

```python
def add(a: int, b: int) -> int:
    return a + b

# This "works" even though we pass strings
print(add("hello", " world"))  # "hello world"
```

No error. Python doesn't check types at runtime. Type hints are for **humans** and **tools** (like mypy, which we'll cover next).

> **Wait, What?** "If Python ignores them, why bother?" Because *you* don't ignore them. Your IDE doesn't ignore them. Your linter doesn't ignore them. Type hints catch bugs in your editor before you even run the code. They're like lane markings on a road - your car can cross them, but they tell you where you should be.

## mypy: The Type Checker

**mypy** is a tool that reads your type hints and checks them *before* you run your code. It catches type-related bugs at development time.

```bash
pip install mypy
```

Create a file called `calculator.py`:

```python
def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b

# These lines have type errors
result: str = add(1, 2)          # Bug: int assigned to str
divide("10", 3)                   # Bug: str passed where float expected
```

Run mypy:

```bash
mypy calculator.py
```

Output:
```
calculator.py:8: error: Incompatible types in assignment
    (expression has type "int", variable has type "str")
calculator.py:9: error: Argument 1 to "divide" has incompatible type "str";
    expected "float"
Found 2 errors in 1 file
```

mypy found both bugs without running the code. In a large project, this catches errors that would otherwise slip through to production.

## PEP 8: Python's Style Guide

**PEP 8** is the official style guide for Python code. It was written by Guido van Rossum (Python's creator). Yes, there's an official opinion on whether to use tabs or spaces. (Spaces. Always spaces. Four of them.)

The key PEP 8 rules:

```python
# -- NAMING --

# Variables and functions: snake_case
user_name = "Alice"
def calculate_total():
    pass

# Classes: PascalCase
class ShoppingCart:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DATABASE_URL = "sqlite:///app.db"

# -- SPACING --

# Two blank lines before top-level definitions
def function_one():
    pass


def function_two():
    pass


class MyClass:
    # One blank line between methods
    def method_one(self):
        pass
    
    def method_two(self):
        pass

# -- LINE LENGTH --

# Keep lines under 79 characters (or 88 with black)
# Break long lines like this:
result = (first_value
          + second_value
          + third_value)

# Or for function calls:
user = create_user(
    name="Alice",
    email="alice@example.com",
    age=28
)

# -- IMPORTS --

# Standard library first, then third-party, then local
import os
import sys

import requests
from bs4 import BeautifulSoup

from my_project.utils import helper
```

> **Fun Fact:** PEP stands for "Python Enhancement Proposal." PEP 8 was written in 2001 and has been the de facto standard ever since. The tabs-vs-spaces debate is officially settled in Python: four spaces. And yes, there was a whole episode of *Silicon Valley* about this.

## black: The Code Formatter That Ends All Arguments

Arguing about code formatting is a waste of time. **black** formats your code automatically, and it's opinionated - it makes the decisions so you don't have to.

```bash
pip install black
```

Before black:

```python
# Messy formatting
x={'name':'Alice','age':28,'scores':[90,85,92]}
def   calculate(  a,b,  c  ):
    return(a+b  *c)
result=calculate(1,2,    3)
if result>5 :
        print(  "big")
```

Run black:

```bash
black messy_code.py
```

After black:

```python
# Clean, consistent formatting
x = {"name": "Alice", "age": 28, "scores": [90, 85, 92]}


def calculate(a, b, c):
    return a + b * c


result = calculate(1, 2, 3)
if result > 5:
    print("big")
```

That's it. No configuration needed. No arguments about style. black decides, and everyone on the team uses the same format.

You can also check without modifying:

```bash
black -check my_file.py     # Check without changing
black -diff my_file.py      # Show what would change
black my_project/             # Format an entire directory
```

Most teams add black to their CI/CD pipeline so code is automatically formatted on every commit.

## pylint and flake8: The Grammar Checkers for Code

**Linters** analyze your code for potential errors, style violations, and suspicious patterns - like a grammar checker for code.

### flake8 (Lighter, Faster)

```bash
pip install flake8
```

```python
# sample.py
import os
import sys
import json  # Unused import

def bad_function(x,y):
    result = x+y
    unused_variable = 42
    if result == True:
        print ("hello")
    return result
```

```bash
flake8 sample.py
```

Output:
```
sample.py:3:1: F401 'json' imported but unused
sample.py:5:20: E231 missing whitespace after ','
sample.py:6:14: E225 missing whitespace around operator
sample.py:7:5: F841 local variable 'unused_variable' is assigned but never used
sample.py:8:8: E712 comparison to True should be 'if result:' or 'if result is True:'
sample.py:9:14: E211 whitespace before '('
```

Every issue identified with a specific code and line number.

### pylint (More Thorough, More Opinionated)

```bash
pip install pylint
```

pylint is stricter and catches more issues, including missing docstrings, too many arguments, and code complexity:

```bash
pylint sample.py
```

pylint gives your code a score out of 10. Aim for 8+.

### Which One Should You Use?

- **flake8** for quick style checks (most projects use this)
- **pylint** for thorough analysis (useful but noisy)
- **black** + **flake8** is the most common combination

## Before and After: Clean Code in Practice

Let's see a real transformation. Here's a function written quickly without thinking about cleanliness:

### Before

```python
def p(d):
    t = 0
    for i in d:
        t = t + i['a'] * (1 + i['r'])
    return t

data = [{'a': 100, 'r': 0.08}, {'a': 250, 'r': 0.1}, {'a': 50, 'r': 0.05}]
print(p(data))
```

What does this do? Who knows. Let's clean it up.

### After

```python
def calculate_total_with_tax(items: list[dict[str, float]]) -> float:
    """Calculate the total price of items including tax.
    
    Args:
        items: List of dicts with 'amount' and 'tax_rate' keys.
        
    Returns:
        Total price including tax for all items.
    """
    total = 0.0
    for item in items:
        total += item["amount"] * (1 + item["tax_rate"])
    return round(total, 2)


items = [
    {"amount": 100.00, "tax_rate": 0.08},
    {"amount": 250.00, "tax_rate": 0.10},
    {"amount": 50.00, "tax_rate": 0.05},
]

total = calculate_total_with_tax(items)
print(f"Total with tax: ${total}")
```

Same logic. Completely different readability. Changes made:
- Function name describes what it does
- Parameter names are descriptive
- Type hints tell you what goes in and what comes out
- Docstring explains the purpose
- Variable names have meaning (`total` not `t`, `item` not `i`)
- Output is formatted nicely

### Another Before and After

```python
# Before: A mess
def check(u, p):
    if len(p) < 8:
        return False
    if u == "":
        return False
    for c in "!@#$%":
        if c in p:
            return True
    return False
```

```python
# After: Professional
def validate_credentials(username: str, password: str) -> bool:
    """Check if username and password meet security requirements.
    
    Requirements:
        - Username must not be empty
        - Password must be at least 8 characters
        - Password must contain at least one special character
    """
    SPECIAL_CHARACTERS = "!@#$%"
    
    if not username:
        return False
    
    if len(password) < 8:
        return False
    
    has_special = any(char in SPECIAL_CHARACTERS for char in password)
    return has_special
```

## Putting It All Together: Your Clean Code Workflow

Here's the workflow professional developers use:

1. **Write code** with type hints and descriptive names
2. **Format** with black (`black my_file.py`)
3. **Lint** with flake8 (`flake8 my_file.py`)
4. **Type check** with mypy (`mypy my_file.py`)
5. **Test** with pytest (`pytest`)

Or automate it all. Most projects use a `Makefile` or scripts:

```bash
# Run everything at once
black src/ tests/
flake8 src/ tests/
mypy src/
pytest
```

Many developers configure their IDE to run black on save and show flake8/mypy warnings inline. VS Code does this beautifully with the Python extension.

## IDE Integration: Let Your Editor Help

If you use VS Code (and you should), install the Python extension and add this to your settings:

```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true
}
```

Now your code formats itself every time you save, and type errors show up as red squiggly lines. It's like having a co-pilot who catches your mistakes in real time.

## Your Turn: Add Type Hints and Linting to Expense Tracker

**Challenge:** Take the expense tracker from Chapter 22 and make it professional:

1. Add type hints to every function
2. Add docstrings to every function
3. Run black to format the code
4. Run flake8 and fix all warnings
5. Run mypy and fix all type errors

Here's what the refactored functions should look like:

```python
import sqlite3
from typing import Optional

DB_NAME: str = "expenses.db"


def add_expense(
    amount: float,
    category: str,
    description: str = ""
) -> int:
    """Add a new expense and return its ID.
    
    Args:
        amount: The expense amount (must be positive).
        category: Expense category (e.g., 'food', 'transport').
        description: Optional description of the expense.
        
    Returns:
        The ID of the newly created expense.
        
    Raises:
        ValueError: If amount is not positive.
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (amount, category, description),
        )
        return cursor.lastrowid


def get_expenses(
    category: Optional[str] = None,
    limit: int = 50
) -> list[dict[str, object]]:
    """Retrieve expenses, optionally filtered by category.
    
    Args:
        category: If provided, only return expenses in this category.
        limit: Maximum number of expenses to return.
        
    Returns:
        List of expense dictionaries.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        if category:
            rows = conn.execute(
                "SELECT * FROM expenses WHERE category = ? ORDER BY date DESC LIMIT ?",
                (category, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM expenses ORDER BY date DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(row) for row in rows]
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-25-clean-code/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-25-clean-code/)

## TL;DR

| Tool | What It Does |
|--|--|
| Type hints (`x: int`) | Document what types your code expects |
| mypy | Check type hints for errors without running code |
| PEP 8 | Python's official style guide |
| black | Auto-format code (no configuration needed) |
| flake8 | Check for style violations and common errors |
| pylint | Thorough code analysis (more detailed than flake8) |

**The one-sentence version:** Use type hints to document your code's expectations, black to format it consistently, flake8 to catch mistakes, and mypy to verify types - these tools turn "code that works" into "code that's professional."

Next up: The Sprint 4 Checkpoint project - where you put everything from this sprint together into a real application.
