"""
Chapter 24: Testing — Making Sure Your Code Actually Works
=============================================================

"Untested code is broken code." — Someone who learned the hard way.

Why test?
  - Catch bugs BEFORE users do
  - Refactor with confidence ("did I break anything?")
  - Document what your code SHOULD do
  - Sleep better at night

We'll cover:
  1. unittest (built-in, classic)
  2. pytest (modern, popular, easier)
  3. Assert statements
  4. Fixtures
  5. Parametrize
  6. Mocking

Install pytest: pip install pytest
Run tests: pytest examples.py -v  (or python -m pytest examples.py -v)
"""

# ============================================================
# 0. Code to Test — A Simple Calculator
# ============================================================

class Calculator:
    """A basic calculator. Our guinea pig for testing."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero! Math says no.")
        return a / b

    def power(self, base, exp):
        return base ** exp


def is_palindrome(text):
    """Check if text is a palindrome (reads the same forwards and backwards)."""
    cleaned = text.lower().replace(" ", "").replace(",", "").replace("!", "").replace(".", "")
    return cleaned == cleaned[::-1]


def fizzbuzz(n):
    """The classic FizzBuzz problem."""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


# ============================================================
# 1. unittest — The Built-In Testing Framework
# ============================================================
import unittest


class TestCalculatorUnittest(unittest.TestCase):
    """
    unittest.TestCase is the classic way to write tests in Python.
    Every test method must start with 'test_'.
    """

    def setUp(self):
        """
        setUp() runs BEFORE each test method.
        Use it to create fresh test objects.
        """
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333, places=4)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        """
        tearDown() runs AFTER each test method.
        Use it to clean up (close files, connections, etc.)
        """
        pass  # nothing to clean up here


# ============================================================
# 2. pytest — The Modern Way (Simpler, More Powerful)
# ============================================================
# pytest doesn't need a class! Just write functions starting with test_

def test_add_simple():
    """pytest is simpler — just use plain assert statements!"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract_simple():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_divide_by_zero_pytest():
    """pytest uses pytest.raises instead of assertRaises."""
    import pytest
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)


# ============================================================
# 3. Assert Statements — The Building Blocks
# ============================================================

def test_assert_examples():
    """
    Different ways to assert things in tests.

    unittest style:
        self.assertEqual(a, b)
        self.assertTrue(x)
        self.assertFalse(x)
        self.assertIn(item, list)
        self.assertIsNone(x)
        self.assertRaises(Error)

    pytest style (just use assert — much cleaner!):
        assert a == b
        assert x is True
        assert x is False
        assert item in collection
        assert result is None
    """
    # Equality
    assert 2 + 2 == 4, "Basic math should work!"

    # Truthiness
    assert is_palindrome("racecar")
    assert not is_palindrome("python")

    # Containment
    assert "hello" in "hello world"
    assert 3 in [1, 2, 3, 4, 5]

    # None check
    assert None is None

    # Type check
    assert isinstance(42, int)
    assert isinstance("hello", str)


# ============================================================
# 4. Testing is_palindrome
# ============================================================

def test_palindrome_basic():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False


def test_palindrome_case_insensitive():
    assert is_palindrome("Racecar") is True
    assert is_palindrome("RaCeCaR") is True


def test_palindrome_with_spaces():
    assert is_palindrome("taco cat") is True
    assert is_palindrome("was it a car or a cat i saw") is True


def test_palindrome_empty():
    assert is_palindrome("") is True


def test_palindrome_single_char():
    assert is_palindrome("a") is True


# ============================================================
# 5. Testing FizzBuzz
# ============================================================

def test_fizzbuzz_regular():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(7) == "7"


def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"


def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


# ============================================================
# 6. Fixtures — Shared Setup for Tests
# ============================================================
try:
    import pytest

    @pytest.fixture
    def calculator():
        """
        A fixture creates a fresh Calculator for each test that needs it.
        Just add it as a parameter to your test function — pytest injects it!
        """
        return Calculator()

    @pytest.fixture
    def sample_data():
        """Fixture providing sample test data."""
        return {
            "palindromes": ["racecar", "madam", "level", "civic"],
            "not_palindromes": ["hello", "python", "world", "testing"],
        }

    def test_with_fixture(calculator):
        """This test receives the calculator fixture automatically!"""
        assert calculator.add(1, 2) == 3
        assert calculator.multiply(3, 4) == 12

    def test_palindrome_fixture(sample_data):
        """Using the sample_data fixture."""
        for word in sample_data["palindromes"]:
            assert is_palindrome(word), f"'{word}' should be a palindrome!"

        for word in sample_data["not_palindromes"]:
            assert not is_palindrome(word), f"'{word}' should NOT be a palindrome!"


    # ============================================================
    # 7. Parametrize — Test Multiple Cases Elegantly
    # ============================================================

    @pytest.mark.parametrize("input_text,expected", [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("python", False),
        ("A man a plan a canal Panama", True),
        ("", True),
        ("a", True),
    ])
    def test_palindrome_parametrized(input_text, expected):
        """
        @pytest.mark.parametrize runs the SAME test with DIFFERENT inputs.
        Way cleaner than writing 7 separate test functions!
        """
        assert is_palindrome(input_text) == expected


    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (100, 200, 300),
        (-5, -3, -8),
    ])
    def test_add_parametrized(calculator, a, b, expected):
        """Parametrize + fixture = testing power!"""
        assert calculator.add(a, b) == expected

except ImportError:
    print("pytest not installed. Install with: pip install pytest")
    print("Skipping pytest-specific examples.")


# ============================================================
# 8. Mocking — Faking External Dependencies
# ============================================================
from unittest.mock import Mock, patch


def get_weather(city):
    """
    Pretend this calls a real weather API.
    In tests, we don't want to hit the real API — we MOCK it!
    """
    import requests
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()


def test_mock_example():
    """
    Mock replaces real objects with fake ones for testing.
    This way we can test our code WITHOUT hitting real APIs!
    """
    # Create a mock object
    mock_response = Mock()
    mock_response.json.return_value = {"temp": 72, "city": "New York"}
    mock_response.status_code = 200

    # Use the mock
    assert mock_response.json() == {"temp": 72, "city": "New York"}
    assert mock_response.status_code == 200

    # Verify it was called
    mock_response.json.assert_called_once()


def format_weather(weather_data):
    """Format weather data for display."""
    return f"{weather_data['city']}: {weather_data['temp']}F"


def test_format_weather():
    """Test formatting without needing real weather data."""
    fake_data = {"city": "Gotham", "temp": 55}
    result = format_weather(fake_data)
    assert result == "Gotham: 55F"


# ============================================================
# Run the tests
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  CHAPTER 24: TESTING EXAMPLES")
    print("=" * 55)
    print("""
How to run these tests:

  1. Using unittest:
     python -m unittest examples.py -v

  2. Using pytest (recommended):
     pytest examples.py -v

  3. Run just this file to see the demo below:
     python examples.py
""")

    # Quick demo run with unittest
    print("--- Running unittest demo ---\n")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculatorUnittest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    print("""
\n--- Recap ---

Testing Cheat Sheet:
-----------------------------------------------------------------
UNITTEST (built-in):
  class TestX(unittest.TestCase):
      def setUp(self):         → runs before each test
      def test_something(self): → test method (must start with test_)
      def tearDown(self):      → runs after each test

PYTEST (recommended):
  def test_something():        → just a function!
  assert result == expected    → plain assert statements

FIXTURES (pytest):
  @pytest.fixture
  def my_data():
      return {"key": "value"}
  def test_x(my_data):        → fixture injected as parameter

PARAMETRIZE (pytest):
  @pytest.mark.parametrize("input,expected", [(1, 2), (3, 4)])
  def test_x(input, expected): → runs once per case

MOCKING:
  from unittest.mock import Mock, patch
  mock_obj = Mock()
  mock_obj.method.return_value = "fake"

RUN: pytest -v                 → verbose output
     pytest -x                 → stop on first failure
     pytest --tb=short         → shorter tracebacks
     pytest -k "palindrome"    → run only matching tests
-----------------------------------------------------------------
""")
