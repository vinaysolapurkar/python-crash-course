"""
Chapter 10 Exercise SOLUTION: Password Strength Checker
========================================================
A complete password strength checker with scoring, tips,
and a visual strength meter. Fort Knox would be proud.
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
    score = 0
    tips = []
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Check 1: Length
    if len(password) >= 8:
        score += 1
    else:
        tips.append(f"Make it at least 8 characters (currently {len(password)})")

    # Check 2: Uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add at least one UPPERCASE letter")

    # Check 3: Lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter")

    # Check 4: Digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add at least one digit (0-9)")

    # Check 5: Special characters
    if any(c in special_chars for c in password):
        score += 1
    else:
        tips.append(f"Add a special character (e.g., !@#$%^&*)")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, tips


def display_strength_meter(strength):
    """Show a visual strength meter -- because visuals are fun!"""
    meters = {
        "Weak":   "[##--------]  WEAK -- a hacker's dream!",
        "Medium": "[######----]  MEDIUM -- getting there...",
        "Strong": "[##########]  STRONG -- Fort Knox approved!"
    }
    print(f"  Strength: {meters[strength]}")


def main():
    """Test the password checker interactively."""
    print("=" * 45)
    print("   PASSWORD STRENGTH CHECKER")
    print("   'Is your password tougher than a Nokia?'")
    print("=" * 45)
    print("Type 'quit' to exit.\n")

    # Run some test cases first
    test_passwords = [
        "abc",                    # Weak -- too short, no upper/digit/special
        "hello123",               # Medium -- has lower + digits + length
        "Hello123",               # Medium -- has upper + lower + digits + length
        "H3llo_W0rld!",           # Strong -- has everything!
        "password",               # Weak -- common, no upper/digit/special
        "P@ssw0rd",               # Strong -- meets all criteria
    ]

    print("--- Test Cases ---")
    for pwd in test_passwords:
        strength, tips = check_password_strength(pwd)
        # Show a masked version for display (show first 2 chars)
        masked = pwd[:2] + "*" * (len(pwd) - 2)
        print(f"\n  Password: {pwd}")
        display_strength_meter(strength)
        if tips:
            print(f"  Tips: {'; '.join(tips)}")
        else:
            print("  Tips: None needed -- this password is a beast!")

    # Interactive mode
    print("\n\n--- Try Your Own ---")
    while True:
        password = input("\nEnter a password to check (or 'quit'): ")
        if password.lower() == "quit":
            print("\nStay safe! Remember: 'password123' is never okay.")
            print("Neither is your cat's name. Or your birthday. Or 'qwerty'.")
            break

        if not password:
            print("  Empty password? That's not even trying!")
            continue

        strength, tips = check_password_strength(password)
        print()
        display_strength_meter(strength)

        if tips:
            print("  Improvement tips:")
            for i, tip in enumerate(tips, 1):
                print(f"    {i}. {tip}")
        else:
            print("  No tips needed -- your password is unbreakable!")
            print("  (Well, probably. Don't quote me on that.)")


if __name__ == "__main__":
    main()
