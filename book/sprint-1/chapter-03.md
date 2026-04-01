# Chapter 3: Numbers & Math: Python is Your New Calculator

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-03-numbers-math/)**

Remember when your math teacher said "you won't always have a calculator"? Well, you now have something way better. Python can do everything your TI-84 could do, plus a million things it couldn't. And unlike your math teacher, Python never judges you for using it.

## What You'll Learn
- Every math operator Python offers
- Order of operations (yes, PEMDAS matters here too)
- Why `"5"` is NOT the same as `5`
- How to get input from users
- Handy built-in math functions

## All the Math Operators

Python's arithmetic operators work exactly like you'd expect, with a couple of bonus ones your calculator didn't have:

```python
print(10 + 3)    # 13    Addition
print(10 - 3)    # 7     Subtraction
print(10 * 3)    # 30    Multiplication
print(10 / 3)    # 3.333 Division (always returns a float!)
print(10 // 3)   # 3     Floor division (rounds down, no decimals)
print(10 % 3)    # 1     Modulo (the remainder)
print(10 ** 3)   # 1000  Exponentiation (10 to the power of 3)
```

A few things to note:

**Regular division `/` always gives you a float**, even when it divides evenly:

```python
print(10 / 2)    # 5.0 (not 5)
```

**Floor division `//` drops the decimals** - it doesn't round, it chops:

```python
print(7 // 2)    # 3 (not 3.5, not 4... just 3)
```

**Modulo `%` gives you the remainder.** This one seems random but it's crazy useful. Need to check if a number is even? If `number % 2 == 0`, it's even. Need to cycle through colors? Modulo. It shows up everywhere.

```python
print(10 % 3)   # 1 (10 / 3 = 3 remainder 1)
print(10 % 2)   # 0 (10 is even - no remainder)
print(7 % 2)    # 1 (7 is odd)
```

> **Fun Fact:** The `**` operator is Python's way of doing exponents. Other languages use `^` for this, but in Python, `^` does something completely different (bitwise XOR - don't worry about it yet). So `2 ** 10` gives you 1024, not `2 ^ 10`.

## PEMDAS: Order of Operations

Python follows the same order of operations you learned in school. Remember PEMDAS? (Some people learned BODMAS or BEDMAS - same thing, different accent.)

**P**arentheses > **E**xponents > **M**ultiplication/**D**ivision > **A**ddition/**S**ubtraction

```python
result = 2 + 3 * 4
print(result)    # 14 (not 20!)
```

Python does `3 * 4` first (12), then adds 2. If you want addition first, use parentheses:

```python
result = (2 + 3) * 4
print(result)    # 20
```

When in doubt, add parentheses. They make your code clearer AND ensure the right order. Nobody ever got fired for using too many parentheses.

```python
# Hard to read:
total = price * quantity + price * quantity * tax_rate - discount

# Much clearer:
total = (price * quantity) + (price * quantity * tax_rate) - discount
```

## Augmented Assignment: The Shortcuts

Updating a variable with math is so common that Python has shortcuts:

```python
score = 100

score = score + 10   # The long way
score += 10          # The shortcut (same thing)

score -= 5           # score = score - 5
score *= 2           # score = score * 2
score /= 4           # score = score / 4
score //= 3          # score = score // 3
score %= 7           # score = score % 7
score **= 2          # score = score ** 2
```

`+=` is by far the most common. You'll see it everywhere. It just means "add this to whatever's already there."

```python
lives = 3
lives -= 1
print(f"Lives remaining: {lives}")  # Lives remaining: 2
```

## Type Conversion: When "5" Isn't 5

Here's where it gets spicy. Look at this:

```python
a = "5"
b = "3"
print(a + b)  # "53"
```

Wait, what? 5 + 3 = 53? Nope. `"5"` and `"3"` are **strings** (they have quotes), not numbers. When you `+` two strings, Python glues them together. This is called **concatenation**, and it's one of the most common beginner bugs.

> **Wait, What?** "Why did my addition give me '55' instead of 10?" Because your numbers are secretly strings! This happens ALL the time with `input()` (which we'll cover in a second). The fix: convert them to numbers with `int()` or `float()`.

The fix is **type conversion**:

```python
a = "5"
b = "3"
print(int(a) + int(b))    # 8 (now they're integers!)
print(float(a) + float(b)) # 8.0 (now they're floats!)
```

You can convert between types like this:

```python
# String to number
age = int("25")        # 25 (integer)
price = float("9.99")  # 9.99 (float)

# Number to string
score = str(100)       # "100" (string now)
pi = str(3.14)         # "3.14" (string now)

# Float to int (chops the decimal!)
rounded = int(3.99)    # 3 (not 4! it truncates, doesn't round)

# Int to float
precise = float(5)     # 5.0
```

Notice that `int()` doesn't round - it chops. `int(3.99)` is `3`, not `4`. If you want actual rounding, use `round()` (we'll cover that soon).

## The input() Function: Talk to Me

So far, our programs have been monologues. Let's make them conversations. `input()` lets you ask the user for information:

```python
name = input("What's your name? ")
print(f"Hey, {name}! Welcome to the game.")
```

When Python hits `input()`, it pauses, shows the message, and waits for the user to type something and press Enter. Whatever they type gets stored in the variable.

**Here's the critical thing to remember about `input()`:**

**`input()` ALWAYS returns a string.** Always. Even if the user types a number.

```python
age = input("How old are you? ")
print(type(age))  # <class 'str'> - it's a STRING!
```

If someone types `25`, you get the string `"25"`, not the integer `25`. This means you can't do math with it directly:

```python
age = input("How old are you? ")
# print(age + 5)  # ERROR! Can't add a string and an integer

# Do this instead:
age = int(input("How old are you? "))  # Convert immediately
print(f"In 5 years, you'll be {age + 5}")
```

That `int(input(...))` combo is a pattern you'll use a LOT. Burn it into your brain. You're wrapping `input()` inside `int()` so the conversion happens right away.

```python
# The pattern for getting numbers from users:
whole_number = int(input("Enter a number: "))
decimal_number = float(input("Enter a price: "))
```

> **Pro Tip:** If the user types "abc" when you're expecting a number, `int("abc")` will crash your program with a `ValueError`. We'll learn how to handle that gracefully in Sprint 2 with try/except. For now, just trust your users (famous last words).

## Built-in Math Functions

Python comes with some handy math functions right out of the box:

```python
print(abs(-42))         # 42 (absolute value - removes the negative)
print(round(3.7))       # 4 (rounds to nearest integer)
print(round(3.14159, 2)) # 3.14 (rounds to 2 decimal places)
print(max(4, 7, 2, 9))  # 9 (returns the biggest)
print(min(4, 7, 2, 9))  # 2 (returns the smallest)
print(pow(2, 10))        # 1024 (same as 2 ** 10)
```

`round()` is especially useful for money:

```python
total = 19.99 * 3
tax = total * 0.08
final = total + tax

print(f"Total: ${round(final, 2)}")  # Total: $64.77
```

And if you need more advanced math (square roots, trigonometry, logarithms), Python has a `math` module:

```python
import math

print(math.sqrt(144))    # 12.0
print(math.pi)           # 3.141592653589793
print(math.ceil(3.2))    # 4 (rounds UP)
print(math.floor(3.8))   # 3 (rounds DOWN)
```

Don't worry about the `import` line for now. Just know it's there when you need it. We'll cover imports properly in Sprint 2.

## Your Turn: Tip Calculator

Build a tip calculator! Create a file called `tip_calculator.py`:

```python
# Tip Calculator
print("=== Tip Calculator ===")

# Get the bill amount
bill = float(input("What's the total bill? $"))

# Get the tip percentage
tip_percent = int(input("What tip % do you want to give? (15, 18, 20): "))

# Get the number of people splitting
people = int(input("How many people are splitting the bill? "))

# Calculate
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

# Display results
print(f"\nBill:        ${bill:.2f}")
print(f"Tip ({tip_percent}%):   ${tip_amount:.2f}")
print(f"Total:       ${total:.2f}")
print(f"Per person:  ${round(per_person, 2):.2f}")
```

Run it and calculate some tips! Notice the `:.2f` inside the f-strings? That formats numbers to exactly 2 decimal places. Perfect for money. We'll cover more formatting tricks in Chapter 4.

**Bonus challenge:** Add a "round up" feature that rounds each person's share up to the nearest dollar. (Hint: `math.ceil()`)

## TL;DR

- Python has all the standard math operators plus `//` (floor division), `%` (modulo/remainder), and `**` (exponent)
- PEMDAS order of operations applies - when in doubt, use parentheses
- `"5"` (string) is NOT `5` (integer) - use `int()` or `float()` to convert
- `input()` **always returns a string**, even if the user types a number
- Pattern for numeric input: `int(input("prompt"))` or `float(input("prompt"))`
- Built-in math helpers: `abs()`, `round()`, `max()`, `min()`, `pow()`
- For advanced math, `import math` gives you `sqrt`, `pi`, `ceil`, `floor`, and more
