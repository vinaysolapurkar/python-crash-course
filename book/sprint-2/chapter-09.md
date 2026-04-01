# Chapter 9: Dictionaries: The Real MVP

> **Sprint 2, Chapter 9** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Lists are great. You know that. You've been slicing them, looping through them, and generally having a good time. But lists have a secret weakness -- you can only access things by number. "Give me item number 3." That works, but what if you could say "Give me the *email*" or "Give me the *price*"? What if you could access things by NAME?

Enter dictionaries. The real MVP of Python data structures.

## Key-Value Pairs: Like a Real Dictionary (But Better)

Think about an actual dictionary. You look up a **word** and get a **definition**. You don't say "give me the 47,382nd entry." You say "give me the definition of 'serendipity.'"

Python dictionaries work the same way. Instead of word and definition, we call them **key** and **value**. You give it a key, it gives you the value. Simple as that.

```python
# A real-world example: a student's profile
student = {
    "name": "Priya",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}
```

See those curly braces `{}`? That's how Python knows it's a dictionary. Each entry is a `key: value` pair, separated by commas. The key is always a string (usually), and the value can be anything -- a string, a number, a list, even another dictionary.

> **Remember When?** Remember lists from Chapter 6? Dictionaries are like lists that went to college. Lists store things in order by position. Dictionaries store things by label. Both are useful, but dictionaries are what you reach for when your data has *meaning*.

## Creating Dictionaries

You've already seen one way. Here are all the ways to create a dictionary:

```python
# Method 1: Curly braces (most common)
person = {"name": "Alex", "age": 30}

# Method 2: dict() constructor
person = dict(name="Alex", age=30)

# Method 3: Empty dictionary (fill it later)
person = {}

# Method 4: From a list of tuples
person = dict([("name", "Alex"), ("age", 30)])
```

Method 1 is what you'll use 90% of the time. Method 2 is nice when your keys are simple strings. Methods 3 and 4 exist for specific situations, but don't stress about them.

## Accessing Values: [] vs .get()

There are two ways to grab a value from a dictionary. One is reckless. One is safe.

```python
student = {"name": "Priya", "age": 22, "major": "CS"}

# Method 1: Square brackets (reckless)
print(student["name"])    # Priya
print(student["age"])     # 22

# Method 2: .get() (safe)
print(student.get("name"))    # Priya
print(student.get("gpa"))     # None (no crash!)
```

Here's the difference: if you use square brackets and the key doesn't exist, Python throws a `KeyError` and your program crashes. If you use `.get()` and the key doesn't exist, it quietly returns `None`. No drama.

```python
# This crashes:
# print(student["gpa"])   # KeyError: 'gpa'

# This doesn't:
print(student.get("gpa"))           # None
print(student.get("gpa", "N/A"))    # N/A (custom default)
```

That second argument to `.get()` is a default value. "If you can't find the key, give me this instead." It's incredibly useful.

> **Pro Tip:** Use square brackets `[]` when you're *sure* the key exists and you *want* it to crash if it doesn't (because that means something is seriously wrong). Use `.get()` when the key *might* not exist and that's okay.

## Adding, Updating, and Deleting

Dictionaries are mutable -- you can change them whenever you want.

```python
student = {"name": "Priya", "age": 22}

# Adding a new key-value pair
student["major"] = "Computer Science"
student["gpa"] = 3.8
print(student)
# {'name': 'Priya', 'age': 22, 'major': 'Computer Science', 'gpa': 3.8}

# Updating an existing value
student["age"] = 23    # Happy birthday, Priya!
print(student["age"])  # 23

# Deleting a key-value pair
del student["gpa"]
print(student)
# {'name': 'Priya', 'age': 23, 'major': 'Computer Science'}

# .pop() -- delete AND get the value back
major = student.pop("major")
print(major)      # Computer Science
print(student)    # {'name': 'Priya', 'age': 23}
```

Notice that adding and updating use the exact same syntax: `dict[key] = value`. If the key exists, it updates. If it doesn't, it creates. Python figures it out.

## Looping Through Dictionaries

This is where dictionaries get really fun. You can loop through keys, values, or both.

```python
scores = {"math": 95, "english": 87, "science": 92, "history": 78}

# Loop through keys (default behavior)
for subject in scores:
    print(subject)
# math, english, science, history

# Loop through values
for score in scores.values():
    print(score)
# 95, 87, 92, 78

# Loop through both (this is the good one)
for subject, score in scores.items():
    print(f"{subject}: {score}")
# math: 95
# english: 87
# science: 92
# history: 78
```

`.items()` is the one you'll use the most. It gives you both the key and the value on each loop, unpacked into two variables. It's clean, it's readable, it's *chef's kiss*.

```python
# Practical example: find the highest score
scores = {"math": 95, "english": 87, "science": 92, "history": 78}

best_subject = ""
best_score = 0

for subject, score in scores.items():
    if score > best_score:
        best_score = score
        best_subject = subject

print(f"Best subject: {best_subject} ({best_score})")
# Best subject: math (95)
```

## Checking if a Key Exists

Before you access a key, you might want to check if it's there.

```python
student = {"name": "Priya", "age": 22}

# Check if a key exists
if "name" in student:
    print("Name found!")

if "gpa" not in student:
    print("No GPA on file.")
```

The `in` keyword checks keys, not values. If you want to check values, use `in student.values()`.

## Nested Dictionaries: Dictionaries Inside Dictionaries

Things get really powerful when you put dictionaries inside dictionaries. This is how real-world data is structured.

```python
# A class of students with their grades
classroom = {
    "priya": {
        "math": 95,
        "english": 87,
        "science": 92
    },
    "alex": {
        "math": 78,
        "english": 91,
        "science": 85
    },
    "jordan": {
        "math": 88,
        "english": 76,
        "science": 94
    }
}

# Access Priya's math grade
print(classroom["priya"]["math"])  # 95

# Loop through all students and their grades
for student, grades in classroom.items():
    average = sum(grades.values()) / len(grades)
    print(f"{student}: average = {average:.1f}")
# priya: average = 91.3
# alex: average = 84.7
# jordan: average = 86.0
```

Two levels of square brackets: `classroom["priya"]["math"]`. First, get Priya's dictionary. Then, get the math value from that dictionary. It reads like English: "from the classroom, get priya's math."

You can also have lists of dictionaries -- this is extremely common when working with data from the internet (APIs, databases, etc.):

```python
# A list of products (like you'd get from an online store API)
products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Mouse", "price": 29, "in_stock": True},
    {"name": "Webcam", "price": 79, "in_stock": False}
]

# Find all in-stock products under $100
affordable = [p["name"] for p in products if p["in_stock"] and p["price"] < 100]
print(affordable)  # ['Mouse']
```

## Dictionary Comprehensions

Just like list comprehensions (remember those from Chapter 7?), you can create dictionaries with a one-liner.

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Convert a list of names to a dictionary with name lengths
names = ["Priya", "Alex", "Jordan"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Priya': 5, 'Alex': 4, 'Jordan': 6}

# Filter a dictionary (only keep scores above 85)
scores = {"math": 95, "english": 87, "science": 72, "history": 78}
good_scores = {subj: score for subj, score in scores.items() if score > 85}
print(good_scores)  # {'math': 95, 'english': 87}
```

The syntax is `{key_expression: value_expression for item in iterable}`. It's the same idea as list comprehensions, but with a colon separating the key and value.

## Merging Dictionaries

Sometimes you need to combine two dictionaries into one. Python gives you a few ways.

```python
defaults = {"theme": "light", "language": "en", "font_size": 14}
user_prefs = {"theme": "dark", "font_size": 18}

# Method 1: ** spread operator (Python 3.5+)
settings = {**defaults, **user_prefs}
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}

# Method 2: | merge operator (Python 3.9+)
settings = defaults | user_prefs
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}

# Method 3: .update() (modifies in place)
settings = defaults.copy()    # Don't modify the original!
settings.update(user_prefs)
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}
```

Notice that when both dictionaries have the same key (like "theme"), the second one wins. The user's preferences override the defaults. That's usually exactly what you want.

> **Wait, What?** The `**` spread operator "unpacks" a dictionary into key-value pairs. When you write `{**dict1, **dict2}`, you're saying "take everything from dict1, then take everything from dict2, and put it all in a new dictionary." If there are duplicates, the last one wins. It's like merging two playlists -- the second playlist's version of a song takes priority.

## Useful Dictionary Methods Cheat Sheet

Here are the methods you'll use the most:

```python
student = {"name": "Priya", "age": 22, "major": "CS"}

student.keys()      # dict_keys(['name', 'age', 'major'])
student.values()    # dict_values(['Priya', 22, 'CS'])
student.items()     # dict_items([('name', 'Priya'), ('age', 22), ('major', 'CS')])
student.get("gpa", 0)   # 0 (safe access with default)
student.pop("major")     # Removes and returns 'CS'
student.copy()           # Shallow copy
student.clear()          # Empties the dictionary
len(student)             # Number of key-value pairs
```

## Your Turn: Contact Book

Build a contact book program that lets users:

1. Add a contact (name, phone, email)
2. Look up a contact by name
3. Update a contact's info
4. Delete a contact
5. Display all contacts
6. Quit

Each contact should be stored as a dictionary inside a main contacts dictionary. Use `.get()` for safe lookups and `.items()` for displaying all contacts.

**Starter hint:**

```python
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Look Up Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Quit")

    choice = input("\nPick an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Added {name}!")

    # ... fill in the rest!
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-09-dictionaries/`

## TL;DR

- **Dictionaries** store data as **key-value pairs** -- access by name, not position.
- Use `dict["key"]` when you're sure the key exists. Use `dict.get("key")` when you're not.
- Add/update with `dict["key"] = value`. Delete with `del dict["key"]` or `.pop("key")`.
- Loop with `.keys()`, `.values()`, or `.items()` (the best one).
- **Nested dictionaries** let you store complex, structured data.
- **Dictionary comprehensions** create dictionaries in one line: `{k: v for k, v in stuff}`.
- **Merge** with `{**dict1, **dict2}` or `dict1 | dict2`.
- Dictionaries are everywhere in Python. APIs, configs, databases -- they all speak dictionary.
