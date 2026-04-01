"""
Chapter 20 Exercise SOLUTION: Fibonacci & Prime Generators
===========================================================
Two of math's greatest hits, now in generator form!
Fibonacci: nature's favorite sequence. Primes: the atoms of numbers.
"""

import sys
import math
import time


def fibonacci(limit=None):
    """
    Generate Fibonacci numbers lazily.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    Each number is the sum of the two before it.
    Fun fact: these numbers show up everywhere in nature —
    sunflower spirals, pinecone patterns, even rabbit populations!
    """
    a, b = 0, 1
    count = 0

    while limit is None or count < limit:
        yield a
        a, b = b, a + b  # the classic Fibonacci swap
        count += 1


def is_prime(n):
    """
    Check if n is a prime number.
    A prime is only divisible by 1 and itself.
    We only need to check up to sqrt(n) — math saves the day!
    """
    if n < 2:
        return False
    if n < 4:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check odd numbers up to sqrt(n)
    # We can skip even numbers (already checked 2)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(limit=None):
    """
    Generate prime numbers lazily.
    2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    Fun fact: There are infinitely many primes.
    Euclid proved this around 300 BC. Legend.
    """
    count = 0
    candidate = 2

    while limit is None or count < limit:
        if is_prime(candidate):
            yield candidate
            count += 1
        candidate += 1


def fibonacci_primes(limit=None):
    """
    Bonus: Generate Fibonacci numbers that are also prime.
    These are surprisingly rare! The first few:
    2, 3, 5, 13, 89, 233, 1597, ...
    """
    count = 0
    for fib_num in fibonacci():
        if fib_num >= 2 and is_prime(fib_num):
            yield fib_num
            count += 1
            if limit is not None and count >= limit:
                return


def take(n, generator):
    """Helper: take the first n items from a generator."""
    return [next(generator) for _ in range(n)]


# ============================================================
# Test Drive!
# ============================================================
print("FIBONACCI & PRIME GENERATORS")
print("=" * 50)

# ---- Fibonacci ----
print("\n--- Fibonacci ---")
print(f"First 10: {list(fibonacci(10))}")
print(f"First 20: {list(fibonacci(20))}")

# Infinite fibonacci — take what you need
fib_gen = fibonacci()
print(f"\nFirst 15 from infinite generator:")
print(f"  {take(15, fib_gen)}")

# The generator remembers where it left off
print(f"Next 5: {take(5, fib_gen)}")

# ---- Primes ----
print("\n--- Primes ---")
print(f"First 10: {list(primes(10))}")
print(f"First 25: {list(primes(25))}")

# Infinite primes
prime_gen = primes()
print(f"\nFirst 20 from infinite generator:")
print(f"  {take(20, prime_gen)}")

# ---- Fibonacci Primes (the rare gems!) ----
print("\n--- Fibonacci Primes (Bonus) ---")
print("These are Fibonacci numbers that are also prime.")
print("They're like finding a four-leaf clover in a field of three-leaf ones!")
print(f"First 10 Fibonacci primes: {list(fibonacci_primes(10))}")

# ---- Memory Comparison ----
print("\n--- Memory Comparison ---")
n = 100_000

# List approach
start = time.time()
fib_list = list(fibonacci(n))
list_time = time.time() - start
list_size = sys.getsizeof(fib_list)

# Generator approach (just the generator object, not consumed)
start = time.time()
fib_gen = fibonacci(n)
gen_time = time.time() - start
gen_size = sys.getsizeof(fib_gen)

print(f"Generating {n:,} Fibonacci numbers:")
print(f"  List:      {list_size:>12,} bytes | Created in {list_time:.4f}s")
print(f"  Generator: {gen_size:>12,} bytes | Created in {gen_time:.6f}s")
print(f"  Memory ratio: list is {list_size // gen_size}x larger!")
print(f"  Speed: generator creation is {list_time / max(gen_time, 0.000001):.0f}x faster")
print(f"  (but generator hasn't computed values yet — that's the point!)")

# ---- Practical: Sum first N Fibonacci numbers ----
print("\n--- Practical Use ---")

# With a generator, we can sum huge sequences without storing them
start = time.time()
total = sum(fibonacci(100_000))
elapsed = time.time() - start
print(f"Sum of first 100,000 Fibonacci numbers:")
print(f"  {str(total)[:50]}... ({len(str(total))} digits!)")
print(f"  Computed in {elapsed:.3f}s using generator (constant memory!)")

# ---- Generator Pipeline: Filtered Fibonacci ----
print("\n--- Pipeline: Even Fibonacci numbers under 1000 ---")
even_fibs = [f for f in fibonacci() if f >= 1000][:1]  # just to find the cutoff
even_fibs_under_1000 = [f for f in fibonacci(50) if f < 1000 and f % 2 == 0]
print(f"  {even_fibs_under_1000}")
print(f"  Sum: {sum(even_fibs_under_1000)}")

# ---- Fun Facts ----
print(f"""
\n--- Fun Facts ---
- The 100th Fibonacci number has {len(str(list(fibonacci(101))[-1]))} digits
- There are {len(list(primes(1000)))} primes in the first 1000 primes
  (the 1000th prime is {list(primes(1000))[-1]})
- Only about 0.1% of Fibonacci numbers are prime
- The golden ratio (1.618...) is hiding in the Fibonacci sequence:
  each number divided by the previous one approaches it!
""")

# Demonstrate the golden ratio
print("Golden ratio convergence:")
fib = list(fibonacci(15))
for i in range(2, len(fib)):
    ratio = fib[i] / fib[i-1] if fib[i-1] != 0 else 0
    print(f"  {fib[i]:>5} / {fib[i-1]:<5} = {ratio:.10f}")
