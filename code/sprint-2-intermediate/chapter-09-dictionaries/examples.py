"""
Chapter 9: Dictionaries -- The Swiss Army Knife of Python
=========================================================
If lists are like playlists (ordered by position), dictionaries are like
actual dictionaries -- you look things up by NAME, not by number.

Think of them as real-world lookup tables:
  - Phone book: name -> number
  - Menu: dish -> price
  - Pokédex: name -> stats

Let's dive in!
"""

# =============================================================================
# 1. CREATING DICTIONARIES (Key-Value Pairs)
# =============================================================================
# A dictionary is a collection of key: value pairs wrapped in curly braces.

# The classic way -- literal syntax
hero = {
    "name": "Spider-Man",
    "real_name": "Peter Parker",
    "age": 17,
    "powers": ["web-slinging", "spider-sense", "wall-crawling"],
    "is_avenger": True
}

print("=== Our Hero ===")
print(hero)
# Output: {'name': 'Spider-Man', 'real_name': 'Peter Parker', ...}

# You can also create a dict with the dict() constructor
villain = dict(name="Green Goblin", real_name="Norman Osborn", threat_level=9)
print(f"\nVillain: {villain}")

# Empty dict -- two ways
empty1 = {}
empty2 = dict()
print(f"\nEmpty dicts: {empty1}, {empty2}")  # Both are {}

# =============================================================================
# 2. ACCESSING VALUES
# =============================================================================
print("\n=== Accessing Values ===")

# Method 1: Square bracket notation (like asking loudly -- crashes if key missing!)
print(f"Hero name: {hero['name']}")        # Spider-Man
print(f"Powers: {hero['powers']}")          # ['web-slinging', ...]

# Uncomment to see the crash:
# print(hero["girlfriend"])  # KeyError: 'girlfriend' -- ouch, just like Peter's love life

# Method 2: .get() -- the polite way (returns None or a default if key missing)
print(f"Girlfriend: {hero.get('girlfriend')}")           # None (no crash!)
print(f"Girlfriend: {hero.get('girlfriend', 'MJ?')}")    # MJ? (custom default)
print(f"Age: {hero.get('age', 'unknown')}")               # 17 (key exists, returns value)

# PRO TIP: Use .get() when you're not sure the key exists.
# Use [] when you KNOW it does (or WANT to crash on missing keys).

# =============================================================================
# 3. ADDING & UPDATING VALUES
# =============================================================================
print("\n=== Adding & Updating ===")

# Adding a new key-value pair -- just assign it!
hero["city"] = "New York"
hero["mentor"] = "Tony Stark"
print(f"Added city and mentor: {hero['city']}, {hero['mentor']}")

# Updating an existing value -- same syntax
hero["age"] = 18  # Happy birthday, Peter!
print(f"Updated age: {hero['age']}")

# Update multiple values at once with .update()
hero.update({
    "team": "Avengers",
    "suit_color": "red and blue",
    "age": 19  # Another birthday already? Time flies in comics.
})
print(f"After .update(): team={hero['team']}, age={hero['age']}")

# =============================================================================
# 4. DELETING FROM DICTIONARIES
# =============================================================================
print("\n=== Deleting ===")

# Method 1: del -- removes a specific key (crashes if missing)
del hero["mentor"]  # Sorry Tony... *snaps*
print(f"After del mentor: {'mentor' in hero}")  # False

# Method 2: .pop() -- removes AND returns the value (with optional default)
suit = hero.pop("suit_color", "unknown")
print(f"Popped suit_color: {suit}")  # red and blue

# Method 3: .pop() without default on missing key = KeyError
# hero.pop("nonexistent")  # KeyError! Don't do this without a default.

# Method 4: .clear() -- nuclear option, removes EVERYTHING
temp_dict = {"a": 1, "b": 2, "c": 3}
temp_dict.clear()
print(f"After .clear(): {temp_dict}")  # {}

# =============================================================================
# 5. LOOPING THROUGH DICTIONARIES
# =============================================================================
print("\n=== Looping ===")

menu = {
    "Krabby Patty": 2.99,
    "Kelp Shake": 1.50,
    "Coral Bits": 3.49,
    "Barnacle Fries": 1.99
}

# Loop through KEYS (default behavior)
print("--- Keys ---")
for item in menu:  # Same as: for item in menu.keys()
    print(f"  {item}")

# Loop through VALUES
print("\n--- Values ---")
for price in menu.values():
    print(f"  ${price:.2f}")

# Loop through KEY-VALUE PAIRS (the most useful one!)
print("\n--- Items (key, value) ---")
for item, price in menu.items():
    print(f"  {item}: ${price:.2f}")

# Quick math on values
total = sum(menu.values())
print(f"\nTotal menu cost: ${total:.2f}")
print(f"Average price: ${total / len(menu):.2f}")

# =============================================================================
# 6. NESTED DICTIONARIES (Dicts inside dicts -- Inception style!)
# =============================================================================
print("\n=== Nested Dictionaries ===")

# Students with their grades -- a very common pattern
classroom = {
    "hermione": {
        "full_name": "Hermione Granger",
        "house": "Gryffindor",
        "grades": {"potions": 99, "charms": 100, "defense": 95}
    },
    "harry": {
        "full_name": "Harry Potter",
        "house": "Gryffindor",
        "grades": {"potions": 72, "charms": 85, "defense": 100}
    },
    "draco": {
        "full_name": "Draco Malfoy",
        "house": "Slytherin",
        "grades": {"potions": 88, "charms": 76, "defense": 80}
    }
}

# Accessing nested values -- chain the brackets
print(f"Hermione's Charms grade: {classroom['hermione']['grades']['charms']}")
# Output: 100 (obviously)

# Looping through nested dicts
print("\n--- Report Cards ---")
for username, info in classroom.items():
    avg = sum(info["grades"].values()) / len(info["grades"])
    print(f"  {info['full_name']} ({info['house']}): Average = {avg:.1f}")

# =============================================================================
# 7. DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n=== Dictionary Comprehensions ===")
# Just like list comprehensions, but with {key: value for ...}

# Squares dict: {1: 1, 2: 4, 3: 9, ...}
squares = {n: n**2 for n in range(1, 8)}
print(f"Squares: {squares}")

# Convert temperatures: Celsius to Fahrenheit
celsius_temps = {"London": 15, "Tokyo": 22, "Dubai": 40, "Moscow": -5}
fahrenheit = {city: round(c * 9/5 + 32, 1) for city, c in celsius_temps.items()}
print(f"Fahrenheit: {fahrenheit}")

# Filter with comprehension -- only hot cities (above 25°C)
hot_cities = {city: temp for city, temp in celsius_temps.items() if temp > 25}
print(f"Hot cities: {hot_cities}")  # {'Dubai': 40}

# Swap keys and values (careful -- values must be unique!)
reversed_squares = {v: k for k, v in squares.items()}
print(f"Reversed squares: {reversed_squares}")  # {1: 1, 4: 2, 9: 3, ...}

# =============================================================================
# 8. USEFUL METHODS & OPERATIONS
# =============================================================================
print("\n=== Useful Methods ===")

avengers = {
    "iron_man": "Tony Stark",
    "captain_america": "Steve Rogers",
    "thor": "Thor Odinson",
    "hulk": "Bruce Banner",
    "black_widow": "Natasha Romanoff"
}

# .keys() -- returns all keys (as a special view object)
print(f"Heroes: {list(avengers.keys())}")

# .values() -- returns all values
print(f"Real names: {list(avengers.values())}")

# .items() -- returns all (key, value) tuples
print(f"First item: {list(avengers.items())[0]}")

# "in" keyword -- checks if a KEY exists (not value!)
print(f"\n'thor' in avengers? {'thor' in avengers}")              # True
print(f"'hawkeye' in avengers? {'hawkeye' in avengers}")          # False
print(f"'Tony Stark' in avengers? {'Tony Stark' in avengers}")    # False! (it's a value, not a key)

# To check values, use .values()
print(f"'Tony Stark' in values? {'Tony Stark' in avengers.values()}")  # True

# len() -- number of key-value pairs
print(f"\nTeam size: {len(avengers)}")

# .setdefault() -- get value if key exists, otherwise SET and return default
avengers.setdefault("hawkeye", "Clint Barton")  # Adds it!
avengers.setdefault("thor", "Chris Hemsworth")   # Key exists, does nothing
print(f"Hawkeye: {avengers['hawkeye']}")  # Clint Barton
print(f"Thor: {avengers['thor']}")         # Thor Odinson (unchanged!)

# =============================================================================
# 9. MERGING DICTIONARIES
# =============================================================================
print("\n=== Merging Dictionaries ===")

defaults = {"theme": "dark", "font_size": 14, "language": "en"}
user_prefs = {"font_size": 18, "language": "es", "notifications": True}

# Method 1: ** spread operator (Python 3.5+)
# Later dict wins on conflicts
merged = {**defaults, **user_prefs}
print(f"Merged (spread): {merged}")
# {'theme': 'dark', 'font_size': 18, 'language': 'es', 'notifications': True}

# Method 2: | merge operator (Python 3.9+ -- the cool new way)
merged2 = defaults | user_prefs
print(f"Merged (pipe):   {merged2}")

# Method 3: |= in-place merge (also Python 3.9+)
settings = defaults.copy()  # Don't modify the original!
settings |= user_prefs
print(f"Merged (|=):     {settings}")

# Method 4: .update() -- modifies in-place (older Python compatible)
settings2 = defaults.copy()
settings2.update(user_prefs)
print(f"Merged (update): {settings2}")

# =============================================================================
# 10. REAL-WORLD EXAMPLE: Word Frequency Counter
# =============================================================================
print("\n=== Word Frequency Counter ===")

quote = "to be or not to be that is the question to be is to exist"
words = quote.split()

# Count word frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
    # .get(word, 0) returns 0 if word not found, then we add 1

print(f"Word frequencies: {freq}")

# Sort by frequency (most common first)
sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted: {sorted_freq}")

# Top 3 words
top_3 = list(sorted_freq.items())[:3]
print(f"Top 3 words: {top_3}")

# =============================================================================
# RECAP
# =============================================================================
print("\n" + "=" * 50)
print("CHAPTER 9 RECAP -- Dictionaries")
print("=" * 50)
print("""
- Dicts store key: value pairs in {} braces
- Access: dict['key'] (crashes on missing) or dict.get('key') (safe)
- Add/Update: dict['key'] = value
- Delete: del dict['key'], dict.pop('key'), dict.clear()
- Loop: .keys(), .values(), .items()
- Nest dicts inside dicts for complex data
- Dict comprehensions: {k: v for k, v in iterable}
- Check membership: 'key' in dict
- Merge: {**d1, **d2} or d1 | d2 (3.9+)

Dictionaries are EVERYWHERE in Python. APIs return them,
databases use them, config files become them. Master dicts
and you'll feel like Neo seeing the Matrix.
""")
