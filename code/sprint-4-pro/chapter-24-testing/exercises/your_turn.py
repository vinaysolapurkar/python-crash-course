"""
Chapter 24 Exercise: Test the Password Strength Checker
========================================================

Write tests for a password strength checker function.

The password checker (provided below) rates passwords as:
  "weak"     → less than 8 characters
  "medium"   → 8+ chars, has letters and numbers
  "strong"   → 8+ chars, has uppercase, lowercase, numbers, and special chars
  "very strong" → 12+ chars, meets all strong criteria

Your job: Write comprehensive tests using pytest!

Requirements:
  1. Test weak passwords (short, empty, common)
  2. Test medium passwords
  3. Test strong passwords
  4. Test very strong passwords
  5. Test edge cases (empty string, only spaces, unicode, etc.)
  6. Use @pytest.mark.parametrize for at least one test group
  7. Use a fixture for common test data

Bonus:
  - Test that the function handles None input gracefully
  - Test performance (should be fast for any reasonable password)
  - Achieve 100% code coverage of the password checker

Starter code below:
"""

import pytest


# ---- The code to test (don't modify this!) ----

def check_password_strength(password):
    """
    Check password strength and return a rating.

    Returns: "weak", "medium", "strong", or "very strong"
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string!")

    if len(password) < 8:
        return "weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if len(password) >= 12 and score == 4:
        return "very strong"
    elif score >= 3:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"


# ---- Your tests go below! ----

# TODO: Create a fixture for test data
# @pytest.fixture
# def common_passwords():
#     return { ... }


# TODO: Test weak passwords
# def test_weak_short_password():
#     assert check_password_strength("abc") == "weak"


# TODO: Test medium passwords
# def test_medium_password():
#     ...


# TODO: Test strong passwords
# def test_strong_password():
#     ...


# TODO: Test very strong passwords
# def test_very_strong_password():
#     ...


# TODO: Test edge cases
# def test_empty_password():
#     ...
# def test_none_password():
#     ...


# TODO: Use parametrize for multiple test cases
# @pytest.mark.parametrize("password,expected", [
#     ...
# ])
# def test_password_strengths(password, expected):
#     assert check_password_strength(password) == expected


# ---- Run instructions ----
# pytest your_turn.py -v
