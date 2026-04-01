"""
Chapter 13: Error Handling -- When Things Go Boom
==================================================
Errors happen. Users type "banana" when you ask for a number.
Files go missing. Servers go down. Dividing by zero tears the
fabric of the universe.

Error handling is like wearing a seatbelt -- you hope you don't
need it, but you're glad it's there when you do.

Let's learn to catch errors like a pro!
"""

# =============================================================================
# 1. COMMON EXCEPTIONS -- The Usual Suspects
# =============================================================================
print("=== Common Exceptions (The Rogues Gallery) ===")

# Let's meet the most common errors. These are all COMMENTED OUT
# so the script doesn't crash. Uncomment one at a time to see them!

# TypeError -- wrong type for an operation
# result = "hello" + 5  # Can't add string and int

# ValueError -- right type but wrong value
# number = int("banana")  # "banana" is a string, but not a number string

# KeyError -- accessing a dict key that doesn't exist
# d = {"name": "Yoda"}
# print(d["age"])  # "age" isn't in the dict

# IndexError -- accessing a list index that doesn't exist
# my_list = [1, 2, 3]
# print(my_list[10])  # Only indices 0, 1, 2 exist

# FileNotFoundError -- trying to open a file that doesn't exist
# with open("definitely_not_a_real_file.txt") as f:
#     data = f.read()

# ZeroDivisionError -- the classic math crime
# result = 42 / 0  # The universe doesn't allow this

# NameError -- using a variable that doesn't exist
# print(totally_undefined_variable)

# AttributeError -- calling a method that doesn't exist on the object
# "hello".append("!")  # Strings don't have .append()

print("(All error demos are commented out. Uncomment to see them!)")

# =============================================================================
# 2. TRY / EXCEPT -- The Safety Net
# =============================================================================
print("\n=== try / except -- Catching Errors ===")

# Basic structure: try something risky, catch the error if it happens
try:
    result = 10 / 0  # This WILL cause a ZeroDivisionError
except ZeroDivisionError:
    print("  Caught: Division by zero! The universe is safe.")

# Catch a specific error type
try:
    number = int("not_a_number")
except ValueError:
    print("  Caught: That's not a valid number!")

# What if you don't know which error will happen?
# You can catch the general Exception (but be specific when possible)
try:
    risky_list = [1, 2, 3]
    print(risky_list[99])
except Exception as e:
    print(f"  Caught general exception: {type(e).__name__}: {e}")

# =============================================================================
# 3. CATCHING MULTIPLE EXCEPTION TYPES
# =============================================================================
print("\n=== Catching Multiple Exceptions ===")

# Method 1: Multiple except blocks (handle each differently)
def risky_division(a, b):
    """Try to divide, handling various ways it could go wrong."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("  Error: Can't divide by zero!")
        return None
    except TypeError:
        print("  Error: Both inputs must be numbers!")
        return None

risky_division(10, 0)       # ZeroDivisionError
risky_division(10, "two")   # TypeError

# Method 2: Catch multiple types in one line (handle them the same way)
try:
    # Could be ValueError, KeyError, or IndexError...
    data = {"scores": [90, 85, 77]}
    score = data["scores"][10]  # IndexError!
except (KeyError, IndexError, TypeError) as e:
    print(f"  Caught one of several: {type(e).__name__}: {e}")

# =============================================================================
# 4. THE 'as e' PATTERN -- Getting Error Details
# =============================================================================
print("\n=== 'except ... as e' -- Error Details ===")

try:
    ages = {"Gandalf": 2019, "Frodo": 50}
    print(ages["Sauron"])
except KeyError as e:
    print(f"  Missing key: {e}")
    print(f"  Error type: {type(e).__name__}")
    # e contains the missing key name -- super useful for debugging!

try:
    int("yolo")
except ValueError as e:
    print(f"  ValueError details: {e}")
    # Prints: invalid literal for int() with base 10: 'yolo'

# =============================================================================
# 5. ELSE and FINALLY -- The Full try Block
# =============================================================================
print("\n=== else and finally ===")

# Full structure:
#   try:      -- attempt the risky thing
#   except:   -- handle errors
#   else:     -- runs ONLY if no error occurred (success path)
#   finally:  -- runs NO MATTER WHAT (cleanup)

def safe_divide(a, b):
    """Demonstrate the full try/except/else/finally structure."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  {a}/{b}: ERROR -- division by zero!")
    except TypeError:
        print(f"  ERROR -- invalid types!")
    else:
        # Only runs if try block succeeded (no exceptions!)
        print(f"  {a}/{b} = {result:.2f}  (success!)")
    finally:
        # ALWAYS runs -- errors or not. Great for cleanup!
        print(f"  (finally block ran -- I always run, like the Terminator)")

safe_divide(10, 3)   # Success path
print()
safe_divide(10, 0)   # Error path
print()

# Real-world use of finally: closing resources
print("--- finally for cleanup ---")
try:
    print("  Opening connection...")
    # Pretend we opened a database connection
    data = {"connected": True}
    # Pretend something goes wrong:
    result = data["missing_key"]
except KeyError:
    print("  ERROR: Data not found!")
finally:
    # This runs even after an error -- perfect for cleanup
    print("  Closing connection... (always happens)")

# =============================================================================
# 6. RAISING EXCEPTIONS -- Creating Your Own Errors
# =============================================================================
print("\n=== Raising Exceptions ===")

# Sometimes YOU want to raise an error on purpose.
# This is for enforcing rules in your code.

def set_age(age):
    """Set age with validation -- no time travelers allowed!"""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age can't be negative! Got {age}. Are you Benjamin Button?")
    if age > 150:
        raise ValueError(f"Age {age} seems unrealistic. Are you a vampire?")
    return f"Age set to {age}"

# Test the valid case
print(f"  {set_age(25)}")

# Test the error cases (wrapped in try/except so we don't crash)
for test_age in [-5, 200, "twenty"]:
    try:
        set_age(test_age)
    except (ValueError, TypeError) as e:
        print(f"  set_age({test_age!r}): {e}")

# =============================================================================
# 7. CUSTOM EXCEPTION CLASSES -- Your Very Own Errors
# =============================================================================
print("\n=== Custom Exceptions ===")

# Create custom exceptions by inheriting from Exception (or a subclass).
# This is great for domain-specific errors in your app.

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance.
    Tony Stark never sees this error. The rest of us? Frequently."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. "
            f"Balance: ${balance:.2f}. "
            f"You're ${self.deficit:.2f} short!"
        )


class NegativeAmountError(Exception):
    """Raised when someone tries to deposit/withdraw a negative amount.
    Nice try, hacker."""

    def __init__(self, amount):
        super().__init__(f"Amount must be positive, got ${amount:.2f}. No funny business!")


# A simple bank account using custom exceptions
class BankAccount:
    """A tiny bank account that throws custom errors like confetti."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        print(f"  Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"  Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


# Test the bank account
account = BankAccount("Peter Parker", 100)

try:
    account.deposit(50)       # OK: balance -> $150
    account.withdraw(30)      # OK: balance -> $120
    account.withdraw(200)     # ERROR: only have $120!
except InsufficientFundsError as e:
    print(f"  DENIED: {e}")

try:
    account.deposit(-50)      # ERROR: negative amount!
except NegativeAmountError as e:
    print(f"  DENIED: {e}")

# =============================================================================
# 8. DEBUGGING TIPS -- Finding the Bug Before It Finds You
# =============================================================================
print("\n=== Debugging Tips ===")
print("""
  1. READ THE ERROR MESSAGE -- Python tells you EXACTLY what went wrong.
     - The last line is the error type and message
     - The 'Traceback' shows you WHERE it happened (line numbers!)

  2. USE print() DEBUGGING -- The OG debugging method.
     - print(f"DEBUG: x = {x}") before the crash line
     - Remove prints when done (or use logging module)

  3. CHECK YOUR TYPES -- print(type(variable)) when in doubt.
     - "5" is not the same as 5!

  4. GOOGLE THE ERROR -- Copy the error message into Google.
     - StackOverflow has probably solved it already.

  5. RUBBER DUCK DEBUGGING -- Explain your code to a rubber duck.
     - Sounds silly. Works amazingly. The duck judges silently.

  6. COMMON GOTCHAS:
     - Off-by-one: list[len(list)] is out of range, use list[len(list)-1]
     - Mutable defaults: def f(items=[]): is a trap! Use None instead.
     - String vs int: input() always returns a string, even "42"
     - Indent errors: mixing tabs and spaces is a war crime in Python
""")

# =============================================================================
# 9. PUTTING IT ALL TOGETHER -- Safe User Input
# =============================================================================
print("=== Safe User Input (Practical Example) ===")

def get_number(prompt, min_val=None, max_val=None):
    """
    Safely get a number from the user with validation.
    This is a pattern you'll use ALL the time!
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  Must be at least {min_val}!")
                continue
            if max_val is not None and value > max_val:
                print(f"  Must be at most {max_val}!")
                continue
            return value
        except ValueError:
            print("  That's not a valid number! Try again.")

# Demo (commented out so the script runs without user input):
# age = get_number("Enter your age: ", min_val=0, max_val=150)
# print(f"Your age: {age}")

print("(get_number() demo is commented out -- try it yourself!)")

# =============================================================================
# RECAP
# =============================================================================
print("\n" + "=" * 50)
print("CHAPTER 13 RECAP -- Error Handling")
print("=" * 50)
print("""
- Common errors: TypeError, ValueError, KeyError, IndexError,
  FileNotFoundError, ZeroDivisionError
- try/except: catch errors without crashing
- except ErrorType as e: get error details
- Multiple except blocks for different error types
- else: runs only on success (no error)
- finally: ALWAYS runs (cleanup code)
- raise: throw your own errors on purpose
- Custom exceptions: class MyError(Exception)
- Debugging: read errors, print debug, check types, Google it

Error handling is what separates a toy script from a real app.
Handle your errors, and your users will never see an ugly
traceback. They'll just see your friendly error message instead.
""")
