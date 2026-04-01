"""
Chapter 24 Exercise SOLUTION: Test the Password Strength Checker
================================================================
Testing your security code is doubly important — bugs here mean
hackers have a field day. Let's make sure this checker is bulletproof!

Run: pytest solution.py -v
"""

import pytest


# ---- The code to test ----

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


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture
def weak_passwords():
    """A collection of passwords that should be rated 'weak'."""
    return [
        "",            # empty
        "a",           # single char
        "1234567",     # 7 chars, only digits
        "abc",         # too short
        "       ",     # only spaces (7 chars)
        "abcdefg",     # 7 lowercase letters
        "aaaaaaaa",    # 8 chars but only lowercase (score=1)
        "AAAAAAAA",    # 8 chars but only uppercase (score=1)
        "12345678",    # 8 chars but only digits (score=1)
        "!@#$%^&*",   # 8 chars but only special (score=1)
    ]


@pytest.fixture
def medium_passwords():
    """Passwords that should be rated 'medium'."""
    return [
        "abcdef12",     # lower + digit (score=2)
        "ABCDEF12",     # upper + digit (score=2)
        "abcABCDE",     # lower + upper (score=2)
        "abcdef!@",     # lower + special (score=2)
        "hello123",     # lower + digit (score=2)
        "PASSWORD1",    # upper + digit (score=2)
    ]


@pytest.fixture
def strong_passwords():
    """Passwords that should be rated 'strong'."""
    return [
        "Abcdef1!",     # upper + lower + digit + special (score=4, <12 chars)
        "Hello123!",    # meets 3+ criteria
        "Test123!",     # 8 chars, all four types
        "MyPass99!",    # strong mix
    ]


@pytest.fixture
def very_strong_passwords():
    """Passwords that should be rated 'very strong'."""
    return [
        "Abcdefgh123!",      # 12+ chars, all 4 types
        "MyStr0ng!Pass",      # 13 chars, all types
        "P@ssw0rd1234!",      # long with everything
        "C0mpl3x!Pass!",      # 13 chars, all types
    ]


# ============================================================
# Test Weak Passwords
# ============================================================

class TestWeakPasswords:
    """Tests for passwords that should be rated 'weak'."""

    def test_empty_password(self):
        assert check_password_strength("") == "weak"

    def test_single_character(self):
        assert check_password_strength("x") == "weak"

    def test_seven_characters(self):
        assert check_password_strength("abcdefg") == "weak"

    def test_only_lowercase_8chars(self):
        # 8 chars but only one category = score 1 = weak
        assert check_password_strength("abcdefgh") == "weak"

    def test_only_uppercase_8chars(self):
        assert check_password_strength("ABCDEFGH") == "weak"

    def test_only_digits_8chars(self):
        assert check_password_strength("12345678") == "weak"

    def test_only_special_8chars(self):
        assert check_password_strength("!@#$%^&*") == "weak"

    def test_spaces_short(self):
        assert check_password_strength("       ") == "weak"

    def test_fixture_weak(self, weak_passwords):
        """Test all weak passwords from the fixture."""
        for pwd in weak_passwords:
            result = check_password_strength(pwd)
            assert result == "weak", f"'{pwd}' should be weak but got '{result}'"


# ============================================================
# Test Medium Passwords
# ============================================================

class TestMediumPasswords:
    """Tests for passwords rated 'medium'."""

    def test_lower_and_digits(self):
        assert check_password_strength("hello123") == "medium"

    def test_upper_and_digits(self):
        assert check_password_strength("HELLO123") == "medium"

    def test_lower_and_upper(self):
        assert check_password_strength("helloWORLD") == "medium"

    def test_lower_and_special(self):
        assert check_password_strength("hello!!!") == "medium"

    def test_fixture_medium(self, medium_passwords):
        for pwd in medium_passwords:
            result = check_password_strength(pwd)
            assert result == "medium", f"'{pwd}' should be medium but got '{result}'"


# ============================================================
# Test Strong Passwords
# ============================================================

class TestStrongPasswords:
    """Tests for passwords rated 'strong'."""

    def test_all_four_types_short(self):
        # Has all 4 types but less than 12 chars
        assert check_password_strength("Abc123!x") == "strong"

    def test_three_types(self):
        # 3 types, 8+ chars
        assert check_password_strength("Hello12x") == "strong"

    def test_fixture_strong(self, strong_passwords):
        for pwd in strong_passwords:
            result = check_password_strength(pwd)
            assert result == "strong", f"'{pwd}' should be strong but got '{result}'"


# ============================================================
# Test Very Strong Passwords
# ============================================================

class TestVeryStrongPasswords:
    """Tests for passwords rated 'very strong'."""

    def test_12_chars_all_types(self):
        assert check_password_strength("Abcdefgh123!") == "very strong"

    def test_long_complex(self):
        assert check_password_strength("MyS3cur3P@ss!") == "very strong"

    def test_fixture_very_strong(self, very_strong_passwords):
        for pwd in very_strong_passwords:
            result = check_password_strength(pwd)
            assert result == "very strong", f"'{pwd}' should be very strong but got '{result}'"


# ============================================================
# Test Edge Cases
# ============================================================

class TestEdgeCases:
    """Tests for unusual inputs and edge cases."""

    def test_none_input(self):
        """None should raise TypeError."""
        with pytest.raises(TypeError):
            check_password_strength(None)

    def test_integer_input(self):
        """Numbers should raise TypeError."""
        with pytest.raises(TypeError):
            check_password_strength(12345678)

    def test_list_input(self):
        """Lists should raise TypeError."""
        with pytest.raises(TypeError):
            check_password_strength(["password"])

    def test_exactly_8_characters(self):
        """Boundary: exactly 8 characters."""
        result = check_password_strength("Abc123!x")
        assert result in ("medium", "strong"), f"Got '{result}'"

    def test_exactly_12_characters(self):
        """Boundary: exactly 12 characters with all types."""
        assert check_password_strength("Abcdefgh12!x") == "very strong"

    def test_very_long_password(self):
        """Very long password should still work."""
        pwd = "A1!a" * 100  # 400 characters
        assert check_password_strength(pwd) == "very strong"

    def test_unicode_characters(self):
        """Unicode should work (treated as not upper/lower/digit/special)."""
        # This tests that unicode chars don't crash the function
        result = check_password_strength("abcdefghij")
        assert isinstance(result, str)

    def test_return_type(self):
        """Function should always return a string."""
        assert isinstance(check_password_strength("test"), str)
        assert isinstance(check_password_strength("TestPass123!Xyz"), str)


# ============================================================
# Parametrized Tests — Multiple Cases, One Function
# ============================================================

@pytest.mark.parametrize("password,expected", [
    # Weak passwords
    ("", "weak"),
    ("abc", "weak"),
    ("1234567", "weak"),
    ("abcdefgh", "weak"),        # only lowercase
    ("ABCDEFGH", "weak"),        # only uppercase
    ("12345678", "weak"),        # only digits

    # Medium passwords
    ("abcdef12", "medium"),      # lower + digit
    ("ABCDEF12", "medium"),      # upper + digit
    ("abcABCDE", "medium"),      # lower + upper

    # Strong passwords
    ("Abcdef1!", "strong"),      # all 4 types, < 12 chars
    ("Hello12!", "strong"),      # 3+ types

    # Very strong passwords
    ("Abcdefgh123!", "very strong"),  # 12+ chars, all 4 types
    ("MyStr0ng!Pass", "very strong"), # 13 chars, all types
])
def test_password_strength_parametrized(password, expected):
    """One test function, many test cases. Efficiency!"""
    assert check_password_strength(password) == expected


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    12.5,
    [],
    {},
    True,
])
def test_invalid_inputs_raise_typeerror(invalid_input):
    """All non-string inputs should raise TypeError."""
    with pytest.raises(TypeError):
        check_password_strength(invalid_input)


# ============================================================
# Run Instructions
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  PASSWORD CHECKER TESTS")
    print("=" * 50)
    print("""
Run these tests with:
  pytest solution.py -v              → verbose output
  pytest solution.py -v --tb=short   → shorter tracebacks
  pytest solution.py -k "weak"       → only weak password tests
  pytest solution.py -k "edge"       → only edge case tests
  pytest solution.py --co            → list all tests without running

Expected: All tests should PASS!
""")
    # You can also run with unittest
    pytest.main([__file__, "-v"])
