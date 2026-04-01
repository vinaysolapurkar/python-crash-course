# Chapter 19: Decorators -- Functions That Upgrade Functions

> **Sprint 4, Chapter 19** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Have you ever seen code like this?

```python
@app.route("/home")
def home():
    return "Welcome!"
```

Or this?

```python
@login_required
def dashboard():
    return render_template("dashboard.html")
```

That `@` symbol is a **decorator**. And they're everywhere. Flask uses `@app.route` for web URLs. Django uses `@login_required` for authentication. pytest uses `@pytest.fixture` for test setup. FastAPI uses `@app.get` for API endpoints.

If you want to work with any modern Python framework, you need to understand decorators. And here's the good news -- they're simpler than they look.

## The Gift Wrapping Analogy

Think of decorators as **gift wrapping**.

You have a gift (your function). It does something useful. A decorator wraps that gift with extra behavior -- maybe a nice bow, maybe some tissue paper, maybe a card that says "Happy Birthday." The gift inside doesn't change. It still does exactly what it always did. But now it has something extra on the outside.

A `@timer` decorator wraps your function with timing code. A `@login_required` decorator wraps your function with an authentication check. The original function stays the same. The wrapper adds the extra behavior.

That's it. That's decorators.

## Functions Are Objects (A Quick Refresher)

Before we can understand decorators, we need to remember something important: **in Python, functions are objects.** You can pass them around, store them in variables, and return them from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

# Store a function in a variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Pass a function as an argument
def call_twice(func, arg):
    print(func(arg))
    print(func(arg))

call_twice(greet, "Bob")
# Hello, Bob!
# Hello, Bob!
```

Notice we wrote `greet` without parentheses when assigning it to `say_hello`. That's because we're passing the function itself, not calling it. `greet` is the function. `greet("Alice")` is calling the function.

> **Remember When?** In Chapter 10, we passed functions as arguments to `map()` and `filter()`. Same idea here. Functions are just values you can hand around like any other variable.

## Functions That Return Functions

Here's where it gets interesting. A function can **return another function**:

```python
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello = make_greeter("Hello")
howdy = make_greeter("Howdy")

print(hello("Alice"))   # Hello, Alice!
print(howdy("Bob"))     # Howdy, Bob!
```

Read that carefully. `make_greeter` doesn't return a string. It returns a **function**. And that inner function (`greeter`) remembers the `greeting` variable from its parent, even after `make_greeter` has finished running.

This is called a **closure** -- a function that remembers values from the scope where it was created.

## Closures: Functions That Remember

Let's make this concrete:

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20
```

`double` remembers that `factor` is 2. `triple` remembers that `factor` is 3. They each "closed over" their own copy of `factor`. That's a closure.

Why does this matter? Because **decorators are closures.** Understanding closures is the key to understanding decorators.

## Your First Decorator (Step by Step)

Let's build a decorator from scratch. We'll make one that prints a message before and after any function runs.

### Step 1: Write the wrapper function

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function.")
        func()
        print("Something happened after the function.")
    return wrapper
```

Look at what this does:
1. It takes a function (`func`) as input
2. It creates a new function (`wrapper`) that calls the original function with some extra behavior
3. It returns the new function

### Step 2: Use it manually

```python
def say_hello():
    print("Hello!")

# "Decorate" the function manually
say_hello = my_decorator(say_hello)

# Now call it
say_hello()
```

Output:
```
Something is happening before the function.
Hello!
Something happened after the function.
```

The original `say_hello` just printed "Hello!" But after wrapping it, we get the extra behavior too. The function was **decorated**.

### Step 3: Use the @ syntax

That `say_hello = my_decorator(say_hello)` line is exactly what the `@` symbol does. These two are identical:

```python
# The manual way
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)

# The @ way (syntactic sugar)
@my_decorator
def say_hello():
    print("Hello!")
```

The `@` version is just cleaner. That's it. There's no magic. `@my_decorator` means "pass this function to `my_decorator` and replace it with whatever `my_decorator` returns."

> **Don't Panic:** Decorators are just functions that take a function and return a new function. Read that three times and it'll click. Seriously. Read it again. One more time. See? It clicked.

## Handling Arguments with *args and **kwargs

Our decorator above only works with functions that take no arguments. Let's fix that:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(3, 5))
# Calling add...
# add finished.
# 8

print(greet("Alice", greeting="Hey"))
# Calling greet...
# greet finished.
# Hey, Alice!
```

The `*args, **kwargs` pattern means "accept any arguments and pass them through." This makes our decorator work with **any** function, regardless of its parameters.

## Practical Decorator: @timer

Here's a decorator you'll actually use. It measures how long a function takes to run:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

@timer
def sum_numbers(n):
    return sum(range(n))

print(slow_function())
# slow_function took 1.0012 seconds
# Done!

print(sum_numbers(1_000_000))
# sum_numbers took 0.0234 seconds
# 499999500000
```

This is genuinely useful. When you're trying to figure out why your program is slow, slap `@timer` on your functions and find the bottleneck.

## Practical Decorator: @logger

This one logs every function call with its arguments:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {repr(result)}")
        return result
    return wrapper

@logger
def calculate_total(price, tax_rate=0.08):
    return price * (1 + tax_rate)

calculate_total(100, tax_rate=0.1)
# [LOG] calculate_total(100, tax_rate=0.1)
# [LOG] calculate_total returned 110.00000000000001
```

In production code, you'd write to a log file instead of printing, but the idea is the same.

## Preserving Function Identity with functools.wraps

There's one gotcha with decorators. When you decorate a function, the wrapper replaces it -- including its name and docstring:

```python
@timer
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)    # wrapper  (not "my_function"!)
print(my_function.__doc__)     # None     (docstring is gone!)
```

Fix this with `functools.wraps`:

```python
import functools
import time

def timer(func):
    @functools.wraps(func)  # This preserves the original function's identity
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)    # my_function (correct!)
print(my_function.__doc__)     # This is my function. (preserved!)
```

Always use `@functools.wraps(func)` in your decorators. It's a one-liner and it prevents subtle bugs.

## @property: Pythonic Getters and Setters

Python has a built-in decorator that's incredibly useful: `@property`. It lets you access a method as if it were an attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(circle.radius)     # 5 (looks like an attribute, but it's a method)
print(circle.area)       # 78.53981633974483

circle.radius = 10       # Uses the setter
print(circle.area)       # 314.1592653589793

# circle.radius = -1     # ValueError: Radius cannot be negative
```

Notice how `circle.area` doesn't have parentheses. It looks like a regular attribute, but it's actually computed every time you access it. This is the Pythonic way to do getters and setters -- no `get_radius()` and `set_radius()` methods needed.

## A Real-World Example: Retry Decorator

Here's a decorator you might actually use in production -- it retries a function if it fails:

```python
import functools
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data(url):
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Server not responding")
    return {"data": "success"}

# This will retry up to 3 times if it fails
result = fetch_data("https://api.example.com")
```

Notice this is a decorator *with arguments* (`max_attempts`, `delay`). That requires an extra layer of nesting -- a function that returns the decorator. It looks complicated, but it's just one more layer of the same pattern.

## Your Turn: Build a @timer Decorator

**Challenge:** Build a `@timer` decorator that:

1. Measures how long a function takes to run
2. Prints the function name, arguments, and elapsed time
3. Uses `functools.wraps` to preserve function identity
4. Returns the original function's result

Test it with:

```python
@timer
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(30)
print(f"Result: {result}")
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-19-decorators/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-19-decorators/)

## TL;DR

| Concept | What It Does |
|---|---|
| First-class functions | Functions can be passed around like any other value |
| Closure | A function that remembers variables from its enclosing scope |
| Decorator | A function that takes a function and returns a new function with added behavior |
| `@decorator` syntax | Shorthand for `func = decorator(func)` |
| `*args, **kwargs` | Accept and pass through any arguments |
| `functools.wraps` | Preserves the decorated function's name and docstring |
| `@property` | Makes a method behave like an attribute |

**The one-sentence version:** A decorator is just a function that wraps another function to add extra behavior, and the `@` symbol is just a shortcut for applying it.

Next up: Generators and Iterators -- where we learn to process data without loading it all into memory at once.
