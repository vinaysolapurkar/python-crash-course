# ============================================================
# SOLUTION: Username Generator
# ============================================================
# Because "xXx_DarkLord69_xXx" is not a professional username.
# ============================================================

import random

print("=" * 40)
print("     USERNAME GENERATOR 3000")
print("  (Better than your old AOL screenname)")
print("=" * 40)

# Get user input and clean it up
first_name = input("\nEnter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Validate input (bonus feature)
if not first_name.isalpha() or not last_name.isalpha():
    print("\nWhoa there — names should only contain letters!")
    print("No numbers, spaces, or mysterious symbols. Try again.")
else:
    # Build the username components
    first_part = first_name[:3].lower()     # First 3 letters, lowercase
    last_part = last_name.lower()           # Full last name, lowercase

    # Generate 3 options (bonus feature)
    print("\n--- YOUR USERNAME OPTIONS ---")

    options = []
    for i in range(3):
        num = random.randint(1, 999)
        # Option 1 style: petparker472
        username = f"{first_part}{last_part}{num}"
        options.append(username)
        print(f"  [{i + 1}] {username}")

    # Bonus: add some extra style options
    special_num = random.randint(1, 999)
    underscore_version = f"{first_part}_{last_part}_{special_num}"
    dot_version = f"{first_part}.{last_part}.{random.randint(1, 999)}"
    print(f"  [4] {underscore_version}")
    print(f"  [5] {dot_version}")

    options.extend([underscore_version, dot_version])

    # Let the user pick
    print("-" * 35)
    choice = input("\nPick your favorite (1-5): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= 5:
        chosen = options[int(choice) - 1]
        print(f"\nYour new username: {chosen}")
        print(f"Username length: {len(chosen)} characters")
        print(f"All lowercase: {chosen == chosen.lower()}")
        print("\nGo forth and conquer the internet! (Responsibly.)")
    else:
        print("\nThat wasn't a valid choice, but we'll go with #1.")
        print(f"Your new username: {options[0]}")
