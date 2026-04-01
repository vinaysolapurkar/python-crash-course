"""
Chapter 19 Exercise: Build Your Own Decorators
================================================

Build three practical decorators that you'd actually use in real projects!

Requirements:

1. @timer decorator:
   - Measure and print how long a function takes
   - Use @wraps to preserve function identity
   - Print the function name and elapsed time

2. @logger decorator:
   - Log every function call with arguments and return value
   - Print timestamp, function name, args, kwargs, and result
   - Use @wraps

3. @retry decorator (with arguments!):
   - Takes max_attempts (default 3) and delay (default 1 second)
   - Retries the function if it raises an exception
   - Prints which attempt number it's on
   - Re-raises the exception after all attempts fail
   - Use @wraps

Starter code below:
"""

import time
from functools import wraps
from datetime import datetime


def timer(func):
    """
    Decorator that measures execution time.

    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    """
    # TODO: Implement the wrapper
    # Hint: time.time() before and after, calculate difference
    pass


def logger(func):
    """
    Decorator that logs function calls with timestamp.

    Usage:
        @logger
        def add(a, b):
            return a + b

    Should print something like:
        [2024-01-15 10:30:45] Calling add(3, 5)
        [2024-01-15 10:30:45] add returned: 8
    """
    # TODO: Implement the wrapper
    # Hint: datetime.now().strftime("%Y-%m-%d %H:%M:%S") for timestamp
    pass


def retry(max_attempts=3, delay=1):
    """
    Decorator that retries a function on failure.

    Usage:
        @retry(max_attempts=5, delay=0.5)
        def flaky_function():
            ...

    Remember: decorators with arguments need THREE levels of nesting!
    """
    # TODO: This is a decorator FACTORY (returns a decorator)
    # Level 1: retry(max_attempts, delay) — the factory
    # Level 2: decorator(func) — the actual decorator
    # Level 3: wrapper(*args, **kwargs) — the wrapped function
    pass


# ----- Test your decorators! -----

# TODO: Test @timer
# @timer
# def calculate_sum(n):
#     """Calculate sum of 1 to n."""
#     return sum(range(n + 1))
#
# result = calculate_sum(1_000_000)
# print(f"Sum: {result}\n")

# TODO: Test @logger
# @logger
# def multiply(a, b):
#     return a * b
#
# @logger
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# multiply(6, 7)
# greet("Alice", greeting="Hey")
# print()

# TODO: Test @retry
# import random
#
# @retry(max_attempts=5, delay=0.1)
# def unstable_operation():
#     """Simulates an operation that fails randomly."""
#     if random.random() < 0.6:
#         raise ConnectionError("Connection lost!")
#     return "Success!"
#
# try:
#     result = unstable_operation()
#     print(f"Result: {result}")
# except ConnectionError:
#     print("All attempts failed!")

# TODO: Test stacking decorators
# @timer
# @logger
# def divide(a, b):
#     return a / b
#
# divide(10, 3)
