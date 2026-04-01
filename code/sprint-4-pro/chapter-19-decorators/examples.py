"""
Chapter 19: Decorators — Supercharging Your Functions
=====================================================

Decorators are like adding superpowers to your functions without
changing the functions themselves.

Imagine you have a plain donut (your function). A decorator is like
dipping it in chocolate, adding sprinkles, or drizzling caramel on top.
The donut is still a donut — but now it's BETTER.

Before we get to decorators, we need to understand two key concepts:
1. Functions are first-class objects (they can be passed around)
2. Closures (functions that remember their environment)
"""

# ============================================================
# 1. Functions Are First-Class Objects
# ============================================================
print("=" * 50)
print("1. FUNCTIONS AS FIRST-CLASS OBJECTS")
print("=" * 50)


def greet(name):
    return f"Hello, {name}!"


# Functions can be assigned to variables
say_hello = greet  # No parentheses! We're assigning the function itself.
print(say_hello("World"))  # Same as greet("World")

# Functions can be passed as arguments
def apply_function(func, value):
    """Takes a function and a value, applies the function."""
    return func(value)

print(apply_function(greet, "Python"))
print(apply_function(len, "Hello"))  # Built-in functions work too!
print(apply_function(str.upper, "whisper"))


# Functions can be returned from other functions
def create_multiplier(factor):
    """Returns a NEW function that multiplies by the given factor."""
    def multiplier(x):
        return x * factor
    return multiplier  # returning the function itself!

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(5) = {double(5)}")   # 10
print(f"triple(5) = {triple(5)}")   # 15


# ============================================================
# 2. Closures — Functions That Remember
# ============================================================
print("\n" + "=" * 50)
print("2. CLOSURES")
print("=" * 50)


def create_counter():
    """
    A closure: the inner function 'remembers' the count variable
    even after create_counter() has finished running.
    It's like a function with a built-in memory. Inception vibes! 🌀
    """
    count = 0

    def increment():
        nonlocal count  # "I want to modify the outer variable"
        count += 1
        return count

    return increment


counter = create_counter()
print(f"Count: {counter()}")  # 1
print(f"Count: {counter()}")  # 2
print(f"Count: {counter()}")  # 3

# Each counter is independent!
another_counter = create_counter()
print(f"Another: {another_counter()}")  # 1 (fresh counter)


# ============================================================
# 3. Your First Decorator — The Basic Pattern
# ============================================================
print("\n" + "=" * 50)
print("3. YOUR FIRST DECORATOR")
print("=" * 50)


def shout_decorator(func):
    """
    A decorator that makes any function's result UPPERCASE.

    The pattern:
    1. Take a function as input
    2. Create a wrapper that adds behavior
    3. Return the wrapper
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # call the original function
        return result.upper() + "!!!"   # modify the result
    return wrapper


# Method 1: Manual decoration
def say_hi(name):
    return f"Hi, {name}"

say_hi_loud = shout_decorator(say_hi)
print(say_hi_loud("Alice"))  # "HI, ALICE!!!"


# Method 2: The @ syntax (syntactic sugar — same thing, prettier)
@shout_decorator
def say_goodbye(name):
    return f"Goodbye, {name}"

# This is EXACTLY the same as: say_goodbye = shout_decorator(say_goodbye)
print(say_goodbye("Bob"))  # "GOODBYE, BOB!!!"


# ============================================================
# 4. Practical Decorators — The Useful Ones
# ============================================================
print("\n" + "=" * 50)
print("4. PRACTICAL DECORATORS")
print("=" * 50)

import time
from functools import wraps

# ---- Timer Decorator ----
def timer(func):
    """Measure how long a function takes to run."""
    @wraps(func)  # preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  [{func.__name__}] took {elapsed:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    """I'm a slow function. Don't judge me."""
    time.sleep(0.3)
    return "Done being slow!"

print(slow_function())
print(f"  Function name preserved: {slow_function.__name__}")  # "slow_function" thanks to @wraps


# ---- Logger Decorator ----
def logger(func):
    """Log every call to a function — who called what, with what args."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"  Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned: {result!r}")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b

@logger
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet_person("Alice", greeting="Hey")


# ---- Retry Decorator ----
print("\n--- Retry Decorator ---")

import random

def retry(max_attempts=3, delay=0.1):
    """
    Retry a function if it raises an exception.
    This is a DECORATOR WITH ARGUMENTS — it needs an extra layer.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
                    else:
                        print(f"  All {max_attempts} attempts failed!")
                        raise
        return wrapper
    return decorator


@retry(max_attempts=5, delay=0.05)
def unreliable_api_call():
    """Simulates a flaky API that fails randomly."""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Server is having a bad day")
    return "API response: Success!"

try:
    result = unreliable_api_call()
    print(f"  Result: {result}")
except ConnectionError:
    print("  Even after retries, still failed. The server is REALLY having a bad day.")


# ============================================================
# 5. Decorator with Arguments — The Triple Wrapper
# ============================================================
print("\n" + "=" * 50)
print("5. DECORATORS WITH ARGUMENTS")
print("=" * 50)


def repeat(n=2):
    """Run a function n times. Because once is never enough."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


@repeat(n=3)
def say_hello_again(name):
    print(f"  Hello, {name}!")
    return f"greeted {name}"

results = say_hello_again("World")
print(f"  Results: {results}")


# ============================================================
# 6. @wraps — Why It Matters
# ============================================================
print("\n" + "=" * 50)
print("6. @wraps — PRESERVING FUNCTION IDENTITY")
print("=" * 50)


# WITHOUT @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_func():
    """I'm a well-documented function."""
    pass

print(f"Without @wraps: name='{my_func.__name__}', doc='{my_func.__doc__}'")
# Shows: name='wrapper', doc=None  — the original identity is LOST!


# WITH @wraps (always use this!)
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_func2():
    """I'm a well-documented function."""
    pass

print(f"With @wraps:    name='{my_func2.__name__}', doc='{my_func2.__doc__}'")
# Shows: name='my_func2', doc="I'm a well-documented function." — preserved!


# ============================================================
# 7. @property — The Most Useful Built-in Decorator
# ============================================================
print("\n" + "=" * 50)
print("7. @property — COMPUTED ATTRIBUTES")
print("=" * 50)


class Circle:
    """
    @property lets you access a method like an attribute.
    Instead of: circle.get_area()
    You write:  circle.area     (no parentheses! looks like an attribute)
    """

    def __init__(self, radius):
        self._radius = radius  # protected attribute

    @property
    def radius(self):
        """Getter: access radius like an attribute."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter: validates before setting."""
        if value < 0:
            raise ValueError("Radius can't be negative! That's not how circles work.")
        self._radius = value

    @property
    def area(self):
        """Computed property: always calculated from current radius."""
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """Another computed property."""
        import math
        return 2 * math.pi * self._radius

    def __str__(self):
        return f"Circle(r={self.radius}, area={self.area:.2f})"


c = Circle(5)
print(f"Radius: {c.radius}")           # uses @property getter
print(f"Area: {c.area:.2f}")           # computed on the fly!
print(f"Circumference: {c.circumference:.2f}")

c.radius = 10  # uses @radius.setter
print(f"\nAfter resize: {c}")

try:
    c.radius = -5  # setter validates!
except ValueError as e:
    print(f"Error: {e}")


# ============================================================
# 8. Stacking Decorators
# ============================================================
print("\n" + "=" * 50)
print("8. STACKING DECORATORS")
print("=" * 50)


@timer
@logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# This is equivalent to: multiply = timer(logger(multiply))
# logger wraps first, then timer wraps around that
print(f"Result: {multiply(6, 7)}")


# ============================================================
# 9. Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 19 RECAP")
print("=" * 50)
print("""
Decorator Cheat Sheet:
-----------------------------------------------------------------
FIRST-CLASS FUNCTIONS:
  Functions can be assigned, passed, and returned like any value.

CLOSURE:
  A function that remembers variables from its enclosing scope.

BASIC DECORATOR:
  def my_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          # do something before
          result = func(*args, **kwargs)
          # do something after
          return result
      return wrapper

DECORATOR WITH ARGS:
  def my_decorator(arg):
      def decorator(func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              ...
          return wrapper
      return decorator

@wraps(func):
  ALWAYS use this! Preserves the original function's name and docstring.

@property:
  Access methods like attributes. Great for computed values and validation.

COMMON PATTERNS:
  @timer      — measure execution time
  @logger     — log function calls
  @retry      — retry on failure
  @property   — computed attributes with validation
-----------------------------------------------------------------
""")
