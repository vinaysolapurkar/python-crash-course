"""
Chapter 19 Exercise SOLUTION: Build Your Own Decorators
========================================================
Three decorators that'll make your code feel like it has superpowers. 🦸
"""

import time
import random
from functools import wraps
from datetime import datetime


# ============================================================
# 1. @timer — Measure Execution Time
# ============================================================

def timer(func):
    """
    Decorator that measures how long a function takes to execute.
    Essential for finding performance bottlenecks!
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start

        # Color-code the time (just with text, no ANSI needed)
        if elapsed < 0.01:
            speed = "lightning fast"
        elif elapsed < 0.1:
            speed = "pretty quick"
        elif elapsed < 1.0:
            speed = "moderate"
        else:
            speed = "slow — maybe optimize?"

        print(f"  [TIMER] {func.__name__} took {elapsed:.4f}s ({speed})")
        return result
    return wrapper


# ============================================================
# 2. @logger — Log Function Calls
# ============================================================

def logger(func):
    """
    Decorator that logs every function call with timestamp,
    arguments, and return value. Like a security camera for your code.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format arguments nicely
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"  [{timestamp}] Calling {func.__name__}({all_args})")

        try:
            result = func(*args, **kwargs)
            print(f"  [{timestamp}] {func.__name__} returned: {result!r}")
            return result
        except Exception as e:
            print(f"  [{timestamp}] {func.__name__} raised: {type(e).__name__}: {e}")
            raise

    return wrapper


# ============================================================
# 3. @retry — Retry on Failure
# ============================================================

def retry(max_attempts=3, delay=1):
    """
    Decorator that retries a function if it raises an exception.
    Perfect for network calls, API requests, and other flaky operations.

    This is a decorator WITH ARGUMENTS, so we need three levels:
    retry(args) → decorator(func) → wrapper(*args, **kwargs)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        print(f"  [RETRY] {func.__name__} succeeded on attempt {attempt}!")
                    return result
                except Exception as e:
                    last_exception = e
                    remaining = max_attempts - attempt
                    if remaining > 0:
                        print(f"  [RETRY] {func.__name__} attempt {attempt}/{max_attempts} "
                              f"failed: {e}. Retrying in {delay}s... "
                              f"({remaining} attempts left)")
                        time.sleep(delay)
                    else:
                        print(f"  [RETRY] {func.__name__} FAILED after {max_attempts} attempts.")

            raise last_exception  # re-raise the last exception

        return wrapper
    return decorator


# ============================================================
# Test Drive!
# ============================================================
print("DECORATOR TEST DRIVE")
print("=" * 50)

# ---- Test @timer ----
print("\n--- @timer ---")

@timer
def calculate_sum(n):
    """Calculate sum of 1 to n."""
    return sum(range(n + 1))

@timer
def sort_random_list(size):
    """Sort a random list."""
    data = [random.randint(0, 1000) for _ in range(size)]
    return sorted(data)

result = calculate_sum(1_000_000)
print(f"  Sum of 1 to 1,000,000: {result:,}\n")

sorted_list = sort_random_list(100_000)
print(f"  Sorted {len(sorted_list):,} numbers. First 5: {sorted_list[:5]}\n")


# ---- Test @logger ----
print("\n--- @logger ---")

@logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

@logger
def greet(name, greeting="Hello"):
    """Greet someone."""
    return f"{greeting}, {name}!"

@logger
def risky_divide(a, b):
    """Divide, but might fail."""
    return a / b

multiply(6, 7)
print()

greet("Alice", greeting="Hey")
print()

try:
    risky_divide(10, 0)
except ZeroDivisionError:
    print("  (Caught the logged exception!)")
print()


# ---- Test @retry ----
print("\n--- @retry ---")

@retry(max_attempts=5, delay=0.1)
def flaky_api_call():
    """Simulates an unreliable API."""
    if random.random() < 0.6:  # 60% failure rate
        raise ConnectionError("Server timeout")
    return {"status": "ok", "data": "Important stuff"}

try:
    result = flaky_api_call()
    print(f"  API Result: {result}")
except ConnectionError:
    print("  API is completely down. Try again later!")
print()

@retry(max_attempts=3, delay=0.05)
def always_fails():
    """This one never works. Poor thing."""
    raise ValueError("I'm broken and I know it")

try:
    always_fails()
except ValueError:
    print("  Confirmed: it always fails.\n")


# ---- Test Stacking Decorators ----
print("\n--- Stacked Decorators ---")

@timer
@logger
def power(base, exponent):
    """Calculate base ** exponent."""
    time.sleep(0.05)  # simulate some work
    return base ** exponent

# timer wraps logger wraps power
# So we get: timing includes logging overhead
result = power(2, 10)
print(f"  Final result: {result}\n")


# ---- Verify @wraps works ----
print("\n--- @wraps Verification ---")
print(f"  calculate_sum.__name__ = '{calculate_sum.__name__}'")
print(f"  calculate_sum.__doc__  = '{calculate_sum.__doc__}'")
print(f"  flaky_api_call.__name__ = '{flaky_api_call.__name__}'")
print(f"  (All original names and docstrings preserved!)")


# ---- Bonus: Using all three together ----
print("\n--- All Three Together (The Ultimate Function) ---")

@retry(max_attempts=3, delay=0.05)
@timer
@logger
def ultimate_function(x):
    """A function with ALL the decorators. Maximum power!"""
    if random.random() < 0.3:
        raise RuntimeError("Random failure!")
    return x * 42

try:
    result = ultimate_function(10)
    print(f"  Ultimate result: {result}")
except RuntimeError:
    print("  Even the ultimate function can fail sometimes.")
