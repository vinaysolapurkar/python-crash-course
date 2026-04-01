# Chapter 17: Magic Methods & Operator Overloading

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-17-magic-methods/)**

What if your custom objects could work with `+`, `-`, `==`, and `print()` just like numbers and strings do? What if you could write `price1 + price2` and get back a new price object, or `print(my_object)` and get something useful instead of `<__main__.Pizza object at 0x7f...>`?

That's magic methods. And yes, they really do feel like magic.

## What You'll Learn

- What magic methods are (and why they have those weird double underscores)
- `__str__` and `__repr__` - making your objects printable
- `__len__` and `__getitem__` - making objects act like lists
- `__add__` and `__eq__` - custom math and comparisons
- `__lt__`, `__gt__` - who's bigger?
- A taste of `__enter__` and `__exit__` (context managers)

## Why Should I Care?

You know how you can do `len("hello")` on a string and `len([1, 2, 3])` on a list and they both just... work? That's because both strings and lists implement a magic method called `__len__` behind the scenes. The `len()` function just calls it.

Libraries like **pandas** and **numpy** use magic methods *everywhere*. That's how you can add two DataFrames together or compare arrays with `>`. It's how `with open("file.txt")` works. It's how `for item in my_object` works. Magic methods are the secret engine behind Python's clean, readable syntax.

If you want your objects to feel like first-class Python citizens instead of awkward outsiders, magic methods are how you get there.

> **Remember When?** Remember when we used `len()` on lists and strings? That called `__len__` behind the scenes. When you wrote `"hello" + " world"`, that called `__add__`. When you did `for item in my_list`, that called `__iter__` and `__next__`. You've been using magic methods all along. Now you'll learn to write your own.

## What Are Magic Methods?

Magic methods (also called **dunder methods**, short for "double underscore") are special methods that Python calls automatically in certain situations. You've already met one - `__init__`, which runs when you create an object.

Here's the pattern: when you write normal Python syntax, Python translates it into magic method calls:

| You Write | Python Calls |
|------|-------|
| `len(obj)` | `obj.__len__()` |
| `print(obj)` | `obj.__str__()` |
| `obj1 + obj2` | `obj1.__add__(obj2)` |
| `obj1 == obj2` | `obj1.__eq__(obj2)` |
| `obj[index]` | `obj.__getitem__(index)` |
| `for x in obj` | `obj.__iter__()` |

That's the whole trick. There's no actual "magic." Python sees `+` and calls `__add__`. It sees `len()` and calls `__len__`. You define these methods, and your objects suddenly work with Python's built-in syntax.

> **Don't Panic:** The double underscores look intimidating, but these are just regular methods with funny names. You define them exactly like any other method. The only difference is that Python calls them automatically when you use certain syntax.

## `__str__` and `__repr__` - Making Objects Printable

Right now, if you print a custom object, you get garbage:

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

p = Pizza("large", ["pepperoni"])
print(p)  # <__main__.Pizza object at 0x7f3b2c1a4f10>
```

Nobody wants to see a memory address. Let's fix that with `__str__`:

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        topping_list = ", ".join(self.toppings)
        return f"{self.size} pizza with {topping_list}"

    def __repr__(self):
        return f"Pizza('{self.size}', {self.toppings})"
```

```python
p = Pizza("large", ["pepperoni", "mushrooms"])

print(p)  # large pizza with pepperoni, mushrooms
print(repr(p))  # Pizza('large', ['pepperoni', 'mushrooms'])
```

The difference:
- **`__str__`** is the "pretty" version - what users see. Called by `print()` and `str()`.
- **`__repr__`** is the "developer" version - what you'd type to recreate the object. Called in the REPL and by `repr()`.

**Rule of thumb:** `__str__` is for humans. `__repr__` is for developers. If you only implement one, make it `__repr__` - Python falls back to it when `__str__` isn't defined.

## `__len__` and `__getitem__` - Acting Like a List

Want your object to work with `len()` and square brackets? Easy:

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"
```

```python
rock = Playlist("Classic Rock")
rock.add("Bohemian Rhapsody")
rock.add("Stairway to Heaven")
rock.add("Hotel California")

print(len(rock))    # 3
print(rock[0])      # Bohemian Rhapsody
print(rock[-1])     # Hotel California
print(rock)         # Playlist 'Classic Rock' (3 songs)

# Bonus: __getitem__ makes it iterable for free!
for song in rock:
    print(f"  Now playing: {song}")
```

By implementing `__getitem__`, your Playlist magically works with `for` loops too. Python sees `__getitem__` and thinks "oh, I can iterate over this by calling `[0]`, `[1]`, `[2]`..." Pretty neat.

## `__add__` and `__eq__` - Custom Math and Comparisons

This is where it gets fun. Let's build a `Money` class that actually understands addition and equality:

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Can't add {self.currency} and {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        if isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __str__(self):
        symbols = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3"}
        symbol = symbols.get(self.currency, self.currency + " ")
        return f"{symbol}{self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
```

```python
price = Money(9.99)
tax = Money(0.80)
total = price + tax  # Calls price.__add__(tax)

print(total)         # $10.79
print(price == tax)  # False
print(Money(5) == Money(5))  # True

# You can even add a plain number
tip = total + 2.00
print(tip)           # $12.79

# But mixing currencies? Nope.
dollars = Money(10, "USD")
euros = Money(10, "EUR")
# dollars + euros  # ValueError: Can't add USD and EUR
```

The `+ ` operator isn't just for numbers anymore. *Your* objects understand it. That's operator overloading, and it's genuinely powerful.

### What's `NotImplemented`?

When you return `NotImplemented` (note: not the *exception* `NotImplementedError`, just the value `NotImplemented`), you're telling Python: "I don't know how to handle this." Python will then try the *other* object's method. It's a polite way of saying "not my problem."

## `__lt__`, `__gt__` - Who's Bigger?

Want to sort your objects? You need comparison methods:

```python
class Money:
    # ... (same __init__ as above)

    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount > other.amount
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other
```

```python
cheap = Money(4.99)
expensive = Money(49.99)

print(cheap < expensive)   # True
print(cheap > expensive)   # False

# Now you can sort a list of Money objects!
prices = [Money(15.99), Money(3.49), Money(27.00), Money(9.99)]
prices.sort()
for p in prices:
    print(p)
# $3.49
# $9.99
# $15.99
# $27.00
```

> **Pro Tip:** Python has a `functools.total_ordering` decorator that fills in the missing comparison methods for you. Define `__eq__` and one of `__lt__`/`__gt__`/`__le__`/`__ge__`, and it generates the rest. Less typing, same result.

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        return NotImplemented

    # __gt__, __le__, __ge__ are auto-generated!
```

## `__enter__` and `__exit__` - Context Managers (Quick Taste)

Remember `with open("file.txt") as f:`? That `with` block calls two magic methods:

- `__enter__` - runs when you enter the `with` block
- `__exit__` - runs when you leave it (even if there's an error)

Here's a quick example - a timer that measures how long a block of code takes:

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions
```

```python
with Timer():
    # Do some work
    total = sum(range(1_000_000))
    print(f"Sum: {total}")

# Sum: 499999500000
# Elapsed: 0.0312 seconds
```

The `with` block guarantees `__exit__` runs no matter what, even if your code throws an error. That's why `with open(...)` is so reliable - it always closes the file. We'll see more of this pattern in later chapters, but now you know the secret: it's just two magic methods.

## The Full Magic Method Cheat Sheet

Here are the ones you'll use most often:

| Method | Triggered By | Purpose |
|----|-------|-----|
| `__init__` | `MyClass()` | Set up the object |
| `__str__` | `print(obj)`, `str(obj)` | Human-readable string |
| `__repr__` | REPL, `repr(obj)` | Developer-readable string |
| `__len__` | `len(obj)` | Return length |
| `__getitem__` | `obj[key]` | Index/key access |
| `__setitem__` | `obj[key] = val` | Index/key assignment |
| `__contains__` | `x in obj` | Membership test |
| `__add__` | `obj + other` | Addition |
| `__sub__` | `obj - other` | Subtraction |
| `__mul__` | `obj * other` | Multiplication |
| `__eq__` | `obj == other` | Equality check |
| `__lt__` | `obj < other` | Less than |
| `__gt__` | `obj > other` | Greater than |
| `__bool__` | `if obj:` | Truthiness |
| `__iter__` | `for x in obj` | Iteration |
| `__enter__` | `with obj:` | Enter context |
| `__exit__` | End of `with` | Exit context |

You don't need to memorize this. Bookmark it. Come back when you need one.

## Your Turn

Build a complete `Money` class with the following:

1. `__init__(self, amount, currency="USD")` - store amount (rounded to 2 decimals) and currency
2. `__str__` - display as `$10.99` (use proper symbol for USD, EUR, GBP)
3. `__repr__` - display as `Money(10.99, 'USD')`
4. `__add__` - add two Money objects (same currency only) or add a number
5. `__sub__` - subtract Money objects or numbers
6. `__eq__` - check if two Money objects are equal (same amount AND currency)
7. `__lt__` and `__gt__` - compare amounts (same currency only)
8. `__mul__` - multiply by a number (useful for tax: `price * 1.08`)
9. `__bool__` - `Money(0)` is falsy, anything else is truthy

Test it:

```python
price = Money(29.99)
tax = price * 0.08
total = price + tax
discount = Money(5.00)
final = total - discount

print(f"Price: {price}")
print(f"Tax: {tax}")
print(f"Total: {total}")
print(f"After discount: {final}")
print(f"Is free? {not final}")
```

**Bonus:** Add `__radd__` so that `5.00 + Money(10)` works too (not just `Money(10) + 5.00`).

## TL;DR

- **Magic methods** (dunder methods) are special methods Python calls automatically for built-in operations
- `__str__` makes `print()` work nicely; `__repr__` is the developer-facing version
- `__add__`, `__sub__`, `__eq__`, `__lt__` let your objects use `+`, `-`, `==`, `<`
- `__len__` and `__getitem__` make your objects work with `len()` and `[]`
- `__enter__` and `__exit__` power the `with` statement
- Return `NotImplemented` (not `NotImplementedError`) when your method can't handle the other type
- You've been using magic methods since Chapter 1 - `print()`, `len()`, `+`, `for` loops all rely on them
- The double underscores look scary but they're just regular methods that Python happens to call automatically
