# Chapter 8: Tuples & Sets: Lists' Cousins

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-08-tuples-sets/)**

If lists are the extroverts of Python data types -- flexible, changeable, always growing -- tuples are the introverts and sets are the bouncers. Tuples are quiet, reliable, and never change. Sets refuse to let duplicates in. Together with lists, these three data types cover almost every way you'll need to store collections of data.

## What You'll Learn
- Tuples: what they are, when to use them, and why immutability matters
- Tuple unpacking and the swap trick
- Sets: the duplicate destroyers
- Set operations (union, intersection, difference) with Marvel examples
- When to use list vs tuple vs set

## Tuples: The "Read-Only" List

A tuple looks like a list, but with parentheses instead of square brackets:

```python
# A tuple
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person = ("Tony Stark", 48, "Genius")

# A list (for comparison)
shopping = ["milk", "eggs", "bread"]
```

You can access items with indexing and slicing, just like lists:

```python
person = ("Tony Stark", 48, "Genius")
print(person[0])     # Tony Stark
print(person[-1])    # Genius
print(person[1:])    # (48, 'Genius')
```

But here's the catch: **you can't change a tuple after you create it.** That's the whole point.

```python
person = ("Tony Stark", 48, "Genius")
# person[1] = 49   # TypeError: 'tuple' object does not support item assignment
```

No appending. No removing. No sorting in place. It's locked down. Sealed. Immutable.

### "Why Would I Want That?"

Great question. Here's why tuples exist:

1. **Safety.** Some data shouldn't change. GPS coordinates, RGB colors, database records -- if something accidentally modifies them, bad things happen. Tuples prevent that.

2. **Performance.** Tuples are slightly faster than lists because Python knows they won't change. For most programs you won't notice, but it matters at scale.

3. **Dictionary keys.** You'll learn about dictionaries in Sprint 2, but here's a preview: you can use tuples as dictionary keys, but not lists. That's because keys must be immutable.

4. **Signals intent.** When another programmer sees a tuple, they immediately know: "this data isn't supposed to change." It's a communication tool.

```python
# Things that make sense as tuples
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
http_status = (200, "OK")
screen_resolution = (1920, 1080)

# Things that make sense as lists
shopping_cart = ["laptop", "mouse", "keyboard"]  # You'll add/remove items
high_scores = [500, 450, 400, 350]               # New scores get added
```

### Tuple Quirks

A few things that trip people up:

```python
# A tuple with one item needs a trailing comma
single = (42,)     # This is a tuple
not_a_tuple = (42) # This is just the number 42 with pointless parentheses

print(type(single))       # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>

# You can create tuples without parentheses (tuple packing)
point = 10, 20
print(type(point))  # <class 'tuple'>

# len, in, count, index all work
colors = ("red", "green", "blue", "green")
print(len(colors))           # 4
print("red" in colors)       # True
print(colors.count("green")) # 2
print(colors.index("blue"))  # 2
```

That single-element tuple thing is a classic gotcha. `(42)` is just math grouping. `(42,)` is a tuple. The comma is what makes it a tuple, not the parentheses.

## Tuple Unpacking: The Elegant Move

This is one of Python's most satisfying features. Instead of accessing tuple items by index, you can unpack them into separate variables in one shot:

```python
# Instead of this
person = ("Peter Parker", 22, "New York")
name = person[0]
age = person[1]
city = person[2]

# Do this
name, age, city = ("Peter Parker", 22, "New York")
print(f"{name}, {age}, from {city}")
# Peter Parker, 22, from New York
```

One line instead of three. And it reads beautifully. The number of variables on the left must match the number of items in the tuple.

This works with lists too, but it's most commonly used with tuples.

### The * Operator for "Everything Else"

What if you only care about the first item and want to lump the rest together?

```python
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (a list!)

leader, *team, benchwarmer = ("Cap", "Iron Man", "Thor", "Hulk", "Hawkeye")
print(leader)       # Cap
print(team)         # ['Iron Man', 'Thor', 'Hulk']
print(benchwarmer)  # Hawkeye
```

The `*` collects all the "extras" into a list. It's like saying "I'll take the first one, the last one, and shove everything in between into a bag."

## The Swap Trick

In most languages, swapping two variables requires a temporary variable:

```python
# The old-school way
a = 1
b = 2
temp = a
a = b
b = temp
```

Python's tuple unpacking makes this a one-liner:

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
```

That's it. No temp variable. Under the hood, Python creates a tuple `(b, a)` and unpacks it into `(a, b)`. It's clean, it's Pythonic, and it's a great party trick at coding meetups. (Okay, maybe not a *great* party trick.)

## Sets: The Bouncers

A set is an **unordered** collection with **no duplicates**. Think of it as a bouncer at a club: every name gets in, but only once. Try to get in twice? "You're already inside, buddy."

```python
# Create a set with curly braces
colors = {"red", "green", "blue"}

# Or from a list (instant deduplication!)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}
```

That deduplication trick is incredibly useful. Got a list with duplicates? Wrap it in `set()` and they're gone.

```python
# Empty set -- this is a gotcha!
empty_set = set()      # Correct
empty_dict = {}        # This is an empty DICTIONARY, not a set!
```

### Adding and Removing

```python
fruits = {"apple", "banana", "cherry"}

# Add an item
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'cherry', 'mango'} (order may vary)

# Add a duplicate -- nothing happens, no error
fruits.add("apple")
print(fruits)  # Still the same set, no second "apple"

# Remove an item (raises error if not found)
fruits.remove("banana")

# Discard an item (no error if not found -- safer!)
fruits.discard("kiwi")  # No error, even though "kiwi" isn't there

# Pop a random item (sets are unordered, so you can't pick which one)
removed = fruits.pop()
print(f"Removed: {removed}")

# Clear everything
fruits.clear()
```

> **Pro Tip:** Use `discard()` instead of `remove()` when you're not sure if the item is in the set. `remove()` throws a `KeyError` if the item doesn't exist; `discard()` just shrugs and moves on.

### Sets Are Unordered

This is important: sets have **no index** and **no order**. You can't do `my_set[0]`. The items might print in a different order each time.

```python
numbers = {3, 1, 4, 1, 5, 9}
print(numbers)  # Maybe {1, 3, 4, 5, 9} -- you can't predict the order
# print(numbers[0])  # TypeError! Sets don't support indexing
```

If you need order, use a list. If you need uniqueness, use a set. If you need both... convert between them as needed.

## Set Operations: The Marvel Example

This is where sets really shine. They can do math-like operations that would take multiple loops with lists.

Let's say we have two teams of superheroes:

```python
avengers = {"Iron Man", "Thor", "Hulk", "Black Widow", "Captain America"}
guardians = {"Star-Lord", "Gamora", "Groot", "Rocket", "Thor"}
```

(Yes, Thor is in both. Multiverse stuff.)

**Union** -- everyone from both teams (combined roster):

```python
all_heroes = avengers | guardians  # or avengers.union(guardians)
print(all_heroes)
# {'Iron Man', 'Thor', 'Hulk', 'Black Widow', 'Captain America',
#  'Star-Lord', 'Gamora', 'Groot', 'Rocket'}
# Thor appears only ONCE -- no duplicates!
```

**Intersection** -- heroes on BOTH teams:

```python
both_teams = avengers & guardians  # or avengers.intersection(guardians)
print(both_teams)
# {'Thor'}
```

**Difference** -- in Avengers but NOT in Guardians:

```python
avengers_only = avengers - guardians  # or avengers.difference(guardians)
print(avengers_only)
# {'Iron Man', 'Hulk', 'Black Widow', 'Captain America'}
```

**Symmetric Difference** -- in one team OR the other, but NOT both:

```python
exclusive = avengers ^ guardians  # or avengers.symmetric_difference(guardians)
print(exclusive)
# {'Iron Man', 'Hulk', 'Black Widow', 'Captain America',
#  'Star-Lord', 'Gamora', 'Groot', 'Rocket'}
# Thor is excluded because he's in both!
```

These operations are not just cool -- they're blazing fast. Checking if an item is in a set is nearly instant, no matter how large the set is. Doing the same with a list gets slower as the list grows.

**Subset and superset checks:**

```python
og_avengers = {"Iron Man", "Thor", "Hulk"}
print(og_avengers.issubset(avengers))      # True (all of them are in avengers)
print(avengers.issuperset(og_avengers))    # True (avengers contains all of them)
print(avengers.isdisjoint(guardians))      # False (they share Thor)
```

## When to Use What: The Decision Guide

Here's your cheat sheet:

| Feature | List `[]` | Tuple `()` | Set `{}` |
|---------|-----------|------------|----------|
| Ordered? | Yes | Yes | No |
| Mutable? | Yes | No | Yes |
| Duplicates? | Allowed | Allowed | Not allowed |
| Indexable? | Yes | Yes | No |
| Use when... | You need a changeable, ordered collection | Data shouldn't change | You need unique items or set math |

**Use a list when:**
- You need to add/remove items
- Order matters
- You'll access items by position

**Use a tuple when:**
- Data shouldn't change (coordinates, config values, database rows)
- You want to use it as a dictionary key (Sprint 2)
- You're returning multiple values from a function (Sprint 2)

**Use a set when:**
- You need to eliminate duplicates
- You need fast "is this item in here?" checks
- You need union/intersection/difference operations

## Your Turn: Playlist Duplicate Finder

Create `playlist_dedup.py`:

```python
# Playlist Duplicate Finder
print("=== Playlist Duplicate Finder ===\n")

# Simulate two playlists
playlist_road_trip = [
    "Bohemian Rhapsody", "Hotel California", "Sweet Child O' Mine",
    "Don't Stop Believin'", "Bohemian Rhapsody", "Back in Black",
    "Hotel California", "Thunderstruck", "Livin' on a Prayer"
]

playlist_workout = [
    "Lose Yourself", "Eye of the Tiger", "Stronger",
    "Don't Stop Believin'", "Thunderstruck", "Till I Collapse",
    "Remember the Name", "Stronger"
]

# Find duplicates within each playlist
road_trip_set = set(playlist_road_trip)
workout_set = set(playlist_workout)

road_trip_dupes = len(playlist_road_trip) - len(road_trip_set)
workout_dupes = len(playlist_workout) - len(workout_set)

print(f"Road Trip playlist: {len(playlist_road_trip)} songs, {road_trip_dupes} duplicates")
print(f"Workout playlist: {len(playlist_workout)} songs, {workout_dupes} duplicates")

# Songs in both playlists
shared = road_trip_set & workout_set
print(f"\nSongs in BOTH playlists: {shared}")

# Songs unique to each
only_road = road_trip_set - workout_set
only_workout = workout_set - road_trip_set
print(f"Only in Road Trip: {only_road}")
print(f"Only in Workout: {only_workout}")

# Merged super-playlist (no duplicates!)
mega_playlist = road_trip_set | workout_set
print(f"\nMega playlist ({len(mega_playlist)} unique songs):")
for i, song in enumerate(sorted(mega_playlist), 1):
    print(f"  {i}. {song}")

# Bonus: use tuple unpacking
print("\n--- Now Playing ---")
current_song, *up_next = sorted(mega_playlist)
print(f"Now playing: {current_song}")
print(f"Up next: {up_next[0]}")
print(f"Songs remaining: {len(up_next)}")
```

**Bonus challenges:**
1. Let the user add songs to either playlist via `input()` and re-run the analysis
2. Find which songs appear more than once in the road trip playlist (not just that duplicates exist, but which specific songs are duplicated)
3. Create a tuple of `(song_title, playlist_name)` for each song and practice unpacking

## TL;DR

- **Tuples** are immutable (read-only) lists: `point = (10, 20)` -- use for data that shouldn't change
- **Tuple unpacking** assigns each item to a variable: `name, age = ("Alice", 30)`
- **Swap trick:** `a, b = b, a` -- no temp variable needed
- **Sets** are unordered collections with no duplicates: `unique = {1, 2, 3}`
- **Set deduplication:** `set([1, 1, 2, 2, 3])` gives you `{1, 2, 3}`
- **Set operations:** `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference)
- **Use lists** for ordered, changeable collections
- **Use tuples** for fixed data (coordinates, configs, multi-return values)
- **Use sets** for uniqueness and set math
