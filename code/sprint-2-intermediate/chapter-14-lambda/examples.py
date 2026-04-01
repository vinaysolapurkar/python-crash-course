"""
Chapter 14: Lambda, Map, Filter, Reduce -- Functional Python
=============================================================
Welcome to the "I can do that in one line" chapter!

Functional programming is a style where you transform data
using small functions, often without naming them (lambdas).

Think of it like a factory assembly line:
  - map()    -> Do something to EVERY item
  - filter() -> Keep only items that pass a test
  - reduce() -> Combine all items into one result

Let's go functional!
"""

from functools import reduce

# =============================================================================
# 1. LAMBDA -- Anonymous Functions (One-Hit Wonders)
# =============================================================================
print("=== Lambda -- Quick & Nameless Functions ===")

# A lambda is a tiny function you define INLINE.
# Syntax: lambda parameters: expression

# Regular function
def square(x):
    return x ** 2

# Same thing as a lambda
square_lambda = lambda x: x ** 2

print(f"Regular: square(5) = {square(5)}")
print(f"Lambda:  square(5) = {square_lambda(5)}")

# More lambda examples
double = lambda x: x * 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
full_name = lambda first, last: f"{first} {last}"

print(f"\ndouble(7) = {double(7)}")
print(f"add(3, 4) = {add(3, 4)}")
print(f"is_even(6) = {is_even(6)}")
print(f"full_name('Tony', 'Stark') = {full_name('Tony', 'Stark')}")

# Lambdas can have default values too!
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"\ngreet('Yoda') = {greet('Yoda')}")
print(f"greet('Yoda', 'Hmm') = {greet('Yoda', 'Hmm')}")

# WHEN TO USE LAMBDA:
# - Short throwaway functions (usually as arguments to map/filter/sort)
# - If it's more than one line, use a regular def function instead!

# =============================================================================
# 2. SORTING WITH LAMBDA -- The Key to Custom Sorts
# =============================================================================
print("\n=== Sorting with Lambda ===")

# The key parameter lets you sort by any criteria using a lambda

# Sort strings by length
words = ["python", "is", "absolutely", "amazing", "yo"]
by_length = sorted(words, key=lambda w: len(w))
print(f"By length: {by_length}")
# ['yo', 'is', 'python', 'amazing', 'absolutely']

# Sort tuples by second element
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 91)]
by_grade = sorted(students, key=lambda s: s[1], reverse=True)
print(f"By grade (desc): {by_grade}")

# Sort dicts by a specific key
heroes = [
    {"name": "Spider-Man", "power": 85},
    {"name": "Hulk", "power": 99},
    {"name": "Hawkeye", "power": 60},
    {"name": "Thor", "power": 95},
]
by_power = sorted(heroes, key=lambda h: h["power"], reverse=True)
print(f"By power: {[h['name'] for h in by_power]}")
# ['Hulk', 'Thor', 'Spider-Man', 'Hawkeye']

# Sort by multiple criteria (last resort = second key)
players = [("Alice", 10), ("Bob", 10), ("Charlie", 8), ("Diana", 10)]
by_score_then_name = sorted(players, key=lambda p: (-p[1], p[0]))
print(f"By score desc, then name asc: {by_score_then_name}")
# Score 10 first (Alice, Bob, Diana), then score 8 (Charlie)

# =============================================================================
# 3. MAP() -- Transform Every Item
# =============================================================================
print("\n=== map() -- Transform Everything ===")

# map(function, iterable) -> applies function to EVERY item
# Returns a map object (lazy -- convert to list to see results)

numbers = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]

# Double every number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]

# Convert strings to integers (map with a built-in function!)
string_nums = ["10", "20", "30", "40"]
int_nums = list(map(int, string_nums))
print(f"Strings to ints: {int_nums}")  # [10, 20, 30, 40]

# Uppercase all strings
names = ["harry", "hermione", "ron"]
upper_names = list(map(str.upper, names))
print(f"Uppercased: {upper_names}")  # ['HARRY', 'HERMIONE', 'RON']

# Map with multiple iterables -- zip them together!
prices = [10, 20, 30]
quantities = [2, 5, 1]
totals = list(map(lambda p, q: p * q, prices, quantities))
print(f"Order totals: {totals}")  # [20, 100, 30]

# =============================================================================
# 4. FILTER() -- Keep Only What Passes the Test
# =============================================================================
print("\n=== filter() -- The Bouncer ===")

# filter(function, iterable) -> keeps items where function returns True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")  # [2, 4, 6, 8, 10]

# Keep numbers greater than 5
big = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {big}")  # [6, 7, 8, 9, 10]

# Filter strings -- keep only long words
words = ["I", "am", "the", "senate", "and", "I", "love", "democracy"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(f"Long words: {long_words}")  # ['senate', 'love', 'democracy']

# Filter with None -- removes all "falsy" values (0, "", None, False, [])
messy = [0, 1, "", "hello", None, True, False, [], [1, 2], "world"]
clean = list(filter(None, messy))
print(f"Cleaned (truthy only): {clean}")  # [1, 'hello', True, [1, 2], 'world']

# Filter dicts -- keep passing students
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 38},
    {"name": "Eve", "grade": 85},
]
passing = list(filter(lambda s: s["grade"] >= 60, students))
print(f"Passing: {[s['name'] for s in passing]}")  # ['Alice', 'Charlie', 'Eve']

# =============================================================================
# 5. REDUCE() -- Combine Everything Into One
# =============================================================================
print("\n=== reduce() -- The Ultimate Combiner ===")

# reduce(function, iterable) -> combines all items into a single value
# It takes the first two items, applies the function, then takes that
# result and the next item, and so on until one value remains.
# You must import it: from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers (reduce style)
total = reduce(lambda a, b: a + b, numbers)
print(f"Sum: {total}")  # 15
# How it works: ((((1+2)+3)+4)+5) = 15

# Product of all numbers
product = reduce(lambda a, b: a * b, numbers)
print(f"Product: {product}")  # 120

# Find maximum (reduce style -- just to show it can be done)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Maximum: {maximum}")  # 5

# Concatenate strings
words = ["Python", "is", "absolutely", "incredible"]
sentence = reduce(lambda a, b: f"{a} {b}", words)
print(f"Sentence: {sentence}")  # "Python is absolutely incredible"

# Reduce with an initial value (3rd argument)
# Useful when you want to start from something other than the first element
total_plus_100 = reduce(lambda a, b: a + b, numbers, 100)
print(f"Sum + 100: {total_plus_100}")  # 115

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
flat = reduce(lambda a, b: a + b, nested)
print(f"Flattened: {flat}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# =============================================================================
# 6. PRACTICAL EXAMPLES -- Chaining map, filter, reduce
# =============================================================================
print("\n=== Practical Examples -- Chaining Operations ===")

# Example 1: Process a list of prices
# Apply 10% discount, filter out items over $50, find total
prices = [25.0, 60.0, 45.0, 80.0, 15.0, 35.0, 90.0, 20.0]

discounted = list(map(lambda p: round(p * 0.9, 2), prices))
affordable = list(filter(lambda p: p <= 50, discounted))
total = reduce(lambda a, b: a + b, affordable)

print(f"Original prices: {prices}")
print(f"After 10% discount: {discounted}")
print(f"Under $50: {affordable}")
print(f"Total for affordable items: ${total:.2f}")

# Example 2: Process student data
students = [
    {"name": "Alice", "scores": [90, 85, 92]},
    {"name": "Bob", "scores": [65, 70, 58]},
    {"name": "Charlie", "scores": [80, 75, 88]},
    {"name": "Diana", "scores": [95, 98, 100]},
]

# Calculate averages (map), filter passing (filter), find top (reduce)
with_avg = list(map(
    lambda s: {**s, "avg": sum(s["scores"]) / len(s["scores"])},
    students
))
passing = list(filter(lambda s: s["avg"] >= 70, with_avg))
top_student = reduce(lambda a, b: a if a["avg"] > b["avg"] else b, passing)

avg_display = [(s['name'], round(s['avg'], 1)) for s in with_avg]
print(f"\nWith averages: {avg_display}")
print(f"Passing: {[s['name'] for s in passing]}")
print(f"Top student: {top_student['name']} ({top_student['avg']:.1f})")

# =============================================================================
# 7. LIST COMPREHENSION ALTERNATIVES -- The Pythonic Way
# =============================================================================
print("\n=== List Comprehensions vs map/filter ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# MAP alternatives
print("--- map vs comprehension ---")
# map
squared_map = list(map(lambda x: x**2, numbers))
# List comprehension (usually preferred in Python!)
squared_comp = [x**2 for x in numbers]
print(f"  map:  {squared_map}")
print(f"  comp: {squared_comp}")  # Same result, often more readable!

# FILTER alternatives
print("\n--- filter vs comprehension ---")
# filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
# List comprehension
evens_comp = [x for x in numbers if x % 2 == 0]
print(f"  filter: {evens_filter}")
print(f"  comp:   {evens_comp}")  # Same result!

# MAP + FILTER combined
print("\n--- map + filter vs comprehension ---")
# Functional style
result_func = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
# Comprehension (cleaner!)
result_comp = [x**2 for x in numbers if x % 2 == 0]
print(f"  functional: {result_func}")
print(f"  comprehension: {result_comp}")

# VERDICT:
print("""
  WHEN TO USE WHAT:
  - List comprehensions: when the logic is simple (most of the time!)
  - map/filter: when passing existing functions (map(int, strings))
  - reduce: when you need to combine everything into one value
  - lambda: for short throwaway functions in sort/map/filter

  The Pythonic way often prefers comprehensions, but knowing
  map/filter/reduce makes you a more versatile programmer.
  And they're VERY common in other languages (JavaScript, etc.)!
""")

# =============================================================================
# RECAP
# =============================================================================
print("=" * 50)
print("CHAPTER 14 RECAP -- Lambda, Map, Filter, Reduce")
print("=" * 50)
print("""
- lambda x: expression -> anonymous function (one-liner)
- sorted(list, key=lambda ...) -> custom sorting
- map(func, iterable) -> transform every item
- filter(func, iterable) -> keep items where func returns True
- filter(None, iterable) -> remove falsy values
- reduce(func, iterable) -> combine all into one value
- List comprehensions are often more "Pythonic" for simple cases
- Chain map -> filter -> reduce for powerful data pipelines

Functional programming gives you a different way to think about
data transformation. It's like having a new superpower -- you
don't always need it, but when you do, it's amazing.
""")
