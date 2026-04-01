# Chapter 24: Testing -- Proving Your Code Works

> **Sprint 4, Chapter 24** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Picture this. It's Friday at 4:45 PM. You push a "small change" to production. You head home feeling productive. At 6 PM, your phone starts buzzing. The signup page is broken. New users can't create accounts. Your "small change" had a typo in the email validation function. Thousands of potential users hit an error page over the weekend.

A single test would have caught it.

"It works on my machine" isn't good enough. Tests catch bugs before your users do. They let you change code without fear. They're the difference between "I think this works" and "I know this works."

Every serious software company requires tests. Every open-source project worth using has tests. If you want to write professional code, you need to write tests.

## The Proofreading Analogy

Testing is like **proofreading an essay**. You could skip it -- the essay is done, the ideas are there. But do you really want to submit it with typos, missing paragraphs, and your introduction accidentally pasted in twice?

You *could* proofread by reading the whole thing yourself. That's manual testing -- running your program and clicking around. It works, but it's slow, tedious, and you'll miss things because you're human.

Automated tests are like having a robot proofreader that checks every word, every sentence, every paragraph, instantly, every time you make a change. It never gets tired. It never misses the same mistake twice.

## A Bug That Testing Would Have Caught

Let's look at a real example. Here's a discount calculator:

```python
def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    return price - (price * discount_percent / 100)
```

Looks fine, right? Let's use it:

```python
print(apply_discount(100, 20))  # 80.0 -- correct!
print(apply_discount(50, 10))   # 45.0 -- correct!
```

Ship it! But wait... what about edge cases?

```python
print(apply_discount(100, 110))  # -10.0 -- negative price?!
print(apply_discount(-50, 20))   # -40.0 -- negative input?!
print(apply_discount(100, 0))    # 100.0 -- okay
print(apply_discount(0, 50))     # 0.0 -- okay
```

A 110% discount gives a **negative price** -- the store pays the customer. That's a bug. If you had a test that checked "discount should not exceed 100%", you'd have caught it before deploying.

Here's the fixed version:

```python
def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)
```

Now let's write tests that *prove* this works correctly.

## unittest: The Built-In Way (Brief)

Python comes with a testing framework called `unittest`. It works, but it's verbose:

```python
import unittest

class TestApplyDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(apply_discount(100, 20), 80.0)
    
    def test_zero_discount(self):
        self.assertEqual(apply_discount(100, 0), 100.0)
    
    def test_full_discount(self):
        self.assertEqual(apply_discount(100, 100), 0.0)
    
    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            apply_discount(-50, 20)

if __name__ == "__main__":
    unittest.main()
```

It works, but all that `self.assertEqual`, `self.assertRaises`, and class boilerplate gets old fast. There's a better way.

## pytest: The Modern Way

**pytest** is the testing framework that professional Python developers actually use. It's simpler, more powerful, and more readable. Install it:

```bash
pip install pytest
```

Here's the same test, written with pytest:

```python
import pytest

def apply_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)

def test_basic_discount():
    assert apply_discount(100, 20) == 80.0

def test_zero_discount():
    assert apply_discount(100, 0) == 100.0

def test_full_discount():
    assert apply_discount(100, 100) == 0.0

def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        apply_discount(-50, 20)

def test_discount_over_100_raises_error():
    with pytest.raises(ValueError):
        apply_discount(100, 110)
```

No classes. No `self.assertEqual`. Just `assert` -- Python's built-in keyword. pytest discovers functions that start with `test_` and runs them automatically.

Run your tests:

```bash
pytest test_discount.py -v
```

Output:
```
test_discount.py::test_basic_discount PASSED
test_discount.py::test_zero_discount PASSED
test_discount.py::test_full_discount PASSED
test_discount.py::test_negative_price_raises_error PASSED
test_discount.py::test_discount_over_100_raises_error PASSED

============= 5 passed in 0.02s =============
```

Five green checkmarks. That's the feeling you're chasing.

> **Don't Panic:** Testing feels like extra work. It is. But it's the kind of extra work that saves you hours of debugging later. Think of it as an investment: 5 minutes writing tests now saves 2 hours debugging at midnight.

## Writing Good Test Cases

Good tests follow the **AAA pattern**: Arrange, Act, Assert.

```python
def test_discount_calculation():
    # Arrange -- set up the inputs
    price = 100
    discount = 20
    
    # Act -- call the function
    result = apply_discount(price, discount)
    
    # Assert -- check the result
    assert result == 80.0
```

What makes a good test?

1. **Test one thing.** Each test should check a single behavior.
2. **Use descriptive names.** `test_negative_price_raises_error` tells you exactly what it tests.
3. **Test edge cases.** Zero, negative numbers, empty strings, `None`, very large numbers.
4. **Test both success and failure.** Don't just test that correct inputs work -- test that incorrect inputs fail properly.
5. **Tests should be independent.** Each test should work alone, not depend on other tests running first.

Here's a complete test suite for a password strength checker:

```python
import pytest

def check_password_strength(password):
    """Return 'weak', 'medium', or 'strong'."""
    if len(password) < 8:
        return "weak"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score >= 3 and len(password) >= 12:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"

# --- Tests ---

def test_short_password_is_weak():
    assert check_password_strength("abc") == "weak"

def test_empty_password_is_weak():
    assert check_password_strength("") == "weak"

def test_only_lowercase_is_weak():
    assert check_password_strength("abcdefgh") == "weak"

def test_mixed_case_and_digits_is_medium():
    assert check_password_strength("Abcdefg1") == "medium"

def test_strong_password():
    assert check_password_strength("MyP@ssw0rd2024") == "strong"

def test_long_with_variety_is_strong():
    assert check_password_strength("Hello!World9") == "strong"
```

> **Remember When?** Remember the password checker from Chapter 10? Perfect candidate for tests. If you built it then, go back and add tests now. Future you will thank you.

## Fixtures: Reusable Test Setup

Sometimes multiple tests need the same setup. **Fixtures** provide that:

```python
import pytest
import sqlite3

@pytest.fixture
def sample_users():
    """Provide sample user data for tests."""
    return [
        {"name": "Alice", "email": "alice@test.com", "age": 28},
        {"name": "Bob", "email": "bob@test.com", "age": 34},
        {"name": "Charlie", "email": "charlie@test.com", "age": 22},
    ]

@pytest.fixture
def db_connection():
    """Create a test database that's cleaned up after each test."""
    conn = sqlite3.connect(":memory:")  # In-memory database
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """)
    yield conn  # This is where the test runs
    conn.close()  # Cleanup after the test

def test_insert_user(db_connection, sample_users):
    """Test inserting a user into the database."""
    user = sample_users[0]
    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (user["name"], user["email"], user["age"])
    )
    
    result = db_connection.execute("SELECT * FROM users").fetchone()
    assert result[1] == "Alice"
    assert result[2] == "alice@test.com"

def test_unique_email_constraint(db_connection):
    """Test that duplicate emails are rejected."""
    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Alice", "same@test.com", 28)
    )
    
    with pytest.raises(sqlite3.IntegrityError):
        db_connection.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Bob", "same@test.com", 34)
        )
```

Key fixture concepts:
- `@pytest.fixture` marks a function as a fixture
- Tests receive fixtures by including them as parameters (pytest handles the wiring)
- `yield` lets you do cleanup after the test
- `:memory:` SQLite databases are perfect for testing -- they're fast and auto-delete

## Parametrize: Many Inputs, One Test

Instead of writing separate tests for every input, use `@pytest.mark.parametrize`:

```python
import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("number, expected", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (-2, True),
    (-3, False),
    (100, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
```

One test function, seven test cases. pytest runs each one separately and reports which (if any) fail. This is incredibly powerful for testing functions with many possible inputs.

```python
@pytest.mark.parametrize("password, expected_strength", [
    ("", "weak"),
    ("abc", "weak"),
    ("abcdefgh", "weak"),
    ("Abcdefg1", "medium"),
    ("MyP@ssw0rd2024", "strong"),
])
def test_password_strength(password, expected_strength):
    assert check_password_strength(password) == expected_strength
```

## TDD: Test-Driven Development (The Red-Green-Refactor Cycle)

TDD flips the script: you write the test **before** you write the code.

The cycle:

1. **Red:** Write a test that fails (because the code doesn't exist yet)
2. **Green:** Write the simplest code that makes the test pass
3. **Refactor:** Clean up the code while keeping tests green

Let's try it. We want a function that converts temperatures:

**Step 1: Red -- Write the test first**

```python
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
```

Run pytest: **FAIL** (functions don't exist yet). Red.

**Step 2: Green -- Write the minimum code**

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
```

Run pytest: **PASS**. Green.

**Step 3: Refactor -- Improve if needed**

Maybe add input validation, type hints, or docstrings. Run tests after each change to make sure nothing breaks.

TDD feels backward at first. But it forces you to think about what your code should do *before* you write it, and it guarantees you have tests when you're done.

## Organizing Your Tests

For a real project, keep tests in a separate directory:

```
my_project/
    src/
        calculator.py
        password_checker.py
    tests/
        test_calculator.py
        test_password_checker.py
```

Name your test files `test_*.py` and your test functions `test_*`. pytest finds them automatically. Just run:

```bash
# Run all tests
pytest

# Run tests in a specific file
pytest tests/test_calculator.py

# Run a specific test
pytest tests/test_calculator.py::test_basic_discount

# Run with verbose output
pytest -v

# Run and stop at first failure
pytest -x

# Run tests matching a keyword
pytest -k "password"
```

## Bonus: Testing with Coverage

Want to know how much of your code is tested? Use `pytest-cov`:

```bash
pip install pytest-cov

pytest --cov=src --cov-report=term-missing
```

Output:
```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
src/calculator.py          10      0   100%
src/password_checker.py    15      3    80%   22-24
-----------------------------------------------------
TOTAL                      25      3    88%
```

This tells you that lines 22-24 of `password_checker.py` aren't tested. Go write a test for those lines.

100% coverage isn't always necessary, but aiming for 80%+ is a good habit.

## Your Turn: Write Tests for Password Strength Checker

**Challenge:** Write a complete test suite for the password strength checker. Include:

1. Tests for weak passwords (too short, only lowercase)
2. Tests for medium passwords (mixed case with digits)
3. Tests for strong passwords (long with variety)
4. Tests for edge cases (empty string, very long password, only special characters)
5. Use `@pytest.mark.parametrize` for at least one test
6. Use a fixture to provide sample passwords

```python
# test_password.py
import pytest

# Import your password checker
from password_checker import check_password_strength

@pytest.fixture
def common_passwords():
    """Common passwords that should all be rated 'weak'."""
    return ["password", "12345678", "qwerty123", "letmein!!"]

@pytest.mark.parametrize("password, expected", [
    # Add your test cases here
])
def test_password_strength(password, expected):
    assert check_password_strength(password) == expected

def test_common_passwords_are_weak(common_passwords):
    for password in common_passwords:
        result = check_password_strength(password)
        # What should this assert?
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-24-testing/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-24-testing/)

## TL;DR

| Concept | What It Does |
|---|---|
| `pytest` | Modern testing framework for Python |
| `assert` | Check that something is true (test fails if not) |
| `pytest.raises(Error)` | Test that code raises a specific exception |
| `@pytest.fixture` | Reusable test setup (and cleanup) |
| `@pytest.mark.parametrize` | Run one test with many different inputs |
| TDD (Red-Green-Refactor) | Write test first, then code, then clean up |
| `pytest -v` | Run tests with detailed output |
| `pytest --cov` | Check how much code your tests cover |

**The one-sentence version:** Write functions that start with `test_`, use `assert` to check results, and run `pytest` to automatically discover and execute all your tests.

Next up: Type Hints, Linting & Clean Code -- the chapter that turns your code from "it works" to "it's professional."
