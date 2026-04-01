# ============================================================
# Chapter 7: Loops — Repeat After Me
# ============================================================
# Loops let you do things over and over without copy-pasting.
# Because if you copy-paste code more than twice, a senior
# developer somewhere feels a disturbance in the Force.
# ============================================================

# ----------------------------------------------------------
# FOR LOOPS — When You Know How Many Times
# ----------------------------------------------------------
print("=== FOR LOOPS ===")

# Looping through a list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
print("The inner planets (+Jupiter, because it's cool):")
for planet in planets:
    print(f"  - {planet}")

# ----------------------------------------------------------
# range() — Your Loop's Best Friend
# ----------------------------------------------------------
print("\n=== RANGE() ===")

# range(stop) — 0 to stop-1
print("range(5):")
for i in range(5):
    print(f"  i = {i}", end="")    # 0, 1, 2, 3, 4
print()  # newline

# range(start, stop) — start to stop-1
print("\nrange(1, 6):")
for i in range(1, 6):
    print(f"  i = {i}", end="")    # 1, 2, 3, 4, 5
print()

# range(start, stop, step) — with custom step size
print("\nrange(0, 20, 5) — counting by fives:")
for i in range(0, 20, 5):
    print(f"  {i}", end="")        # 0, 5, 10, 15
print()

print("\nrange(10, 0, -2) — counting down by twos:")
for i in range(10, 0, -2):
    print(f"  {i}", end="")        # 10, 8, 6, 4, 2
print()

# ----------------------------------------------------------
# COUNTDOWN — Because Rockets Need Countdowns
# ----------------------------------------------------------
print("\n=== COUNTDOWN ===")

print("Launch sequence initiated!")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  LIFTOFF! (To infinity and beyond!)")

# ----------------------------------------------------------
# WHILE LOOPS — When You Don't Know How Many Times
# ----------------------------------------------------------
print("\n=== WHILE LOOPS ===")

# While loops keep going until the condition is False.
# They're like that friend who won't leave the party.

count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1    # Don't forget this, or INFINITE LOOP!
# If you forget to update the condition, your program runs forever.
# Ctrl+C is your emergency brake.

# Practical: password prompt
print("\nPassword demo (password is 'letmein'):")
attempts = 3
password = ""
# Simulating with a hardcoded answer so the file runs:
correct_password = "letmein"
# In real code, you'd use: password = input("Enter password: ")
while password != correct_password and attempts > 0:
    password = correct_password  # Pretend user typed it correctly
    attempts -= 1
print("  Access granted! Welcome back, Agent Smith.")

# ----------------------------------------------------------
# BREAK — The Emergency Exit
# ----------------------------------------------------------
print("\n=== BREAK ===")

# break immediately exits the loop, no questions asked.
# It's like pulling the fire alarm — everything stops.

print("Looking for the number 7:")
for num in range(1, 20):
    if num == 7:
        print(f"  Found {num}! Breaking out of the loop.")
        break
    print(f"  Checking {num}... nope.")

# break in a while loop — searching for input
print("\nMagic 8-Ball (break when 'quit'):")
responses = ["Ask again later", "Yes definitely", "My sources say no"]
# Simulated — in real life you'd use input()
questions = ["Will I be rich?", "Will I find love?", "quit"]
for q in questions:
    if q.lower() == "quit":
        print("  The Magic 8-Ball says: Goodbye!")
        break
    import random
    print(f"  Q: {q}")
    print(f"  A: {random.choice(responses)}")

# ----------------------------------------------------------
# CONTINUE — Skip This One, Keep Going
# ----------------------------------------------------------
print("\n=== CONTINUE ===")

# continue skips the REST of the current iteration
# and jumps to the NEXT one. Like skipping a song on Spotify.

print("Printing odd numbers only (skip evens):")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # Skip even numbers
    print(f"  {i}", end="")
print()  # newline

# Practical: skip blank lines in data
data = ["Alice", "", "Bob", "", "", "Charlie", ""]
print("\nCleaning data (skipping blanks):")
for name in data:
    if not name:
        continue
    print(f"  Processing: {name}")

# ----------------------------------------------------------
# NESTED LOOPS — Loops Inside Loops (Inception!)
# ----------------------------------------------------------
print("\n=== NESTED LOOPS ===")

# A grid / multiplication snippet
print("3x3 Grid:")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"  ({row},{col})", end="")
    print()    # New line after each row

# Practical: a mini multiplication table
print("\nMini Multiplication Table:")
print("      ", end="")
for col in range(1, 6):
    print(f"{col:>4}", end="")
print()
print("     " + "-" * 20)

for row in range(1, 6):
    print(f"  {row:>2} |", end="")
    for col in range(1, 6):
        print(f"{row * col:>4}", end="")
    print()

# Star pattern — because every programming book has one
print("\nStar Triangle:")
for i in range(1, 6):
    print("  " + "* " * i)

print("\nInverted Star Triangle:")
for i in range(5, 0, -1):
    print("  " + "* " * i)

# ----------------------------------------------------------
# THE else CLAUSE ON LOOPS — Python's Secret Feature
# ----------------------------------------------------------
print("\n=== LOOP else CLAUSE ===")

# The else block runs when the loop completes NORMALLY
# (i.e., it did NOT hit a break). Most people don't know this exists.
# It's Python's best-kept secret. Until now.

print("Searching for a prime factor of 7:")
for i in range(2, 7):
    if 7 % i == 0:
        print(f"  {i} is a factor!")
        break
else:
    # This runs because the loop finished without break
    print("  7 is prime! No factors found.")

print("\nSearching for a prime factor of 12:")
for i in range(2, 12):
    if 12 % i == 0:
        print(f"  {i} is a factor of 12!")
        break
else:
    print("  12 is prime!")   # This WON'T run (break was hit)

# Think of it as: "else" = "if no break happened"

# ----------------------------------------------------------
# LOOP PATTERNS — Common Recipes
# ----------------------------------------------------------
print("\n=== LOOP PATTERNS ===")

# Accumulator pattern — summing up values
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Finding the maximum (without using max())
values = [34, 67, 12, 89, 45, 23]
biggest = values[0]
for val in values:
    if val > biggest:
        biggest = val
print(f"Biggest in {values}: {biggest}")

# Building a string
words = ["Python", "is", "incredibly", "fun"]
sentence = ""
for word in words:
    sentence += word + " "
print(f"Built sentence: '{sentence.strip()}'")

# Better way with join:
print(f"Join version:   '{' '.join(words)}'")

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 7 RECAP ===")
print("1. for loop: iterate over lists, strings, range()")
print("2. range(stop), range(start, stop), range(start, stop, step)")
print("3. while loop: keep going until condition is False")
print("4. break: exit the loop immediately")
print("5. continue: skip to the next iteration")
print("6. Nested loops: loops inside loops (watch the indentation!)")
print("7. else clause: runs if loop finishes WITHOUT break")
print("\nRemember: if you're writing the same code 3 times,")
print("you probably need a loop. Or a vacation. Maybe both.")
