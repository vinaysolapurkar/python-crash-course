# Chapter 15: Classes & Objects -- Building Your Own Types

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-15-classes-and-objects/)**

Imagine you're opening a pizza shop. You need to track each pizza -- its size, toppings, price. You *could* use a dictionary for each pizza:

```python
pizza1 = {"size": "large", "toppings": ["pepperoni", "mushrooms"], "price": 15.99}
pizza2 = {"size": "medium", "toppings": ["margherita"], "price": 12.99}
```

But what if you want every pizza to be able to calculate its own total with tax? Or describe itself? Or check if it's vegetarian? Dictionaries can hold data, but they can't *do* things. You'd need separate functions floating around, and pretty soon your code looks like a junk drawer.

What if there was a better way?

There is. It's called a **class**.

## What You'll Learn

- Why OOP matters (and why every app you use relies on it)
- How to define a class and create objects
- The `__init__` method -- the automatic setup function
- `self` -- demystified, once and for all
- Class vs instance attributes
- Methods -- things your object can do

## Why Should I Care?

Every app, game, and website you use is built with OOP. That Instagram post you liked? An object. That Spotify song in your queue? An object. That Uber ride you took? Also an object -- with attributes like `driver`, `pickup_location`, `fare`, and methods like `cancel()` and `rate_driver()`.

OOP isn't some academic exercise. It's the way professional software is actually built. And once you get it, you'll never want to go back to juggling loose variables and random functions.

## The Pizza Shop Analogy

Here's the core idea, and it's simpler than you think:

- A **class** is a recipe. It describes *what a pizza is* -- it has a size, toppings, and a price.
- An **object** is an actual pizza. Made from the recipe, sitting on the counter, ready to eat.

One recipe, infinite pizzas. One class, infinite objects.

That's it. That's OOP.

## Your First Class

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size
        self.toppings = toppings
        self.price = price

# Create actual pizzas (objects)
my_pizza = Pizza("large", ["pepperoni", "mushrooms"], 15.99)
your_pizza = Pizza("medium", ["margherita"], 12.99)

print(my_pizza.size)       # large
print(your_pizza.toppings)  # ['margherita']
```

Let's break this down piece by piece.

### `class Pizza:` -- The Recipe

This line says "I'm defining a new type called Pizza." By convention, class names use **CamelCase** (capital first letter of each word). Not `pizza`, not `PIZZA`, not `my_pizza_class`. Just `Pizza`.

### `__init__` -- The Setup Function

```python
def __init__(self, size, toppings, price):
```

This is the **initializer** (some people call it the constructor). It runs automatically every time you create a new Pizza object. You never call `__init__` directly -- Python calls it for you.

Think of it like the moment the pizza comes out of the oven. The second it exists, it *already* has a size, toppings, and a price. That's what `__init__` does -- it sets up the object the instant it's born.

### `self` -- The Most Confusing Word in Python

Okay, let's talk about `self`. It trips up literally everyone. Here's the simple version:

**`self` means "this particular pizza."**

When you write `self.size = size`, you're saying "this pizza's size is whatever was passed in." When `my_pizza` is created, `self` refers to `my_pizza`. When `your_pizza` is created, `self` refers to `your_pizza`.

It's just Python's way of saying "the object we're currently talking about."

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size          # THIS pizza's size
        self.toppings = toppings  # THIS pizza's toppings
        self.price = price        # THIS pizza's price
```

> **Don't Panic:** If `self` confuses you, you're in excellent company. It confuses *everyone* at first. Seriously -- there are thousands of Stack Overflow questions about it. Just remember: **self = "this specific object."** Use it, and one day it'll click. Promise.

### Why Do We Need `self`?

Because a class is a recipe for *many* objects. Python needs to know which pizza you're talking about:

```python
pepperoni = Pizza("large", ["pepperoni"], 14.99)
veggie = Pizza("small", ["mushrooms", "peppers"], 11.99)

# These are DIFFERENT pizzas with DIFFERENT sizes
print(pepperoni.size)  # large
print(veggie.size)     # small
```

`self` is what keeps them separate. Without it, Python would have no idea whose `size` you mean.

## Methods -- Things Your Object Can Do

A class isn't just data storage. The whole point is that objects can *do stuff*. Those actions are called **methods** -- they're just functions that live inside a class.

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size
        self.toppings = toppings
        self.price = price

    def describe(self):
        topping_list = ", ".join(self.toppings)
        return f"{self.size} pizza with {topping_list} -- ${self.price}"

    def total_with_tax(self, tax_rate=0.08):
        return round(self.price * (1 + tax_rate), 2)

    def is_vegetarian(self):
        meat = {"pepperoni", "sausage", "bacon", "ham", "chicken"}
        return not any(t in meat for t in self.toppings)
```

```python
my_pizza = Pizza("large", ["pepperoni", "mushrooms"], 15.99)

print(my_pizza.describe())
# large pizza with pepperoni, mushrooms -- $15.99

print(my_pizza.total_with_tax())
# 17.27

print(my_pizza.is_vegetarian())
# False
```

Notice how every method takes `self` as its first parameter. That's how the method knows which pizza it's working on. When you call `my_pizza.describe()`, Python secretly passes `my_pizza` as `self` behind the scenes.

> **Remember When?** Remember dictionaries from Chapter 9? A class is like a dictionary that can also *do things*. A dictionary holds data: `pizza["size"]`. A class holds data *and* behavior: `pizza.size` plus `pizza.describe()`. It's the upgrade you didn't know you needed.

## Class vs Instance Attributes

There are two kinds of attributes:

**Instance attributes** belong to a specific object. Each pizza has its own size and toppings. These are the ones you set in `__init__` with `self.something`.

**Class attributes** are shared by ALL objects of that class. They're defined directly in the class body:

```python
class Pizza:
    restaurant = "Py's Pizzeria"  # Class attribute -- same for ALL pizzas
    total_pizzas_made = 0         # Class attribute -- shared counter

    def __init__(self, size, toppings, price):
        self.size = size           # Instance attribute -- unique per pizza
        self.toppings = toppings   # Instance attribute
        self.price = price         # Instance attribute
        Pizza.total_pizzas_made += 1
```

```python
p1 = Pizza("large", ["pepperoni"], 15.99)
p2 = Pizza("small", ["cheese"], 9.99)

print(p1.restaurant)          # Py's Pizzeria
print(p2.restaurant)          # Py's Pizzeria (same!)
print(Pizza.total_pizzas_made)  # 2
```

**Rule of thumb:** If every object should share the same value, make it a class attribute. If each object gets its own value, make it an instance attribute.

## Putting It All Together

Let's build a slightly more complete pizza ordering system:

```python
class Pizza:
    restaurant = "Py's Pizzeria"

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()

    def _calculate_price(self):
        base = {"small": 8.99, "medium": 11.99, "large": 14.99}
        topping_cost = len(self.toppings) * 1.50
        return base.get(self.size, 11.99) + topping_cost

    def describe(self):
        topping_list = ", ".join(self.toppings) if self.toppings else "just cheese"
        return f"{self.size.title()} pizza with {topping_list} -- ${self.price:.2f}"

    def total_with_tax(self, tax_rate=0.08):
        return round(self.price * (1 + tax_rate), 2)


# Let's order some pizza
order = [
    Pizza("large", ["pepperoni", "mushrooms"]),
    Pizza("small", []),
    Pizza("medium", ["olives", "onions", "peppers"]),
]

print(f"Order from {Pizza.restaurant}")
print("-" * 40)

total = 0
for pizza in order:
    print(pizza.describe())
    total += pizza.total_with_tax()

print("-" * 40)
print(f"Total (with tax): ${total:.2f}")
```

Output:

```
Order from Py's Pizzeria
----------------------------------------
Large pizza with pepperoni, mushrooms -- $17.99
Small pizza with just cheese -- $8.99
Medium pizza with olives, onions, peppers -- $16.49
----------------------------------------
Total (with tax): $46.95
```

Look at that. Clean, organized, and each pizza knows how to describe itself and calculate its own price. Try doing *that* with a pile of dictionaries.

## Common Mistakes

**Forgetting `self` in method definitions:**

```python
# WRONG -- will crash
class Pizza:
    def describe():  # Missing self!
        return f"{self.size} pizza"

# RIGHT
class Pizza:
    def describe(self):
        return f"{self.size} pizza"
```

**Forgetting `self` when accessing attributes:**

```python
# WRONG -- will crash
def describe(self):
    return f"{size} pizza"  # What's 'size'? Python doesn't know

# RIGHT
def describe(self):
    return f"{self.size} pizza"  # Ah, THIS pizza's size
```

**Using the class name instead of `self`:**

```python
# WRONG (usually) -- this changes it for ALL pizzas
def apply_discount(self):
    Pizza.price = Pizza.price * 0.9

# RIGHT -- changes it for THIS pizza
def apply_discount(self):
    self.price = self.price * 0.9
```

## Your Turn

Time to practice. Create a `Dog` class with:

1. Instance attributes: `name`, `breed`, `age`
2. A method `bark()` that returns `"{name} says: Woof!"`
3. A method `dog_years()` that returns the age multiplied by 7
4. A method `describe()` that returns a formatted string like `"Buddy is a 3-year-old Golden Retriever"`
5. A class attribute `species` set to `"Canis familiaris"`

Create at least two Dog objects and call all their methods.

**Bonus:** Add a method `is_puppy()` that returns `True` if the dog is under 2 years old.

## TL;DR

- A **class** is a blueprint/recipe. An **object** is a thing made from that blueprint
- `__init__` runs automatically when you create an object -- it sets up the initial data
- `self` means "this specific object" -- it's how each object keeps its own data separate
- **Instance attributes** (`self.x`) are unique to each object. **Class attributes** are shared by all objects
- **Methods** are functions inside a class -- they define what an object can *do*
- OOP = data + behavior, bundled together. It's a dictionary that can do things
- If `self` is still confusing, keep going. It clicks with practice. Everyone gets there eventually
