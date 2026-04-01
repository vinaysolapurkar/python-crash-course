# Appendix A: Python Cheat Sheet

A quick-reference guide to Python syntax and common patterns. Bookmark this page -- you'll come back to it constantly.

---

## Variables and Data Types

| Syntax | Example | Notes |
|--------|---------|-------|
| Integer | `x = 42` | Whole numbers, no size limit |
| Float | `pi = 3.14` | Decimal numbers |
| String | `name = "Alice"` | Text, single or double quotes |
| Boolean | `done = True` | `True` or `False` (capitalized) |
| None | `result = None` | Represents "no value" |
| Type check | `type(x)` | Returns `<class 'int'>` etc. |
| Type convert | `int("42")`, `str(42)`, `float("3.14")` | Can raise ValueError |

## Strings

| Operation | Syntax | Result |
|-----------|--------|--------|
| Concatenation | `"Hello" + " " + "World"` | `"Hello World"` |
| Repetition | `"ha" * 3` | `"hahaha"` |
| f-string | `f"Hello, {name}!"` | `"Hello, Alice!"` |
| Length | `len("hello")` | `5` |
| Index | `"hello"[0]` | `"h"` |
| Slice | `"hello"[1:4]` | `"ell"` |
| Upper/Lower | `"hi".upper()`, `"HI".lower()` | `"HI"`, `"hi"` |
| Strip | `" hi ".strip()` | `"hi"` |
| Split | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| Join | `", ".join(["a", "b"])` | `"a, b"` |
| Replace | `"hello".replace("l", "L")` | `"heLLo"` |
| Find | `"hello".find("ll")` | `2` (-1 if not found) |
| Startswith | `"hello".startswith("he")` | `True` |
| Contains | `"ll" in "hello"` | `True` |

## f-String Formatting

| Syntax | Example | Result |
|--------|---------|--------|
| Variable | `f"{name}"` | Value of `name` |
| Expression | `f"{2 + 3}"` | `"5"` |
| Decimal places | `f"{3.14159:.2f}"` | `"3.14"` |
| Comma separator | `f"{1000000:,}"` | `"1,000,000"` |
| Percentage | `f"{0.85:.1%}"` | `"85.0%"` |
| Padding | `f"{'hi':<10}"` | `"hi        "` |
| Right align | `f"{'hi':>10}"` | `"        hi"` |
| Center | `f"{'hi':^10}"` | `"    hi    "` |
| Zero pad | `f"{42:05d}"` | `"00042"` |

## Lists

| Operation | Syntax | Result/Effect |
|-----------|--------|---------------|
| Create | `nums = [1, 2, 3]` | |
| Empty list | `items = []` | |
| Access | `nums[0]`, `nums[-1]` | `1`, `3` |
| Slice | `nums[1:3]` | `[2, 3]` |
| Append | `nums.append(4)` | `[1, 2, 3, 4]` |
| Insert | `nums.insert(0, 0)` | `[0, 1, 2, 3]` |
| Remove | `nums.remove(2)` | Removes first `2` |
| Pop | `nums.pop()` | Removes and returns last |
| Pop at index | `nums.pop(0)` | Removes and returns first |
| Sort | `nums.sort()` | In-place sort |
| Reverse | `nums.reverse()` | In-place reverse |
| Length | `len(nums)` | Number of items |
| Contains | `2 in nums` | `True` |
| Index of | `nums.index(2)` | `1` |
| Count | `nums.count(2)` | Number of occurrences |
| Copy | `nums.copy()` or `nums[:]` | Shallow copy |
| Extend | `nums.extend([4, 5])` | Adds all items |

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# With transformation
upper = [s.upper() for s in names]

# Nested
flat = [x for row in matrix for x in row]
```

## Dictionaries

| Operation | Syntax | Result/Effect |
|-----------|--------|---------------|
| Create | `d = {"name": "Alice", "age": 30}` | |
| Empty dict | `d = {}` | |
| Access | `d["name"]` | `"Alice"` (KeyError if missing) |
| Safe access | `d.get("name", "default")` | `"Alice"` or `"default"` |
| Set | `d["email"] = "a@b.com"` | Adds or updates |
| Delete | `del d["age"]` | Removes key |
| Pop | `d.pop("age", None)` | Removes and returns value |
| Keys | `d.keys()` | Dict keys view |
| Values | `d.values()` | Dict values view |
| Items | `d.items()` | Key-value pairs |
| Contains | `"name" in d` | `True` |
| Length | `len(d)` | Number of key-value pairs |
| Update | `d.update({"age": 31})` | Merge another dict |
| Comprehension | `{k: v for k, v in items}` | |

## Sets

| Operation | Syntax | Result |
|-----------|--------|--------|
| Create | `s = {1, 2, 3}` | |
| Empty set | `s = set()` | NOT `{}` (that's a dict) |
| Add | `s.add(4)` | |
| Remove | `s.remove(2)` | KeyError if missing |
| Discard | `s.discard(2)` | No error if missing |
| Union | `s1 \| s2` or `s1.union(s2)` | All items from both |
| Intersection | `s1 & s2` | Items in both |
| Difference | `s1 - s2` | Items in s1 but not s2 |
| Contains | `2 in s` | `True` |

## Tuples

| Operation | Syntax | Notes |
|-----------|--------|-------|
| Create | `t = (1, 2, 3)` | Immutable (can't change) |
| Single item | `t = (1,)` | Comma required |
| Unpack | `a, b, c = t` | `a=1, b=2, c=3` |
| Access | `t[0]` | `1` |
| Contains | `2 in t` | `True` |

## Conditionals

```python
# if / elif / else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary (one-line if)
status = "pass" if score >= 60 else "fail"

# Multiple conditions
if age >= 18 and has_id:
    print("Allowed")

if day == "Saturday" or day == "Sunday":
    print("Weekend")

# Membership check
if name in ["Alice", "Bob", "Charlie"]:
    print("Known user")
```

## Loops

```python
# for loop with range
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

# for loop with list
for item in my_list:
    print(item)

# for loop with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# for loop with dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# while loop
while count < 10:
    count += 1

# break and continue
for item in items:
    if item == "stop":
        break        # Exit the loop entirely
    if item == "skip":
        continue     # Skip to next iteration
    print(item)
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = get_min_max([3, 1, 4, 1, 5])

# *args (variable positional arguments)
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)  # 6

# **kwargs (variable keyword arguments)
def create_user(**kwargs):
    return kwargs

create_user(name="Alice", age=30)  # {"name": "Alice", "age": 30}

# Lambda (anonymous function)
square = lambda x: x ** 2
sorted_list = sorted(items, key=lambda x: x["name"])
```

## Classes

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"{self.name}, age {self.age}"

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"

# Usage
dog = Dog("Rex", 5)
print(dog.bark())
print(dog)
```

## File I/O

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()      # List of lines

# Read line by line (memory efficient)
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")

# Append
with open("file.txt", "a") as f:
    f.write("Another line\n")

# JSON
import json
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=2)

with open("data.json", "r") as f:
    data = json.load(f)

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## Error Handling

```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch-all with details
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")

# Finally (always runs)
try:
    f = open("file.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Raise your own exceptions
if age < 0:
    raise ValueError("Age cannot be negative")
```

## Common Built-in Functions

| Function | Example | Result |
|----------|---------|--------|
| `print()` | `print("hi", end="")` | Output to console |
| `input()` | `name = input("Name: ")` | Read from user |
| `len()` | `len([1, 2, 3])` | `3` |
| `range()` | `range(5)` | `0, 1, 2, 3, 4` |
| `type()` | `type(42)` | `<class 'int'>` |
| `int()` | `int("42")` | `42` |
| `str()` | `str(42)` | `"42"` |
| `float()` | `float("3.14")` | `3.14` |
| `bool()` | `bool(0)` | `False` |
| `list()` | `list(range(3))` | `[0, 1, 2]` |
| `dict()` | `dict(a=1, b=2)` | `{"a": 1, "b": 2}` |
| `sorted()` | `sorted([3, 1, 2])` | `[1, 2, 3]` |
| `reversed()` | `list(reversed([1, 2, 3]))` | `[3, 2, 1]` |
| `enumerate()` | `list(enumerate(["a", "b"]))` | `[(0, "a"), (1, "b")]` |
| `zip()` | `list(zip([1, 2], ["a", "b"]))` | `[(1, "a"), (2, "b")]` |
| `map()` | `list(map(str, [1, 2, 3]))` | `["1", "2", "3"]` |
| `filter()` | `list(filter(bool, [0, 1, "", "hi"]))` | `[1, "hi"]` |
| `sum()` | `sum([1, 2, 3])` | `6` |
| `min()` / `max()` | `min(3, 1, 4)` | `1` |
| `abs()` | `abs(-5)` | `5` |
| `round()` | `round(3.14159, 2)` | `3.14` |
| `isinstance()` | `isinstance(42, int)` | `True` |

## Common Imports

```python
import os                  # File/directory operations
import sys                 # System-specific parameters
import json                # JSON encoding/decoding
import csv                 # CSV file handling
import datetime            # Date and time
import random              # Random numbers
import math                # Mathematical functions
import re                  # Regular expressions
import collections         # Specialized containers
from pathlib import Path   # Modern file paths
```
