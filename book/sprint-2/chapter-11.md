# Chapter 11: Modules & Packages: Standing on Giants' Shoulders

> **Sprint 2, Chapter 11** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Why build everything from scratch when thousands of developers have already built it for you? That would be like insisting on growing your own wheat every time you want a sandwich.

Python's real superpower isn't the language itself -- it's the ecosystem. There are tens of thousands of ready-made packages for everything from sending emails to training AI models. And you get to use them with a single line of code.

## Import Styles: Three Ways to Borrow Code

A **module** is just a Python file full of useful stuff. A **package** is a folder full of modules. When you `import` something, you're saying "hey, let me use that code."

```python
# Style 1: Import the whole module
import random
print(random.randint(1, 10))

# Style 2: Import specific things
from random import randint, choice
print(randint(1, 10))
print(choice(["pizza", "tacos", "sushi"]))

# Style 3: Import with an alias
import datetime as dt
today = dt.date.today()
print(today)
```

**Style 1** is the safest -- you always know where a function came from because it's prefixed with the module name. **Style 2** is convenient for things you use a lot. **Style 3** is great for modules with long names.

One style you should almost never use:

```python
# Don't do this (imports EVERYTHING into your namespace)
from random import *
```

This dumps every function from the module into your code, and you lose track of where things came from. It's like dumping every tool from the toolbox onto the floor. Sure, they're all "available," but good luck finding anything.

> **Remember When?** Remember how we used `random` in the username generator back in the early chapters? That was a module! You've been using modules this whole time. Now you'll understand what's actually happening behind the scenes.

## Standard Library Greatest Hits

Python comes with a massive standard library -- modules that are installed automatically with Python. No `pip install` needed. Here are the greatest hits.

### random -- When You Need Chaos

```python
import random

# Random integer between 1 and 100
print(random.randint(1, 100))

# Random choice from a list
foods = ["pizza", "tacos", "ramen", "sushi"]
print(random.choice(foods))

# Shuffle a list in place
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(cards)   # Different every time!

# Random float between 0 and 1
print(random.random())   # 0.7234... something

# Random sample (pick 3 without repeating)
lottery = random.sample(range(1, 50), 3)
print(lottery)   # e.g., [17, 42, 3]
```

### datetime -- Time Is on Your Side

```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)                           # 2026-04-01 14:30:00.123456
print(now.strftime("%B %d, %Y"))     # April 01, 2026
print(now.strftime("%I:%M %p"))      # 02:30 PM

# Just the date
today = date.today()
print(today)              # 2026-04-01
print(today.year)         # 2026
print(today.month)        # 4
print(today.weekday())    # 2 (Wednesday, 0=Monday)

# Date math with timedelta
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")

# How many days until New Year?
new_year = date(2027, 1, 1)
days_left = (new_year - today).days
print(f"Days until 2027: {days_left}")
```

### os -- Talk to Your Computer

```python
import os

# Current working directory
print(os.getcwd())

# List files in a directory
files = os.listdir(".")
print(files)

# Check if a file exists
if os.path.exists("data.txt"):
    print("File found!")
else:
    print("No such file.")

# Create a directory
os.makedirs("output/reports", exist_ok=True)

# Get environment variables
home = os.environ.get("HOME", "Not found")
print(f"Home directory: {home}")
```

### math -- For When You Need Real Math

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(144))   # 12.0
print(math.ceil(4.1))   # 5 (round up)
print(math.floor(4.9))  # 4 (round down)
print(math.factorial(5)) # 120 (5! = 5*4*3*2*1)

# Practical: calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance(0, 0, 3, 4))  # 5.0
```

### json -- The Internet's Favorite Format

JSON is how the internet passes data around. It looks almost exactly like Python dictionaries, which makes it really easy to work with.

```python
import json

# Python dictionary to JSON string
data = {"name": "Priya", "age": 22, "scores": [95, 87, 92]}
json_string = json.dumps(data, indent=2)
print(json_string)
# {
#   "name": "Priya",
#   "age": 22,
#   "scores": [95, 87, 92]
# }

# JSON string back to Python dictionary
parsed = json.loads(json_string)
print(parsed["name"])   # Priya
print(type(parsed))     # <class 'dict'>
```

We'll use JSON a lot more in Chapter 12 when we learn file handling. For now, just know that `json.dumps()` converts Python to JSON, and `json.loads()` converts JSON back to Python.

## pip install: Getting Packages from the Internet

The standard library is great, but the real magic is **PyPI** (Python Package Index) -- a massive repository of packages built by the community. Over 500,000 packages and counting.

To install a package, you use `pip`:

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install multiple packages
pip install requests flask pandas

# See what's installed
pip list

# Uninstall a package
pip uninstall requests
```

Let's install and use `requests`, the most popular package for making web requests:

```python
# After: pip install requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200
print(response.json())        # The response as a dictionary
```

Three lines of code to talk to the internet. That's the power of packages.

## Virtual Environments: Keeping Your Projects from Fighting

Here's the problem: you're working on Project A, which needs `requests` version 2.25. Then you start Project B, which needs `requests` version 2.31. If you install both globally, they'll conflict.

Virtual environments solve this. They're isolated Python environments for each project. Think of them like separate apartments -- each project gets its own space with its own furniture.

```bash
# Create a virtual environment
python -m venv myproject_env

# Activate it (Windows)
myproject_env\Scripts\activate

# Activate it (Mac/Linux)
source myproject_env/bin/activate

# Your terminal prompt changes to show you're in the venv
# (myproject_env) $

# Now pip install only affects THIS environment
pip install requests

# When you're done
deactivate
```

> **Pro Tip:** Always create a virtual environment for every new project. It takes 5 seconds and saves hours of debugging dependency conflicts. The standard workflow is: create folder, create venv, activate venv, pip install stuff, start coding.

### requirements.txt: Sharing Your Dependencies

When you share your project, other people need to know what packages to install. That's what `requirements.txt` is for.

```bash
# Save your current packages to a file
pip freeze > requirements.txt

# Someone else can install everything at once
pip install -r requirements.txt
```

A typical `requirements.txt` looks like:

```
requests==2.31.0
flask==3.0.0
pandas==2.1.0
```

It's like a grocery list for your project. "Here's everything you need to run this code."

## Creating Your Own Modules

You can also make your own modules. It's literally just a Python file.

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

```python
# main.py (same folder)
import helpers

print(helpers.greet("Priya"))   # Hello, Priya!
print(helpers.add(3, 5))        # 8
print(helpers.PI)               # 3.14159

# Or import specific things
from helpers import greet, PI
print(greet("Alex"))   # Hello, Alex!
```

That's it. Any `.py` file can be imported as a module. This is how you keep your code organized as projects grow.

## The if __name__ == "__main__" Pattern

You'll see this in almost every Python file. Here's what it does:

```python
# my_module.py
def calculate_tax(amount, rate=0.08):
    return amount * rate

# This code ONLY runs if you execute this file directly
# It does NOT run if someone imports this file
if __name__ == "__main__":
    # Test our function
    print(calculate_tax(100))    # 8.0
    print(calculate_tax(50, 0.1))  # 5.0
```

When you run `python my_module.py`, `__name__` is `"__main__"`, so the test code runs. When someone does `import my_module`, `__name__` is `"my_module"`, so the test code is skipped. It's a way to have test code that doesn't interfere with imports.

## Your Turn: Random Quote Generator from JSON

Create a file called `quotes.json` with at least 10 quotes:

```json
{
    "quotes": [
        {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
        {"text": "Two things are infinite: the universe and human stupidity.", "author": "Albert Einstein"},
        {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"}
    ]
}
```

Then write a Python script that:
1. Loads the quotes from the JSON file
2. Picks a random quote
3. Displays it nicely formatted
4. Asks if the user wants another quote (loop until they say no)
5. Bonus: Let the user filter quotes by author

You'll need: `json`, `random`, and file handling (sneak peek of Chapter 12 -- use `open("quotes.json") as f` and `json.load(f)`).

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-11-modules/`

## TL;DR

- **Modules** are Python files with reusable code. **Packages** are folders of modules.
- Three import styles: `import x`, `from x import y`, `import x as z`. Avoid `from x import *`.
- **Standard library** highlights: `random`, `datetime`, `os`, `math`, `json`.
- **pip** installs packages from PyPI: `pip install requests`.
- **Virtual environments** keep project dependencies isolated: `python -m venv myenv`.
- **requirements.txt** documents your dependencies for others.
- Any `.py` file is a module. Use `if __name__ == "__main__":` to separate importable code from test code.
- Don't reinvent the wheel. Someone probably already wrote a package for what you need.
