"""
Chapter 10 Exercise: Password Strength Checker
===============================================
Build a function that checks how strong a password is!

Your function should:
  - Take a password string as input
  - Return a TUPLE: (strength, tips)
    - strength: "Weak", "Medium", or "Strong"
    - tips: a list of suggestions to improve the password

Scoring rules:
  - Length >= 8 characters       (+1 point)
  - Contains uppercase letter    (+1 point)
  - Contains lowercase letter    (+1 point)
  - Contains a digit             (+1 point)
  - Contains a special char      (+1 point)
    (special chars: !@#$%^&*()_+-=[]{}|;:,.<>?)

Strength levels:
  - 0-2 points: "Weak"
  - 3-4 points: "Medium"
  - 5 points:   "Strong"

HINTS:
  - Use any() with a generator: any(c.isupper() for c in password)
  - Define special_chars as a string: "!@#$%^&*()_+-=[]{}|;:,.<>?"
  - Build the tips list based on what's MISSING
"""


def check_password_strength(password):
    """
    Check password strength and return (strength_level, tips).

    Parameters:
        password (str): The password to check

    Returns:
        tuple: (strength, tips) where strength is "Weak"/"Medium"/"Strong"
               and tips is a list of improvement suggestions
    """
    # TODO: Initialize a score counter and tips list

    # TODO: Check length >= 8
    # HINT: if len(password) >= 8: score += 1 / else: tips.append(...)

    # TODO: Check for uppercase letters
    # HINT: any(c.isupper() for c in password)

    # TODO: Check for lowercase letters

    # TODO: Check for digits
    # HINT: any(c.isdigit() for c in password)

    # TODO: Check for special characters
    # HINT: special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # TODO: Determine strength based on score
    # 0-2: "Weak", 3-4: "Medium", 5: "Strong"

    # TODO: Return (strength, tips)
    pass


def main():
    """Test the password checker interactively."""
    print("=== PASSWORD STRENGTH CHECKER ===")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "quit":
            print("Stay safe out there! Don't use 'password123'.")
            break

        # TODO: Call check_password_strength() and display results
        # HINT: strength, tips = check_password_strength(password)
        # Print the strength and any tips
        pass


if __name__ == "__main__":
    main()
