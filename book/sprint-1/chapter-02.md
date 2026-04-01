# Chapter 2: Variables: Giving Names to Stuff

> **Sprint 1** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-02-variables/)**

Imagine your brain had no names for anything. You couldn't say "pass me my phone." You'd have to say "pass me that flat glowing rectangle that I stare at for six hours a day." Names make life easier. Variables are how we give names to stuff in Python.

## What You'll Learn
- What variables are and how to create them
- The four basic data types: strings, integers, floats, and booleans
- How to check a variable's type
- Naming rules that'll keep you out of trouble
- f-strings -- the single coolest feature for beginners

## Variables: Labeled Boxes

Think of a variable as a **labeled box**. You write a name on the outside (the variable name), and you put something inside (the value). Later, when you need that thing, you just call it by its label.

```python
player_name = "Zelda"
player_health = 100
player_level = 7.5
is_alive = True
```

That's it. Four variables, four values. Let's break down what's happening:

- `player_name` is a box labeled "player_name" with the text `"Zelda"` inside
- `player_health` is a box with the number `100` inside
- `player_level` has `7.5` (a decimal number)
- `is_alive` has `True` (a yes/no value)

The `=` sign doesn't mean "equals" like in math class. It means **"put this value in this box."** It's an assignment, not a comparison. (We'll get to actual comparison in Chapter 5.)

## The Four Basic Data Types

Python has four types you'll use constantly:

| Type | What It Is | Example |
|------|-----------|---------|
| `str` | Text (string) | `"Hello"`, `'Netflix'` |
| `int` | Whole number (integer) | `42`, `-7`, `0` |
| `float` | Decimal number | `3.14`, `-0.5`, `99.99` |
| `bool` | True or False (boolean) | `True`, `False` |

Strings need quotes (single `'` or double `"` -- Python doesn't care which, just be consistent). Numbers don't get quotes. Booleans are capitalized: `True` and `False`, not `true` or `false`.

```python
movie = "Inception"          # str
year = 2010                  # int
rating = 8.8                 # float
is_mind_bending = True       # bool
```

## The type() Function -- What's in the Box?

Ever pick up a mystery package and shake it? Python has a built-in way to check what type of data is in a variable:

```python
movie = "Inception"
year = 2010
rating = 8.8
is_mind_bending = True

print(type(movie))           # <class 'str'>
print(type(year))            # <class 'int'>
print(type(rating))          # <class 'float'>
print(type(is_mind_bending)) # <class 'bool'>
```

`type()` is like an X-ray machine for your variables. Super handy when things break and you're not sure why. (Spoiler: it's usually because something is a string when you thought it was a number.)

## Naming Rules: The Dos and Don'ts

Python has opinions about variable names. Some are hard rules (break them and Python yells at you), and some are style conventions (break them and other programmers judge you silently).

**Hard Rules:**
- Can contain letters, numbers, and underscores
- Must start with a letter or underscore (not a number)
- No spaces
- Case-sensitive (`Name` and `name` are different variables)
- Can't use Python's reserved words (`if`, `for`, `True`, `class`, etc.)

```python
# GOOD variable names
user_name = "Mario"
score_2 = 150
_secret = "hidden"

# BAD -- these will crash
# 2nd_place = "Luigi"    # Can't start with a number
# user name = "Peach"    # No spaces allowed
# class = "Warrior"      # 'class' is a reserved word
```

**Style Conventions (snake_case is king):**

```python
# Python style (snake_case) -- DO THIS
player_health = 100
max_score = 999
is_game_over = False

# Other languages' style -- DON'T do this in Python
playerHealth = 100    # This is camelCase (JavaScript vibes)
MaxScore = 999        # This is PascalCase (C# energy)
MAXSCORE = 999        # ALL CAPS is reserved for constants
```

Use `snake_case`: all lowercase, words separated by underscores. It's the Python way. When in Rome, use underscores.

## f-strings: The Single Coolest Feature for Beginners

Okay, you've got variables. How do you combine them with text? You could do this:

```python
name = "Tony Stark"
age = 48
print("My name is " + name + " and I am " + str(age) + " years old.")
```

That works, but it looks like someone assembled a sentence with duct tape. Enter **f-strings** -- the elegant way:

```python
name = "Tony Stark"
age = 48
print(f"My name is {name} and I am {age} years old.")
```

Output:
```
My name is Tony Stark and I am 48 years old.
```

See that little `f` before the opening quote? That tells Python: "Hey, anything inside `{}` is a variable -- go grab its value." That's it. No plus signs, no `str()` conversion, no mess.

You can even do math inside the curly braces:

```python
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")
```

Output:
```
Total: $59.97
```

f-strings are going to be your best friend in this book. We'll use them in almost every chapter from here on out.

> **Fun Fact:** f-strings were added in Python 3.6 (2016). Before that, people used `.format()` and `%` formatting, which were clunkier. If you see old tutorials using `"Hello, {}".format(name)`, that's the old way. f-strings are better in every way.

## Reassigning Variables: It's YOUR Box

Remember the box analogy? You can empty a box and put something new in it whenever you want:

```python
mood = "happy"
print(mood)        # happy

mood = "hungry"
print(mood)        # hungry

mood = "coding"
print(mood)        # coding
```

Each time you assign a new value, the old one is gone. Python doesn't ask "are you sure?" It just does it.

And here's something that trips people up coming from other languages:

```python
x = 10        # x is an integer
x = "ten"     # now x is a string!?
print(type(x)) # <class 'str'>
```

> **Wait, What?** "Why can I put a string in a variable that had a number?" Because Python uses **dynamic typing**. The variable doesn't have a fixed type -- the *value* does. The box doesn't care what you put in it. A box that held books can now hold shoes. Python is chill like that.

This is different from languages like Java or C++ where you declare a variable's type upfront and it's locked in forever. Python says: "Nah, live your life."

> **Pro Tip:** If you're coming from JavaScript, Java, or C#, note that Python has no `let`, `const`, `var`, or type declarations. You just write `x = 5` and Python figures out the rest. There's no `int x = 5;` -- that semicolon alone will give Python a panic attack.

## Multiple Assignment (The Shortcut)

Feeling fancy? Assign multiple variables in one line:

```python
name, age, city = "Peter Parker", 22, "New York"
print(f"{name}, age {age}, from {city}")
```

Output:
```
Peter Parker, age 22, from New York
```

Or give multiple variables the same value:

```python
x = y = z = 0
print(x, y, z)  # 0 0 0
```

This is handy for initializing counters or scores at the start of a program.

## Your Turn: Build an "About Me" Card

Create a file called `about_me.py` and build a little profile card using variables and f-strings:

```python
# Create these variables with YOUR info
name = "Your Name"
age = 25
city = "Your City"
hobby = "gaming"
favorite_show = "Stranger Things"
python_skill = 1  # on a scale of 1-10

# Print a formatted card
print("=" * 40)
print(f"  Name:          {name}")
print(f"  Age:           {age}")
print(f"  City:          {city}")
print(f"  Hobby:         {hobby}")
print(f"  Favorite Show: {favorite_show}")
print(f"  Python Skill:  {python_skill}/10")
print("=" * 40)
print(f"  {name} will be a {python_skill + 5}/10 by Sprint 3!")
```

Run it. Admire your work. Change the values. Notice how everything updates automatically because you used variables instead of hardcoding the text. That's the power of variables -- change one thing, and it ripples everywhere.

**Bonus challenge:** Add a `is_student` boolean variable and use it in an f-string: `f"Student: {is_student}"`

## TL;DR

- **Variables** are labeled boxes that store values: `name = "Zelda"`
- **Four basic types:** `str` (text), `int` (whole numbers), `float` (decimals), `bool` (True/False)
- Use `type()` to check what type a variable is
- **Naming:** use `snake_case`, start with a letter, no spaces, no reserved words
- **f-strings** are the best way to mix variables with text: `f"Hello, {name}!"`
- Python is **dynamically typed** -- a variable's type can change. Python doesn't judge.
- You can reassign variables anytime. It's your box. Do what you want with it.
