# Chapter 13: Error Handling: When Things Go Wrong (And They Will)

> **Sprint 2, Chapter 13** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Here's a truth bomb: your code WILL crash. Not might. Will. Every developer in the world writes code that breaks. The difference between a junior and a senior isn't that the senior writes bug-free code - it's that the senior's code breaks *gracefully*.

Think of error handling like a seatbelt. You don't wear a seatbelt because you plan to crash. You wear it because you're not an idiot.

## The Common Exceptions Tour

Before we learn to catch errors, let's meet the usual suspects. These are the errors you'll see most often, and recognizing them is half the battle.

```python
# TypeError - wrong type for an operation
result = "hello" + 5
# TypeError: can only concatenate str (not "int") to str

# ValueError - right type, wrong value
number = int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'

# KeyError - dictionary key doesn't exist
data = {"name": "Priya"}
print(data["age"])
# KeyError: 'age'

# IndexError - list index out of range
colors = ["red", "blue", "green"]
print(colors[10])
# IndexError: list index out of range

# NameError - variable doesn't exist
print(undefined_variable)
# NameError: name 'undefined_variable' is not defined

# FileNotFoundError - file doesn't exist
with open("nonexistent.txt") as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'

# ZeroDivisionError - math says no
result = 10 / 0
# ZeroDivisionError: division by zero

# AttributeError - object doesn't have that method/property
number = 42
number.upper()
# AttributeError: 'int' object has no attribute 'upper'
```

> **Don't Panic:** Errors aren't failures. They're Python telling you exactly what went wrong and where. Read the last line of the error message first - it tells you the error type and what happened. Then look at the line number. It's actually being helpful. Like a friend who says "Hey, you have spinach in your teeth" instead of letting you walk around like that.

## try/except: Your Safety Net

The `try/except` block lets you attempt something risky and handle the fallout if it goes wrong.

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a number!")
```

If the user types "42", it works normally. If they type "pizza", Python catches the `ValueError` and runs the `except` block instead of crashing. The program keeps going.

```python
# Without error handling:
age = int(input("Age: "))   # Crashes if user types "twenty"

# With error handling:
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number, not text.")
    age = 0   # Fallback value
```

## Catching Specific vs General Exceptions

You should always catch *specific* exceptions when you can.

```python
# Good - specific exceptions
try:
    data = {"name": "Priya"}
    print(data["age"])
except KeyError:
    print("Key not found!")

# Okay for quick scripts - catch multiple specific exceptions
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero!")

# You can also group them
try:
    # risky code
    value = int(input("Number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Something went wrong: {e}")
```

Catching the general `Exception` is like using a giant net to catch fish - sure, you'll catch everything, but you might also catch a boot, a tire, and a very confused turtle.

```python
# Avoid this unless you have a good reason
try:
    # some code
    pass
except Exception:
    print("Something went wrong!")  # But WHAT went wrong??

# If you must catch everything, at least log the error
try:
    risky_operation()
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
```

The `as e` part captures the exception object so you can see what actually happened. Always do this if you're catching broad exceptions.

## else and finally: The Cleanup Crew

`try/except` has two optional sidekicks: `else` and `finally`.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    # Only runs if NO exception occurred
    print(f"Great! {number} squared is {number ** 2}")
finally:
    # ALWAYS runs, no matter what
    print("Thanks for playing!")
```

- **`else`** runs only if the `try` block succeeded. It's the "if everything went well" block.
- **`finally`** runs no matter what - exception or no exception. It's the "cleanup" block. Use it for things that must happen regardless: closing connections, saving progress, etc.

```python
# Practical example: file handling with full error handling
def read_config(filename):
    try:
        with open(filename, "r") as f:
            config = f.read()
    except FileNotFoundError:
        print(f"Config file '{filename}' not found. Using defaults.")
        config = "default settings"
    except PermissionError:
        print(f"No permission to read '{filename}'.")
        config = "default settings"
    else:
        print(f"Config loaded successfully from '{filename}'.")
    finally:
        print("Config initialization complete.")

    return config
```

## Raising Your Own Exceptions

Sometimes YOU want to be the one throwing the error. Maybe a function received invalid input and you want to stop everything with a clear message.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    if age > 150:
        raise ValueError("That's not a realistic age!")
    return age

# This works fine
set_age(25)

# These raise exceptions
try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age can't be negative!

try:
    set_age(200)
except ValueError as e:
    print(e)   # That's not a realistic age!
```

`raise` is the keyword. You create an exception with a descriptive message, and it bubbles up until something catches it. If nothing catches it, the program crashes with your message.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds. Balance: ${balance}")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print(f"Transaction failed: {e}")
# Transaction failed: Insufficient funds. Balance: $100
```

## Custom Exception Classes

For bigger projects, you can create your own exception types. This makes your error handling more specific and meaningful.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw ${amount}. "
            f"Balance: ${balance}. "
            f"Short by: ${self.deficit}"
        )

class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 250)
except InsufficientFundsError as e:
    print(e)
    print(f"You're short by ${e.deficit}")
except InvalidAmountError as e:
    print(e)
```

Don't worry if custom exceptions feel advanced right now. We'll dig deeper into classes in Sprint 3. For now, just know that the pattern exists.

## The try/except Loop Pattern

One of the most useful patterns is wrapping user input in a try/except loop that keeps asking until they get it right.

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again!")

# This will keep asking until the user enters a real number
age = get_number("Enter your age: ")
price = get_number("Enter the price: ")
```

This is the bulletproof input pattern. The user can type "fish" seventeen times and your program won't crash. It'll just patiently ask again. Like a kindergarten teacher.

> **Remember When?** Remember the tip calculator from Chapter 3? If someone typed "pizza" instead of a number, the whole thing crashed. Now you can make it unbreakable. That's growth.

## Five Practical Debugging Tips

When errors happen and you're staring at your screen in confusion, try these:

**1. Read the error message. No, actually read it.**

```python
# Python gives you the file, line number, and error type
# Traceback (most recent call last):
#   File "app.py", line 15, in calculate_total
#     result = price * quantity
# TypeError: can't multiply sequence by non-int of type 'str'
```

Start from the bottom. `TypeError` - wrong type. `can't multiply sequence by non-int of type 'str'` - you're trying to multiply a string. Line 15 in `app.py`. Go fix it.

**2. Print everything.**

```python
def calculate(data):
    print(f"DEBUG: data = {data}, type = {type(data)}")  # Temporary
    # ... rest of function
```

When in doubt, print the value AND its type. Half of all bugs are type mismatches.

**3. Isolate the problem.**

Comment out code until the error goes away. Then uncomment line by line until it comes back. Now you've found the culprit.

**4. Check your assumptions.**

"I'm SURE this variable is a list." Are you? Print it. "This file DEFINITELY exists." Does it? Check. Your assumptions are lying to you more often than you think.

**5. Rubber duck debugging.**

Explain your code, line by line, to a rubber duck (or a pet, or an imaginary friend, or an actual friend who owes you a favor). The act of explaining it out loud often reveals the bug. This is a real technique used by actual professional developers. No, seriously.

## Your Turn: Crash-Proof Tip Calculator

Take this basic tip calculator and make it completely crash-proof:

```python
# The fragile version
meal_cost = float(input("Meal cost: $"))
tip_percent = float(input("Tip percentage: "))
num_people = int(input("Split between how many people? "))

tip = meal_cost * (tip_percent / 100)
total = meal_cost + tip
per_person = total / num_people

print(f"\nTip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Per person: ${per_person:.2f}")
```

Your crash-proof version should handle:
- Non-numeric input (ValueError)
- Zero or negative meal cost
- Negative tip percentage
- Zero or negative number of people (ZeroDivisionError)
- Use the `get_number` loop pattern from this chapter
- Wrap the whole thing in a "calculate again?" loop

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-13-error-handling/`

## TL;DR

- **Your code will crash.** Error handling decides whether it crashes gracefully or explosively.
- **`try/except`** catches exceptions before they kill your program.
- Always catch **specific exceptions** (`ValueError`, `KeyError`) instead of bare `except`.
- **`else`** runs when no exception occurs. **`finally`** runs no matter what.
- **`raise`** lets you throw your own exceptions with custom messages.
- **Custom exception classes** make your errors more descriptive (we'll learn more about classes in Sprint 3).
- **Read error messages** from the bottom up. Python is literally telling you what went wrong.
- The **try/except input loop** pattern is your best friend for user-facing code.
- Debugging is a skill, not a talent. Print stuff, isolate the problem, and talk to a duck.
