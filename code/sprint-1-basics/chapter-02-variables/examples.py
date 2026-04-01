# ============================================================
# Chapter 2: Variables — Giving Names to Things
# ============================================================
# Variables are like sticky notes you slap onto values.
# They help you remember stuff so Python doesn't have to.
# ============================================================

# ----------------------------------------------------------
# BASIC VARIABLE ASSIGNMENT
# ----------------------------------------------------------
# Think of it like Tony Stark labeling his suits.
# The variable is the label, the value is the suit.

hero_name = "Tony Stark"
alter_ego = "Iron Man"
suit_number = 85            # Mark LXXXV — yes, he made that many
net_worth = 12.4            # Billions, obviously
is_genius = True            # Billionaire, playboy, philanthropist

print("=== MEET THE HERO ===")
print(hero_name)
print(alter_ego)
print(suit_number)
print(net_worth)
print(is_genius)

# ----------------------------------------------------------
# CHECKING TYPES WITH type()
# ----------------------------------------------------------
# Python is dynamically typed — it figures out the type for you.
# But sometimes you want to double-check, like Jarvis running diagnostics.

print("\n=== TYPE CHECK (Jarvis Diagnostics) ===")
print(type(hero_name))      # <class 'str'>    — text
print(type(suit_number))    # <class 'int'>    — whole number
print(type(net_worth))      # <class 'float'>  — decimal number
print(type(is_genius))      # <class 'bool'>   — True or False

# ----------------------------------------------------------
# THE FOUR BASIC TYPES
# ----------------------------------------------------------
# str   → text:      "Hello", 'World', "42" (yes, "42" is text!)
# int   → integers:  42, -7, 0, 1_000_000 (underscores for readability)
# float → decimals:  3.14, -0.5, 1.0
# bool  → boolean:   True, False (capital T and F — Python is picky)

big_number = 1_000_000      # Python lets you use underscores for readability
print(f"\nA million looks cleaner: {big_number}")  # prints 1000000

# ----------------------------------------------------------
# NAMING CONVENTIONS (The Rules of the Road)
# ----------------------------------------------------------
# Good names:   hero_name, suit_count, is_active  (snake_case)
# Bad names:    x, thing2, HeroName               (confusing or wrong style)
# Illegal:      2fast, my-var, class               (starts with number, has dash, reserved word)

# Python convention: use snake_case for variables
# camelCase is for JavaScript people. We don't do that here.

sidekick_name = "Peter Parker"       # Good: descriptive, snake_case
sidekick_age = 17                    # Good: clear what it represents
# p = "Peter"                        # Bad: what does 'p' even mean?

# ----------------------------------------------------------
# F-STRINGS — The Best Thing Since Sliced Bread
# ----------------------------------------------------------
# f-strings let you embed variables (and expressions!) inside strings.
# Just put an 'f' before the quotes and use {curly braces}.

print("\n=== F-STRINGS (Tony's Favorite) ===")
print(f"{hero_name} is also known as {alter_ego}.")
print(f"He's built {suit_number} suits. That's dedication (or obsession).")
print(f"Net worth: ${net_worth} billion. Must be nice.")

# You can put EXPRESSIONS inside the braces — not just variables!
print(f"\nSuit number doubled: {suit_number * 2}")
print(f"Is Tony a genius? {is_genius}. Obviously.")
print(f"Name in ALL CAPS: {hero_name.upper()}")

# ----------------------------------------------------------
# VARIABLE REASSIGNMENT
# ----------------------------------------------------------
# Variables can change — that's why they're called "variables."
# It's like when Peter Parker goes from intern to Avenger.

print("\n=== REASSIGNMENT (Character Development) ===")
role = "Stark Industries Intern"
print(f"Peter's role: {role}")

role = "Spider-Man"
print(f"Peter's role: {role}")

role = "Avenger"
print(f"Peter's role: {role}")
# The old values are gone. Python doesn't hoard — it moves on.

# ----------------------------------------------------------
# MULTIPLE ASSIGNMENT (The Efficient Way)
# ----------------------------------------------------------
# Assign multiple variables in one line. Tony would approve.

name, age, city = "Peter Parker", 17, "Queens, NY"
print(f"\n{name}, age {age}, from {city}")

# Same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")  # All zero. Fresh start.

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 2 RECAP ===")
print("1. Variables store values with descriptive names")
print("2. Python has 4 basic types: str, int, float, bool")
print("3. Use type() to check what you're dealing with")
print("4. snake_case is the Python way")
print("5. f-strings are your new best friend")
print("6. Variables can be reassigned — they grow up!")
print("\nNow go build something. Tony believes in you. Probably.")
