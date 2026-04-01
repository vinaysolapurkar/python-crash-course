# ============================================================
# Chapter 8: Tuples & Sets — The Other Containers
# ============================================================
# Lists get all the fame, but tuples and sets are the unsung
# heroes of Python data structures. Think of tuples as
# read-only lists and sets as lists that hate duplicates.
# ============================================================

# ==========================================================
#  PART 1: TUPLES — Immutable and Proud of It
# ==========================================================

# ----------------------------------------------------------
# CREATING TUPLES
# ----------------------------------------------------------
print("=== CREATING TUPLES ===")

# Tuples use parentheses (or no parens at all — Python is chill)
coordinates = (40.7128, -74.0060)     # NYC coordinates
rgb_red = (255, 0, 0)                 # Red in RGB
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")

print(f"NYC:      {coordinates}")
print(f"Red RGB:  {rgb_red}")
print(f"Weekdays: {weekdays}")

# Single-element tuple needs a trailing comma!
# Without it, Python thinks it's just parentheses around a value.
not_a_tuple = ("oops")       # This is just a string
is_a_tuple = ("yay",)        # THIS is a tuple (note the comma)
print(f"\nType of ('oops'):  {type(not_a_tuple)}")   # str
print(f"Type of ('yay',): {type(is_a_tuple)}")        # tuple
# That trailing comma is like the period at the end of a sentence.
# Small but important.

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# ----------------------------------------------------------
# TUPLE UNPACKING — The Cool Party Trick
# ----------------------------------------------------------
print("\n=== TUPLE UNPACKING ===")

# Instead of accessing by index, unpack into variables
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Works with any iterable, not just tuples
r, g, b = rgb_red
print(f"Red: {r}, Green: {g}, Blue: {b}")

# Practical: functions that return multiple values
# (sneak preview — we'll cover functions properly later)
def get_user():
    return "Neo", 30, "The One"

name, age, title = get_user()
print(f"\n{name}, age {age}, a.k.a. '{title}'")

# ----------------------------------------------------------
# THE SWAP TRICK — No Temp Variable Needed!
# ----------------------------------------------------------
print("\n=== THE SWAP TRICK ===")

a = "Batman"
b = "Robin"
print(f"Before swap: a={a}, b={b}")

# In other languages, you need a temp variable. In Python?
a, b = b, a    # BAM. Swapped. Mic drop.

print(f"After swap:  a={a}, b={b}")
# This works because Python creates a tuple (b, a) on the right
# and unpacks it into (a, b) on the left. Elegant!

# ----------------------------------------------------------
# *REST UNPACKING — Catch the Extras
# ----------------------------------------------------------
print("\n=== *REST UNPACKING ===")

# What if you have more values than variables?
# Use * to catch the overflow. Like a catcher's mitt for data.

scores = (98, 87, 92, 76, 88, 95, 91)

first, second, *rest = scores
print(f"First:  {first}")       # 98
print(f"Second: {second}")      # 87
print(f"Rest:   {rest}")        # [92, 76, 88, 95, 91] — it's a list!

# You can put the star anywhere
first, *middle, last = scores
print(f"\nFirst:  {first}")      # 98
print(f"Middle: {middle}")       # [87, 92, 76, 88, 95]
print(f"Last:   {last}")         # 91

# Practical: head and tail of a sequence
head, *tail = ["command", "--verbose", "--output", "file.txt"]
print(f"\nCommand: {head}")
print(f"Args:    {tail}")

# ----------------------------------------------------------
# FUNCTIONS RETURNING TUPLES
# ----------------------------------------------------------
print("\n=== FUNCTIONS RETURNING TUPLES ===")

def min_max(numbers):
    """Return the minimum and maximum of a list as a tuple."""
    return min(numbers), max(numbers)

data = [45, 12, 89, 34, 67, 23, 91, 56]
lowest, highest = min_max(data)
print(f"Data: {data}")
print(f"Min:  {lowest}, Max: {highest}")

def divide(a, b):
    """Return quotient and remainder as a tuple. Like divmod() but homemade."""
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(f"\n17 / 5 = {quotient} remainder {remainder}")
# Fun fact: Python has a built-in for this: divmod(17, 5)

# ----------------------------------------------------------
# TUPLE vs LIST — When to Use Which
# ----------------------------------------------------------
print("\n=== TUPLE vs LIST ===")

# Use TUPLES when:
# - Data shouldn't change (coordinates, RGB colors, dates)
# - Returning multiple values from a function
# - Dictionary keys (tuples are hashable, lists aren't)
# - You want to signal "this data is fixed" to other developers

# Use LISTS when:
# - Data needs to change (shopping carts, to-do lists)
# - You need append, remove, sort, etc.
# - Order matters AND you need mutability

# Tuples are also slightly faster and use less memory.
# Not that you'll notice, but it's fun at parties. Nerdy parties.

# ============================================================
#  PART 2: SETS — The Duplicate Destroyers
# ============================================================

# ----------------------------------------------------------
# CREATING SETS
# ----------------------------------------------------------
print("\n" + "=" * 50)
print("=== SETS — The Duplicate Destroyers ===")

# Sets use curly braces and automatically remove duplicates
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(f"Fruits set: {fruits}")
# Notice: duplicates are gone! Sets don't play favorites.

# Empty set — CAREFUL! {} creates a dict, not a set
empty_set = set()          # Correct!
empty_dict = {}            # This is a DICTIONARY, not a set!
print(f"\ntype(set()):  {type(empty_set)}")
print(f"type({{}}):     {type(empty_dict)}")

# ----------------------------------------------------------
# DEDUPLICATION — Sets' #1 Superpower
# ----------------------------------------------------------
print("\n=== DEDUPLICATION ===")

# Got duplicates? Set them straight. (Pun absolutely intended.)
playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Bohemian Rhapsody",
            "Hotel California", "Stairway to Heaven", "Imagine",
            "Bohemian Rhapsody", "Imagine"]

print(f"Original playlist ({len(playlist)} songs): {playlist}")

unique_songs = set(playlist)
print(f"Unique songs ({len(unique_songs)}): {unique_songs}")

# Convert back to a list if you need order/indexing
unique_list = list(set(playlist))
print(f"As a list: {unique_list}")
# WARNING: sets are UNORDERED. The order might change!

# To deduplicate AND keep original order:
seen = set()
unique_ordered = []
for song in playlist:
    if song not in seen:
        seen.add(song)
        unique_ordered.append(song)
print(f"Ordered unique: {unique_ordered}")
# This pattern is your secret weapon. Remember it.

# ----------------------------------------------------------
# ADDING AND REMOVING FROM SETS
# ----------------------------------------------------------
print("\n=== ADD & REMOVE ===")

skills = {"Python", "JavaScript", "HTML"}
print(f"Skills: {skills}")

# add() — add one element
skills.add("CSS")
print(f"After add('CSS'):     {skills}")

# add() with existing element — no error, just ignored
skills.add("Python")
print(f"After add('Python'):  {skills}")   # No duplicate!

# discard() — remove safely (no error if missing)
skills.discard("HTML")
print(f"After discard('HTML'): {skills}")

skills.discard("Ruby")    # Ruby was never there, but no error
print(f"After discard('Ruby'): {skills}")   # No crash!

# remove() — remove strictly (RAISES ERROR if missing)
# skills.remove("Ruby")  # KeyError! Don't do this unless you're sure.

# pop() — removes and returns a RANDOM element
popped = skills.pop()
print(f"Popped: '{popped}', Remaining: {skills}")

# ----------------------------------------------------------
# SET OPERATIONS — This is Where Sets SHINE
# ----------------------------------------------------------
print("\n=== SET OPERATIONS ===")

# Let's say we're comparing music tastes
alice_likes = {"Rock", "Pop", "Jazz", "Blues", "Classical"}
bob_likes = {"Pop", "Hip Hop", "R&B", "Jazz", "Electronic"}

print(f"Alice likes: {alice_likes}")
print(f"Bob likes:   {bob_likes}")

# UNION (|) — everything combined
all_genres = alice_likes | bob_likes     # or: alice_likes.union(bob_likes)
print(f"\nUnion (all genres):         {all_genres}")

# INTERSECTION (&) — what they BOTH like
shared = alice_likes & bob_likes         # or: alice_likes.intersection(bob_likes)
print(f"Intersection (both like):   {shared}")

# DIFFERENCE (-) — what Alice likes that Bob doesn't
alice_only = alice_likes - bob_likes     # or: alice_likes.difference(bob_likes)
print(f"Alice only:                 {alice_only}")

bob_only = bob_likes - alice_likes
print(f"Bob only:                   {bob_only}")

# SYMMETRIC DIFFERENCE (^) — what they DON'T share
unique_to_each = alice_likes ^ bob_likes   # or: alice_likes.symmetric_difference(bob_likes)
print(f"Unique to each:             {unique_to_each}")

# Set comparisons
small = {1, 2, 3}
big = {1, 2, 3, 4, 5}
print(f"\n{small} is subset of {big}:   {small.issubset(big)}")       # True
print(f"{big} is superset of {small}: {big.issuperset(small)}")       # True
print(f"Are they disjoint?          {small.isdisjoint({6, 7, 8})}")   # True (no overlap)

# ----------------------------------------------------------
# PRACTICAL: Quick Membership Testing
# ----------------------------------------------------------
print("\n=== MEMBERSHIP TESTING ===")

# Sets are WAY faster than lists for "in" checks.
# Lists check every element. Sets use hash tables.
# For small data, you won't notice. For big data? Game changer.

banned_words = {"spam", "scam", "free money", "nigerian prince", "you won"}
message = "Congratulations, you won a free cruise!"

# Check if any banned word is in the message
flagged = any(word in message.lower() for word in banned_words)
print(f"Message: '{message}'")
print(f"Flagged as spam: {flagged}")

# ----------------------------------------------------------
# WHEN TO USE LIST vs TUPLE vs SET
# ----------------------------------------------------------
print("\n=== LIST vs TUPLE vs SET ===")
print("""
+----------+----------+-----------+----------+
| Feature  |  List    |  Tuple    |  Set     |
+----------+----------+-----------+----------+
| Syntax   |  [1,2,3] |  (1,2,3)  | {1,2,3}  |
| Ordered  |  Yes     |  Yes      |  No      |
| Mutable  |  Yes     |  No       |  Yes     |
| Dupes    |  Allowed |  Allowed  |  No      |
| Indexing |  Yes     |  Yes      |  No      |
+----------+----------+-----------+----------+

Use LIST  when: order matters + need to change items
Use TUPLE when: order matters + data is fixed/constant
Use SET   when: need unique values + fast lookups
""")

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("=== CHAPTER 8 RECAP ===")
print("TUPLES:")
print("  1. Created with () or just commas: x = 1, 2, 3")
print("  2. Immutable — can't change after creation")
print("  3. Unpacking: a, b, c = my_tuple")
print("  4. Swap trick: a, b = b, a")
print("  5. *rest catches extra values")
print("  6. Great for function return values")
print("\nSETS:")
print("  1. Created with {} or set()")
print("  2. No duplicates, no order")
print("  3. add(), discard(), remove()")
print("  4. Union |, Intersection &, Difference -, Symmetric ^")
print("  5. Lightning-fast membership testing with 'in'")
print("  6. Perfect for deduplication")
