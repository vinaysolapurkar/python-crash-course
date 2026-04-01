"""
Chapter 20: Generators & Iterators — The Lazy Geniuses
========================================================

Generators are like vending machines:
  - A regular function is like buying ALL the snacks at once
  - A generator is like the vending machine — it gives you one snack at a time

Why does this matter? MEMORY.
  - A list of 10 million numbers? Lives entirely in memory. Ouch.
  - A generator of 10 million numbers? Produces one at a time. Lightweight!

Generators are LAZY — they only compute values when you ask for them.
Like a student who only studies the night before the exam. Efficient? Debatable.
But for Python? Absolutely.
"""

# ============================================================
# 1. The Iterator Protocol — Under the Hood
# ============================================================
print("=" * 50)
print("1. THE ITERATOR PROTOCOL")
print("=" * 50)


class CountUp:
    """
    A manual iterator that counts from start to end.

    The Iterator Protocol requires two methods:
    - __iter__() → returns the iterator object (usually self)
    - __next__() → returns the next value, or raises StopIteration
    """

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """Return the iterator object. For loops call this first."""
        return self

    def __next__(self):
        """Return the next value. For loops call this repeatedly."""
        if self.current > self.end:
            raise StopIteration  # "I'm done! No more values!"
        value = self.current
        self.current += 1
        return value


# Using our custom iterator
print("Counting from 1 to 5:")
for num in CountUp(1, 5):
    print(f"  {num}")

# What the for loop actually does behind the scenes:
print("\nManual iteration (what 'for' does under the hood):")
counter = CountUp(10, 13)
iterator = iter(counter)  # calls __iter__()
while True:
    try:
        value = next(iterator)  # calls __next__()
        print(f"  Got: {value}")
    except StopIteration:
        print("  StopIteration raised — done!")
        break


# ============================================================
# 2. Generators — The Easy Way to Make Iterators
# ============================================================
print("\n" + "=" * 50)
print("2. GENERATORS — yield IS THE MAGIC WORD")
print("=" * 50)


def count_up(start, end):
    """
    Same as CountUp class above, but as a generator function.
    Instead of a whole class, it's just a function with 'yield'.

    'yield' is like 'return', but the function PAUSES instead of ending.
    Next time you call next(), it RESUMES from where it paused.
    It's like bookmarking your place in a book.
    """
    current = start
    while current <= end:
        yield current  # pause here, give this value, resume later
        current += 1


# Using our generator — looks the same as a regular loop!
print("Generator counting 1 to 5:")
for num in count_up(1, 5):
    print(f"  {num}")

# Under the hood, it's a generator OBJECT
gen = count_up(1, 3)
print(f"\nType: {type(gen)}")
print(f"next(): {next(gen)}")  # 1
print(f"next(): {next(gen)}")  # 2
print(f"next(): {next(gen)}")  # 3
# next(gen) here would raise StopIteration


# ============================================================
# 3. Generator Expressions — One-Liner Generators
# ============================================================
print("\n" + "=" * 50)
print("3. GENERATOR EXPRESSIONS")
print("=" * 50)

# List comprehension: creates the ENTIRE list in memory
squares_list = [x**2 for x in range(10)]
print(f"List: {squares_list}")
print(f"Type: {type(squares_list)}")

# Generator expression: creates values on-demand (lazy!)
squares_gen = (x**2 for x in range(10))
print(f"\nGenerator: {squares_gen}")
print(f"Type: {type(squares_gen)}")

# Consume the generator
print("Values from generator:")
for sq in squares_gen:
    print(f"  {sq}", end=" ")
print()

# IMPORTANT: Generators are one-shot! Once consumed, they're empty.
print(f"\nTrying again: {list(squares_gen)}")  # Empty! Already consumed.


# ============================================================
# 4. Memory Comparison — Why Generators Rock
# ============================================================
print("\n" + "=" * 50)
print("4. MEMORY COMPARISON")
print("=" * 50)

import sys

# Compare memory usage
n = 1_000_000

# List: stores ALL numbers in memory
numbers_list = [x for x in range(n)]
list_size = sys.getsizeof(numbers_list)

# Generator: stores almost nothing
numbers_gen = (x for x in range(n))
gen_size = sys.getsizeof(numbers_gen)

print(f"List of {n:,} numbers:     {list_size:>10,} bytes ({list_size / 1024 / 1024:.2f} MB)")
print(f"Generator of {n:,} numbers: {gen_size:>10,} bytes")
print(f"Memory saved:                {(1 - gen_size / list_size) * 100:.1f}%")
print(f"\nThe generator is {list_size // gen_size}x smaller. That's like comparing")
print(f"a warehouse to a Post-it note. 📝")


# ============================================================
# 5. Practical Generators
# ============================================================
print("\n" + "=" * 50)
print("5. PRACTICAL GENERATORS")
print("=" * 50)


# ---- Infinite Generator ----
def infinite_ids(prefix="ID"):
    """
    Generate unique IDs forever. Yes, FOREVER.
    This would be impossible with a list (infinite memory!).
    But a generator? No problem — it only makes one at a time.
    """
    counter = 1
    while True:  # infinite loop, but yield makes it safe
        yield f"{prefix}-{counter:05d}"
        counter += 1


id_gen = infinite_ids("USER")
print("Generating IDs on demand:")
for _ in range(5):
    print(f"  {next(id_gen)}")
# We could keep going forever... but let's not.


# ---- File Line Reader (memory-efficient) ----
def read_large_file(filepath):
    """
    Read a file line by line using a generator.
    Even a 10GB file won't blow up your memory!
    (We won't actually read a 10GB file here, just showing the pattern)
    """
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()


# ---- Data Pipeline with Generators ----
print("\n--- Data Pipeline ---")

def generate_data():
    """Step 1: Generate raw data."""
    data = ["  Alice, 85  ", "  Bob, 92  ", "  Charlie, 78  ",
            "  Diana, 95  ", "  Eve, 88  ", ""]
    for item in data:
        yield item

def clean_data(data_gen):
    """Step 2: Clean the data (strip whitespace, skip empty)."""
    for item in data_gen:
        cleaned = item.strip()
        if cleaned:
            yield cleaned

def parse_data(data_gen):
    """Step 3: Parse into structured data."""
    for item in data_gen:
        name, score = item.split(",")
        yield {"name": name.strip(), "score": int(score.strip())}

def filter_high_scores(data_gen, threshold=90):
    """Step 4: Filter for high scores."""
    for item in data_gen:
        if item["score"] >= threshold:
            yield item


# Chain the generators together — like connecting pipes!
# Data flows through each stage ONE ITEM AT A TIME
pipeline = filter_high_scores(parse_data(clean_data(generate_data())))

print("High scorers (generator pipeline):")
for student in pipeline:
    print(f"  {student['name']}: {student['score']}")


# ============================================================
# 6. send() — Talking Back to Generators
# ============================================================
print("\n" + "=" * 50)
print("6. send() — TWO-WAY COMMUNICATION")
print("=" * 50)


def accumulator():
    """
    A generator that receives values via send() and keeps a running total.
    send() lets you push data INTO a generator. It's like a walkie-talkie!
    """
    total = 0
    while True:
        value = yield total  # yield current total, receive new value
        if value is not None:
            total += value


acc = accumulator()
next(acc)  # "prime" the generator (advance to first yield)

print(f"Send 10: total = {acc.send(10)}")
print(f"Send 20: total = {acc.send(20)}")
print(f"Send 5:  total = {acc.send(5)}")
print(f"Send 15: total = {acc.send(15)}")


# ============================================================
# 7. yield from — Delegating to Sub-Generators
# ============================================================
print("\n" + "=" * 50)
print("7. yield from")
print("=" * 50)


def flatten(nested_list):
    """
    Flatten a nested list using 'yield from'.
    'yield from' delegates to another iterable.
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # recursively yield from sub-lists
        else:
            yield item


nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
print(f"Nested:    {nested}")
print(f"Flattened: {list(flatten(nested))}")


# ============================================================
# Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 20 RECAP")
print("=" * 50)
print("""
Generator Cheat Sheet:
-----------------------------------------------------------------
ITERATOR PROTOCOL:
  __iter__()  → return the iterator
  __next__()  → return next value or raise StopIteration

GENERATOR FUNCTION:
  def my_gen():
      yield value1
      yield value2

GENERATOR EXPRESSION:
  gen = (x**2 for x in range(10))

KEY DIFFERENCES FROM LISTS:
  - Lazy: computes values on demand
  - Memory efficient: doesn't store all values
  - One-shot: can only iterate once
  - Can be infinite!

USEFUL TOOLS:
  next(gen)      → get next value
  send(value)    → send value into generator
  yield from     → delegate to sub-generator

WHEN TO USE:
  - Large datasets that don't fit in memory
  - Data processing pipelines
  - Infinite sequences
  - Streaming/real-time data
-----------------------------------------------------------------
""")
