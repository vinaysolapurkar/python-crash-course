"""
Chapter 10: Functions -- Your Code's Superpowers
=================================================
Functions are reusable blocks of code. Think of them as recipes:
  - You define them once (write the recipe)
  - You call them whenever you need them (cook the dish)

Without functions, you'd be copy-pasting code everywhere like a
caveman. With functions, you're a coding wizard.

Let's learn ALL the function tricks!
"""

# =============================================================================
# 1. DEFINING & CALLING FUNCTIONS
# =============================================================================
print("=== Basic Functions ===")

# The simplest function -- no parameters, no return
def greet():
    """Say hello! (This triple-quote string is called a 'docstring')."""
    print("Hello, World! I'm a function!")

# Call it -- just use the name followed by ()
greet()                 # Hello, World! I'm a function!
greet()                 # You can call it as many times as you want!

# A function that takes parameters (inputs)
def greet_person(name):
    """Greet someone by name. Much more personal!"""
    print(f"Hello, {name}! Welcome to the Python dojo.")

greet_person("Naruto")   # Hello, Naruto! Welcome to the Python dojo.
greet_person("Goku")     # Hello, Goku! Welcome to the Python dojo.

# =============================================================================
# 2. RETURN VALUES
# =============================================================================
print("\n=== Return Values ===")

# Functions can send data BACK using 'return'
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")  # 8

# You can use the return value directly
print(f"10 + 20 = {add(10, 20)}")  # 30

# Return multiple values as a tuple!
def divide(a, b):
    """Return both quotient and remainder -- two for the price of one!"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns a tuple

q, r = divide(17, 5)
print(f"17 / 5 = {q} remainder {r}")  # 3 remainder 2

# A function without 'return' returns None
def say_hi():
    print("Hi!")

result = say_hi()
print(f"Return value: {result}")  # None

# =============================================================================
# 3. DEFAULT PARAMETERS
# =============================================================================
print("\n=== Default Parameters ===")

# Give parameters default values -- callers can override or skip them
def make_coffee(size="medium", milk=True, sugar=2):
    """Make a coffee order. Customize to your heart's content!"""
    milk_str = "with milk" if milk else "black"
    print(f"  One {size} coffee, {milk_str}, {sugar} sugar(s). Coming right up!")

make_coffee()                         # Uses all defaults
make_coffee("large")                  # Override size only
make_coffee("small", False)           # Override size and milk
make_coffee("large", True, 0)         # Override everything

# IMPORTANT: Default params must come AFTER non-default params!
# def bad_function(name="default", age):  # SyntaxError!

# =============================================================================
# 4. KEYWORD ARGUMENTS
# =============================================================================
print("\n=== Keyword Arguments ===")

# You can pass arguments by NAME -- order doesn't matter!
make_coffee(sugar=5, size="extra-large", milk=False)
# Same as: make_coffee("extra-large", False, 5)

# This is super useful when functions have lots of parameters
def create_character(name, health=100, attack=10, defense=5, speed=7):
    """Create an RPG character. Keyword args let you skip to what matters."""
    return {
        "name": name,
        "health": health,
        "attack": attack,
        "defense": defense,
        "speed": speed
    }

# Only customize what you care about!
tank = create_character("Reinhardt", health=500, defense=50, speed=2)
speedster = create_character("Tracer", health=60, speed=20, attack=15)
print(f"Tank: {tank}")
print(f"Speedster: {speedster}")

# =============================================================================
# 5. *args -- VARIABLE POSITIONAL ARGUMENTS
# =============================================================================
print("\n=== *args (Variable Arguments) ===")

# *args lets a function accept ANY number of positional arguments
# They arrive as a tuple
def sum_all(*numbers):
    """Sum any number of values. One, ten, a hundred -- bring 'em on!"""
    print(f"  Received: {numbers} (type: {type(numbers).__name__})")
    return sum(numbers)

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20: {sum_all(10, 20)}")
print(f"Sum of single 42: {sum_all(42)}")
print(f"Sum of nothing: {sum_all()}")  # 0 -- empty tuple

# Real-world example: a flexible print function
def shout(*words):
    """SHOUT all the words! Like a sports commentator."""
    message = " ".join(words).upper()
    print(f"  >> {message}!! <<")

shout("goal")                          # >> GOAL!! <<
shout("it's", "a", "home", "run")      # >> IT'S A HOME RUN!! <<

# =============================================================================
# 6. **kwargs -- VARIABLE KEYWORD ARGUMENTS
# =============================================================================
print("\n=== **kwargs (Variable Keyword Arguments) ===")

# **kwargs lets a function accept ANY number of keyword arguments
# They arrive as a dictionary
def print_profile(**info):
    """Print whatever profile info you give me. I'm flexible like that."""
    print("  --- Profile ---")
    for key, value in info.items():
        # Make the key look nice: "first_name" -> "First Name"
        nice_key = key.replace("_", " ").title()
        print(f"  {nice_key}: {value}")

print_profile(name="Yoda", age=900, occupation="Jedi Master", planet="Dagobah")
print()
print_profile(name="Gandalf", title="The Grey", hobby="fireworks")

# =============================================================================
# 7. COMBINING PARAMETER TYPES
# =============================================================================
print("\n=== Combining All Parameter Types ===")

# The order MUST be: regular -> *args -> keyword defaults -> **kwargs
def ultimate_function(required, *args, option="default", **kwargs):
    """
    This function takes everything Python can throw at it.
    Order matters: positional, *args, keyword defaults, **kwargs.
    """
    print(f"  Required: {required}")
    print(f"  Extra args: {args}")
    print(f"  Option: {option}")
    print(f"  Keyword args: {kwargs}")

ultimate_function(
    "hello",               # required
    1, 2, 3,               # *args
    option="custom",       # keyword with default
    name="Bob", age=30     # **kwargs
)

# =============================================================================
# 8. SCOPE -- Local vs Global Variables
# =============================================================================
print("\n=== Scope (Local vs Global) ===")

# Global variable -- accessible everywhere
universe = "Marvel"

def describe_hero():
    """This function can READ the global variable."""
    hero = "Iron Man"  # Local variable -- only exists inside this function
    print(f"  {hero} is from the {universe} universe")

describe_hero()  # Works fine!
# print(hero)    # NameError! 'hero' is local to the function

# Trying to MODIFY a global inside a function? You need the 'global' keyword.
counter = 0

def increment():
    global counter  # Tell Python: "I mean the GLOBAL counter, not a new local one"
    counter += 1

increment()
increment()
increment()
print(f"Counter after 3 increments: {counter}")  # 3

# PRO TIP: Avoid 'global' when possible. It makes code harder to debug.
# Better approach: pass the value in and return the new value.
def increment_better(count):
    """A cleaner way -- no global needed!"""
    return count + 1

my_count = 0
my_count = increment_better(my_count)
my_count = increment_better(my_count)
print(f"Better counter: {my_count}")  # 2

# =============================================================================
# 9. FUNCTIONS AS FIRST-CLASS OBJECTS
# =============================================================================
print("\n=== Functions as First-Class Objects ===")

# In Python, functions are OBJECTS. You can:
# - Assign them to variables
# - Pass them as arguments
# - Return them from other functions

# Assign a function to a variable (no parentheses -- don't call it!)
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Pass a function as an argument!
def apply_operation(func, numbers):
    """Apply any function to a list of numbers. The power of abstraction!"""
    return [func(n) for n in numbers]

nums = [1, 2, 3, 4, 5]
print(f"Squared: {apply_operation(square, nums)}")  # [1, 4, 9, 16, 25]
print(f"Cubed:   {apply_operation(cube, nums)}")     # [1, 8, 27, 64, 125]

# Store functions in a data structure -- because why not?
operations = {
    "square": square,
    "cube": cube,
    "double": lambda x: x * 2,  # Sneak peek of lambdas! (Chapter 14)
}

for name, func in operations.items():
    print(f"  {name}(5) = {func(5)}")

# A function that RETURNS a function (this is called a "closure")
def make_multiplier(factor):
    """Create a custom multiplier function. Function factory!"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"\ndouble(10) = {double(10)}")  # 20
print(f"triple(10) = {triple(10)}")    # 30

# =============================================================================
# 10. PRACTICAL EXAMPLE: A Mini Calculator with Function Dispatch
# =============================================================================
print("\n=== Mini Calculator ===")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero! Even Python can't do that."
    return a / b

# Function dispatch table -- mapping strings to functions
calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Use it!
for op_symbol, func in calculator.items():
    result = func(10, 3)
    print(f"  10 {op_symbol} 3 = {result}")

# =============================================================================
# RECAP
# =============================================================================
print("\n" + "=" * 50)
print("CHAPTER 10 RECAP -- Functions")
print("=" * 50)
print("""
- def function_name(params): ... defines a function
- return sends a value back (without it, you get None)
- Default params: def f(x=10) -- optional arguments
- Keyword args: f(name="Bob") -- order doesn't matter
- *args: catch unlimited positional args as a tuple
- **kwargs: catch unlimited keyword args as a dict
- Scope: local vars live inside functions, globals live outside
- Functions are objects: pass them around like any other value
- Closures: functions that remember their creation environment

Functions are the building blocks of clean, reusable code.
Write them small, name them well, and your future self
will thank your present self.
""")
