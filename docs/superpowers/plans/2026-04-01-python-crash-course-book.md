# Python Crash Course Book — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete Kindle-ready Python crash course book with companion GitHub repo — 32 chapters across 5 sprints, 10 progressive projects, ADHD-friendly format, funny and engaging tone, covering basics through AI.

**Architecture:** GitHub repo is built first with all code examples, exercises, and project starters/solutions organized by sprint. Then book chapters are written as Markdown files referencing the repo. Each chapter is a standalone Markdown file. Final assembly compiles all chapters into a single Kindle-ready manuscript.

**Tech Stack:** Python 3.12+, Markdown for book content, Git/GitHub for code repo

---

## File Structure

```
python-crash-course/
├── book/
│   ├── front-matter/
│   │   ├── title-page.md
│   │   ├── copyright.md
│   │   ├── dedication.md
│   │   ├── how-to-use-this-book.md
│   │   └── what-you-need.md
│   ├── sprint-1/
│   │   ├── sprint-1-intro.md
│   │   ├── chapter-01.md through chapter-08.md
│   │   └── sprint-1-checkpoint.md
│   ├── sprint-2/
│   │   ├── sprint-2-intro.md
│   │   ├── chapter-09.md through chapter-14.md
│   │   └── sprint-2-checkpoint.md
│   ├── sprint-3/
│   │   ├── sprint-3-intro.md
│   │   ├── chapter-15.md through chapter-18.md
│   │   └── sprint-3-checkpoint.md
│   ├── sprint-4/
│   │   ├── sprint-4-intro.md
│   │   ├── chapter-19.md through chapter-25.md
│   │   └── sprint-4-checkpoint.md
│   ├── sprint-5/
│   │   ├── sprint-5-intro.md
│   │   ├── chapter-26.md through chapter-32.md
│   │   └── sprint-5-checkpoint.md
│   ├── final-projects/
│   │   ├── final-zone-intro.md
│   │   └── project-01.md through project-10.md
│   ├── back-matter/
│   │   ├── appendix-a-cheat-sheet.md
│   │   ├── appendix-b-common-errors.md
│   │   ├── appendix-c-what-next.md
│   │   ├── appendix-d-resources.md
│   │   └── about-author.md
│   └── manuscript.md  (final assembled book)
├── code/
│   ├── README.md
│   ├── requirements.txt
│   ├── sprint-1-basics/
│   │   ├── chapter-01-why-python/
│   │   │   └── hello.py
│   │   ├── chapter-02-variables/
│   │   │   ├── examples.py
│   │   │   └── exercises/
│   │   │       ├── your_turn.py
│   │   │       └── solution.py
│   │   ├── ... (chapters 03-08 same pattern)
│   │   └── checkpoint-mad-libs/
│   │       ├── starter.py
│   │       └── solution.py
│   ├── sprint-2-intermediate/
│   │   ├── ... (chapters 09-14 same pattern)
│   │   └── checkpoint-expense-tracker/
│   │       ├── starter.py
│   │       └── solution.py
│   ├── sprint-3-oop/
│   │   ├── ... (chapters 15-18 same pattern)
│   │   └── checkpoint-library-system/
│   │       ├── starter.py
│   │       └── solution.py
│   ├── sprint-4-pro/
│   │   ├── ... (chapters 19-25 same pattern)
│   │   └── checkpoint-job-scraper/
│   │       ├── starter.py
│   │       └── solution.py
│   ├── sprint-5-ai/
│   │   ├── ... (chapters 26-32 same pattern)
│   │   └── checkpoint-resume-analyzer/
│   │       ├── starter.py
│   │       └── solution.py
│   └── final-projects/
│       ├── project-01-quiz-game/
│       │   ├── starter.py
│       │   └── solution.py
│       ├── ... (projects 02-10 same pattern)
│       └── project-10-ai-study-buddy/
│           ├── starter.py
│           └── solution.py
└── docs/
    └── superpowers/
        ├── specs/
        │   └── 2026-04-01-python-crash-course-book-design.md
        └── plans/
            └── 2026-04-01-python-crash-course-book.md
```

---

## Phase 0: Project Setup & GitHub Repo Scaffolding

### Task 1: Initialize Git Repo and Project Structure

**Files:**
- Create: `code/README.md`
- Create: `code/requirements.txt`
- Create: `code/.gitignore`

- [ ] **Step 1: Initialize git repo**

```bash
cd /c/Users/vinay/projects/python-crash-course
git init
```

- [ ] **Step 2: Create .gitignore**

Create file `code/.gitignore`:
```
__pycache__/
*.pyc
.env
venv/
.venv/
*.egg-info/
dist/
build/
.pytest_cache/
*.db
*.sqlite3
```

- [ ] **Step 3: Create requirements.txt**

Create file `code/requirements.txt`:
```
# Sprint 1-3: No external packages needed (stdlib only)

# Sprint 4
requests==2.31.0
beautifulsoup4==4.12.3
pytest==8.1.1
sqlalchemy==2.0.29
black==24.3.0
mypy==1.9.0

# Sprint 5
numpy==1.26.4
pandas==2.2.1
matplotlib==3.8.4
seaborn==0.13.2
plotly==5.20.0
scikit-learn==1.4.1
openai==1.14.3
google-generativeai==0.4.1
langchain==0.1.13
langchain-openai==0.1.1
chromadb==0.4.24
selenium==4.18.1
flask==3.0.2
```

- [ ] **Step 4: Create repo README.md**

Create file `code/README.md`:
```markdown
# 🐍 Python Crash Course: From Zero to AI

### The companion code repository for *Python Crash Course: From Zero to AI — The Fun, ADHD-Friendly Guide to Python Programming*

---

## 📖 How to Use This Repo

This repo contains **every code example, exercise, and project** from the book.

### Structure

| Folder | What's Inside |
|--------|--------------|
| `sprint-1-basics/` | Chapters 1-8: Variables, strings, loops, lists |
| `sprint-2-intermediate/` | Chapters 9-14: Dictionaries, functions, files, errors |
| `sprint-3-oop/` | Chapters 15-18: Classes, inheritance, design patterns |
| `sprint-4-pro/` | Chapters 19-25: Decorators, APIs, databases, testing |
| `sprint-5-ai/` | Chapters 26-32: NumPy, pandas, ML, AI APIs, LangChain |
| `final-projects/` | 10 progressive portfolio projects |

### Each Chapter Folder Contains

- `examples.py` — All code examples from the chapter
- `exercises/your_turn.py` — The "Your Turn" exercise starter
- `exercises/solution.py` — The complete solution

### Getting Started

1. **Clone this repo:**
   ```bash
   git clone https://github.com/<your-username>/python-crash-course.git
   cd python-crash-course
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies (when you reach Sprint 4+):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to your current chapter and start coding!**

---

## 🚀 Sprint Checkpoint Projects

| Sprint | Project | Skills Used |
|--------|---------|-------------|
| 1 | Mad Libs Generator | strings, input, lists, loops, conditions |
| 2 | Expense Tracker | CSV, functions, dictionaries, error handling |
| 3 | Library Management System | OOP, file persistence |
| 4 | Job Listing Scraper | scraping, SQLite, decorators, testing |
| 5 | AI Resume Analyzer | pandas, ML, OpenAI API, email |

## 🏆 Final Projects (Portfolio-Ready)

1. Quiz Game
2. Personal Budget Tracker
3. To-Do App (CLI)
4. Hangman Game
5. Weather Dashboard
6. Web Scraper & Data Analyzer
7. Chat Application (CLI)
8. Blog REST API
9. ML Prediction App
10. AI-Powered Study Buddy

---

**Happy coding! 🎉**
```

- [ ] **Step 5: Create all directory scaffolding**

```bash
# Sprint 1
mkdir -p code/sprint-1-basics/{chapter-01-why-python,chapter-02-variables/exercises,chapter-03-numbers/exercises,chapter-04-strings/exercises,chapter-05-decisions/exercises,chapter-06-lists/exercises,chapter-07-loops/exercises,chapter-08-tuples-sets/exercises,checkpoint-mad-libs}

# Sprint 2
mkdir -p code/sprint-2-intermediate/{chapter-09-dictionaries/exercises,chapter-10-functions/exercises,chapter-11-modules/exercises,chapter-12-files/exercises,chapter-13-errors/exercises,chapter-14-lambda/exercises,checkpoint-expense-tracker}

# Sprint 3
mkdir -p code/sprint-3-oop/{chapter-15-classes/exercises,chapter-16-inheritance/exercises,chapter-17-magic-methods/exercises,chapter-18-design-principles/exercises,checkpoint-library-system}

# Sprint 4
mkdir -p code/sprint-4-pro/{chapter-19-decorators/exercises,chapter-20-generators/exercises,chapter-21-apis/exercises,chapter-22-databases/exercises,chapter-23-scraping/exercises,chapter-24-testing/exercises,chapter-25-clean-code/exercises,checkpoint-job-scraper}

# Sprint 5
mkdir -p code/sprint-5-ai/{chapter-26-numpy/exercises,chapter-27-pandas/exercises,chapter-28-visualization/exercises,chapter-29-ml/exercises,chapter-30-ai-apis/exercises,chapter-31-langchain/exercises,chapter-32-automation/exercises,checkpoint-resume-analyzer}

# Final projects
mkdir -p code/final-projects/{project-01-quiz-game,project-02-budget-tracker,project-03-todo-app,project-04-hangman,project-05-weather-dashboard,project-06-web-scraper,project-07-chat-app,project-08-blog-api,project-09-ml-app,project-10-ai-study-buddy}

# Book structure
mkdir -p book/{front-matter,sprint-1,sprint-2,sprint-3,sprint-4,sprint-5,final-projects,back-matter}
```

- [ ] **Step 6: Commit project scaffolding**

```bash
git add .
git commit -m "chore: scaffold project structure for Python Crash Course book and code repo"
```

---

## Phase 1: Sprint 1 Code Examples & Exercises

### Task 2: Chapter 1 — Why Python (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-01-why-python/hello.py`
- Create: `code/sprint-1-basics/chapter-01-why-python/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-01-why-python/exercises/solution.py`

- [ ] **Step 1: Create hello.py example**

Create file `code/sprint-1-basics/chapter-01-why-python/hello.py`:
```python
# Chapter 1: Your Very First Python Program
# Welcome to Python! Let's start with the classic.

print("Hello, World!")

# You can print anything!
print("Python is awesome!")
print("I'm learning to code!")

# You can even do math right away
print(2 + 2)
print("In 30 days, I'll be building AI apps. No pressure.")
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-01-why-python/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Chapter 1 Exercise
# ============================================
# 1. Print your name
# 2. Print your favorite joke
# 3. Print a friendly insult to your best friend
# 4. Print the result of a math problem
#
# Go ahead — type your code below!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-01-why-python/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Chapter 1 Exercise
# ============================================

# 1. Print your name
print("My name is Alex!")

# 2. Print your favorite joke
print("Why do programmers prefer dark mode?")
print("Because light attracts bugs! 🐛")

# 3. Print a friendly insult to your best friend
print("Hey Dave, even Python can't fix your taste in music.")

# 4. Print the result of a math problem
print(42 * 3.14)
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-01-why-python/
git commit -m "feat: add Chapter 1 code examples and exercises"
```

### Task 3: Chapter 2 — Variables (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-02-variables/examples.py`
- Create: `code/sprint-1-basics/chapter-02-variables/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-02-variables/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-02-variables/examples.py`:
```python
# Chapter 2: Variables — Giving Names to Stuff

# --- What are variables? ---
# Think of them as labeled boxes. You put stuff in, slap a name on it.

name = "Tony Stark"
age = 45
height = 5.9
is_superhero = True

print(name)       # Tony Stark
print(age)        # 45
print(height)     # 5.9
print(is_superhero)  # True

# --- Types ---
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_superhero))  # <class 'bool'>

# --- Naming rules ---
# Good names:
user_name = "peter_parker"
score_total = 100
is_logged_in = False

# Bad names (don't do this):
# x = "peter_parker"      # What is x? Nobody knows.
# a = 100                 # a for... what?

# --- f-strings: Python's coolest feature for beginners ---
name = "Peter"
city = "New York"
age = 22

# The OLD way (boring):
print("My name is " + name + " and I live in " + city)

# The NEW way (f-strings — notice the 'f' before the quote):
print(f"My name is {name} and I live in {city}")
print(f"In 10 years, I'll be {age + 10} years old")
print(f"{'=' * 30}")  # Prints 30 equal signs. Fancy!

# --- Reassigning variables ---
mood = "happy"
print(f"I'm {mood}")  # I'm happy

mood = "excited"
print(f"Now I'm {mood}")  # Now I'm excited

# Python doesn't care if you change what's in the box.
# It's YOUR box.
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-02-variables/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Build an "About Me" Card
# ============================================
# Create variables for:
#   - Your name
#   - Your age
#   - Your city
#   - Your favorite movie
#   - Whether you're a morning person (True/False)
#
# Then use f-strings to print a nice "About Me" card like:
#
# ╔══════════════════════════╗
#   Name: Alex
#   Age: 25
#   City: Austin
#   Fav Movie: Inception
#   Morning Person: Absolutely not
# ╚══════════════════════════╝
#
# Bonus: Make the border dynamic based on the longest line!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-02-variables/exercises/solution.py`:
```python
# ============================================
# SOLUTION: About Me Card
# ============================================

name = "Alex"
age = 25
city = "Austin"
favorite_movie = "Inception"
is_morning_person = False

morning_status = "Yes, I love mornings!" if is_morning_person else "Absolutely not"

print("╔══════════════════════════════╗")
print(f"  Name:           {name}")
print(f"  Age:            {age}")
print(f"  City:           {city}")
print(f"  Fav Movie:      {favorite_movie}")
print(f"  Morning Person: {morning_status}")
print("╚══════════════════════════════╝")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-02-variables/
git commit -m "feat: add Chapter 2 code examples and exercises"
```

### Task 4: Chapter 3 — Numbers & Math (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-03-numbers/examples.py`
- Create: `code/sprint-1-basics/chapter-03-numbers/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-03-numbers/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-03-numbers/examples.py`:
```python
# Chapter 3: Numbers & Math — Python is Your New Calculator

# --- Arithmetic operators ---
print(10 + 3)    # 13  (addition)
print(10 - 3)    # 7   (subtraction)
print(10 * 3)    # 30  (multiplication)
print(10 / 3)    # 3.3333... (division — always returns float!)
print(10 // 3)   # 3   (floor division — chops off the decimal)
print(10 % 3)    # 1   (modulo — the remainder)
print(10 ** 3)   # 1000 (exponent — 10 to the power of 3)

# --- Order of operations (PEMDAS flashbacks) ---
result = 2 + 3 * 4       # 14, not 20! Multiplication first.
result = (2 + 3) * 4     # 20. Parentheses save the day.
print(f"Without parens: {2 + 3 * 4}")
print(f"With parens: {(2 + 3) * 4}")

# --- Type conversion: when "5" isn't 5 ---
text_number = "42"
real_number = 42

# This FAILS:
# print(text_number + real_number)  # TypeError!

# Fix it with int() or float():
print(int(text_number) + real_number)   # 84
print(float("3.14"))                     # 3.14
print(str(42) + " is the answer")        # "42 is the answer"

# --- The input() function ---
# input() ALWAYS returns a string. Always. Every time. No exceptions.
# So if you need a number, you must convert it.

name = input("What's your name? ")
print(f"Hey {name}! Nice to meet you.")

age = int(input("How old are you? "))
print(f"In 5 years you'll be {age + 5}!")

# --- Useful built-in math functions ---
print(abs(-42))         # 42 (absolute value)
print(round(3.14159, 2))  # 3.14 (round to 2 decimals)
print(max(1, 5, 3, 9))   # 9
print(min(1, 5, 3, 9))   # 1
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-03-numbers/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Build a Tip Calculator
# ============================================
# Ask the user for:
#   1. The total bill amount
#   2. The tip percentage they want to give
#   3. How many people are splitting the bill
#
# Then calculate and display:
#   - The tip amount
#   - The total (bill + tip)
#   - How much each person pays
#
# Example output:
#   Bill: $85.50
#   Tip (20%): $17.10
#   Total: $102.60
#   Each person pays: $34.20 (split 3 ways)
#
# Hint: Remember to convert input() to float/int!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-03-numbers/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Tip Calculator
# ============================================

bill = float(input("What's the total bill? $"))
tip_percent = float(input("What tip % do you want to give? "))
people = int(input("How many people are splitting? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print(f"\n{'=' * 30}")
print(f"  Bill:            ${bill:.2f}")
print(f"  Tip ({tip_percent:.0f}%):       ${tip_amount:.2f}")
print(f"  Total:           ${total:.2f}")
print(f"  Each person pays: ${per_person:.2f} (split {people} ways)")
print(f"{'=' * 30}")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-03-numbers/
git commit -m "feat: add Chapter 3 code examples and exercises"
```

### Task 5: Chapter 4 — Strings (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-04-strings/examples.py`
- Create: `code/sprint-1-basics/chapter-04-strings/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-04-strings/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-04-strings/examples.py`:
```python
# Chapter 4: Strings — Text is Everywhere

# --- String methods ---
message = "  Hello, Python World!  "

print(message.upper())          # "  HELLO, PYTHON WORLD!  "
print(message.lower())          # "  hello, python world!  "
print(message.strip())          # "Hello, Python World!" (removes spaces)
print(message.replace("World", "Universe"))  # "  Hello, Python Universe!  "
print(message.split(","))       # ['  Hello', ' Python World!  ']
print(message.count("l"))       # 3
print(message.find("Python"))   # 9 (index where "Python" starts)
print(message.startswith("  H"))  # True
print(message.endswith("!  "))    # True

# --- Chaining methods (like combo moves in a video game) ---
clean = "  messy DATA  ".strip().lower().replace(" ", "_")
print(clean)  # "messy_data"

# --- Slicing strings like a ninja ---
text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5
#      -6 -5 -4 -3 -2 -1

print(text[0])       # "P" (first character)
print(text[-1])      # "n" (last character)
print(text[0:3])     # "Pyt" (index 0, 1, 2 — NOT 3!)
print(text[2:])      # "thon" (from index 2 to the end)
print(text[:4])      # "Pyth" (from start to index 3)
print(text[::-1])    # "nohtyP" (reversed! The party trick.)

# --- Escape characters ---
print("She said \"Hello!\"")     # She said "Hello!"
print("Line 1\nLine 2")          # Two separate lines
print("Column1\tColumn2")        # Tab between them
print(r"C:\new\test")            # Raw string — backslashes stay literal

# --- String formatting deep dive ---
name = "Groot"
times = 1000

# f-strings (the best way)
print(f"I am {name}! Said {times:,} times.")  # "I am Groot! Said 1,000 times."

# Padding and alignment
print(f"{'left':<20}|")     # "left                |"
print(f"{'center':^20}|")   # "       center       |"
print(f"{'right':>20}|")    # "               right|"

# Number formatting
pi = 3.14159265
print(f"Pi is approximately {pi:.2f}")   # "Pi is approximately 3.14"
print(f"Big number: {1000000:,}")        # "Big number: 1,000,000"
print(f"Percentage: {0.856:.1%}")        # "Percentage: 85.6%"
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-04-strings/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Build a Username Generator
# ============================================
# Ask the user for:
#   1. Their first name
#   2. Their last name
#
# Generate a username that:
#   - Combines first 3 letters of first name + last name
#   - Makes everything lowercase
#   - Removes any spaces
#   - Adds a random number between 100 and 999
#
# Example:
#   Input: "Tony", "Stark"
#   Output: "tonstark472"
#
# Hint: You'll need: import random, then random.randint(100, 999)
# ============================================

import random


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-04-strings/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Username Generator
# ============================================

import random

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

first_part = first_name[:3].lower()
last_part = last_name.lower().replace(" ", "")
random_num = random.randint(100, 999)

username = f"{first_part}{last_part}{random_num}"

print(f"\nYour generated username: {username}")
print(f"Username length: {len(username)} characters")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-04-strings/
git commit -m "feat: add Chapter 4 code examples and exercises"
```

### Task 6: Chapter 5 — Decisions (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-05-decisions/examples.py`
- Create: `code/sprint-1-basics/chapter-05-decisions/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-05-decisions/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-05-decisions/examples.py`:
```python
# Chapter 5: Making Decisions — if, elif, else

# --- Comparison operators ---
print(10 == 10)   # True  (equal to)
print(10 != 5)    # True  (not equal to)
print(10 > 5)     # True  (greater than)
print(10 < 5)     # False (less than)
print(10 >= 10)   # True  (greater or equal)
print(10 <= 9)    # False (less or equal)

# --- Basic if/elif/else ---
temperature = 35

if temperature > 30:
    print("It's hot! Stay hydrated! 🔥")
elif temperature > 20:
    print("Nice weather! Go outside! ☀️")
elif temperature > 10:
    print("A bit chilly. Grab a jacket. 🧥")
else:
    print("It's freezing! Stay home! 🥶")

# --- Logical operators ---
age = 25
has_id = True

# AND — both must be true
if age >= 18 and has_id:
    print("Welcome to the club!")

# OR — at least one must be true
is_vip = False
is_on_list = True

if is_vip or is_on_list:
    print("You're in!")

# NOT — flips True to False and vice versa
is_banned = False

if not is_banned:
    print("You're welcome here!")

# --- Nested conditions (and when to avoid them) ---

# BAD (nested spaghetti):
age = 25
if age >= 18:
    if has_id:
        if not is_banned:
            print("Welcome!")

# GOOD (flat and clean):
if age >= 18 and has_id and not is_banned:
    print("Welcome!")

# --- Truthy and Falsy ---
# These are all "falsy" (Python treats them as False):
# False, 0, 0.0, "", [], {}, None

# These are all "truthy" (Python treats them as True):
# True, any non-zero number, any non-empty string/list/dict

name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name!")

# --- Ternary operator (one-line if/else) ---
age = 20
status = "adult" if age >= 18 else "minor"
print(f"You are a {status}")
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-05-decisions/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Movie Rating Classifier
# ============================================
# Ask the user for their age, then tell them
# which movie ratings they can watch:
#
#   Age < 7:   "You can watch: G rated movies"
#   Age 7-12:  "You can watch: G, PG rated movies"
#   Age 13-16: "You can watch: G, PG, PG-13 rated movies"
#   Age 17+:   "You can watch: All movies! 🎬"
#
# Bonus: Also ask if they have a parent with them.
#   If they do, bump them up one tier!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-05-decisions/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Movie Rating Classifier
# ============================================

age = int(input("How old are you? "))
has_parent = input("Is a parent with you? (yes/no) ").strip().lower() == "yes"

# Bump up one tier if parent is present
effective_age = age + 4 if has_parent else age

if effective_age < 7:
    print("You can watch: G rated movies")
elif effective_age < 13:
    print("You can watch: G, PG rated movies")
elif effective_age < 17:
    print("You can watch: G, PG, PG-13 rated movies")
else:
    print("You can watch: All movies! 🎬")

if has_parent and age < 17:
    print("(Bumped up a tier because your parent is with you!)")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-05-decisions/
git commit -m "feat: add Chapter 5 code examples and exercises"
```

### Task 7: Chapter 6 — Lists (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-06-lists/examples.py`
- Create: `code/sprint-1-basics/chapter-06-lists/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-06-lists/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-06-lists/examples.py`:
```python
# Chapter 6: Lists — Your First Superpower

# --- Creating lists ---
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Python doesn't care about mixing types
empty = []

# --- Accessing items ---
print(fruits[0])     # "apple" (first item)
print(fruits[-1])    # "cherry" (last item)
print(fruits[1:3])   # ["banana", "cherry"] (slicing!)

# --- Modifying lists ---
fruits.append("dragon fruit")     # Add to the end
fruits.insert(1, "blueberry")    # Insert at position 1
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'dragon fruit']

fruits.remove("banana")          # Remove by value
popped = fruits.pop()            # Remove and return last item
print(f"Popped: {popped}")      # "dragon fruit"
del fruits[0]                    # Remove by index

# --- Sorting ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                   # Sorts in place: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)       # Descending: [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns a NEW list (doesn't change original)
original = [3, 1, 4]
new_list = sorted(original)
print(original)   # [3, 1, 4] — unchanged!
print(new_list)   # [1, 3, 4]

# --- Useful list methods ---
print(len(fruits))               # How many items
print("apple" in fruits)         # Is it in there? True/False
print(fruits.count("cherry"))    # How many times does it appear
print(fruits.index("cherry"))    # Where is it?

# --- Looping through lists ---
heroes = ["Iron Man", "Spider-Man", "Thor", "Hulk"]

for hero in heroes:
    print(f"{hero} is awesome!")

# With index (enumerate is your friend)
for i, hero in enumerate(heroes):
    print(f"{i + 1}. {hero}")

# --- List comprehensions (the "show off" move) ---
# The OLD way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# The COOL way:
squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With a condition (filter while creating)
even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Practical example: clean up messy data
messy_names = ["  Alice  ", "BOB", "  charlie"]
clean_names = [name.strip().title() for name in messy_names]
print(clean_names)  # ['Alice', 'Bob', 'Charlie']
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-06-lists/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Grocery List Manager
# ============================================
# Build a program that lets the user:
#   1. View the grocery list
#   2. Add an item
#   3. Remove an item
#   4. Quit
#
# Use a while loop + if/elif to handle the menu.
# Start with an empty list and let the user build it up.
#
# Example:
#   --- Grocery List Manager ---
#   1. View list
#   2. Add item
#   3. Remove item
#   4. Quit
#   Choice: 2
#   Item to add: Milk
#   Added "Milk" to your list!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-06-lists/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Grocery List Manager
# ============================================

grocery_list = []

while True:
    print(f"\n{'=' * 30}")
    print("  🛒 Grocery List Manager")
    print(f"{'=' * 30}")
    print("  1. View list")
    print("  2. Add item")
    print("  3. Remove item")
    print("  4. Quit")
    print(f"{'=' * 30}")

    choice = input("  Choice: ").strip()

    if choice == "1":
        if grocery_list:
            print("\n  Your grocery list:")
            for i, item in enumerate(grocery_list, 1):
                print(f"    {i}. {item}")
        else:
            print("\n  Your list is empty! Add something.")

    elif choice == "2":
        item = input("  Item to add: ").strip()
        if item:
            grocery_list.append(item.title())
            print(f'  Added "{item.title()}" to your list!')
        else:
            print("  You didn't type anything!")

    elif choice == "3":
        item = input("  Item to remove: ").strip().title()
        if item in grocery_list:
            grocery_list.remove(item)
            print(f'  Removed "{item}" from your list!')
        else:
            print(f'  "{item}" is not in your list.')

    elif choice == "4":
        print("  Bye! Happy shopping! 🛍️")
        break

    else:
        print("  Invalid choice. Pick 1-4.")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-06-lists/
git commit -m "feat: add Chapter 6 code examples and exercises"
```

### Task 8: Chapter 7 — Loops (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-07-loops/examples.py`
- Create: `code/sprint-1-basics/chapter-07-loops/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-07-loops/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-07-loops/examples.py`:
```python
# Chapter 7: Loops — Doing Things on Repeat

# --- for loops ---
colors = ["red", "green", "blue"]
for color in colors:
    print(f"I like {color}!")

# --- range() — the loop's best friend ---
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 20, 3):
    print(i)  # 0, 3, 6, 9, 12, 15, 18

# Counting backwards
for i in range(5, 0, -1):
    print(f"{i}...")
print("Liftoff! 🚀")

# --- while loops ---
# Use when you don't know how many times you'll loop

attempts = 0
password = ""

while password != "python123":
    password = input("Enter the password: ")
    attempts += 1
    if attempts >= 3:
        print("Too many attempts! Locked out.")
        break

if password == "python123":
    print(f"Access granted! Took {attempts} attempt(s).")

# --- break and continue ---
# break = "I'm outta here!" (exits the loop entirely)
for num in range(1, 100):
    if num == 7:
        print(f"Found lucky number {num}!")
        break

# continue = "Skip this one" (jumps to next iteration)
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"{num} is odd")

# --- Nested loops ---
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)

# --- The else clause (weird but useful) ---
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # This runs if the loop completed WITHOUT hitting break
        print(f"{n} is prime!")
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-07-loops/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Multiplication Table Printer
# ============================================
# Ask the user for a number (1-12), then print
# a clean multiplication table for that number.
#
# Example (if user enters 5):
#
#   ✖️ Multiplication Table for 5
#   ─────────────────────────────
#   5 x  1 =   5
#   5 x  2 =  10
#   5 x  3 =  15
#   ...
#   5 x 12 =  60
#   ─────────────────────────────
#
# Bonus: Let the user keep entering numbers
# until they type "quit"
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-07-loops/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Multiplication Table Printer
# ============================================

while True:
    user_input = input("\nEnter a number (1-12) or 'quit': ").strip()

    if user_input.lower() == "quit":
        print("Bye! Keep multiplying! ✌️")
        break

    if not user_input.isdigit() or not (1 <= int(user_input) <= 12):
        print("Please enter a number between 1 and 12.")
        continue

    num = int(user_input)
    print(f"\n  Multiplication Table for {num}")
    print(f"  {'─' * 25}")

    for i in range(1, 13):
        result = num * i
        print(f"  {num} x {i:>2} = {result:>4}")

    print(f"  {'─' * 25}")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-07-loops/
git commit -m "feat: add Chapter 7 code examples and exercises"
```

### Task 9: Chapter 8 — Tuples & Sets (Code)

**Files:**
- Create: `code/sprint-1-basics/chapter-08-tuples-sets/examples.py`
- Create: `code/sprint-1-basics/chapter-08-tuples-sets/exercises/your_turn.py`
- Create: `code/sprint-1-basics/chapter-08-tuples-sets/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-1-basics/chapter-08-tuples-sets/examples.py`:
```python
# Chapter 8: Tuples & Sets — Lists' Cousins

# ==========================================
# TUPLES — Like lists, but you can't change them
# ==========================================

# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)  # Note the comma! Without it, it's just a number in parens.

# Accessing (same as lists)
print(coordinates[0])   # 10
print(rgb_color[-1])    # 0

# Why use tuples? They're:
# 1. Faster than lists
# 2. Signal "this shouldn't change"
# 3. Can be dictionary keys (lists can't!)

# --- Tuple unpacking (the elegant move) ---
point = (5, 10, 15)
x, y, z = point  # Boom. Three variables in one line.
print(f"x={x}, y={y}, z={z}")

# Swap variables without a temp variable
a, b = 1, 2
a, b = b, a  # Python magic!
print(f"a={a}, b={b}")  # a=2, b=1

# Unpacking with * (grab the rest)
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# Functions that return multiple values use tuples
def get_user():
    return "Alice", 25, "alice@email.com"

name, age, email = get_user()
print(f"{name} is {age} and reachable at {email}")


# ==========================================
# SETS — Unique items only. No duplicates. Ever.
# ==========================================

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 2, 1}  # Duplicates removed!
print(numbers)  # {1, 2, 3}

# From a list (great for removing duplicates!)
messy_list = [1, 2, 2, 3, 3, 3, 4]
clean = set(messy_list)
print(clean)  # {1, 2, 3, 4}

# Adding and removing
fruits.add("dragon fruit")
fruits.discard("banana")  # Safe — no error if not found
# fruits.remove("banana")  # Raises error if not found

# --- Set operations (math class flashbacks) ---
marvel = {"Iron Man", "Thor", "Hulk", "Spider-Man"}
avengers = {"Iron Man", "Thor", "Captain America", "Hulk"}

# Union — everyone from both sets
print(marvel | avengers)  # All heroes combined

# Intersection — who's in BOTH?
print(marvel & avengers)  # {'Iron Man', 'Thor', 'Hulk'}

# Difference — in marvel but NOT in avengers
print(marvel - avengers)  # {'Spider-Man'}

# Symmetric difference — in one but NOT both
print(marvel ^ avengers)  # {'Spider-Man', 'Captain America'}

# --- When to use what ---
# List:  Ordered, allows duplicates, changeable    → grocery list, scores
# Tuple: Ordered, allows duplicates, NOT changeable → coordinates, RGB colors
# Set:   Unordered, NO duplicates, changeable       → unique tags, seen items
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-1-basics/chapter-08-tuples-sets/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Duplicate Finder for a Playlist
# ============================================
# You have a playlist with some duplicate songs.
# Write a program that:
#   1. Finds and displays duplicate songs
#   2. Removes duplicates (keeping order)
#   3. Shows the clean playlist
#
# Start with this playlist:
playlist = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Stairway to Heaven",
    "Bohemian Rhapsody",
    "Imagine",
    "Hotel California",
    "Smells Like Teen Spirit",
    "Imagine",
    "Bohemian Rhapsody",
    "Yesterday",
]
#
# Expected output:
#   Duplicate songs found:
#     - Bohemian Rhapsody (appears 3 times)
#     - Hotel California (appears 2 times)
#     - Imagine (appears 2 times)
#
#   Clean playlist (9 → 6 unique songs):
#     1. Bohemian Rhapsody
#     2. Hotel California
#     ... etc
#
# Hint: Use a set to track what you've seen!
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-1-basics/chapter-08-tuples-sets/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Duplicate Finder for a Playlist
# ============================================

playlist = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Stairway to Heaven",
    "Bohemian Rhapsody",
    "Imagine",
    "Hotel California",
    "Smells Like Teen Spirit",
    "Imagine",
    "Bohemian Rhapsody",
    "Yesterday",
]

# Find duplicates using a set
seen = set()
duplicates = set()

for song in playlist:
    if song in seen:
        duplicates.add(song)
    seen.add(song)

# Display duplicates with counts
print("🎵 Duplicate songs found:")
for song in duplicates:
    count = playlist.count(song)
    print(f"  - {song} (appears {count} times)")

# Remove duplicates while keeping order
clean_playlist = []
seen_clean = set()
for song in playlist:
    if song not in seen_clean:
        clean_playlist.append(song)
        seen_clean.add(song)

# Display clean playlist
print(f"\n🎵 Clean playlist ({len(playlist)} → {len(clean_playlist)} unique songs):")
for i, song in enumerate(clean_playlist, 1):
    print(f"  {i}. {song}")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-1-basics/chapter-08-tuples-sets/
git commit -m "feat: add Chapter 8 code examples and exercises"
```

### Task 10: Sprint 1 Checkpoint — Mad Libs Generator (Code)

**Files:**
- Create: `code/sprint-1-basics/checkpoint-mad-libs/starter.py`
- Create: `code/sprint-1-basics/checkpoint-mad-libs/solution.py`

- [ ] **Step 1: Create starter.py**

Create file `code/sprint-1-basics/checkpoint-mad-libs/starter.py`:
```python
# ============================================
# SPRINT 1 CHECKPOINT PROJECT: Mad Libs Generator
# ============================================
# Build a Mad Libs word game that:
#   1. Has at least 3 different story templates
#   2. Asks the user for words (nouns, verbs, adjectives, etc.)
#   3. Fills in the blanks and prints the funny story
#   4. Asks if they want to play again
#
# Skills used: strings, variables, input, lists, loops, conditions, f-strings
#
# YOUR CODE BELOW:
# ============================================


```

- [ ] **Step 2: Create solution.py**

Create file `code/sprint-1-basics/checkpoint-mad-libs/solution.py`:
```python
# ============================================
# SOLUTION: Mad Libs Generator
# ============================================

import random

# Story templates — each is a tuple of (title, template_string, word_prompts)
stories = [
    (
        "The Adventurous Day",
        "Today I woke up feeling very {adjective1}. I decided to {verb1} to the {place}. "
        "On the way, I saw a {adjective2} {animal} trying to {verb2} a {noun}. "
        "I shouted '{exclamation}!' and the {animal} {verb3} away. "
        "What a {adjective3} day!",
        {
            "adjective1": "Enter an adjective (feeling): ",
            "verb1": "Enter a verb (movement): ",
            "place": "Enter a place: ",
            "adjective2": "Enter another adjective: ",
            "animal": "Enter an animal: ",
            "verb2": "Enter a verb: ",
            "noun": "Enter a noun (thing): ",
            "exclamation": "Enter an exclamation: ",
            "verb3": "Enter a verb (past tense): ",
            "adjective3": "Enter one more adjective: ",
        }
    ),
    (
        "The Job Interview",
        "I walked into the interview feeling {adjective1}. The interviewer, a {adjective2} "
        "{animal}, asked me to {verb1} a {noun}. I said 'I can {verb2} at least {number} "
        "of those per {time_period}!' They looked {adjective3} and offered me a job as "
        "Chief {noun} Officer with a salary of {number2} {food} per year.",
        {
            "adjective1": "Enter an adjective (feeling): ",
            "adjective2": "Enter an adjective (describing someone): ",
            "animal": "Enter an animal: ",
            "verb1": "Enter a verb: ",
            "noun": "Enter a noun: ",
            "verb2": "Enter another verb: ",
            "number": "Enter a large number: ",
            "time_period": "Enter a time period (hour/day/week): ",
            "adjective3": "Enter an adjective (reaction): ",
            "number2": "Enter another number: ",
            "food": "Enter a food (plural): ",
        }
    ),
    (
        "The Superhero Origin",
        "One {adjective1} night, {name} was bitten by a radioactive {animal}. "
        "They gained the power to {verb1} at {number} miles per hour and shoot "
        "{noun_plural} from their {body_part}. Their arch-nemesis, Dr. {adjective2}, "
        "tried to {verb2} the city with a giant {noun}. But {name} {verb3} the day "
        "by {verb4}ing really {adverb}. The crowd chanted '{exclamation}!'",
        {
            "adjective1": "Enter an adjective (time of day): ",
            "name": "Enter a name: ",
            "animal": "Enter an animal: ",
            "verb1": "Enter a verb: ",
            "number": "Enter a number: ",
            "noun_plural": "Enter a noun (plural): ",
            "body_part": "Enter a body part: ",
            "adjective2": "Enter a silly adjective: ",
            "verb2": "Enter a verb: ",
            "noun": "Enter a noun: ",
            "verb3": "Enter a verb (past tense): ",
            "verb4": "Enter a verb: ",
            "adverb": "Enter an adverb (ends in -ly): ",
            "exclamation": "Enter an exclamation: ",
        }
    ),
]

def play_mad_libs():
    """Play one round of Mad Libs."""
    title, template, prompts = random.choice(stories)

    print(f"\n{'=' * 40}")
    print(f"  📝 Mad Libs: {title}")
    print(f"{'=' * 40}")
    print("  Fill in the blanks!\n")

    # Collect words from user
    words = {}
    for key, prompt in prompts.items():
        words[key] = input(f"  {prompt}").strip()
        if not words[key]:
            words[key] = "[blank]"

    # Fill in the story
    story = template.format(**words)

    # Display the result
    print(f"\n{'=' * 40}")
    print(f"  📖 Your Story: {title}")
    print(f"{'=' * 40}")
    print(f"\n  {story}")
    print(f"\n{'=' * 40}")

# Main game loop
print("\n🎭 Welcome to the Mad Libs Generator! 🎭")
print("  The funniest word game in Python.")

while True:
    play_mad_libs()

    play_again = input("\n  Play again? (yes/no): ").strip().lower()
    if play_again not in ("yes", "y"):
        print("\n  Thanks for playing! Stay funny! 😄\n")
        break
```

- [ ] **Step 3: Commit**

```bash
git add code/sprint-1-basics/checkpoint-mad-libs/
git commit -m "feat: add Sprint 1 checkpoint project — Mad Libs Generator"
```

---

## Phase 2: Sprint 2 Code Examples & Exercises

### Task 11: Chapter 9 — Dictionaries (Code)

**Files:**
- Create: `code/sprint-2-intermediate/chapter-09-dictionaries/examples.py`
- Create: `code/sprint-2-intermediate/chapter-09-dictionaries/exercises/your_turn.py`
- Create: `code/sprint-2-intermediate/chapter-09-dictionaries/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-2-intermediate/chapter-09-dictionaries/examples.py`:
```python
# Chapter 9: Dictionaries — The Real MVP

# --- Key-value pairs ---
person = {
    "name": "Tony Stark",
    "age": 45,
    "city": "Malibu",
    "is_hero": True,
}

print(person["name"])          # "Tony Stark"
print(person.get("email", "N/A"))  # "N/A" (safe — no crash if missing)

# --- Adding, updating, deleting ---
person["email"] = "tony@stark.com"   # Add new key
person["age"] = 46                   # Update existing
del person["is_hero"]                # Delete a key
popped = person.pop("city")          # Remove and return
print(f"Removed: {popped}")

# --- Looping through dictionaries ---
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Keys only
for name in scores:
    print(name)

# Values only
for score in scores.values():
    print(score)

# Both (the most useful one)
for name, score in scores.items():
    print(f"{name}: {score}")

# --- Nested dictionaries ---
students = {
    "alice": {
        "age": 20,
        "grades": [90, 85, 92],
        "major": "Computer Science",
    },
    "bob": {
        "age": 22,
        "grades": [78, 82, 88],
        "major": "Mathematics",
    },
}

# Accessing nested values
print(students["alice"]["major"])       # "Computer Science"
print(students["bob"]["grades"][0])     # 78

# Looping through nested dicts
for name, info in students.items():
    avg = sum(info["grades"]) / len(info["grades"])
    print(f"{name.title()} ({info['major']}): avg = {avg:.1f}")

# --- Dictionary comprehensions ---
numbers = [1, 2, 3, 4, 5]
squared = {n: n**2 for n in numbers}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Practical: word frequency counter
sentence = "the cat sat on the mat the cat"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# --- Useful dict methods ---
print(scores.keys())       # dict_keys(['Alice', 'Bob', 'Charlie'])
print(scores.values())     # dict_values([95, 87, 92])
print("Alice" in scores)   # True (checks keys by default)

# Merge two dictionaries
defaults = {"theme": "dark", "font_size": 14, "language": "en"}
user_prefs = {"font_size": 18, "language": "es"}
settings = {**defaults, **user_prefs}  # User prefs override defaults
print(settings)  # {'theme': 'dark', 'font_size': 18, 'language': 'es'}
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-2-intermediate/chapter-09-dictionaries/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Contact Book
# ============================================
# Build a contact book program that lets you:
#   1. View all contacts
#   2. Add a contact (name + phone)
#   3. Search for a contact by name
#   4. Delete a contact
#   5. Quit
#
# Store contacts as: {"name": "phone_number"}
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-2-intermediate/chapter-09-dictionaries/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Contact Book
# ============================================

contacts = {}

while True:
    print(f"\n{'=' * 30}")
    print("  📱 Contact Book")
    print(f"{'=' * 30}")
    print("  1. View all contacts")
    print("  2. Add a contact")
    print("  3. Search for a contact")
    print("  4. Delete a contact")
    print("  5. Quit")
    print(f"{'=' * 30}")

    choice = input("  Choice: ").strip()

    if choice == "1":
        if contacts:
            print("\n  Your contacts:")
            for name, phone in sorted(contacts.items()):
                print(f"    {name}: {phone}")
        else:
            print("\n  No contacts yet. Add someone!")

    elif choice == "2":
        name = input("  Name: ").strip().title()
        phone = input("  Phone: ").strip()
        if name and phone:
            contacts[name] = phone
            print(f"  Added {name}!")
        else:
            print("  Name and phone are required.")

    elif choice == "3":
        query = input("  Search name: ").strip().lower()
        found = {n: p for n, p in contacts.items() if query in n.lower()}
        if found:
            for name, phone in found.items():
                print(f"    {name}: {phone}")
        else:
            print(f"  No contacts matching '{query}'.")

    elif choice == "4":
        name = input("  Name to delete: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"  Deleted {name}.")
        else:
            print(f"  '{name}' not found.")

    elif choice == "5":
        print("  Goodbye! 👋")
        break
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-2-intermediate/chapter-09-dictionaries/
git commit -m "feat: add Chapter 9 code examples and exercises"
```

### Task 12: Chapter 10 — Functions (Code)

**Files:**
- Create: `code/sprint-2-intermediate/chapter-10-functions/examples.py`
- Create: `code/sprint-2-intermediate/chapter-10-functions/exercises/your_turn.py`
- Create: `code/sprint-2-intermediate/chapter-10-functions/exercises/solution.py`

- [ ] **Step 1: Create examples.py**

Create file `code/sprint-2-intermediate/chapter-10-functions/examples.py`:
```python
# Chapter 10: Functions — Stop Repeating Yourself

# --- Defining and calling functions ---
def greet(name):
    """Say hello to someone."""
    print(f"Hey {name}! What's up?")

greet("Alice")
greet("Bob")

# --- Return values ---
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# No return = returns None
def say_hi():
    print("Hi!")

value = say_hi()
print(value)  # None

# --- Default parameters ---
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent=2)
print(power(5, 3))   # 125

# --- Keyword arguments ---
def create_profile(name, age, city="Unknown"):
    return f"{name}, {age}, from {city}"

# You can pass args by name in any order
print(create_profile(age=30, name="Alice", city="NYC"))

# --- *args (variable positional arguments) ---
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100

# --- **kwargs (variable keyword arguments) ---
def print_info(**kwargs):
    """Print whatever key-value pairs are passed."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, hobby="coding")

# --- Combining *args and **kwargs ---
def super_function(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

super_function(1, 2, 3, name="Alice", role="dev")

# --- Scope: local vs global ---
message = "I'm global!"

def change_message():
    message = "I'm local!"  # This is a NEW local variable!
    print(message)  # "I'm local!"

change_message()
print(message)  # "I'm global!" (unchanged!)

# To modify global (usually avoid this):
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

# --- Functions as first-class objects ---
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, text):
    return func(text)

print(speak(shout, "hello"))    # "HELLO"
print(speak(whisper, "HELLO"))  # "hello"
```

- [ ] **Step 2: Create exercise starter**

Create file `code/sprint-2-intermediate/chapter-10-functions/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Password Strength Checker
# ============================================
# Write a function called check_password(password) that:
#   - Returns "Weak" if < 8 characters
#   - Returns "Medium" if >= 8 chars but missing uppercase, lowercase,
#     digit, or special character
#   - Returns "Strong" if >= 8 chars AND has uppercase + lowercase +
#     digit + special character
#   - Also returns a list of tips for improvement
#
# Example:
#   strength, tips = check_password("hello")
#   # strength = "Weak"
#   # tips = ["At least 8 characters", "Add uppercase", "Add digits", "Add special chars"]
#
#   strength, tips = check_password("MyP@ssw0rd")
#   # strength = "Strong"
#   # tips = []
# ============================================


```

- [ ] **Step 3: Create exercise solution**

Create file `code/sprint-2-intermediate/chapter-10-functions/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Password Strength Checker
# ============================================

def check_password(password):
    """Check password strength and return (strength, tips)."""
    tips = []

    if len(password) < 8:
        tips.append("At least 8 characters")

    if not any(c.isupper() for c in password):
        tips.append("Add uppercase letters")

    if not any(c.islower() for c in password):
        tips.append("Add lowercase letters")

    if not any(c.isdigit() for c in password):
        tips.append("Add digits")

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        tips.append("Add special characters (!@#$%...)")

    if len(tips) == 0:
        strength = "Strong"
    elif len(password) < 8:
        strength = "Weak"
    else:
        strength = "Medium"

    return strength, tips


# --- Test it out ---
test_passwords = ["hello", "HelloWorld", "Hello123", "MyP@ssw0rd!", "12345678"]

for pw in test_passwords:
    strength, tips = check_password(pw)
    masked = pw[0] + "*" * (len(pw) - 2) + pw[-1] if len(pw) > 2 else pw
    print(f"\n  Password: {masked}")
    print(f"  Strength: {strength}")
    if tips:
        print(f"  Tips: {', '.join(tips)}")
    else:
        print("  Tips: None needed — you're a security legend!")
```

- [ ] **Step 4: Commit**

```bash
git add code/sprint-2-intermediate/chapter-10-functions/
git commit -m "feat: add Chapter 10 code examples and exercises"
```

### Task 13: Chapters 11-14 + Sprint 2 Checkpoint (Code)

**Files:**
- Create: `code/sprint-2-intermediate/chapter-11-modules/examples.py`
- Create: `code/sprint-2-intermediate/chapter-11-modules/exercises/{your_turn,solution}.py`
- Create: `code/sprint-2-intermediate/chapter-11-modules/exercises/quotes.json`
- Create: `code/sprint-2-intermediate/chapter-12-files/examples.py`
- Create: `code/sprint-2-intermediate/chapter-12-files/exercises/{your_turn,solution}.py`
- Create: `code/sprint-2-intermediate/chapter-13-errors/examples.py`
- Create: `code/sprint-2-intermediate/chapter-13-errors/exercises/{your_turn,solution}.py`
- Create: `code/sprint-2-intermediate/chapter-14-lambda/examples.py`
- Create: `code/sprint-2-intermediate/chapter-14-lambda/exercises/{your_turn,solution}.py`
- Create: `code/sprint-2-intermediate/checkpoint-expense-tracker/{starter,solution}.py`

This task follows the exact same pattern as Tasks 2-10. Each chapter gets:
1. `examples.py` with all code from the chapter, fully commented, with the same fun tone
2. `exercises/your_turn.py` with the exercise prompt and hints
3. `exercises/solution.py` with the complete solution

**Chapter 11 exercise:** Random quote generator reading from `quotes.json`
**Chapter 12 exercise:** Diary app saving entries to a text file with timestamps
**Chapter 13 exercise:** Crash-proof tip calculator (wrap Chapter 3's calculator in try/except)
**Chapter 14 exercise:** Process student grades using lambda, map, filter, reduce

**Sprint 2 checkpoint:** Expense Tracker — CSV-based, with functions for add/view/categorize/summarize, error handling throughout.

- [ ] **Step 1: Create all Chapter 11 files**

Create `code/sprint-2-intermediate/chapter-11-modules/examples.py`:
```python
# Chapter 11: Modules & Packages — Standing on Giants' Shoulders

# --- Importing modules ---
import random
import datetime
import os
import math
import json

# --- random: The fun one ---
print(random.randint(1, 100))        # Random int between 1-100
print(random.choice(["🍕", "🍔", "🌮"]))  # Random pick from list
print(random.random())                # Random float 0.0 to 1.0

items = [1, 2, 3, 4, 5]
random.shuffle(items)                 # Shuffle in place
print(items)

print(random.sample(range(1, 50), 6)) # 6 unique random numbers (lottery!)

# --- datetime: Time is everything ---
now = datetime.datetime.now()
print(f"Right now: {now}")
print(f"Date: {now.strftime('%B %d, %Y')}")  # "April 01, 2026"
print(f"Time: {now.strftime('%I:%M %p')}")    # "02:30 PM"

birthday = datetime.date(2000, 6, 15)
days_alive = (datetime.date.today() - birthday).days
print(f"You've been alive for {days_alive:,} days!")

# --- os: Talking to your computer ---
print(f"Current directory: {os.getcwd()}")
print(f"Your username: {os.getenv('USERNAME', 'unknown')}")
print(f"Files here: {os.listdir('.')[:5]}")  # First 5 files

# --- math: For when things get mathy ---
print(f"Pi: {math.pi}")
print(f"Square root of 144: {math.sqrt(144)}")
print(f"Ceiling of 4.1: {math.ceil(4.1)}")   # 5
print(f"Floor of 4.9: {math.floor(4.9)}")     # 4

# --- json: Data's favorite format ---
data = {"name": "Alice", "scores": [90, 85, 92]}

# Convert dict to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)

# Convert JSON string back to dict
parsed = json.loads(json_string)
print(parsed["name"])

# --- from ... import (pick what you need) ---
from random import choice, randint
from datetime import datetime as dt

print(choice(["heads", "tails"]))
print(dt.now())

# --- Virtual environments (explained in the book, demo here) ---
# python -m venv venv
# source venv/bin/activate   (Mac/Linux)
# venv\Scripts\activate      (Windows)
# pip install requests
# pip freeze > requirements.txt
```

Create `code/sprint-2-intermediate/chapter-11-modules/exercises/quotes.json`:
```json
{
  "quotes": [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"text": "Experience is the name everyone gives to their mistakes.", "author": "Oscar Wilde"},
    {"text": "In order to be irreplaceable, one must always be different.", "author": "Coco Chanel"},
    {"text": "Java is to JavaScript what car is to carpet.", "author": "Chris Heilmann"},
    {"text": "Knowledge is power.", "author": "Francis Bacon"},
    {"text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"}
  ]
}
```

Create `code/sprint-2-intermediate/chapter-11-modules/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Random Quote Generator
# ============================================
# Build a program that:
#   1. Reads quotes from quotes.json (same folder)
#   2. Displays a random quote with the author
#   3. Shows the current date and time
#   4. Asks if the user wants another quote
#
# Hint: Use json, random, and datetime modules
# ============================================

import json
import random
from datetime import datetime


```

Create `code/sprint-2-intermediate/chapter-11-modules/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Random Quote Generator
# ============================================

import json
import random
from datetime import datetime
import os

# Load quotes from JSON file (same directory as this script)
script_dir = os.path.dirname(os.path.abspath(__file__))
quotes_path = os.path.join(script_dir, "quotes.json")

with open(quotes_path, "r") as f:
    data = json.load(f)

quotes = data["quotes"]

print("\n  💡 Random Quote Generator")
print(f"  {datetime.now().strftime('%B %d, %Y — %I:%M %p')}\n")

while True:
    quote = random.choice(quotes)
    print(f'  "{quote["text"]}"')
    print(f'    — {quote["author"]}\n')

    again = input("  Another quote? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("\n  Stay inspired! ✨\n")
        break
    print()
```

- [ ] **Step 2: Create all Chapter 12 files**

Create `code/sprint-2-intermediate/chapter-12-files/examples.py`:
```python
# Chapter 12: File Handling — Reading & Writing Like a Pro

# --- Writing to a file ---
with open("hello.txt", "w") as f:
    f.write("Hello, File World!\n")
    f.write("This is line 2.\n")

# --- Reading a file ---
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("hello.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Hello, File World!\n', 'This is line 2.\n']

# --- Appending (add to the end) ---
with open("hello.txt", "a") as f:
    f.write("This line was appended!\n")

# --- The 'with' statement ---
# It automatically closes the file when done.
# WITHOUT with (don't do this):
# f = open("file.txt", "r")
# content = f.read()
# f.close()  # Easy to forget!

# --- Working with CSV ---
import csv

# Writing CSV
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B+"],
    ["Charlie", 21, "A-"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

# Reading CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        print(f"{row[0]} is {row[1]} years old with grade {row[2]}")

# Reading CSV as dictionaries (even better!)
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']}: {row['Grade']}")

# --- Working with JSON files ---
import json

data = {
    "app": "Python Crash Course",
    "version": 1.0,
    "chapters": 32,
    "topics": ["basics", "OOP", "AI"],
}

# Write JSON
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("config.json", "r") as f:
    loaded = json.load(f)
    print(loaded["app"])
    print(loaded["topics"])

# --- Check if file exists ---
import os
if os.path.exists("hello.txt"):
    print("File exists!")
else:
    print("File not found.")

# Clean up demo files
for f in ["hello.txt", "students.csv", "config.json"]:
    if os.path.exists(f):
        os.remove(f)
```

Create `code/sprint-2-intermediate/chapter-12-files/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Diary App
# ============================================
# Build a diary app that:
#   1. Lets you write a new entry (saves with timestamp)
#   2. Lets you read all past entries
#   3. Saves entries to "diary.txt"
#   4. Each entry has: date, time, and the text
#
# Format in file:
#   [2026-04-01 14:30] Today I learned about files in Python!
#   [2026-04-01 15:00] I built a diary app. I'm basically a developer now.
# ============================================

from datetime import datetime


```

Create `code/sprint-2-intermediate/chapter-12-files/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Diary App
# ============================================

from datetime import datetime
import os

DIARY_FILE = "diary.txt"

def write_entry():
    """Write a new diary entry with timestamp."""
    entry = input("\n  What's on your mind?\n  > ").strip()
    if not entry:
        print("  Empty entry. Nothing saved.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(DIARY_FILE, "a") as f:
        f.write(f"[{timestamp}] {entry}\n")

    print("  Entry saved! 📝")

def read_entries():
    """Read and display all diary entries."""
    if not os.path.exists(DIARY_FILE):
        print("\n  No diary entries yet. Write your first one!")
        return

    with open(DIARY_FILE, "r") as f:
        entries = f.readlines()

    if not entries:
        print("\n  No diary entries yet.")
        return

    print(f"\n  📖 Your Diary ({len(entries)} entries)")
    print(f"  {'─' * 40}")
    for entry in entries:
        print(f"  {entry.strip()}")
    print(f"  {'─' * 40}")

# Main loop
print("\n  📓 My Diary App")

while True:
    print(f"\n  1. Write new entry")
    print(f"  2. Read all entries")
    print(f"  3. Quit")

    choice = input("\n  Choice: ").strip()

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("\n  See you tomorrow! 👋\n")
        break
```

- [ ] **Step 3: Create all Chapter 13 files**

Create `code/sprint-2-intermediate/chapter-13-errors/examples.py`:
```python
# Chapter 13: Error Handling — When Things Go Wrong (And They Will)

# --- Common exceptions ---

# TypeError: wrong type
# print("age: " + 25)  # Can't add str + int

# ValueError: right type, wrong value
# int("hello")  # Can't convert "hello" to int

# KeyError: key doesn't exist
# d = {"a": 1}
# print(d["b"])

# IndexError: index out of range
# lst = [1, 2, 3]
# print(lst[10])

# FileNotFoundError
# open("nonexistent.txt")

# ZeroDivisionError
# print(10 / 0)

# --- try/except ---
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")

# --- Catching multiple exceptions ---
try:
    data = [1, 2, 3]
    index = int(input("Enter an index: "))
    print(data[index])
except (ValueError, IndexError) as e:
    print(f"Error: {e}")

# --- else and finally ---
try:
    f = open("test_file.txt", "w")
    f.write("Hello!")
except IOError:
    print("Could not write to file!")
else:
    print("File written successfully!")  # Runs if NO exception
finally:
    f.close()  # ALWAYS runs, even if there's an exception
    print("File closed.")

import os
os.remove("test_file.txt")

# --- Raising your own exceptions ---
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Are you a vampire?")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")

# --- Custom exception classes ---
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Balance: ${balance:.2f}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100.00, 150.00)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"You're short by ${e.amount - e.balance:.2f}")

# --- Debugging tips ---
# 1. Read the error message — Python tells you what went wrong AND where
# 2. Use print() to check variable values at different points
# 3. Use breakpoint() for interactive debugging
# 4. Google the error — someone else has had it too
# 5. Check the line BEFORE the error line — that's often where the bug is
```

Create `code/sprint-2-intermediate/chapter-13-errors/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Crash-Proof Tip Calculator
# ============================================
# Remember the tip calculator from Chapter 3?
# Now make it crash-proof! Handle:
#   - Non-numeric bill amounts
#   - Negative numbers
#   - Zero people splitting
#   - Tip percentages over 100% (warn but allow)
#   - Empty inputs
#
# The program should NEVER crash, no matter what
# the user types. It should show friendly error
# messages and ask again.
# ============================================


```

Create `code/sprint-2-intermediate/chapter-13-errors/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Crash-Proof Tip Calculator
# ============================================

def get_float(prompt, min_val=None, max_val=None):
    """Get a valid float from user with optional range check."""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  Please enter a value of at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Please enter a value no more than {max_val}.")
                continue
            return value
        except ValueError:
            print("  That's not a valid number. Try again!")

def get_int(prompt, min_val=1):
    """Get a valid integer from user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"  Please enter at least {min_val}.")
                continue
            return value
        except ValueError:
            print("  That's not a valid whole number. Try again!")

print(f"\n{'=' * 35}")
print("  💰 Crash-Proof Tip Calculator")
print(f"{'=' * 35}")

bill = get_float("  Total bill: $", min_val=0.01)
tip_percent = get_float("  Tip percentage: ", min_val=0)

if tip_percent > 100:
    print(f"  Wow, {tip_percent}%? You're incredibly generous! 🎉")

people = get_int("  Splitting between how many people? ", min_val=1)

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print(f"\n{'=' * 35}")
print(f"  Bill:              ${bill:.2f}")
print(f"  Tip ({tip_percent:.0f}%):         ${tip_amount:.2f}")
print(f"  Total:             ${total:.2f}")
print(f"  Per person ({people}):    ${per_person:.2f}")
print(f"{'=' * 35}")
print("  No crashes. Professional. 😎\n")
```

- [ ] **Step 4: Create all Chapter 14 files**

Create `code/sprint-2-intermediate/chapter-14-lambda/examples.py`:
```python
# Chapter 14: Lambda, Map, Filter, Reduce — The One-Liners

# --- Lambda functions ---
# A lambda is a tiny function you write in one line.
# Regular function:
def double(x):
    return x * 2

# Same thing as a lambda:
double = lambda x: x * 2

print(double(5))  # 10

# Lambdas shine when used INSIDE other functions:
pairs = [(1, "b"), (3, "a"), (2, "c")]
pairs.sort(key=lambda pair: pair[1])  # Sort by second element
print(pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# --- map() — transform everything ---
# Apply a function to every item in a list
numbers = [1, 2, 3, 4, 5]

# The old way:
doubled = []
for n in numbers:
    doubled.append(n * 2)

# The map() way:
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Practical: convert strings to ints
string_numbers = ["1", "2", "3", "4"]
real_numbers = list(map(int, string_numbers))
print(real_numbers)  # [1, 2, 3, 4]

# --- filter() — keep only the good stuff ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Practical: filter out empty strings
data = ["Alice", "", "Bob", "", "", "Charlie"]
clean = list(filter(None, data))  # None removes falsy values
print(clean)  # ['Alice', 'Bob', 'Charlie']

# Practical: filter students with passing grades
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 38},
]

passing = list(filter(lambda s: s["grade"] >= 50, students))
print([s["name"] for s in passing])  # ['Alice', 'Charlie']

# --- reduce() — boil it all down to one value ---
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers (reduce takes 2 args at a time)
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 15

# Find the longest word
words = ["Python", "is", "absolutely", "fantastic"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)  # "absolutely"

# --- When to use what ---
# map():     "Transform each item"     → list comprehension is usually cleaner
# filter():  "Keep items that match"    → list comprehension is usually cleaner
# reduce():  "Combine everything"       → sometimes cleaner than a loop
# lambda:    "Quick throwaway function" → keep it simple, one expression only

# List comprehension alternatives (often preferred):
doubled = [x * 2 for x in numbers]           # Instead of map
evens = [x for x in numbers if x % 2 == 0]   # Instead of filter
```

Create `code/sprint-2-intermediate/chapter-14-lambda/exercises/your_turn.py`:
```python
# ============================================
# YOUR TURN: Student Grade Processor
# ============================================
# Given this list of students with their scores:
students = [
    {"name": "Alice", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "scores": [62, 55, 70, 58]},
    {"name": "Charlie", "scores": [95, 98, 92, 97]},
    {"name": "Diana", "scores": [40, 35, 42, 38]},
    {"name": "Eve", "scores": [75, 80, 72, 78]},
]

# Using lambda, map, filter, and reduce:
# 1. Use map() to calculate each student's average score
# 2. Use filter() to find students with average >= 70
# 3. Use reduce() to find the student with the highest average
# 4. Use map() to assign letter grades (A: 90+, B: 80+, C: 70+, D: 60+, F: <60)
#
# Print a nice report card for each student.
# ============================================

from functools import reduce


```

Create `code/sprint-2-intermediate/chapter-14-lambda/exercises/solution.py`:
```python
# ============================================
# SOLUTION: Student Grade Processor
# ============================================

from functools import reduce

students = [
    {"name": "Alice", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "scores": [62, 55, 70, 58]},
    {"name": "Charlie", "scores": [95, 98, 92, 97]},
    {"name": "Diana", "scores": [40, 35, 42, 38]},
    {"name": "Eve", "scores": [75, 80, 72, 78]},
]

# 1. Calculate averages using map
with_averages = list(map(
    lambda s: {**s, "average": sum(s["scores"]) / len(s["scores"])},
    students
))

# 2. Filter passing students (average >= 70)
passing = list(filter(lambda s: s["average"] >= 70, with_averages))

# 3. Find top student using reduce
top_student = reduce(
    lambda a, b: a if a["average"] > b["average"] else b,
    with_averages
)

# 4. Assign letter grades using map
def get_letter(avg):
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

final_report = list(map(
    lambda s: {**s, "letter": get_letter(s["average"])},
    with_averages
))

# Print report
print(f"\n  {'=' * 45}")
print(f"  📊 Student Report Card")
print(f"  {'=' * 45}")

for s in final_report:
    status = "✅ PASS" if s["average"] >= 70 else "❌ FAIL"
    print(f"  {s['name']:<10} | Avg: {s['average']:>5.1f} | Grade: {s['letter']} | {status}")

print(f"  {'=' * 45}")
print(f"  🏆 Top student: {top_student['name']} ({top_student['average']:.1f})")
print(f"  📈 Passing: {len(passing)}/{len(students)} students")
print(f"  {'=' * 45}\n")
```

- [ ] **Step 5: Create Sprint 2 checkpoint project**

Create `code/sprint-2-intermediate/checkpoint-expense-tracker/starter.py`:
```python
# ============================================
# SPRINT 2 CHECKPOINT: Expense Tracker
# ============================================
# Build an expense tracker that:
#   1. Add expense (amount, category, description)
#   2. View all expenses
#   3. View expenses by category
#   4. View summary (total, by category, average)
#   5. Save/load expenses to/from CSV file
#   6. Quit
#
# Skills: CSV files, functions, dictionaries, error handling, lambdas
# ============================================

import csv
import os
from datetime import datetime


```

Create `code/sprint-2-intermediate/checkpoint-expense-tracker/solution.py`:
```python
# ============================================
# SOLUTION: Expense Tracker
# ============================================

import csv
import os
from datetime import datetime
from functools import reduce

EXPENSES_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]

def load_expenses():
    """Load expenses from CSV file."""
    expenses = []
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    """Save all expenses to CSV file."""
    with open(EXPENSES_FILE, "w", newline="") as f:
        fieldnames = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    """Add a new expense."""
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    try:
        cat_choice = int(input("  Pick a category (1-6): "))
        if not 1 <= cat_choice <= 6:
            print("  Invalid choice.")
            return
        category = CATEGORIES[cat_choice - 1]

        amount = float(input("  Amount: $"))
        if amount <= 0:
            print("  Amount must be positive.")
            return

        description = input("  Description: ").strip()
        if not description:
            description = "No description"

        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "amount": amount,
            "category": category,
            "description": description,
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(f"  Added ${amount:.2f} for {category}! 💸")

    except ValueError:
        print("  Invalid input. Try again.")

def view_all(expenses):
    """Display all expenses."""
    if not expenses:
        print("\n  No expenses yet. Start spending! (responsibly)")
        return

    print(f"\n  {'Date':<18} {'Amount':>8}  {'Category':<15} {'Description'}")
    print(f"  {'─' * 65}")
    for e in expenses:
        print(f"  {e['date']:<18} ${e['amount']:>7.2f}  {e['category']:<15} {e['description']}")
    print(f"  {'─' * 65}")
    total = sum(e["amount"] for e in expenses)
    print(f"  {'TOTAL':<18} ${total:>7.2f}")

def view_by_category(expenses):
    """View expenses filtered by category."""
    if not expenses:
        print("\n  No expenses yet.")
        return

    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    try:
        choice = int(input("  Pick a category: "))
        category = CATEGORIES[choice - 1]
    except (ValueError, IndexError):
        print("  Invalid choice.")
        return

    filtered = list(filter(lambda e: e["category"] == category, expenses))

    if not filtered:
        print(f"\n  No expenses in {category}.")
        return

    print(f"\n  📂 {category} expenses:")
    for e in filtered:
        print(f"    {e['date']} — ${e['amount']:.2f} — {e['description']}")

    total = sum(e["amount"] for e in filtered)
    print(f"\n  Total for {category}: ${total:.2f}")

def show_summary(expenses):
    """Show spending summary."""
    if not expenses:
        print("\n  No expenses to summarize.")
        return

    total = reduce(lambda a, b: a + b["amount"], expenses, 0)
    avg = total / len(expenses)

    # Group by category
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]

    top_category = max(by_category, key=by_category.get)

    print(f"\n  {'=' * 40}")
    print(f"  📊 Expense Summary")
    print(f"  {'=' * 40}")
    print(f"  Total expenses:   {len(expenses)}")
    print(f"  Total spent:      ${total:.2f}")
    print(f"  Average expense:  ${avg:.2f}")
    print(f"  Top category:     {top_category} (${by_category[top_category]:.2f})")
    print(f"\n  By category:")
    for cat, amount in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(amount / total * 20)
        print(f"    {cat:<15} ${amount:>8.2f}  {bar}")
    print(f"  {'=' * 40}")

# --- Main Program ---
expenses = load_expenses()

print(f"\n{'=' * 35}")
print("  💰 Expense Tracker")
print(f"{'=' * 35}")

while True:
    print(f"\n  1. Add expense")
    print(f"  2. View all expenses")
    print(f"  3. View by category")
    print(f"  4. Summary")
    print(f"  5. Quit")

    choice = input("\n  Choice: ").strip()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_all(expenses)
    elif choice == "3":
        view_by_category(expenses)
    elif choice == "4":
        show_summary(expenses)
    elif choice == "5":
        print("\n  Keep tracking! Your wallet thanks you. 👋\n")
        break
```

- [ ] **Step 6: Commit all Sprint 2 code**

```bash
git add code/sprint-2-intermediate/
git commit -m "feat: add Sprint 2 code examples, exercises, and checkpoint project"
```

---

## Phase 3: Sprint 3 OOP Code (Tasks 14-18)

### Task 14: Chapters 15-18 + Sprint 3 Checkpoint (Code)

Follows same pattern as previous tasks. Each chapter gets `examples.py`, `exercises/your_turn.py`, `exercises/solution.py`.

**Chapter 15:** Classes & Objects — Dog class, pizza shop analogy, `__init__`, `self`
**Chapter 16:** Inheritance — Vehicle → Car → ElectricCar hierarchy
**Chapter 17:** Magic Methods — `Money` class with `__add__`, `__str__`, `__eq__`
**Chapter 18:** Design Principles — Composition refactoring of vehicle hierarchy

**Sprint 3 Checkpoint:** Library Management System with Book, Member, Library classes, file persistence via JSON.

- [ ] **Step 1: Create Chapter 15 files** — Full OOP intro with Dog class, attributes, methods
- [ ] **Step 2: Create Chapter 16 files** — Inheritance with vehicle hierarchy
- [ ] **Step 3: Create Chapter 17 files** — Magic methods with Money class
- [ ] **Step 4: Create Chapter 18 files** — Design principles, composition refactoring
- [ ] **Step 5: Create checkpoint project** — Library system starter + solution
- [ ] **Step 6: Commit**

```bash
git add code/sprint-3-oop/
git commit -m "feat: add Sprint 3 OOP code examples, exercises, and checkpoint project"
```

---

## Phase 4: Sprint 4 Pro Code (Tasks 15-22)

### Task 15: Chapters 19-25 + Sprint 4 Checkpoint (Code)

**Chapter 19:** Decorators — `@timer` decorator, closures, `@property`
**Chapter 20:** Generators — Fibonacci generator, `yield`, generator expressions
**Chapter 21:** APIs — Weather checker using requests + free API
**Chapter 22:** Databases — SQLite CRUD, expense tracker conversion
**Chapter 23:** Web Scraping — BeautifulSoup, ethical scraping guide
**Chapter 24:** Testing — pytest, TDD intro, test the password checker
**Chapter 25:** Clean Code — type hints, black, pylint, PEP 8

**Sprint 4 Checkpoint:** Job Listing Scraper with SQLite storage, CLI dashboard, decorators, tests.

- [ ] **Step 1: Create Chapter 19 files** — Decorators with timer example
- [ ] **Step 2: Create Chapter 20 files** — Generators with Fibonacci
- [ ] **Step 3: Create Chapter 21 files** — API examples with requests
- [ ] **Step 4: Create Chapter 22 files** — SQLite CRUD operations
- [ ] **Step 5: Create Chapter 23 files** — BeautifulSoup scraping
- [ ] **Step 6: Create Chapter 24 files** — pytest examples and tests
- [ ] **Step 7: Create Chapter 25 files** — Type hints and linting
- [ ] **Step 8: Create checkpoint project** — Job scraper starter + solution
- [ ] **Step 9: Commit**

```bash
git add code/sprint-4-pro/
git commit -m "feat: add Sprint 4 advanced code examples, exercises, and checkpoint project"
```

---

## Phase 5: Sprint 5 AI Code (Tasks 16-24)

### Task 16: Chapters 26-32 + Sprint 5 Checkpoint (Code)

**Chapter 26:** NumPy — arrays, broadcasting, student scores processing
**Chapter 27:** Pandas — DataFrames, movie ratings dataset analysis
**Chapter 28:** Visualization — matplotlib, seaborn, plotly dashboard
**Chapter 29:** ML — scikit-learn, house prices, spam classifier
**Chapter 30:** AI APIs — OpenAI/Gemini chatbot, prompt engineering
**Chapter 31:** LangChain — RAG, PDF Q&A bot, AI agents
**Chapter 32:** Automation — file ops, email, Selenium browser automation

**Sprint 5 Checkpoint:** AI-Powered Resume Analyzer.

- [ ] **Step 1: Create Chapter 26 files** — NumPy arrays and operations
- [ ] **Step 2: Create Chapter 27 files** — Pandas DataFrames
- [ ] **Step 3: Create Chapter 28 files** — Visualization examples
- [ ] **Step 4: Create Chapter 29 files** — ML with scikit-learn
- [ ] **Step 5: Create Chapter 30 files** — OpenAI/Gemini API examples
- [ ] **Step 6: Create Chapter 31 files** — LangChain and RAG
- [ ] **Step 7: Create Chapter 32 files** — Automation scripts
- [ ] **Step 8: Create checkpoint project** — Resume analyzer starter + solution
- [ ] **Step 9: Commit**

```bash
git add code/sprint-5-ai/
git commit -m "feat: add Sprint 5 AI/ML code examples, exercises, and checkpoint project"
```

---

## Phase 6: Final 10 Projects Code

### Task 17: Projects 1-5 (Code)

- [ ] **Step 1: Project 1 — Quiz Game** (starter + solution)
- [ ] **Step 2: Project 2 — Budget Tracker** (starter + solution)
- [ ] **Step 3: Project 3 — To-Do App CLI** (starter + solution)
- [ ] **Step 4: Project 4 — Hangman** (starter + solution)
- [ ] **Step 5: Project 5 — Weather Dashboard** (starter + solution)
- [ ] **Step 6: Commit**

```bash
git add code/final-projects/project-0{1,2,3,4,5}*/
git commit -m "feat: add Final Projects 1-5 code"
```

### Task 18: Projects 6-10 (Code)

- [ ] **Step 1: Project 6 — Web Scraper & Analyzer** (starter + solution)
- [ ] **Step 2: Project 7 — Chat App CLI** (starter + solution)
- [ ] **Step 3: Project 8 — Blog REST API** (starter + solution)
- [ ] **Step 4: Project 9 — ML Prediction App** (starter + solution)
- [ ] **Step 5: Project 10 — AI Study Buddy** (starter + solution)
- [ ] **Step 6: Commit**

```bash
git add code/final-projects/project-{06,07,08,09,10}*/
git commit -m "feat: add Final Projects 6-10 code"
```

---

## Phase 7: Write the Book — Front Matter & Sprint 1 Chapters

### Task 19: Front Matter

**Files:**
- Create: `book/front-matter/title-page.md`
- Create: `book/front-matter/copyright.md`
- Create: `book/front-matter/dedication.md`
- Create: `book/front-matter/how-to-use-this-book.md`
- Create: `book/front-matter/what-you-need.md`

Each chapter follows this Markdown template:

```markdown
# Chapter Title

> **Sprint X** | **Estimated read: 10-15 min** | **Code: github.com/<user>/python-crash-course/sprint-X/chapter-XX/**

*Opening hook — funny, relatable, sets the stage*

## What You'll Learn
- Bullet 1
- Bullet 2
- Bullet 3

## [First Concept]

Explanation with analogy...

```python
# Code example
```

> **Wait, What?** Common confusion point explained here.

## [Second Concept]

...

> **Pro Tip:** For readers who know another language...

## Your Turn 🎯

*Exercise description with clear steps*

## TL;DR

- Key takeaway 1
- Key takeaway 2
- Key takeaway 3
```

- [ ] **Step 1: Write title-page.md**
- [ ] **Step 2: Write copyright.md**
- [ ] **Step 3: Write dedication.md**
- [ ] **Step 4: Write how-to-use-this-book.md** — Sprint model explanation, GitHub link, callout box guide, the "do it, come back" rhythm
- [ ] **Step 5: Write what-you-need.md** — Python 3.12+, VS Code, internet, GitHub account
- [ ] **Step 6: Commit**

```bash
git add book/front-matter/
git commit -m "feat: write book front matter"
```

### Task 20: Sprint 1 Chapters (Book Content)

**Files:** `book/sprint-1/sprint-1-intro.md`, `book/sprint-1/chapter-01.md` through `book/sprint-1/chapter-08.md`, `book/sprint-1/sprint-1-checkpoint.md`

Each chapter must:
- Open with a funny hook or relatable situation
- Use the tone: friendly, funny, pop culture references, memes referenced
- Include all callout boxes (Wait What?, Pro Tip, TL;DR, Your Turn)
- Keep paragraphs short (3-4 sentences max)
- Reference the GitHub repo for code
- End with "Your Turn" exercise and TL;DR

- [ ] **Step 1: Write sprint-1-intro.md** — Welcome to Sprint 1, what you'll learn, pep talk
- [ ] **Step 2: Write chapter-01.md** — Why Python, setup, Hello World
- [ ] **Step 3: Write chapter-02.md** — Variables, types, f-strings
- [ ] **Step 4: Write chapter-03.md** — Numbers, math, input(), tip calculator
- [ ] **Step 5: Write chapter-04.md** — Strings, slicing, methods, username generator
- [ ] **Step 6: Write chapter-05.md** — if/elif/else, logical operators, movie classifier
- [ ] **Step 7: Write chapter-06.md** — Lists, list comprehensions, grocery manager
- [ ] **Step 8: Write chapter-07.md** — Loops, range, break/continue, multiplication table
- [ ] **Step 9: Write chapter-08.md** — Tuples, sets, set operations, playlist deduper
- [ ] **Step 10: Write sprint-1-checkpoint.md** — Mad Libs project guide
- [ ] **Step 11: Commit**

```bash
git add book/sprint-1/
git commit -m "feat: write Sprint 1 book chapters"
```

---

## Phase 8: Write the Book — Sprint 2-5 Chapters

### Task 21: Sprint 2 Chapters

- [ ] **Step 1: Write sprint-2-intro.md**
- [ ] **Step 2: Write chapter-09.md** — Dictionaries
- [ ] **Step 3: Write chapter-10.md** — Functions
- [ ] **Step 4: Write chapter-11.md** — Modules & Packages
- [ ] **Step 5: Write chapter-12.md** — File Handling
- [ ] **Step 6: Write chapter-13.md** — Error Handling
- [ ] **Step 7: Write chapter-14.md** — Lambda, Map, Filter, Reduce
- [ ] **Step 8: Write sprint-2-checkpoint.md** — Expense Tracker project guide
- [ ] **Step 9: Commit**

```bash
git add book/sprint-2/
git commit -m "feat: write Sprint 2 book chapters"
```

### Task 22: Sprint 3 Chapters

- [ ] **Step 1: Write sprint-3-intro.md**
- [ ] **Step 2: Write chapter-15.md** — Classes & Objects (shorter, more analogies)
- [ ] **Step 3: Write chapter-16.md** — Inheritance (Don't Panic box, Remember When? callbacks)
- [ ] **Step 4: Write chapter-17.md** — Magic Methods (Why Should I Care? opener)
- [ ] **Step 5: Write chapter-18.md** — Design Principles (extra encouragement)
- [ ] **Step 6: Write sprint-3-checkpoint.md** — Library system project guide
- [ ] **Step 7: Commit**

```bash
git add book/sprint-3/
git commit -m "feat: write Sprint 3 OOP book chapters"
```

### Task 23: Sprint 4 Chapters

Note: Chapters get shorter as complexity increases. More analogies. More "Don't Panic" and "Remember When?" callouts.

- [ ] **Step 1: Write sprint-4-intro.md** — "If you're here, you're already in the top 10%"
- [ ] **Step 2: Write chapter-19.md** — Decorators (gift wrapping analogy)
- [ ] **Step 3: Write chapter-20.md** — Generators (lazy lists callback)
- [ ] **Step 4: Write chapter-21.md** — APIs (restaurant analogy, very step-by-step)
- [ ] **Step 5: Write chapter-22.md** — Databases (filing cabinet analogy)
- [ ] **Step 6: Write chapter-23.md** — Web Scraping (with ethics discussion)
- [ ] **Step 7: Write chapter-24.md** — Testing (safety net analogy)
- [ ] **Step 8: Write chapter-25.md** — Clean Code (future self analogy)
- [ ] **Step 9: Write sprint-4-checkpoint.md** — Job scraper project guide
- [ ] **Step 10: Commit**

```bash
git add book/sprint-4/
git commit -m "feat: write Sprint 4 advanced book chapters"
```

### Task 24: Sprint 5 Chapters

Note: Maximum encouragement. "You're building AI apps now. That's not normal beginner stuff." Shortest chapters in the book. Most examples per concept.

- [ ] **Step 1: Write sprint-5-intro.md** — "Welcome to the future. You're building it."
- [ ] **Step 2: Write chapter-26.md** — NumPy (supercharged lists analogy)
- [ ] **Step 3: Write chapter-27.md** — Pandas (Excel on steroids)
- [ ] **Step 4: Write chapter-28.md** — Visualization (making data talk)
- [ ] **Step 5: Write chapter-29.md** — ML 101 (teaching a toddler analogy)
- [ ] **Step 6: Write chapter-30.md** — AI APIs (giving your code a brain)
- [ ] **Step 7: Write chapter-31.md** — LangChain (AI with memory)
- [ ] **Step 8: Write chapter-32.md** — Automation (robots doing your chores)
- [ ] **Step 9: Write sprint-5-checkpoint.md** — Resume analyzer project guide
- [ ] **Step 10: Commit**

```bash
git add book/sprint-5/
git commit -m "feat: write Sprint 5 AI/ML book chapters"
```

---

## Phase 9: Write Final Projects & Back Matter

### Task 25: Final Zone — 10 Project Guides

Each project guide follows this template:
```markdown
# Project X: [Name]

> **Difficulty:** ⭐⭐⭐ (out of 5) | **Time:** ~2-3 hours | **Skills:** list of skills

## What You'll Build
One paragraph + screenshot/mockup description

## Skills You'll Use
- Skill 1 (Chapter X)
- Skill 2 (Chapter Y)

## Step-by-Step Build Guide
### Step 1: ...
### Step 2: ...

## Challenges (Level Up!)
- Challenge 1: extend feature
- Challenge 2: harder extension

## Portfolio Tips 💼
How to present this project to employers
```

- [ ] **Step 1: Write final-zone-intro.md**
- [ ] **Step 2: Write project-01.md** — Quiz Game
- [ ] **Step 3: Write project-02.md** — Budget Tracker
- [ ] **Step 4: Write project-03.md** — To-Do App
- [ ] **Step 5: Write project-04.md** — Hangman
- [ ] **Step 6: Write project-05.md** — Weather Dashboard
- [ ] **Step 7: Write project-06.md** — Web Scraper
- [ ] **Step 8: Write project-07.md** — Chat App
- [ ] **Step 9: Write project-08.md** — Blog REST API
- [ ] **Step 10: Write project-09.md** — ML Prediction App
- [ ] **Step 11: Write project-10.md** — AI Study Buddy
- [ ] **Step 12: Commit**

```bash
git add book/final-projects/
git commit -m "feat: write Final Zone 10 project guides"
```

### Task 26: Back Matter

- [ ] **Step 1: Write appendix-a-cheat-sheet.md** — Python syntax quick reference
- [ ] **Step 2: Write appendix-b-common-errors.md** — Top 20 Python errors explained simply
- [ ] **Step 3: Write appendix-c-what-next.md** — Career paths: web dev, data science, AI/ML, DevOps
- [ ] **Step 4: Write appendix-d-resources.md** — YouTube channels, websites, communities
- [ ] **Step 5: Write about-author.md**
- [ ] **Step 6: Commit**

```bash
git add book/back-matter/
git commit -m "feat: write book back matter and appendices"
```

---

## Phase 10: Final Assembly

### Task 27: Assemble the Manuscript

- [ ] **Step 1: Create assembly script**

Create `book/assemble.py`:
```python
"""Assemble all chapter Markdown files into a single manuscript."""
import os

BOOK_ORDER = [
    "front-matter/title-page.md",
    "front-matter/copyright.md",
    "front-matter/dedication.md",
    "front-matter/how-to-use-this-book.md",
    "front-matter/what-you-need.md",
    "sprint-1/sprint-1-intro.md",
    *[f"sprint-1/chapter-{i:02d}.md" for i in range(1, 9)],
    "sprint-1/sprint-1-checkpoint.md",
    "sprint-2/sprint-2-intro.md",
    *[f"sprint-2/chapter-{i:02d}.md" for i in range(9, 15)],
    "sprint-2/sprint-2-checkpoint.md",
    "sprint-3/sprint-3-intro.md",
    *[f"sprint-3/chapter-{i:02d}.md" for i in range(15, 19)],
    "sprint-3/sprint-3-checkpoint.md",
    "sprint-4/sprint-4-intro.md",
    *[f"sprint-4/chapter-{i:02d}.md" for i in range(19, 26)],
    "sprint-4/sprint-4-checkpoint.md",
    "sprint-5/sprint-5-intro.md",
    *[f"sprint-5/chapter-{i:02d}.md" for i in range(26, 33)],
    "sprint-5/sprint-5-checkpoint.md",
    "final-projects/final-zone-intro.md",
    *[f"final-projects/project-{i:02d}.md" for i in range(1, 11)],
    "back-matter/appendix-a-cheat-sheet.md",
    "back-matter/appendix-b-common-errors.md",
    "back-matter/appendix-c-what-next.md",
    "back-matter/appendix-d-resources.md",
    "back-matter/about-author.md",
]

book_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(book_dir, "manuscript.md")

with open(output_path, "w", encoding="utf-8") as out:
    for filename in BOOK_ORDER:
        filepath = os.path.join(book_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                out.write(f.read())
            out.write("\n\n---\n\n")  # Page break between sections
        else:
            print(f"WARNING: Missing file: {filename}")

print(f"Manuscript assembled: {output_path}")
print(f"Total files: {len(BOOK_ORDER)}")
```

- [ ] **Step 2: Run assembly**

```bash
cd /c/Users/vinay/projects/python-crash-course
python book/assemble.py
```

- [ ] **Step 3: Verify manuscript**

```bash
wc -l book/manuscript.md
wc -w book/manuscript.md
```

- [ ] **Step 4: Final commit**

```bash
git add book/assemble.py book/manuscript.md
git commit -m "feat: assemble complete book manuscript"
```

---

## Summary

| Phase | Tasks | What Gets Built |
|-------|-------|----------------|
| 0 | 1 | Git repo, scaffolding, README |
| 1 | 2-10 | Sprint 1 code (8 chapters + checkpoint) |
| 2 | 11-13 | Sprint 2 code (6 chapters + checkpoint) |
| 3 | 14 | Sprint 3 code (4 chapters + checkpoint) |
| 4 | 15 | Sprint 4 code (7 chapters + checkpoint) |
| 5 | 16 | Sprint 5 code (7 chapters + checkpoint) |
| 6 | 17-18 | Final 10 projects code |
| 7 | 19-20 | Front matter + Sprint 1 book chapters |
| 8 | 21-24 | Sprint 2-5 book chapters |
| 9 | 25-26 | Final project guides + back matter |
| 10 | 27 | Assembly script + final manuscript |
