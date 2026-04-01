"""
Chapter 20 Exercise: Fibonacci & Prime Generators
==================================================

Build two generator functions:

1. fibonacci(limit=None):
   - Yields Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
   - If limit is None, generate infinitely
   - If limit is given, stop after yielding that many numbers
   - Remember: each number is the sum of the two before it

2. primes(limit=None):
   - Yields prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
   - If limit is None, generate infinitely
   - If limit is given, stop after yielding that many primes
   - A prime number is only divisible by 1 and itself

Bonus:
   - Create a generator pipeline that finds Fibonacci numbers that are also prime
   - Compare memory usage of generator vs list for first 100,000 Fibonacci numbers

Starter code below:
"""

import sys


def fibonacci(limit=None):
    """
    Generate Fibonacci numbers.

    Args:
        limit: Maximum number of values to yield. None = infinite.

    Yields:
        The next Fibonacci number in the sequence.

    Example:
        list(fibonacci(8))  →  [0, 1, 1, 2, 3, 5, 8, 13]
    """
    # TODO: Implement the Fibonacci generator
    # Hint: Start with a, b = 0, 1
    # Hint: Each step: yield a, then a, b = b, a + b
    # Hint: Keep a counter if limit is not None
    pass


def is_prime(n):
    """
    Helper: Check if a number is prime.

    TODO: Implement this!
    Hint: Check if n is divisible by any number from 2 to sqrt(n)
    """
    pass


def primes(limit=None):
    """
    Generate prime numbers.

    Args:
        limit: Maximum number of primes to yield. None = infinite.

    Yields:
        The next prime number.

    Example:
        list(primes(5))  →  [2, 3, 5, 7, 11]
    """
    # TODO: Implement the prime generator
    # Hint: Start at 2, check each number with is_prime()
    pass


# ----- Test your generators! -----

# TODO: Test fibonacci
# print("First 10 Fibonacci numbers:")
# print(list(fibonacci(10)))

# TODO: Test infinite fibonacci (take first 15)
# fib_gen = fibonacci()
# first_15 = [next(fib_gen) for _ in range(15)]
# print(f"First 15 Fibonacci: {first_15}")

# TODO: Test primes
# print("\nFirst 10 primes:")
# print(list(primes(10)))

# TODO: Test infinite primes
# prime_gen = primes()
# first_20 = [next(prime_gen) for _ in range(20)]
# print(f"First 20 primes: {first_20}")

# BONUS: Fibonacci primes (Fibonacci numbers that are also prime)
# def fibonacci_primes(limit=None):
#     """Generator that yields Fibonacci numbers that are also prime."""
#     # TODO: Combine fibonacci() and is_prime()
#     pass
#
# print("\nFirst 8 Fibonacci primes:")
# print(list(fibonacci_primes(8)))

# BONUS: Memory comparison
# print("\n--- Memory Comparison ---")
# fib_list = list(fibonacci(10000))
# fib_gen = fibonacci(10000)
# print(f"List of 10,000 Fibonacci: {sys.getsizeof(fib_list):,} bytes")
# print(f"Generator:                 {sys.getsizeof(fib_gen):,} bytes")
