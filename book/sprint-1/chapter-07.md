# Chapter 7: Loops: Doing Things on Repeat

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-07-loops/)**

Imagine having to manually send 1000 emails one at a time. Or counting every item in a warehouse by hand. Or liking every photo on your friend's Instagram, one. by. one. Loops are the reason programmers still have their sanity. They let you say "do this thing, but like, a thousand times" and then go grab coffee while the computer does the work.

## What You'll Learn
- `for` loops - when you know what you're looping through
- `range()` - the loop's best friend
- `while` loops - when you don't know how many times
- `break` and `continue` - escape hatches
- Nested loops - when one loop isn't enough

## for Loops: Do This for Each Thing

A `for` loop goes through a collection of items and does something with each one. Think of it like a conveyor belt - each item gets the same treatment:

```python
avengers = ["Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye"]

for hero in avengers:
    print(f"{hero} is ready for battle!")
```

Output:
```
Iron Man is ready for battle!
Thor is ready for battle!
Hulk is ready for battle!
Black Widow is ready for battle!
Hawkeye is ready for battle!
```

Here's how to read it: "FOR each `hero` IN the `avengers` list, do this." The variable `hero` takes on the value of each item, one at a time. First it's `"Iron Man"`, then `"Thor"`, then `"Hulk"`, and so on.

You can name the loop variable whatever you want, but make it descriptive:

```python
# Good - you know exactly what's happening
for student in students:
    print(student)

for number in numbers:
    print(number * 2)

# Works but... what's 'x'?
for x in students:
    print(x)
```

You can loop over strings too (each character is an item):

```python
for letter in "Python":
    print(letter)
# P
# y
# t
# h
# o
# n
```

## range(): The Loop's Best Friend

What if you want to loop a specific number of times but you don't have a list? That's what `range()` is for. It generates a sequence of numbers.

**Three forms of range:**

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
for i in range(2, 6):
    print(i)
# 2, 3, 4, 5

# range(start, stop, step) - with custom step
for i in range(0, 20, 5):
    print(i)
# 0, 5, 10, 15

# Count backwards
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

Just like slicing, `range()` goes up to but **doesn't include** the stop number. `range(5)` gives you 0 through 4, not 0 through 5.

Practical example - print a times table:

```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

Output:
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

## while Loops: When You Don't Know How Many Times

`for` loops are great when you know what you're iterating over. But sometimes you want to keep going until something happens. Enter `while`:

```python
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access granted!")
```

This keeps asking for the password until the user gets it right. We have no idea how many tries it'll take - could be 1, could be 100. That's the sweet spot for `while`.

The pattern is: **while this condition is True, keep looping.**

```python
# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1    # DON'T FORGET THIS or you get an infinite loop!
print("Liftoff!")
```

Output:
```
5
4
3
2
1
Liftoff!
```

See that `count -= 1`? That's crucial. If you forget to change the variable that your `while` condition checks, the condition stays `True` forever and your program runs until the heat death of the universe (or until you hit Ctrl+C).

> **Pro Tip:** If your program seems frozen, it's probably stuck in an infinite loop. Press `Ctrl+C` to break out. It happens to everyone. Even senior developers accidentally create infinite loops - they just press Ctrl+C faster.

**Common while loop patterns:**

```python
# Accumulator - add things up
total = 0
while True:
    price = input("Enter a price (or 'done'): ")
    if price == "done":
        break
    total += float(price)
print(f"Total: ${total:.2f}")

# Validation - keep asking until valid input
age = -1
while age < 0 or age > 150:
    age = int(input("Enter your age (0-150): "))
print(f"Got it, you're {age}!")
```

## break and continue: The Escape Hatches

### break - "I'm Outta Here!"

`break` immediately exits the loop. No more iterations, no more checking conditions. It's the emergency exit.

```python
# Search for a name
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

search = "Charlie"
for name in names:
    if name == search:
        print(f"Found {search}!")
        break
    print(f"Checking {name}...")
```

Output:
```
Checking Alice...
Checking Bob...
Found Charlie!
```

Without `break`, the loop would keep checking Dave and Eve even after finding Charlie. Why waste the effort?

### continue - "Skip This One"

`continue` skips the rest of the current iteration and jumps to the next one. It's like saying "nah, next."

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)
# 1, 3, 5, 7, 9
```

```python
# Process only valid entries
scores = [95, -1, 87, 0, 72, -5, 100]

for score in scores:
    if score <= 0:
        continue    # Skip invalid scores
    print(f"Processing score: {score}")
```

Think of `break` as leaving the building. `continue` is skipping one floor on the elevator.

## Nested Loops: Loop-ception

Sometimes you need a loop inside a loop. The inner loop runs completely for each iteration of the outer loop:

```python
# Print a grid
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()  # New line after each row
```

Output:
```
* * * *
* * * *
* * * *
```

The outer loop runs 3 times (rows). For each row, the inner loop runs 4 times (columns). That's 3 x 4 = 12 stars total.

A more practical example - finding matching pairs:

```python
colors = ["red", "blue", "green"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"{color}-{size}", end="  ")
    print()
```

Output:
```
red-S  red-M  red-L
blue-S  blue-M  blue-L
green-S  green-M  green-L
```

Nested loops can make your brain hurt. That's normal. Just remember: the inner loop resets and runs completely every time the outer loop takes a step.

> **Pro Tip:** Avoid going more than 2 levels deep with nested loops. If you find yourself at 3 or more levels, there's probably a better way. We'll learn about functions in Sprint 2, which help break things up.

## The else Clause on Loops (Weird But Useful)

Python has a feature that confuses even experienced programmers from other languages: loops can have an `else` block.

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

Output:
```
0
1
2
3
4
Loop completed!
```

> **Wait, What?** "Yes, loops can have an `else`. No, it's not what you think." The `else` block runs ONLY if the loop finished **without** hitting a `break`. If the loop was interrupted by `break`, the `else` is skipped.

This is actually really useful for search patterns:

```python
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num % 2 != 0:
        print(f"Found an odd number: {num}")
        break
else:
    print("All numbers are even!")
# Output: All numbers are even!
```

Without `for/else`, you'd need a flag variable. With it, the code is cleaner. But honestly? Most Python developers don't use this feature often. It's good to know it exists, but don't feel pressured to use it.

## Useful Loop Patterns

Here are patterns you'll use all the time:

```python
# Building a list with a loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Summing values
total = 0
for price in [9.99, 14.50, 3.75, 22.00]:
    total += price
print(f"Total: ${total:.2f}")  # Total: $50.24

# Finding something
names = ["Alice", "Bob", "Charlie"]
target = "Bob"
found = False
for name in names:
    if name == target:
        found = True
        break
print(f"Found {target}: {found}")

# Looping with index using enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

## Your Turn: Multiplication Table Printer

Create `multiplication_table.py`:

```python
# Multiplication Table Printer
print("=== Multiplication Table ===\n")

size = int(input("Table size (e.g., 10 for 10x10): "))

# Print header row
print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print()
print("    " + "--" * size)

# Print each row
for row in range(1, size + 1):
    print(f"{row:3} |", end="")
    for col in range(1, size + 1):
        result = row * col
        print(f"{result:4}", end="")
    print()

print(f"\nThat's {size * size} multiplication facts!")
```

Run it with a size of 10 and admire your perfectly aligned multiplication table.

**Bonus challenges:**
1. Highlight (add an asterisk) any result that's a perfect square
2. Add a mode that lets the user quiz themselves: show `5 x 7 = ?` and check their answer
3. Track how many they get right and show a score at the end

## TL;DR

- **`for` loops** iterate over a collection: `for item in collection:`
- **`range()`** generates numbers: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- **`while` loops** run until a condition is False - don't forget to update the condition variable!
- **`break`** exits the loop immediately; **`continue`** skips to the next iteration
- **Nested loops:** the inner loop runs fully for each outer loop iteration
- **`for/else`:** the `else` block runs only if the loop completes without `break`
- If your program freezes, you probably made an infinite loop - hit `Ctrl+C`
- When in doubt about `for` vs `while`: if you're going through a collection, use `for`. If you're waiting for a condition, use `while`.
