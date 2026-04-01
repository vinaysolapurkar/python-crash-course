# Chapter 20: Generators & Iterators - Memory-Friendly Loops

> **Sprint 4, Chapter 20** | **Estimated Time: 15-20 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Imagine you need to process a 10 GB log file. You could load the entire thing into memory... and watch your laptop freeze, crash, and possibly catch fire. Or you could process it one line at a time, using barely any memory at all.

That's what generators do. They let you work with huge amounts of data - or even *infinite* amounts of data - without running out of memory. Data pipelines, machine learning preprocessing, reading massive files, streaming data from APIs - generators are everywhere in professional Python code.

## The Netflix Analogy

Think about the difference between **downloading** and **streaming**.

If you wanted to watch every movie on Netflix, you *could* download all of them first. That would take... well, you'd need a warehouse of hard drives. Or you could **stream** - watch one movie at a time, and the next one loads only when you hit play.

**Lists are like downloading.** They compute and store every value upfront. **Generators are like streaming.** They compute one value at a time, only when you ask for it.

Same movies. Same data. Radically different memory usage.

## The Iterator Protocol (Quick Version)

Before generators, let's understand what they're built on. In Python, anything you can loop over with `for` is called an **iterable**. Lists, strings, dictionaries, files - all iterables.

Under the hood, Python uses two special methods to make looping work:

```python
# What Python actually does when you write: for x in [1, 2, 3]
my_list = [1, 2, 3]
iterator = iter(my_list)    # Calls __iter__() - gets an iterator

print(next(iterator))       # Calls __next__() - gets 1
print(next(iterator))       # Gets 2
print(next(iterator))       # Gets 3
# next(iterator)            # Raises StopIteration
```

An **iterator** is an object with a `__next__()` method. Each call to `next()` gives you the next value. When there are no more values, it raises `StopIteration`. That's it. That's the entire protocol.

You can build your own iterator class:

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)
# 5, 4, 3, 2, 1
```

That works, but it's a lot of code for a simple countdown. There's a much better way.

## Generators: The Easy Way

A **generator** is a function that uses `yield` instead of `return`. And it does the same thing as that entire `Countdown` class above, in about three lines:

```python
def countdown(start):
    current = start
    while current > 0:
        yield current
        current -= 1

for num in countdown(5):
    print(num)
# 5, 4, 3, 2, 1
```

That's it. `yield` is the magic word.

Here's what makes `yield` special: when a generator function hits `yield`, it **pauses**. It hands back the value and freezes in place. The next time you ask for a value (via `next()` or a `for` loop), it **resumes** exactly where it left off.

> **Don't Panic:** `yield` is just `return` that remembers where it left off. That's literally all it is.

Let's trace through it step by step:

```python
def simple_gen():
    print("Step 1")
    yield "A"
    print("Step 2")
    yield "B"
    print("Step 3")
    yield "C"
    print("Done")

gen = simple_gen()        # Nothing happens yet!
print(next(gen))          # "Step 1" prints, then yields "A"
print(next(gen))          # "Step 2" prints, then yields "B"
print(next(gen))          # "Step 3" prints, then yields "C"
# next(gen)               # "Done" prints, then StopIteration
```

Notice: **creating the generator does nothing.** It doesn't start running until you call `next()` on it. This is called **lazy evaluation** - values are computed only when needed.

> **Remember When?** Remember lists from Sprint 1? Generators are just lazy lists. They compute values one at a time instead of all at once. Same data, less memory.

## Generator Expressions: The One-Liner

Just like list comprehensions give you a one-liner for lists, **generator expressions** give you a one-liner for generators. The syntax is identical, except you use parentheses instead of square brackets:

```python
# List comprehension - creates the entire list in memory
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression - creates values one at a time
squares_gen = (x ** 2 for x in range(1000000))

print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>
```

The list version creates one million numbers in memory right now. The generator version creates... nothing yet. It'll compute each square only when you ask for it.

You can use generator expressions anywhere you'd use a list comprehension:

```python
# Sum of squares (no list needed - just pass the generator)
total = sum(x ** 2 for x in range(1000000))

# Find the first even square over 100
result = next(x ** 2 for x in range(1000) if x ** 2 > 100 and x % 2 == 0)
print(result)  # 144
```

When you pass a generator expression as the only argument to a function, you can drop the extra parentheses. `sum(x**2 for x in range(10))` instead of `sum((x**2 for x in range(10)))`.

## Memory Comparison: Lists vs Generators

Let's see the difference in real numbers:

```python
import sys

# A list of 1 million numbers
big_list = [x for x in range(1_000_000)]
print(f"List size: {sys.getsizeof(big_list):,} bytes")
# List size: 8,448,728 bytes (~8 MB)

# A generator for 1 million numbers
big_gen = (x for x in range(1_000_000))
print(f"Generator size: {sys.getsizeof(big_gen):,} bytes")
# Generator size: 200 bytes

# That's a 42,000x difference!
```

The list uses about 8 megabytes. The generator uses 200 bytes. Same million numbers. The generator just doesn't compute them until it needs to.

For 10 million numbers, the list would use ~80 MB. For 100 million, ~800 MB. The generator? Still 200 bytes.

## Practical Example: Reading Large Files

This is probably the most common real-world use of generators. Processing files line by line without loading the whole thing into memory:

```python
def read_large_file(file_path):
    """Read a file line by line using a generator."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

def find_errors(file_path):
    """Find all error lines in a log file."""
    for line in read_large_file(file_path):
        if "ERROR" in line:
            yield line

# Process a 10 GB log file using barely any memory
for error_line in find_errors("server.log"):
    print(error_line)
```

Each line is read, checked, and either yielded or discarded. At any given moment, only one line is in memory. You could process a terabyte file this way.

## Chaining Generators: Data Pipelines

Generators really shine when you chain them together into a pipeline:

```python
def read_csv_lines(file_path):
    """Read CSV lines, skip header."""
    with open(file_path) as f:
        next(f)  # Skip header
        for line in f:
            yield line.strip()

def parse_fields(lines):
    """Split each line into fields."""
    for line in lines:
        yield line.split(",")

def filter_by_amount(records, min_amount):
    """Keep only records above a minimum amount."""
    for record in records:
        if float(record[2]) > min_amount:
            yield record

# Chain them together - nothing runs until the for loop starts
lines = read_csv_lines("transactions.csv")
records = parse_fields(lines)
big_transactions = filter_by_amount(records, 1000)

for record in big_transactions:
    print(record)
```

Each step processes one item at a time and hands it to the next step. It's like an assembly line - nothing is stored, everything flows through.

## Infinite Generators

Because generators don't compute everything upfront, they can be **infinite**:

```python
def count_forever(start=0):
    """Count from start to infinity."""
    n = start
    while True:
        yield n
        n += 1

def fibonacci():
    """Generate Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take the first 10 Fibonacci numbers
from itertools import islice

first_10 = list(islice(fibonacci(), 10))
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

You can't do `list(fibonacci())` - that would try to create an infinite list and crash. But you can take as many as you need with `islice`.

> **Wait, What?** "An infinite loop that doesn't crash?" Yes! Because `yield` pauses the loop. The infinite `while True` only runs one iteration at a time. As long as you stop asking for values at some point, it's perfectly fine.

## The itertools Module: Generator Superpowers

Python's `itertools` module is a treasure chest of generator tools:

```python
from itertools import count, cycle, repeat, chain, islice

# count: infinite counter
for i in islice(count(10, 2), 5):  # Start at 10, step 2
    print(i)  # 10, 12, 14, 16, 18

# cycle: repeat a sequence forever
colors = cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(colors))  # red, green, blue, red, green, blue, red

# chain: combine multiple iterables
combined = chain([1, 2], [3, 4], [5, 6])
print(list(combined))  # [1, 2, 3, 4, 5, 6]
```

## When to Use Generators vs Lists

| Use a **List** when... | Use a **Generator** when... |
|--|--|
| You need to access items by index | You only need to iterate once |
| You need to iterate multiple times | The data is large or infinite |
| You need the length | Memory is a concern |
| You need to sort or reverse | You're chaining operations |
| The data is small | You're reading from files or network |

## Your Turn: Fibonacci Generator

**Challenge:** Build a `fibonacci` generator that:

1. Yields Fibonacci numbers one at a time
2. Can optionally take a `limit` parameter (max value)
3. Write a second generator that filters for even Fibonacci numbers only

```python
# Your goal:
for num in fibonacci(limit=100):
    print(num)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

for num in even_fibonacci(limit=100):
    print(num)
# 0, 2, 8, 34
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-20-generators/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-20-generators/)

## TL;DR

| Concept | What It Does |
|--|--|
| Iterator | An object with `__next__()` that produces values one at a time |
| Generator function | A function with `yield` that becomes an iterator |
| `yield` | Like `return` but pauses and resumes |
| Generator expression | `(x for x in iterable)` - lazy version of list comprehension |
| Lazy evaluation | Values computed only when needed |
| `itertools` | Standard library module with generator utilities |

**The one-sentence version:** Generators let you process data one piece at a time instead of loading everything into memory, using `yield` to pause and resume a function.

Next up: APIs - where we teach Python to talk to the internet.
