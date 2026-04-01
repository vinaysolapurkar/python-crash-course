# ============================================================
# Chapter 6: Lists — Your Data's Favorite Container
# ============================================================
# A list is like a playlist — ordered, changeable, and you
# can put whatever you want in it. Even other lists.
# (It's lists all the way down.)
# ============================================================

# ----------------------------------------------------------
# CREATING LISTS
# ----------------------------------------------------------
print("=== CREATING LISTS ===")

# A list of strings
avengers = ["Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye", "Captain America"]
print(f"Avengers: {avengers}")

# A list of numbers
scores = [98, 85, 92, 77, 89]
print(f"Scores: {scores}")

# Mixed types (Python doesn't care — it's very accepting)
mixed = ["Tony Stark", 42, 3.14, True, None]
print(f"Mixed bag: {mixed}")

# Empty list (a blank canvas, full of potential)
my_list = []
print(f"Empty list: {my_list}")

# ----------------------------------------------------------
# ACCESSING & SLICING — Finding What You Need
# ----------------------------------------------------------
print("\n=== ACCESSING & SLICING ===")

# Indexing (same as strings — 0-based)
print(f"First Avenger:  {avengers[0]}")     # Iron Man
print(f"Last Avenger:   {avengers[-1]}")    # Captain America
print(f"Third Avenger:  {avengers[2]}")     # Hulk

# Slicing (start:stop:step — stop is EXCLUDED)
print(f"\nFirst three:  {avengers[:3]}")       # Iron Man, Thor, Hulk
print(f"Last two:     {avengers[-2:]}")        # Hawkeye, Captain America
print(f"Every other:  {avengers[::2]}")        # Iron Man, Hulk, Hawkeye
print(f"Reversed:     {avengers[::-1]}")       # Reversed Avengers!

# ----------------------------------------------------------
# MODIFYING LISTS — Lists are Mutable (Unlike Strings!)
# ----------------------------------------------------------
print("\n=== MODIFYING LISTS ===")

# Change an element directly
team = ["Mario", "Luigi", "Toad", "Peach"]
print(f"Original team: {team}")

team[2] = "Yoshi"    # Sorry, Toad. You've been traded.
print(f"Updated team:  {team}")

# append() — add to the END
team.append("Bowser")    # Redemption arc!
print(f"After append:  {team}")

# insert() — add at a SPECIFIC position
team.insert(1, "Rosalina")    # Squeeze in at index 1
print(f"After insert:  {team}")

# remove() — removes the FIRST occurrence by VALUE
team.remove("Bowser")    # Nevermind, Bowser was a mole.
print(f"After remove:  {team}")

# pop() — removes by INDEX and RETURNS the item
last_one = team.pop()     # Removes last item
print(f"Popped:        {last_one}")
print(f"After pop:     {team}")

second = team.pop(1)     # Removes item at index 1
print(f"Popped index 1: {second}")
print(f"After pop(1):  {team}")

# del — removes by index (doesn't return anything)
del team[0]
print(f"After del [0]: {team}")

# clear() — nuclear option. Removes EVERYTHING.
# team.clear()  # Don't run this unless you want an empty team!

# extend() — add multiple items at once
team.extend(["Wario", "Waluigi"])
print(f"After extend:  {team}")

# ----------------------------------------------------------
# SORTING — Getting Things in Order
# ----------------------------------------------------------
print("\n=== SORTING ===")

numbers = [42, 17, 93, 5, 28, 71]
print(f"Original:          {numbers}")

# sort() — modifies the list IN PLACE (returns None!)
numbers.sort()
print(f"After sort():      {numbers}")

numbers.sort(reverse=True)
print(f"Reverse sort:      {numbers}")

# sorted() — returns a NEW list, original unchanged
names = ["Zara", "Alice", "Mike", "Bob"]
sorted_names = sorted(names)
print(f"\nOriginal names:  {names}")
print(f"sorted(names):   {sorted_names}")
print(f"Still original:  {names}")   # Unchanged!

# Key difference:
# .sort()  → changes the list, returns None
# sorted() → returns new list, original stays the same
# Choose wisely, like choosing between the red and blue pill.

# ----------------------------------------------------------
# USEFUL LIST OPERATIONS
# ----------------------------------------------------------
print("\n=== USEFUL OPERATIONS ===")

heroes = ["Batman", "Superman", "Wonder Woman", "Batman", "Flash", "Batman"]

print(f"Length:              {len(heroes)}")           # 6
print(f"'Batman' in heroes: {'Batman' in heroes}")    # True
print(f"'Aquaman' in heroes: {'Aquaman' in heroes}")  # False (sorry, Aquaman)
print(f"Count of Batman:     {heroes.count('Batman')}")  # 3 (he's everywhere)
print(f"Index of Flash:      {heroes.index('Flash')}")   # 4

# Concatenation
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined = list_a + list_b
print(f"\n[1,2,3] + [4,5,6] = {combined}")

# Repetition
repeated = ["ha"] * 3
print(f"['ha'] * 3 = {repeated}")    # ['ha', 'ha', 'ha']

# ----------------------------------------------------------
# FOR LOOPS WITH LISTS
# ----------------------------------------------------------
print("\n=== FOR LOOPS WITH LISTS ===")

# Basic for loop
print("Avengers roll call:")
for hero in avengers:
    print(f"  - {hero}")

# enumerate() — when you need the index AND the value
# (Like a bouncer with a clipboard)
print("\nAvengers with numbers:")
for index, hero in enumerate(avengers):
    print(f"  #{index + 1}: {hero}")

# enumerate with custom start
print("\nStarting from 100:")
for i, hero in enumerate(avengers, start=100):
    print(f"  ID-{i}: {hero}")

# ----------------------------------------------------------
# LIST COMPREHENSIONS — The Pythonic Way
# ----------------------------------------------------------
print("\n=== LIST COMPREHENSIONS ===")

# The long way:
squares_long = []
for n in range(1, 6):
    squares_long.append(n ** 2)
print(f"Long way:  {squares_long}")

# The list comprehension way (same result, one line):
squares = [n ** 2 for n in range(1, 6)]
print(f"Comp way:  {squares}")
# Syntax: [expression for item in iterable]

# With a condition (filtering)
even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(f"Even squares: {even_squares}")
# Syntax: [expression for item in iterable if condition]

# Practical: extract initials from names
full_names = ["Tony Stark", "Peter Parker", "Bruce Wayne"]
initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(f"Names:    {full_names}")
print(f"Initials: {initials}")    # ['TS', 'PP', 'BW']

# Practical: filter and transform
words = ["Hello", "", "World", "", "Python", ""]
clean = [w.upper() for w in words if w]    # skip empty strings
print(f"Cleaned: {clean}")

# Uppercase only long words
words2 = ["hi", "hello", "hey", "magnificent", "ok"]
long_words = [w.upper() for w in words2 if len(w) > 3]
print(f"Long words: {long_words}")

# ----------------------------------------------------------
# NESTED LISTS (2D Lists / Grids)
# ----------------------------------------------------------
print("\n=== NESTED LISTS ===")

# Tic-tac-toe board!
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

print("Tic-Tac-Toe:")
for row in board:
    print(f"  {' | '.join(row)}")

# Accessing nested elements
print(f"\nCenter square: {board[1][1]}")   # X
print(f"Top-right:     {board[0][2]}")     # X

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 6 RECAP ===")
print("1. Create: [], [1, 2, 3], list()")
print("2. Access: list[0], list[-1], list[1:3]")
print("3. Modify: append, insert, remove, pop, del, extend")
print("4. Sort:   .sort() (in-place) vs sorted() (new list)")
print("5. Check:  len(), 'in', .count(), .index()")
print("6. Loop:   for item in list / for i, item in enumerate(list)")
print("7. Comprehensions: [expr for item in list if condition]")
print("\nLists are your bread and butter. Master them!")
