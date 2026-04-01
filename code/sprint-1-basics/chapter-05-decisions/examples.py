# ============================================================
# Chapter 5: Making Decisions — if, elif, else
# ============================================================
# Life is full of choices. So is code.
# "Should I order pizza?" → if hungry: order_pizza()
# See? You're already thinking like a programmer.
# ============================================================

# ----------------------------------------------------------
# COMPARISON OPERATORS — Asking Questions
# ----------------------------------------------------------
print("=== COMPARISON OPERATORS ===")

age = 25
print(f"age = {age}")
print(f"age == 25 : {age == 25}")    # Equal to
print(f"age != 30 : {age != 30}")    # Not equal to
print(f"age > 18  : {age > 18}")     # Greater than
print(f"age < 30  : {age < 30}")     # Less than
print(f"age >= 25 : {age >= 25}")    # Greater than or equal
print(f"age <= 24 : {age <= 24}")    # Less than or equal

# Strings can be compared too!
print(f"\n'a' < 'b'      : {'a' < 'b'}")         # True (alphabetical)
print(f"'apple' == 'Apple' : {'apple' == 'Apple'}")   # False (case-sensitive!)
print(f"'Batman' < 'Superman' : {'Batman' < 'Superman'}")  # True (B comes before S)

# ----------------------------------------------------------
# IF / ELIF / ELSE — The Decision Tree
# ----------------------------------------------------------
print("\n=== IF / ELIF / ELSE ===")

# Simple if
temperature = 72
if temperature > 100:
    print("It's scorching! Stay inside and binge Netflix.")
elif temperature > 80:
    print("It's hot. Sunscreen is not optional.")
elif temperature > 60:
    print("Nice weather! Perfect for a walk.")    # <-- This one runs
elif temperature > 40:
    print("Getting chilly. Grab a jacket.")
else:
    print("It's freezing! Time for hot cocoa and existential dread.")

# Quick note: Python uses INDENTATION (4 spaces) to define blocks.
# No curly braces like other languages. The whitespace IS the syntax.
# Mess up the indentation, and Python will judge you. Harshly.

# ----------------------------------------------------------
# LOGICAL OPERATORS — and, or, not
# ----------------------------------------------------------
print("\n=== LOGICAL OPERATORS ===")

has_ticket = True
has_popcorn = False
is_vip = True

# 'and' — BOTH must be True
print(f"ticket AND popcorn: {has_ticket and has_popcorn}")    # False

# 'or' — AT LEAST ONE must be True
print(f"ticket OR popcorn:  {has_ticket or has_popcorn}")     # True

# 'not' — flips True to False and vice versa
print(f"NOT has_popcorn:    {not has_popcorn}")               # True

# Combining them — real-world scenario
can_enter = has_ticket and (has_popcorn or is_vip)
print(f"\nCan enter movie? {can_enter}")
# True — has ticket AND is VIP (even without popcorn)

# A more relatable example:
hour = 14  # 2 PM
is_weekend = True

if is_weekend and 10 <= hour <= 22:
    print("The mall is open, and it's the weekend. Let's go shopping!")
elif not is_weekend and 9 <= hour <= 21:
    print("Weekday hours. Quick trip after work.")
else:
    print("The mall is closed. Online shopping it is.")

# ----------------------------------------------------------
# NESTED vs FLAT CONDITIONS
# ----------------------------------------------------------
print("\n=== NESTED vs FLAT ===")

# NESTED (harder to read — the "inception" approach):
print("--- Nested approach ---")
user_role = "admin"
is_active = True

if user_role == "admin":
    if is_active:
        print("Welcome, admin! Here are all the buttons you shouldn't press.")
    else:
        print("Admin account is deactivated.")
else:
    if is_active:
        print("Welcome, user!")
    else:
        print("Account deactivated. Contact support.")

# FLAT (much cleaner — the "Occam's razor" approach):
print("\n--- Flat approach (better!) ---")
if user_role == "admin" and is_active:
    print("Welcome, admin! Here are all the buttons you shouldn't press.")
elif user_role == "admin" and not is_active:
    print("Admin account is deactivated.")
elif is_active:
    print("Welcome, user!")
else:
    print("Account deactivated. Contact support.")

# Rule of thumb: if you're nesting more than 2 levels deep,
# refactor to flat conditions. Your future self will thank you.

# ----------------------------------------------------------
# TRUTHY AND FALSY VALUES
# ----------------------------------------------------------
print("\n=== TRUTHY & FALSY ===")

# In Python, these are FALSY (treated as False):
#   False, None, 0, 0.0, "" (empty string), [] (empty list),
#   {} (empty dict), () (empty tuple), set()

# Everything else is TRUTHY. So you can do stuff like:

username = "Neo"
if username:
    print(f"Hello, {username}!")    # Runs because "Neo" is truthy
else:
    print("No username provided.")

# Instead of writing: if username != ""
# Just write:          if username
# It's the Pythonic way. Elegant. Clean. Like a freshly linted codebase.

# More examples:
items = []
if not items:
    print("Your cart is empty. Treat yourself!")

score = 0
if score:
    print("You scored something!")
else:
    print("Score is zero. We've all been there.")   # This runs

# ----------------------------------------------------------
# THE TERNARY OPERATOR — One-Liner Decisions
# ----------------------------------------------------------
print("\n=== TERNARY OPERATOR ===")

# Regular if/else:
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary (same thing, one line):
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# More examples:
weather = "rainy"
activity = "Netflix" if weather == "rainy" else "Hiking"
print(f"Weather is {weather}, so: {activity}")

temperature = 35
emoji = "cold" if temperature < 50 else "warm" if temperature < 80 else "hot"
print(f"{temperature}°F feels {emoji}")
# You CAN chain ternaries, but please don't go overboard.
# Two levels max, or future-you will write mean comments about present-you.

# ----------------------------------------------------------
# PRACTICAL EXAMPLES
# ----------------------------------------------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Password strength checker
password = "MyP@ss123"
is_long = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

if is_long and has_upper and has_lower and has_digit:
    print(f"Password '{password}': Strong! Fort Knox would be proud.")
elif is_long:
    print(f"Password '{password}': Decent, but add variety.")
else:
    print(f"Password '{password}': Weak. A goldfish could crack this.")

# Grade calculator
score = 87
grade = (
    "A+" if score >= 97 else
    "A"  if score >= 93 else
    "A-" if score >= 90 else
    "B+" if score >= 87 else
    "B"  if score >= 83 else
    "B-" if score >= 80 else
    "C"  if score >= 70 else
    "D"  if score >= 60 else
    "F"
)
print(f"Score {score} → Grade: {grade}")

# Shipping calculator
order_total = 45.00
is_member = True

if is_member or order_total >= 50:
    shipping = 0.00
    reason = "Member discount" if is_member else "Order over $50"
elif order_total >= 25:
    shipping = 5.99
    reason = "Standard shipping"
else:
    shipping = 9.99
    reason = "Small order surcharge"

print(f"\nOrder: ${order_total:.2f} | Shipping: ${shipping:.2f} ({reason})")

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 5 RECAP ===")
print("1. Comparison: == != > < >= <=")
print("2. if/elif/else for branching (indent with 4 spaces!)")
print("3. Logical: 'and' (both), 'or' (either), 'not' (flip)")
print("4. Flat conditions > nested conditions (readability wins)")
print("5. Falsy: False, None, 0, '', [], {}, ()")
print("6. Ternary: value = X if condition else Y")
print("\n'With great power comes great responsibility.' — Uncle Ben")
print("(He was definitely talking about if/else statements.)")
