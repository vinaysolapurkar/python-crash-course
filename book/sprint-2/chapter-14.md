# Chapter 14: Lambda, Map, Filter, Reduce: The One-Liners

> **Sprint 2, Chapter 14** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

What if I told you that you could replace a 5-line loop with a single line of code? You'd probably say "that sounds either amazing or unreadable." And honestly? You'd be right on both counts.

Welcome to functional programming lite. These tools won't replace everything you've learned - but they'll give you some seriously elegant shortcuts for common patterns.

> **Don't Panic:** This chapter looks fancy, but it's really just shortcuts for things you already know how to do with loops. If `map()` and `filter()` confuse you, you can always fall back to a regular for loop. Nobody will judge you. (Okay, some people on Reddit might. But ignore those people.)

## Lambda Functions: Anonymous and Proud

A lambda is a tiny, nameless function that fits on one line. It's for when you need a quick function and don't want to waste three lines defining it.

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

# Both work the same way
print(double(5))   # 10
```

The syntax is: `lambda parameters: expression`. No `def`, no name, no `return` - the expression IS the return value.

```python
# One parameter
square = lambda x: x ** 2
print(square(4))   # 16

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 7))   # 10

# With a conditional
grade = lambda score: "Pass" if score >= 60 else "Fail"
print(grade(75))    # Pass
print(grade(45))    # Fail
```

Now, here's the thing: storing a lambda in a variable kind of defeats the purpose. If you're going to name it, just write a regular function - it's more readable. Lambdas shine when you use them *inline*, as throwaway functions passed to other functions.

```python
# This is where lambdas actually make sense
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9}
]

# Sort by GPA using a lambda (no need for a named function)
ranked = sorted(students, key=lambda s: s["gpa"], reverse=True)
for s in ranked:
    print(f"{s['name']}: {s['gpa']}")
# Jordan: 3.9
# Priya: 3.8
# Alex: 3.2
```

That `key=lambda s: s["gpa"]` is saying: "for each student `s`, the sorting key is their GPA." Clean, compact, readable. This is the lambda sweet spot.

## map(): Transform Everything

`map()` applies a function to every item in a list (or any iterable). It's the "do this to all of them" function.

```python
# Without map (regular loop)
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)   # [1, 4, 9, 16, 25]

# With map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

`map(function, iterable)` returns a map object (lazy - doesn't compute until needed). Wrap it in `list()` to see the results.

More practical examples:

```python
# Convert strings to integers
str_numbers = ["10", "20", "30", "40"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)   # [10, 20, 30, 40]

# Clean up user input
names = ["  priya  ", "ALEX", " jordan"]
cleaned = list(map(lambda n: n.strip().title(), names))
print(cleaned)   # ['Priya', 'Alex', 'Jordan']

# Extract one field from a list of dictionaries
products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 29},
    {"name": "Keyboard", "price": 79}
]
prices = list(map(lambda p: p["price"], products))
print(prices)   # [999, 29, 79]

# Apply a discount to all prices
discounted = list(map(lambda p: round(p * 0.9, 2), prices))
print(discounted)   # [899.1, 26.1, 71.1]
```

Notice how `map(int, str_numbers)` doesn't need a lambda - `int` is already a function that takes one argument. When the function already exists, just pass it directly.

## filter(): Keep Only the Good Stuff

`filter()` keeps items that pass a test. The function should return `True` (keep) or `False` (discard).

```python
# Without filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)   # [2, 4, 6, 8, 10]

# With filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]
```

The lambda returns `True` for even numbers and `False` for odd ones. `filter()` keeps only the `True` ones.

```python
# Filter out empty strings
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))
print(non_empty)   # ['hello', 'world', 'python']

# Adults only
people = [
    {"name": "Priya", "age": 22},
    {"name": "Timmy", "age": 10},
    {"name": "Alex", "age": 30},
    {"name": "Zoe", "age": 15}
]
adults = list(filter(lambda p: p["age"] >= 18, people))
print(adults)
# [{'name': 'Priya', 'age': 22}, {'name': 'Alex', 'age': 30}]

# Passing scores only
scores = [45, 78, 92, 33, 67, 88, 51, 95]
passing = list(filter(lambda s: s >= 60, scores))
print(passing)   # [78, 92, 67, 88, 95]
```

The `filter(None, words)` trick filters out anything "falsy" - empty strings, `0`, `None`, `False`, etc. Handy for cleaning data.

## Combining map() and filter()

The real power comes from chaining these together.

```python
# Get names of students with GPA above 3.5
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9},
    {"name": "Sam", "gpa": 2.9}
]

# Step 1: Filter (keep GPA > 3.5)
# Step 2: Map (extract just the names)
honor_roll = list(map(
    lambda s: s["name"],
    filter(lambda s: s["gpa"] > 3.5, students)
))
print(honor_roll)   # ['Priya', 'Jordan']
```

This reads inside-out: first filter, then map. It works, but honestly? The list comprehension version is more readable:

```python
# Same thing, but more Pythonic
honor_roll = [s["name"] for s in students if s["gpa"] > 3.5]
print(honor_roll)   # ['Priya', 'Jordan']
```

We'll talk about when to use which in a moment.

## reduce(): Boil It All Down

`reduce()` takes a list and boils it down to a single value. It applies a function to the first two items, then applies the function to the result and the third item, and so on until there's only one value left.

Unlike `map` and `filter`, `reduce` isn't built-in - you have to import it.

```python
from functools import reduce

# Sum all numbers (the hard way, to show how reduce works)
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)   # 15

# How it works, step by step:
# Step 1: 1 + 2 = 3
# Step 2: 3 + 3 = 6
# Step 3: 6 + 4 = 10
# Step 4: 10 + 5 = 15
```

The lambda takes two arguments: the **accumulator** (running result) and the **current item**.

```python
from functools import reduce

# Find the maximum value
numbers = [34, 67, 12, 89, 45]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)   # 89

# Multiply all numbers together
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(product)   # 120 (1 * 2 * 3 * 4 * 5)

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(flat)   # [1, 2, 3, 4, 5, 6]

# Build a sentence from words
words = ["Python", "is", "actually", "pretty", "cool"]
sentence = reduce(lambda a, b: f"{a} {b}", words)
print(sentence)   # Python is actually pretty cool
```

Real talk: `reduce()` is the least-used of this bunch in modern Python. For summing, use `sum()`. For min/max, use `min()` and `max()`. For joining strings, use `" ".join()`. But `reduce()` is worth knowing because it shows up in other languages and in data processing.

## The Honest Comparison: When to Use What

Here's the truth. In Python, you have three ways to do the same thing:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Goal: Get squares of even numbers

# Method 1: Regular loop
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n ** 2)
print(result)   # [4, 16, 36, 64, 100]

# Method 2: map + filter
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)   # [4, 16, 36, 64, 100]

# Method 3: List comprehension (Pythonic winner)
result = [n ** 2 for n in numbers if n % 2 == 0]
print(result)   # [4, 16, 36, 64, 100]
```

**My honest recommendation:**

| Situation | Use |
|------|---|
| Simple transformation | List comprehension |
| Simple filtering | List comprehension |
| Both together | List comprehension |
| Already have a named function | `map()` or `filter()` |
| Need lazy evaluation (huge data) | `map()` or `filter()` (without `list()`) |
| Sorting with custom key | `lambda` with `sorted()` |
| Complex multi-step pipeline | Regular loop (readability wins) |
| Reducing to single value | `sum()`, `max()`, `min()`, or `reduce()` |

List comprehensions are the Pythonic way. But `map`, `filter`, and `lambda` are tools you should know because:
1. You'll see them in other people's code constantly
2. Some situations genuinely call for them
3. They're essential in other languages (JavaScript's `.map()`, `.filter()`, `.reduce()`)

## Bonus: sorted() with Lambda

This is probably the most common real-world use of lambda:

```python
# Sort strings by length
words = ["banana", "pie", "strawberry", "kiwi"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)   # ['pie', 'kiwi', 'banana', 'strawberry']

# Sort dictionaries by a specific field
employees = [
    {"name": "Priya", "salary": 75000},
    {"name": "Alex", "salary": 65000},
    {"name": "Jordan", "salary": 85000}
]

by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
for e in by_salary:
    print(f"{e['name']}: ${e['salary']:,}")
# Jordan: $85,000
# Priya: $75,000
# Alex: $65,000

# Sort by multiple criteria (last name, then first name)
names = ["Jordan Smith", "Alex Smith", "Priya Patel", "Alex Johnson"]
sorted_names = sorted(names, key=lambda n: (n.split()[-1], n.split()[0]))
print(sorted_names)
# ['Alex Johnson', 'Priya Patel', 'Alex Smith', 'Jordan Smith']
```

That last one sorts by last name first, then by first name within the same last name. The `key` function returns a tuple, and Python compares tuples element by element.

## Your Turn: Student Grade Processor

You have this data:

```python
students = [
    {"name": "Priya", "scores": [95, 87, 92, 88]},
    {"name": "Alex", "scores": [72, 68, 75, 80]},
    {"name": "Jordan", "scores": [88, 92, 95, 90]},
    {"name": "Sam", "scores": [55, 60, 58, 62]},
    {"name": "Taylor", "scores": [91, 89, 94, 87]}
]
```

Using lambda, map, filter, and/or list comprehensions, write code to:

1. Calculate each student's average score (use `map`)
2. Filter to only students with average above 80 (use `filter`)
3. Sort the passing students by average, highest first (use `sorted` with `lambda`)
4. Create a final report showing each passing student's name and letter grade:
   - 90+: A
   - 80-89: B
   - 70-79: C
   - Below 70: F
5. Use `reduce` to find the overall class average

**Starter hint:**

```python
from functools import reduce

students = [
    {"name": "Priya", "scores": [95, 87, 92, 88]},
    {"name": "Alex", "scores": [72, 68, 75, 80]},
    {"name": "Jordan", "scores": [88, 92, 95, 90]},
    {"name": "Sam", "scores": [55, 60, 58, 62]},
    {"name": "Taylor", "scores": [91, 89, 94, 87]}
]

# Step 1: Add average to each student
with_averages = list(map(
    lambda s: {**s, "average": sum(s["scores"]) / len(s["scores"])},
    students
))

# Step 2: Filter to passing students (average > 80)
# Your code here...

# Step 3: Sort by average, highest first
# Your code here...

# Step 4: Generate letter grades
# Your code here...

# Step 5: Overall class average using reduce
# Your code here...
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-14-lambda-map-filter/`

## TL;DR

- **Lambda** functions are one-line, anonymous functions: `lambda x: x * 2`.
- **`map(func, iterable)`** applies a function to every item. Like a conveyor belt.
- **`filter(func, iterable)`** keeps items where the function returns `True`. Like a bouncer.
- **`reduce(func, iterable)`** boils a list down to a single value. Import from `functools`.
- **List comprehensions** are usually more Pythonic than `map`/`filter` for simple cases.
- The killer use case for **lambda** is `sorted(data, key=lambda x: x["field"])`.
- These tools show up everywhere in data science, web development, and other people's code. Know them even if you prefer comprehensions.
- If a one-liner is harder to read than a three-line loop, use the loop. Cleverness is not a virtue.
