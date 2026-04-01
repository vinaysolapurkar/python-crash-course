"""
Chapter 11: Modules & Packages -- Standing on the Shoulders of Giants
=====================================================================
Why reinvent the wheel when Python has a module for almost everything?

Modules are just .py files with reusable code. Python's standard library
has HUNDREDS of them, and there are MILLIONS more on PyPI (pip install).

Think of modules as cheat codes -- someone already wrote the hard stuff.
Let's learn how to use them!
"""

# =============================================================================
# 1. IMPORT STYLES -- Many Ways to Bring in Code
# =============================================================================
print("=== Import Styles ===")

# Style 1: Import the whole module
import math
print(f"Pi: {math.pi}")  # Need the prefix: math.pi

# Style 2: Import specific things (no prefix needed)
from math import sqrt, ceil, floor
print(f"sqrt(144) = {sqrt(144)}")  # 12.0 -- no math. prefix!

# Style 3: Import with an alias (nickname)
import datetime as dt
print(f"Module alias: {dt.datetime.now()}")

# Style 4: Import specific thing with alias
from math import factorial as fact
print(f"10! = {fact(10)}")  # 3628800

# Style 5: Import everything (NOT recommended -- pollutes your namespace!)
# from math import *  # Avoid this! You won't know where functions came from.

# =============================================================================
# 2. THE random MODULE -- For When You Need Chaos
# =============================================================================
print("\n=== random Module -- Embrace the Chaos ===")
import random

# randint(a, b) -- random integer between a and b (inclusive!)
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# choice() -- pick a random item from a sequence
foods = ["pizza", "sushi", "tacos", "ramen", "burgers"]
lunch = random.choice(foods)
print(f"Today's lunch: {lunch}  (the RNG has spoken!)")

# sample(population, k) -- pick k unique random items (no repeats)
lottery = random.sample(range(1, 50), 6)
print(f"Lottery numbers: {sorted(lottery)}")

# shuffle() -- randomly reorder a list IN-PLACE
deck = ["Ace", "King", "Queen", "Jack", "10"]
random.shuffle(deck)
print(f"Shuffled hand: {deck}")

# random() -- float between 0.0 and 1.0
print(f"Random float: {random.random():.4f}")

# uniform(a, b) -- float between a and b
temp = random.uniform(60.0, 100.0)
print(f"Random temp: {temp:.1f}F")

# Seed for reproducibility -- same seed = same "random" numbers
random.seed(42)  # The answer to life, the universe, and everything
print(f"Seeded randint: {random.randint(1, 100)}")  # Always 82 with seed 42
print(f"Seeded randint: {random.randint(1, 100)}")  # Always 15 with seed 42

# =============================================================================
# 3. THE datetime MODULE -- Time is an Illusion (Lunchtime Doubly So)
# =============================================================================
print("\n=== datetime Module -- Master of Time ===")
from datetime import datetime, timedelta, date

# Current date and time
now = datetime.now()
print(f"Right now: {now}")
print(f"Just the date: {now.date()}")
print(f"Just the time: {now.time()}")

# Access individual components
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}")

# strftime() -- format dates as strings (str-f-time = string format time)
print(f"Formatted: {now.strftime('%B %d, %Y')}")          # April 01, 2026
print(f"Short: {now.strftime('%m/%d/%Y')}")                # 04/01/2026
print(f"With time: {now.strftime('%I:%M %p')}")            # 02:30 PM (example)
print(f"Day of week: {now.strftime('%A')}")                # Wednesday (example)

# Common format codes:
# %Y = 4-digit year, %m = month (01-12), %d = day (01-31)
# %H = hour 24h, %I = hour 12h, %M = minute, %S = second
# %p = AM/PM, %A = weekday name, %B = month name

# Date math with timedelta -- add or subtract time!
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"\nTomorrow: {tomorrow.strftime('%A, %B %d')}")
print(f"Last week: {last_week.strftime('%A, %B %d')}")

# How many days until New Year?
new_year = datetime(now.year + 1, 1, 1)
days_left = (new_year - now).days
print(f"Days until New Year: {days_left}")

# Create a specific date
moon_landing = date(1969, 7, 20)
days_since = (date.today() - moon_landing).days
print(f"Days since moon landing: {days_since:,}")

# =============================================================================
# 4. THE os MODULE -- Talk to Your Operating System
# =============================================================================
print("\n=== os Module -- System Whisperer ===")
import os

# Get current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# List files in current directory
files = os.listdir(".")
print(f"Files here: {files[:5]}...")  # Show first 5

# Environment variables -- your system's secret settings
path = os.getenv("PATH", "not found")
print(f"PATH (first 80 chars): {path[:80]}...")

user = os.getenv("USERNAME") or os.getenv("USER", "unknown")
print(f"Current user: {user}")

# Check if a path exists
print(f"Does '.' exist? {os.path.exists('.')}")  # True (current dir)
print(f"Is it a directory? {os.path.isdir('.')}")  # True

# Join paths safely (handles / vs \ for you!)
config_path = os.path.join("home", "user", "config.json")
print(f"Joined path: {config_path}")

# Get file extension
filename = "report_final_FINAL_v2.xlsx"
name, ext = os.path.splitext(filename)
print(f"Name: {name}, Extension: {ext}")

# =============================================================================
# 5. THE math MODULE -- For Your Inner Mathematician
# =============================================================================
print("\n=== math Module -- Big Brain Energy ===")
import math

print(f"Pi: {math.pi}")                          # 3.141592653589793
print(f"Euler's number (e): {math.e}")            # 2.718281828459045
print(f"Infinity: {math.inf}")                    # inf (useful for comparisons)

print(f"\nsqrt(256) = {math.sqrt(256)}")          # 16.0
print(f"ceil(4.1) = {math.ceil(4.1)}")            # 5 (round UP)
print(f"floor(4.9) = {math.floor(4.9)}")          # 4 (round DOWN)
print(f"pow(2, 10) = {math.pow(2, 10)}")          # 1024.0
print(f"log2(1024) = {math.log2(1024)}")          # 10.0
print(f"factorial(7) = {math.factorial(7)}")       # 5040
print(f"gcd(48, 18) = {math.gcd(48, 18)}")        # 6
print(f"fabs(-42) = {math.fabs(-42)}")             # 42.0 (absolute value as float)

# Trigonometry (angles in radians!)
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"\nsin(45) = {math.sin(angle_rad):.4f}")   # 0.7071
print(f"cos(45) = {math.cos(angle_rad):.4f}")     # 0.7071

# =============================================================================
# 6. THE json MODULE -- Data's Favorite Format
# =============================================================================
print("\n=== json Module -- The Universal Translator ===")
import json

# Python dict -> JSON string (serialization / "dumps" = dump string)
hero_data = {
    "name": "Batman",
    "city": "Gotham",
    "gadgets": ["batarang", "grapple gun", "batmobile"],
    "has_superpowers": False,  # Python False -> JSON false
    "sidekick": None           # Python None -> JSON null
}

json_string = json.dumps(hero_data, indent=2)
print(f"Python -> JSON:\n{json_string}")

# JSON string -> Python dict (deserialization / "loads" = load string)
json_text = '{"name": "Wonder Woman", "powers": ["super strength", "flight"], "age": null}'
parsed = json.loads(json_text)
print(f"\nJSON -> Python: {parsed}")
print(f"Name: {parsed['name']}")
print(f"Age: {parsed['age']}")  # None (null -> None)

# Quick note: json.dump() and json.load() work with FILES (see Chapter 12!)
# json.dumps() and json.loads() work with STRINGS (the 's' = string)

# =============================================================================
# 7. from ... import -- Cherry-Pick What You Need
# =============================================================================
print("\n=== from...import -- Selective Shopping ===")

# Already used above, but let's be explicit
from random import choice, randint
from datetime import datetime
from os.path import exists, join

# Now use them directly -- no module prefix needed
print(f"Random choice: {choice(['heads', 'tails'])}")
print(f"File exists: {exists('.')}")
print(f"Joined: {join('folder', 'file.txt')}")

# You can import multiple things on one line
from math import pi, e, tau
print(f"Pi={pi:.2f}, e={e:.2f}, tau={tau:.2f}")

# =============================================================================
# 8. VIRTUAL ENVIRONMENTS -- Keep Your Projects Clean
# =============================================================================
print("\n=== Virtual Environments (Explained, Not Executed) ===")
print("""
Virtual environments are like separate Python universes for each project.

WHY? Imagine:
  - Project A needs requests v2.25
  - Project B needs requests v2.31
  Without venvs, they'd fight over which version to use!

HOW TO USE:
  1. Create a venv:
     python -m venv myenv

  2. Activate it:
     Windows: myenv\\Scripts\\activate
     Mac/Linux: source myenv/bin/activate

  3. Install packages (only affects THIS venv):
     pip install requests
     pip install flask

  4. Save your dependencies:
     pip freeze > requirements.txt

  5. Someone else can recreate your setup:
     pip install -r requirements.txt

  6. Deactivate when done:
     deactivate

RULE OF THUMB: One venv per project. Always.
It's like having a separate toolbox for each job.
""")

# =============================================================================
# BONUS: Discover What's Inside a Module
# =============================================================================
print("=== Bonus: Exploring Modules ===")

# dir() shows everything in a module
print(f"Things in 'math' (first 10): {dir(math)[:10]}")

# help() gives documentation (uncomment to try -- it's long!)
# help(math.sqrt)

# __name__ tells you the module name
print(f"math module name: {math.__name__}")
print(f"This file's name: {__name__}")  # __main__ when run directly

# =============================================================================
# RECAP
# =============================================================================
print("\n" + "=" * 50)
print("CHAPTER 11 RECAP -- Modules & Packages")
print("=" * 50)
print("""
- import module / from module import thing / import as alias
- random: randint, choice, shuffle, sample, seed
- datetime: now(), strftime(), timedelta, date math
- os: getcwd, listdir, getenv, path.exists, path.join
- math: pi, sqrt, ceil, floor, factorial, trig functions
- json: dumps/loads (strings), dump/load (files)
- Virtual environments: python -m venv, activate, pip install
- dir(module) to explore, help(thing) for docs

The standard library is MASSIVE. These are just the highlights.
When you think "there must be a module for this" -- there probably is.
Check docs.python.org/3/library/ for the full buffet!
""")
