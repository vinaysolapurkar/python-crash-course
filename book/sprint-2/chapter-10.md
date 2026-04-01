# Chapter 10: Functions: Stop Repeating Yourself

> **Sprint 2, Chapter 10** | **Estimated Time: 15 minutes** | **Difficulty: Intermediate**

Copy-pasting code is like writing the same essay for every class. Sure, it works. But the moment you need to change something, you're editing it in twelve different places, and you WILL forget one. Functions let you write it once and reuse it forever.

Think of a function like a recipe. You define it once -- "here's how to make pancakes" -- and then you just say "make pancakes" whenever you want them. You don't re-explain the recipe every time.

## Defining and Calling Functions

Here's the simplest function in the world:

```python
def greet():
    print("Hello, world!")

# Call it
greet()   # Hello, world!
greet()   # Hello, world!
greet()   # Hello, world!
```

`def` means "I'm defining a function." Then you give it a name, parentheses, and a colon. Everything indented underneath is the function's body -- the code that runs when you call it.

Calling a function is just its name followed by parentheses: `greet()`. Those parentheses are important. Without them, you're just *referring* to the function, not *running* it.

```python
print(greet)    # <function greet at 0x...>  (the function object itself)
print(greet())  # Hello, world!  then  None  (calls the function)
```

## Parameters and Arguments

Functions get really useful when they accept input.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Priya")    # Hello, Priya!
greet("Alex")     # Hello, Alex!
greet("Jordan")   # Hello, Jordan!
```

`name` is a **parameter** -- the variable name in the function definition. `"Priya"` is an **argument** -- the actual value you pass in when calling it. People use these terms interchangeably, but now you know the difference and can be annoyingly precise at parties.

Multiple parameters? No problem:

```python
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}.")

introduce("Priya", 22, "Mumbai")
# I'm Priya, 22 years old, from Mumbai.
```

## Return Values: Getting Something Back

So far, our functions just print stuff. But the real power is when they *return* a value -- give something back that you can store, use, or pass to another function.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8

# Use it directly in expressions
total = add(10, 20) + add(5, 5)
print(total)    # 40
```

`return` is the magic word. It sends a value back to wherever the function was called. The function stops executing the moment it hits `return`.

```python
def is_adult(age):
    if age >= 18:
        return True
    return False

# Even cleaner:
def is_adult(age):
    return age >= 18
```

> **Wait, What?** "None?! Why does my function return None?" If your function doesn't have a `return` statement, it returns `None` by default. This trips up everyone at least once. If you're saving the result of a function and getting `None`, check if you forgot to `return`.

```python
def add_broken(a, b):
    a + b           # Calculates but doesn't return!

result = add_broken(3, 5)
print(result)   # None  (whoops!)

def add_fixed(a, b):
    return a + b    # Now it actually gives you the answer

result = add_fixed(3, 5)
print(result)   # 8
```

## Default Parameters: The Safety Net

Sometimes you want a parameter to have a fallback value if the caller doesn't provide one.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Priya")              # Hello, Priya!
greet("Alex", "Hey")        # Hey, Alex!
greet("Jordan", "Yo")       # Yo, Jordan!
```

`greeting="Hello"` means "use 'Hello' unless they give me something else." Default parameters must come *after* non-default ones. Python needs to know which arguments go where.

```python
def create_profile(name, age, city="Unknown", active=True):
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }

# Only provide what you need
profile = create_profile("Priya", 22)
print(profile)
# {'name': 'Priya', 'age': 22, 'city': 'Unknown', 'active': True}

profile = create_profile("Alex", 30, "London")
print(profile)
# {'name': 'Alex', 'age': 30, 'city': 'London', 'active': True}
```

## Keyword Arguments: Explicit Is Better

When a function has lots of parameters, positional arguments get confusing. Keyword arguments let you name what you're passing.

```python
def create_user(name, age, email, role="viewer"):
    return {"name": name, "age": age, "email": email, "role": role}

# Positional (works but hard to read)
user = create_user("Priya", 22, "priya@email.com", "admin")

# Keyword (crystal clear)
user = create_user(
    name="Priya",
    age=22,
    email="priya@email.com",
    role="admin"
)
```

With keyword arguments, order doesn't matter. You can even mix positional and keyword, but positional must come first.

```python
# This works:
user = create_user("Priya", age=22, email="priya@email.com")

# This doesn't (positional after keyword):
# user = create_user(name="Priya", 22, "priya@email.com")  # SyntaxError!
```

## *args and **kwargs: The Flexible Friends

Sometimes you don't know how many arguments a function will receive. `*args` and `**kwargs` handle that.

```python
# *args: accept any number of positional arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2))           # 3
print(add_all(1, 2, 3, 4, 5)) # 15
print(add_all(10))             # 10
```

`*args` collects all extra positional arguments into a tuple. You can name it anything (`*nums`, `*items`), but `*args` is the convention.

```python
# **kwargs: accept any number of keyword arguments
def build_profile(**info):
    return info

profile = build_profile(name="Priya", age=22, city="Mumbai")
print(profile)  # {'name': 'Priya', 'age': 22, 'city': 'Mumbai'}
```

`**kwargs` collects all extra keyword arguments into a dictionary. Again, the name is just convention.

```python
# Combining everything
def super_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

super_function("hello", 1, 2, 3, color="blue", size="large")
# Required: hello
# Extra positional: (1, 2, 3)
# Extra keyword: {'color': 'blue', 'size': 'large'}
```

> **Pro Tip:** If you're coming from JavaScript, Python functions are like arrow functions but without the `this` headaches. No binding issues, no accidental context loss. `def` is `function`, `return` is `return`, and everything just works. The main difference: Python doesn't hoist functions (well, not exactly), and indentation replaces curly braces.

## Scope: Local vs Global

Variables created inside a function exist only inside that function. This is called **scope**.

```python
def my_function():
    secret = "I only exist in here"
    print(secret)

my_function()       # I only exist in here
# print(secret)     # NameError: name 'secret' is not defined
```

The variable `secret` is **local** to the function. Once the function ends, it's gone. Like a Snapchat message for variables.

Variables created outside functions are **global** -- accessible everywhere.

```python
greeting = "Hello"    # Global

def say_hi(name):
    print(f"{greeting}, {name}!")   # Can READ global variables

say_hi("Priya")   # Hello, Priya!
```

You can *read* global variables from inside a function, but you can't *modify* them without the `global` keyword. And honestly? Don't use `global`. It leads to messy, unpredictable code. If a function needs data, pass it as a parameter. If a function produces data, return it.

```python
# Don't do this:
counter = 0
def increment():
    global counter
    counter += 1

# Do this instead:
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
```

## Functions as First-Class Objects

Here's something that might blow your mind: in Python, functions are objects. You can pass them around like any other value.

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, text):
    return func(text)

print(speak(shout, "hello"))     # HELLO
print(speak(whisper, "HELLO"))   # hello
```

We're passing the function itself (not calling it -- no parentheses) as an argument. The `speak` function then calls it. This is a powerful pattern that shows up everywhere in Python, especially with `map()`, `filter()`, and `sorted()`.

```python
# Practical example: custom sorting
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9}
]

def get_gpa(student):
    return student["gpa"]

# Sort by GPA
ranked = sorted(students, key=get_gpa, reverse=True)
for s in ranked:
    print(f"{s['name']}: {s['gpa']}")
# Jordan: 3.9
# Priya: 3.8
# Alex: 3.2
```

## Multiple Return Values

Python functions can return multiple values using tuples (remember those from Chapter 8?).

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = get_stats([4, 8, 15, 16, 23, 42])
print(f"Low: {low}, High: {high}, Average: {avg:.1f}")
# Low: 4, High: 42, Average: 18.0
```

It looks like magic, but Python is just packing the values into a tuple and then unpacking them into separate variables.

## Your Turn: Password Strength Checker

Write a function called `check_password` that takes a password string and returns a strength rating: "Weak", "Medium", or "Strong".

Rules:
- **Weak:** Less than 8 characters
- **Medium:** At least 8 characters AND has both letters and numbers
- **Strong:** At least 12 characters, has uppercase, lowercase, numbers, AND special characters

Also write a `has_special_chars` helper function that checks for special characters.

```python
def has_special_chars(password):
    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    # Your code here

def check_password(password):
    # Your code here
    pass

# Test it
print(check_password("abc"))           # Weak
print(check_password("hello123"))      # Medium
print(check_password("MyP@ssw0rd!23")) # Strong
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-10-functions/`

## TL;DR

- **Functions** let you write reusable blocks of code with `def`.
- **Parameters** are placeholders; **arguments** are the actual values you pass in.
- **`return`** sends a value back. No `return` = you get `None`.
- **Default parameters** give fallback values: `def greet(name, greeting="Hi")`.
- **Keyword arguments** make calls readable: `greet(name="Priya")`.
- **`*args`** collects extra positional args into a tuple. **`**kwargs`** collects extra keyword args into a dict.
- Variables inside functions are **local** -- they disappear when the function ends.
- Functions are **first-class objects** -- pass them around like any other value.
- When in doubt, make it a function. Seriously.
