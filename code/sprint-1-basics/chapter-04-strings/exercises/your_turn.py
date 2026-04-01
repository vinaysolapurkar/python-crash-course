# ============================================================
# YOUR TURN: Build a Username Generator
# ============================================================
# Create a program that generates a fun username from
# the user's first name, last name, and a random number.
#
# THE RULES:
# 1. Ask for the user's first name and last name
# 2. Take the first 3 letters of the first name (lowercase)
# 3. Take the full last name (lowercase)
# 4. Add a random number between 1 and 999
# 5. Smash them together into a username
#
# EXAMPLE:
#    First name: Peter
#    Last name: Parker
#    Generated username: petparker472
#
# HINTS:
# - import random at the top, then use random.randint(1, 999)
# - Use slicing to grab the first 3 letters: name[:3]
# - Use .lower() to make everything lowercase
# - Use .strip() to clean up any extra spaces from input
# - What if the first name is shorter than 3 letters?
#   (e.g., "Al" → just use "al". Slicing won't crash!)
#
# BONUS:
# - Generate 3 username options and let the user pick
# - Add a special character between parts (e.g., pet_parker_472)
# - Check that the name only contains letters using .isalpha()
#
# Type your code below!
# ============================================================

