# Chapter 4: Strings: Text is Everywhere

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-04-strings/)**

Every text message you've sent, every tweet, every Netflix subtitle, every Google search, every password you've typed - strings. Text is the backbone of computing, and Python is ridiculously good at working with it. By the end of this chapter, you'll be slicing, dicing, and formatting text like a sushi chef.

## What You'll Learn
- Essential string methods that'll make your life easier
- Method chaining - combo moves for strings
- Slicing - cutting strings like a pizza
- Escape characters and raw strings
- f-string formatting superpowers

## String Methods: Your Text Toolkit

Remember how functions like `print()` do things? **Methods** are functions that belong to a specific data type. Strings come with a bunch of built-in methods. Think of them as tools in a Swiss Army knife - each one does something useful.

```python
message = "hello, world"

print(message.upper())       # HELLO, WORLD
print(message.lower())       # hello, world
print(message.title())       # Hello, World
print(message.capitalize())  # Hello, world
print(message.swapcase())    # HELLO, WORLD
```

Notice the pattern? It's `variable.method()`. The dot says "use this method on this string."

Here are the string methods you'll use most often:

```python
text = "  Hello, World!  "

# Cleaning up text
print(text.strip())          # "Hello, World!" (removes leading/trailing spaces)
print(text.lstrip())         # "Hello, World!  " (left side only)
print(text.rstrip())         # "  Hello, World!" (right side only)

# Searching
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("!"))        # True
print("World" in text)                    # True (the 'in' keyword!)
print(text.count("l"))                    # 3

# Finding position
print(text.find("World"))    # 9 (index where "World" starts)
print(text.find("Python"))   # -1 (not found)
```

> **Pro Tip:** Python strings are **immutable** - they can't be changed in place. Every string method returns a **new** string. The original stays the same.

```python
name = "tony stark"
name.upper()          # This creates "TONY STARK" but doesn't save it!
print(name)           # Still "tony stark"

name = name.upper()   # NOW it's saved
print(name)           # "TONY STARK"
```

This trips up beginners all the time. If you call a method but don't save the result, nothing happens. It's like making a photocopy but throwing it in the trash.

### Replacing and Splitting

```python
quote = "I am Iron Man"

# Replace parts of a string
print(quote.replace("Iron Man", "Batman"))  # "I am Batman"
print(quote.replace("I", "You"))            # "You am You ron Man" (replaces ALL occurrences!)

# Split a string into a list
colors = "red,green,blue,yellow"
color_list = colors.split(",")
print(color_list)  # ['red', 'green', 'blue', 'yellow']

# Join a list back into a string
print(" | ".join(color_list))  # "red | green | blue | yellow"

# Check content
print("hello123".isalnum())    # True (letters and numbers only)
print("hello".isalpha())       # True (letters only)
print("12345".isdigit())       # True (digits only)
print("hello".islower())       # True
print("HELLO".isupper())       # True
```

`.split()` and `.join()` are a power duo. Split breaks a string apart, join puts pieces back together. You'll use these constantly when working with data.

## Method Chaining: Combo Moves

Why call one method when you can chain several together? Since each method returns a new string, you can call another method on the result:

```python
user_input = "   hElLo WoRlD   "
clean = user_input.strip().lower().replace("world", "Python")
print(clean)  # "hello python"
```

That single line: (1) strips the spaces, (2) lowercases everything, (3) replaces "world" with "Python." Three operations, one line. It reads left to right, each method working on the result of the previous one.

Think of it like combo moves in a fighting game. Individually they're fine, but chaining them together? That's where the real damage happens.

```python
# Cleaning up messy user input in one shot
email = "   User@Example.COM   "
clean_email = email.strip().lower()
print(clean_email)  # "user@example.com"
```

## Slicing: Cutting Strings Like Pizza

Every character in a string has a position number called an **index**. Python starts counting at 0 (yes, programmers are weird):

```
 H   e   l   l   o
 0   1   2   3   4     <- positive index
-5  -4  -3  -2  -1     <- negative index
```

You can grab individual characters with square brackets:

```python
word = "Hello"
print(word[0])    # H (first character)
print(word[1])    # e (second character)
print(word[-1])   # o (last character!)
print(word[-2])   # l (second to last)
```

Negative indices count from the end. `[-1]` is always the last character. Super useful when you don't know how long the string is.

**Slicing** lets you grab a chunk of a string with `[start:stop:step]`:

```python
text = "Hello, World!"

print(text[0:5])     # "Hello" (from 0 up to but NOT including 5)
print(text[7:12])    # "World"
print(text[:5])      # "Hello" (start defaults to 0)
print(text[7:])      # "World!" (goes to the end)
print(text[:])       # "Hello, World!" (copy the whole thing)
print(text[::2])     # "Hlo ol!" (every 2nd character)
print(text[::-1])    # "!dlroW ,olleH" (reversed!)
```

The key thing to remember: `[start:stop]` goes up to but **does not include** the stop index. Think of it like a hotel checkout - you stay until that day but you don't stay *on* that day.

```python
# Practical example: extracting parts of a date
date = "2025-03-15"
year = date[:4]      # "2025"
month = date[5:7]    # "03"
day = date[8:]       # "15"
print(f"{month}/{day}/{year}")  # "03/15/2025"
```

The reverse trick `[::-1]` is a classic Python one-liner and a favorite interview question:

```python
word = "racecar"
print(word == word[::-1])  # True - it's a palindrome!
```

## Escape Characters and Raw Strings

What if you need a quote inside a string? Or a newline? Escape characters start with a backslash `\`:

```python
# Newline
print("Line 1\nLine 2")
# Line 1
# Line 2

# Tab
print("Name:\tTony Stark")
# Name:    Tony Stark

# Backslash itself
print("C:\\Users\\Documents")
# C:\Users\Documents

# Quote inside a string
print("She said \"hello\"")
# She said "hello"

# Or just use the other type of quote
print('She said "hello"')
# She said "hello"
```

If you have a string with lots of backslashes (like a Windows file path), use a **raw string** with `r` prefix:

```python
# Without raw string - chaos
# path = "C:\new_folder\test"  # \n becomes a newline!

# With raw string - sanity
path = r"C:\new_folder\test"
print(path)  # C:\new_folder\test
```

**Multi-line strings** use triple quotes:

```python
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you."""
print(poem)
```

Triple quotes preserve line breaks and are perfect for long blocks of text. You'll see them used for documentation strings (docstrings) later.

## f-string Formatting: The Advanced Stuff

You already know basic f-strings from Chapter 2. Let's unlock the advanced features.

**Number formatting:**

```python
price = 49.99
tax = price * 0.0825

print(f"Price: ${price:.2f}")       # Price: $49.99 (2 decimal places)
print(f"Tax: ${tax:.2f}")           # Tax: $4.12
print(f"Big number: {1000000:,}")   # Big number: 1,000,000 (commas!)
print(f"Percentage: {0.856:.1%}")   # Percentage: 85.6%
```

The format spec goes after a colon inside the curly braces. `.2f` means "2 decimal places, float format." `,` adds thousand separators. `.1%` converts to a percentage with 1 decimal place.

**Padding and alignment:**

```python
for item, price in [("Coffee", 4.99), ("Sandwich", 8.50), ("Cookie", 2.25)]:
    print(f"{item:<15} ${price:>6.2f}")
```

Output:
```
Coffee           $ 4.99
Sandwich         $ 8.50
Cookie           $ 2.25
```

- `<15` means left-align in a 15-character wide field
- `>6` means right-align in a 6-character wide field
- `^` centers the text

This is great for building neat, aligned output without messing with spaces manually.

**Expressions inside f-strings:**

```python
name = "python"
print(f"Uppercase: {name.upper()}")    # Uppercase: PYTHON
print(f"Length: {len(name)}")           # Length: 6
print(f"Is cool: {10 > 5}")            # Is cool: True
print(f"Quick math: {7 * 6}")          # Quick math: 42
```

You can put any valid Python expression inside those curly braces. Methods, functions, math, comparisons - whatever you need.

## Your Turn: Username Generator

Build a username generator! Create `username_generator.py`:

```python
# Username Generator
print("=== Username Generator ===\n")

# Get user info
first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
lucky_number = input("Enter your lucky number: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Generate username options
option1 = f"{first_name}.{last_name}{lucky_number}"
option2 = f"{first_name[0]}{last_name}{birth_year[-2:]}"
option3 = f"{last_name[::-1]}_{first_name[:3]}"
option4 = f"{first_name}{last_name[0].upper()}_{lucky_number}"

print(f"\nHere are your username options:")
print(f"  1. {option1}")
print(f"  2. {option2}")
print(f"  3. {option3}")
print(f"  4. {option4}")
print(f"\nAll usernames are {len(option1)}-{len(max(option1, option2, option3, option4, key=len))} characters long.")
```

**Bonus challenges:**
1. Add a 5th option that uses `.replace()` to swap vowels with numbers (a=4, e=3, i=1, o=0)
2. Let the user pick their favorite and print it in ALL CAPS as their "official gamer tag"

## TL;DR

- **String methods** are your text Swiss Army knife: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`
- **Strings are immutable** - methods return NEW strings, they don't change the original
- **Method chaining** lets you combo methods: `text.strip().lower().replace("a", "b")`
- **Indexing** starts at 0; negative indices count from the end (`[-1]` = last character)
- **Slicing** with `[start:stop:step]` - stop is exclusive; `[::-1]` reverses a string
- **Escape characters:** `\n` (newline), `\t` (tab), `\\` (backslash); use `r""` for raw strings
- **f-string formatting:** `:.2f` for decimals, `:,` for commas, `:<10` for padding
