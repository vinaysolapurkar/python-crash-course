# Chapter 6: Lists: Your First Superpower

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-06-lists/)**

A variable holds one thing. A list holds EVERYTHING. It's like going from a sticky note to a filing cabinet. Up until now, every variable you've created stored a single value. But what if you need to store 50 student names? 1000 scores? A playlist of songs? You're not going to make 1000 separate variables. That's what lists are for, and they're about to change your whole game.

## What You'll Learn
- Creating and accessing lists
- Adding, removing, and modifying items
- Sorting and searching
- The legendary list comprehension

## Creating and Accessing Lists

A list is an ordered collection of items wrapped in square brackets:

```python
# A list of strings
fruits = ["apple", "banana", "cherry", "mango"]

# A list of numbers
scores = [95, 87, 72, 100, 63]

# A mixed list (Python doesn't care about types)
random_stuff = ["hello", 42, 3.14, True, None]

# An empty list
empty = []
```

Access items by their index. Just like strings, lists start counting at 0:

```python
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])     # apple (first item)
print(fruits[1])     # banana (second item)
print(fruits[-1])    # mango (last item!)
print(fruits[-2])    # cherry (second to last)
```

> **Wait, What?** "Lists start at 0, not 1. I know. Programmers are weird." There's actually a historical reason -- it's about memory offsets -- but honestly, you just have to accept it. The first item is at index 0. The second is at index 1. If a list has 4 items, the last index is 3. You'll get used to it faster than you think.

Slicing works too, same as strings:

```python
fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'mango', 'kiwi']
print(fruits[::-1])   # ['kiwi', 'mango', 'cherry', 'banana', 'apple'] (reversed!)
```

Unlike strings, lists are **mutable** -- you can change them:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

## Modifying Lists: Adding and Removing

Lists come with methods for adding and removing items. This is where lists really flex.

### Adding Items

```python
heroes = ["Iron Man", "Thor"]

# append() -- add to the END
heroes.append("Hulk")
print(heroes)  # ['Iron Man', 'Thor', 'Hulk']

# insert() -- add at a specific position
heroes.insert(1, "Spider-Man")
print(heroes)  # ['Iron Man', 'Spider-Man', 'Thor', 'Hulk']

# extend() -- add multiple items at once
heroes.extend(["Black Widow", "Hawkeye"])
print(heroes)  # ['Iron Man', 'Spider-Man', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye']
```

> **Wait, What?** `append()` vs `extend()` -- `append` adds ONE item (even if it's a list, it adds the whole list as a single item). `extend` unpacks the items and adds them individually. Try `heroes.append(["A", "B"])` and see what happens -- you'll get a list inside a list.

### Removing Items

```python
heroes = ["Iron Man", "Spider-Man", "Thor", "Hulk", "Hawkeye"]

# remove() -- remove by VALUE (first occurrence)
heroes.remove("Thor")
print(heroes)  # ['Iron Man', 'Spider-Man', 'Hulk', 'Hawkeye']

# pop() -- remove by INDEX and return the removed item
removed = heroes.pop(1)
print(removed)     # Spider-Man
print(heroes)      # ['Iron Man', 'Hulk', 'Hawkeye']

# pop() with no argument removes the LAST item
last = heroes.pop()
print(last)        # Hawkeye
print(heroes)      # ['Iron Man', 'Hulk']

# del -- remove by index (doesn't return anything)
del heroes[0]
print(heroes)      # ['Hulk']

# clear() -- nuclear option, removes everything
heroes.clear()
print(heroes)      # []
```

Use `remove()` when you know the value. Use `pop()` when you know the index and want to use the removed item. Use `del` when you know the index but don't need the item back.

## Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() -- sorts IN PLACE (modifies the original list)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sort
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() -- returns a NEW sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
print(original)   # [3, 1, 4, 1, 5] (unchanged!)
print(new_list)    # [1, 1, 3, 4, 5]
```

The difference between `sort()` and `sorted()` is crucial:
- `.sort()` changes the list permanently and returns `None`
- `sorted()` leaves the original alone and gives you a new sorted list

When in doubt, use `sorted()`. It's safer because you don't lose the original order.

```python
# Sorting strings (alphabetical)
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']

# Reverse a list (without sorting)
names.reverse()
print(names)  # ['Charlie', 'Bob', 'Alice']
```

## Useful List Operations

```python
numbers = [10, 20, 30, 20, 40]

# Length
print(len(numbers))         # 5

# Check if something is in the list
print(30 in numbers)        # True
print(99 in numbers)        # False
print(99 not in numbers)    # True

# Count occurrences
print(numbers.count(20))    # 2

# Find the index of an item
print(numbers.index(30))    # 2

# Min, max, sum
print(min(numbers))         # 10
print(max(numbers))         # 40
print(sum(numbers))         # 120
```

The `in` keyword is gold. It reads like English: `if "pizza" in toppings:` -- beautiful.

### enumerate() -- Index AND Value

When you loop through a list (we'll cover loops properly in Chapter 7, but here's a preview), sometimes you need both the item AND its position:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:
```
0: apple
1: banana
2: cherry
```

You can even start counting from 1:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

Output:
```
1. apple
2. banana
3. cherry
```

## List Comprehensions: The Show-Off Move

This is where Python gets elegant. A **list comprehension** lets you create a new list by transforming or filtering an existing one -- in a single line.

The old way:

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)  # [1, 4, 9, 16, 25]
```

The list comprehension way:

```python
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
print(squared)  # [1, 4, 9, 16, 25]
```

One line. Same result. The syntax is `[expression for item in iterable]`.

You can add a filter with `if`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Only even numbers, squared
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

And with strings:

```python
names = ["alice", "BOB", "Charlie", "dave"]
clean_names = [name.strip().title() for name in names]
print(clean_names)  # ['Alice', 'Bob', 'Charlie', 'Dave']
```

> **Don't Panic:** List comprehensions look strange at first. Every single Python developer had a "what the heck is this?" moment when they first saw one. Read it from left to right: "give me `n ** 2` FOR each `n` IN `numbers` IF `n` is even." You'll love them in a week. I promise.

A quick guide for reading them:

```python
# Template:
# [what_to_do   for item in collection   if condition]

# "Give me each name uppercased, from the names list, if the name isn't empty"
upper_names = [name.upper() for name in names if name]
```

## Your Turn: Grocery List Manager

Build a simple grocery list manager in `grocery_list.py`:

```python
# Grocery List Manager
print("=== Grocery List Manager ===")
print("Commands: add, remove, show, sort, clear, quit\n")

grocery_list = []

while True:
    command = input("What do you want to do? ").lower().strip()

    if command == "add":
        item = input("What item? ").strip().title()
        if item in grocery_list:
            print(f"'{item}' is already on the list!")
        else:
            grocery_list.append(item)
            print(f"Added '{item}'. ({len(grocery_list)} items total)")

    elif command == "remove":
        item = input("Which item? ").strip().title()
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"Removed '{item}'.")
        else:
            print(f"'{item}' isn't on the list!")

    elif command == "show":
        if grocery_list:
            print("\nYour grocery list:")
            for i, item in enumerate(grocery_list, 1):
                print(f"  {i}. {item}")
            print()
        else:
            print("Your list is empty!")

    elif command == "sort":
        grocery_list.sort()
        print("List sorted alphabetically!")

    elif command == "clear":
        grocery_list.clear()
        print("List cleared!")

    elif command == "quit":
        print(f"Final list: {grocery_list}")
        print("Bye!")
        break

    else:
        print("Unknown command. Try: add, remove, show, sort, clear, quit")
```

Don't worry if the `while True` loop looks unfamiliar -- we'll cover loops fully in Chapter 7. For now, just know it keeps the program running until you type "quit."

**Bonus challenge:** Add a "search" command that checks if an item is on the list, and a "count" command that shows how many items you have.

## TL;DR

- **Lists** are ordered, mutable collections: `fruits = ["apple", "banana"]`
- **Index** starts at 0; use `[-1]` for the last item
- **Add:** `append()` (one item), `insert()` (at position), `extend()` (multiple)
- **Remove:** `remove()` (by value), `pop()` (by index, returns it), `del` (by index)
- **sort()** changes the list; **sorted()** returns a new one
- **Useful:** `len()`, `in`, `count()`, `index()`, `min()`, `max()`, `sum()`, `enumerate()`
- **List comprehensions** create new lists in one line: `[x**2 for x in nums if x > 0]`
- Lists start at 0. Accept it. Love it. Move on.
