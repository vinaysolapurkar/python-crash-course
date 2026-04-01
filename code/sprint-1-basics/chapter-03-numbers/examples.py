# ============================================================
# Chapter 3: Numbers & Math — Python is Your Calculator
# ============================================================
# Forget your TI-84. Python does math better, faster, and
# without running out of battery during a final exam.
# ============================================================

# ----------------------------------------------------------
# ARITHMETIC OPERATORS — The Basics
# ----------------------------------------------------------
print("=== ARITHMETIC OPERATORS ===")

print(f"Addition:       10 + 3  = {10 + 3}")       # 13
print(f"Subtraction:    10 - 3  = {10 - 3}")       # 7
print(f"Multiplication: 10 * 3  = {10 * 3}")       # 30
print(f"Division:       10 / 3  = {10 / 3}")       # 3.333... (always returns float!)
print(f"Floor Division: 10 // 3 = {10 // 3}")      # 3 (chops off the decimal — brutal)
print(f"Modulo:         10 % 3  = {10 % 3}")       # 1 (the remainder — surprisingly useful)
print(f"Exponent:       10 ** 3 = {10 ** 3}")      # 1000 (10 to the power of 3)

# PRO TIP: Division (/) ALWAYS returns a float, even if it divides evenly
print(f"\n10 / 2 = {10 / 2}")    # 5.0, not 5. Python is dramatic like that.
print(f"10 // 2 = {10 // 2}")   # 5. Floor division keeps it as an int.

# ----------------------------------------------------------
# MODULO — The Unsung Hero
# ----------------------------------------------------------
# Modulo gives you the remainder. It's incredibly useful for:
# - Checking if a number is even/odd
# - Wrapping around (clocks, game boards, etc.)
# - Splitting time into hours/minutes

print("\n=== MODULO MAGIC ===")
print(f"Is 42 even? {42 % 2 == 0}")    # True (no remainder = even)
print(f"Is 7 even?  {7 % 2 == 0}")     # False

# Converting 137 minutes to hours and minutes
total_minutes = 137
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"\n{total_minutes} minutes = {hours} hours and {minutes} minutes")
# Like Gandalf said: "A wizard is never late." But he probably tracked minutes.

# ----------------------------------------------------------
# PEMDAS — Order of Operations
# ----------------------------------------------------------
# Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division,
# Addition/Subtraction). Just like math class, but with less crying.

print("\n=== PEMDAS (Order of Operations) ===")
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")          # 14, NOT 20 (multiplication first!)

result_with_parens = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result_with_parens}")  # 20 (parentheses override!)

# A spicy one:
wild = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {wild}")           # 512! (exponents go right-to-left: 3**2=9, then 2**9=512)

# When in doubt, use parentheses. Future You will thank Present You.

# ----------------------------------------------------------
# TYPE CONVERSION — Shapeshifting Numbers
# ----------------------------------------------------------
# Sometimes you need to convert between types.
# It's like when a Transformer goes from car to robot.

print("\n=== TYPE CONVERSION ===")

# int to float
x = 42
print(f"int to float: {float(x)} (type: {type(float(x)).__name__})")

# float to int (WARNING: it truncates, doesn't round!)
y = 3.99
print(f"float to int: {int(y)} (type: {type(int(y)).__name__})")
# int() chops the decimal. 3.99 becomes 3. Ruthless.

# string to int/float
age_str = "25"
age_num = int(age_str)
print(f"string to int: '{age_str}' -> {age_num} (type: {type(age_num).__name__})")

price_str = "9.99"
price_num = float(price_str)
print(f"string to float: '{price_str}' -> {price_num}")

# number to string (useful for concatenation)
score = 100
message = "Your score is " + str(score)
print(message)

# ----------------------------------------------------------
# THE input() FUNCTION — Talking to Humans
# ----------------------------------------------------------
# input() always returns a STRING. Always. Even if they type a number.
# You MUST convert it if you want to do math with it.

print("\n=== INPUT FUNCTION ===")
# Uncomment the lines below to try it interactively!
# (We'll leave them commented so the file runs without waiting)

# name = input("What's your name? ")
# print(f"Hello, {name}! Welcome to the Matrix.")

# age = int(input("How old are you? "))
# print(f"In 10 years, you'll be {age + 10}. Time flies!")

# Here's a quick demo with hardcoded values:
user_input = "42"                  # Pretend the user typed this
number = int(user_input)           # Convert string to int
print(f"User typed: '{user_input}' (type: {type(user_input).__name__})")
print(f"Converted:  {number} (type: {type(number).__name__})")
print(f"Math works now: {number * 2}")

# ----------------------------------------------------------
# BUILT-IN MATH FUNCTIONS — No Import Needed
# ----------------------------------------------------------
print("\n=== BUILT-IN MATH FUNCTIONS ===")

# abs() — absolute value (always positive, like your attitude should be)
print(f"abs(-42) = {abs(-42)}")        # 42
print(f"abs(42)  = {abs(42)}")         # 42

# round() — rounds to nearest even (banker's rounding) or specified places
print(f"round(3.7)    = {round(3.7)}")       # 4
print(f"round(3.14159, 2) = {round(3.14159, 2)}")   # 3.14
print(f"round(2.5)    = {round(2.5)}")       # 2 (banker's rounding — rounds to even!)
print(f"round(3.5)    = {round(3.5)}")       # 4

# max() and min() — finds the biggest/smallest value
print(f"max(1, 5, 3, 9, 2) = {max(1, 5, 3, 9, 2)}")   # 9
print(f"min(1, 5, 3, 9, 2) = {min(1, 5, 3, 9, 2)}")   # 1

# They also work with lists (sneak preview of Chapter 6!)
scores = [88, 92, 75, 98, 84]
print(f"Highest score: {max(scores)}")
print(f"Lowest score:  {min(scores)}")

# sum() — adds everything up
print(f"sum([1, 2, 3, 4, 5]) = {sum([1, 2, 3, 4, 5])}")   # 15

# ----------------------------------------------------------
# AUGMENTED ASSIGNMENT — The Lazy (Smart) Way
# ----------------------------------------------------------
print("\n=== AUGMENTED ASSIGNMENT ===")

score = 100
print(f"Starting score: {score}")

score += 10    # same as: score = score + 10
print(f"After +10:  {score}")

score -= 5     # same as: score = score - 5
print(f"After -5:   {score}")

score *= 2     # same as: score = score * 2
print(f"After *2:   {score}")

score //= 3   # same as: score = score // 3
print(f"After //3:  {score}")

# These work with all arithmetic operators: += -= *= /= //= %= **=

# ----------------------------------------------------------
# FUN EXAMPLES — Because Math Should Be Fun
# ----------------------------------------------------------
print("\n=== FUN EXAMPLES ===")

# How many mass pizzas do you need for a party?
people = 12
slices_per_person = 3
slices_per_pizza = 8
pizzas_needed = -(-people * slices_per_person // slices_per_pizza)  # ceiling division trick!
print(f"For {people} people: order {pizzas_needed} pizzas")

# Temperature conversion
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F (that's body temperature!)")

# How many days until you've coded 10,000 hours?
hours_per_day = 2
target_hours = 10_000
days_needed = target_hours / hours_per_day
years_needed = round(days_needed / 365, 1)
print(f"At {hours_per_day} hrs/day, 10,000 hours takes {years_needed} years")
print("Better start now. Or yesterday. Yesterday was better.")

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 3 RECAP ===")
print("1. Seven operators: + - * / // % **")
print("2. / always returns float, // returns int (floor)")
print("3. PEMDAS determines order — use parentheses when unsure")
print("4. int(), float(), str() for type conversion")
print("5. input() ALWAYS returns a string — convert it!")
print("6. abs(), round(), max(), min(), sum() are built-in")
print("7. Use += -= *= etc. for augmented assignment")
