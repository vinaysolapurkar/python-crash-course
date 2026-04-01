# ============================================================
# SOLUTION: Build an "About Me" Card
# ============================================================

# Step 1: Create variables
name = "Alex Rivera"
age = 25
city = "Austin, TX"
fav_movie = "Interstellar"
is_morning_person = False
superpower = "Teleportation"

# Bonus: calculate birth year
birth_year = 2026 - age

# Morning person text (ternary expression)
morning_text = "Yes!" if is_morning_person else "Nope!"

# Tagline
tagline = f"{name}: coder by day, {superpower.lower()} enthusiast by night"

# Step 2: Print the card
print("╔══════════════════════════════════════╗")
print("║          ABOUT ME CARD               ║")
print("╠══════════════════════════════════════╣")
print(f"║  Name:    {name:<26} ║")
print(f"║  Age:     {age:<26} ║")
print(f"║  Born:    {birth_year:<26} ║")
print(f"║  City:    {city:<26} ║")
print(f"║  Movie:   {fav_movie:<26} ║")
print(f"║  Morning: {morning_text:<26} ║")
print(f"║  Power:   {superpower:<26} ║")
print("╠══════════════════════════════════════╣")
print(f"║  {tagline:<36} ║")
print("╚══════════════════════════════════════╝")

# Quick type check — just to show off what we learned
print("\n--- Type Check ---")
print(f"name is {type(name).__name__}, age is {type(age).__name__}, "
      f"is_morning_person is {type(is_morning_person).__name__}")
