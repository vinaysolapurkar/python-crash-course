# Chapter 16: Inheritance - Passing Down the Family Traits

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-16-inheritance/)**

In real life, you inherit traits from your parents. Brown eyes, terrible dance moves, strong opinions about pizza toppings, that one laugh that sounds exactly like your dad's. You didn't choose these things. They just... came with the package.

In Python, classes can inherit too. And honestly? It's one of the most useful tricks in all of programming.

## What You'll Learn

- Why inheritance saves you from copy-paste nightmares
- How to create parent and child classes
- What gets inherited (spoiler: everything)
- How to override methods - doing it YOUR way
- `super()` - calling your parent class for help
- `isinstance()` - checking the family tree
- A brief, responsible look at multiple inheritance

## Why Should I Care?

Picture this: you're building a game. You have `Warrior`, `Mage`, and `Archer` classes. They all have `name`, `health`, and a `take_damage()` method. Without inheritance, you'd copy-paste the same code into three different classes. Then when you need to change how damage works, you'd have to change it in three places. Then you'd miss one. Then you'd have a bug. Then you'd cry.

Inheritance fixes that. You write the shared stuff once in a parent class, and the child classes get it for free.

Every major framework uses this. Django models? Inheritance. Flask views? Inheritance. Exception handling (which you learned in Chapter 13)? That entire system is built on inheritance. `ValueError` inherits from `Exception`, which inherits from `BaseException`. You've been *using* inheritance this whole time.

## The Basics: Parent and Child

Let's go back to the pizza shop. We have a `Pizza` class, but now we want to add specialty pizzas - a `DeepDish` and a `ThinCrust`. They're both pizzas, but with some differences.

```python
class Pizza:
    """The parent class - the original recipe."""

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def describe(self):
        topping_list = ", ".join(self.toppings) if self.toppings else "cheese"
        return f"{self.size} pizza with {topping_list}"

    def bake_time(self):
        return 15  # minutes
```

Now, a `DeepDish` is a pizza - it has a size and toppings - but it takes longer to bake and has a thicker crust. Instead of rewriting everything, we **inherit**:

```python
class DeepDish(Pizza):
    """Inherits from Pizza. Gets everything Pizza has, for free."""

    def bake_time(self):
        return 25  # Deep dish needs more time

    def describe(self):
        return f"{super().describe()} (deep dish style)"
```

```python
regular = Pizza("large", ["pepperoni"])
chunky_boi = DeepDish("large", ["sausage", "peppers"])

print(regular.describe())
# large pizza with pepperoni

print(chunky_boi.describe())
# large pizza with sausage, peppers (deep dish style)

print(regular.bake_time())    # 15
print(chunky_boi.bake_time())  # 25
```

Look at what happened. `DeepDish` never defined `__init__`. It didn't need to - it inherited it from `Pizza`. It automatically has `size` and `toppings`. It just overrode the methods it wanted to change.

That's inheritance in a nutshell: **get everything from your parent, change only what you need.**

## What Gets Inherited

Everything. Methods, attributes, the whole package. A child class is a copy of the parent with the option to add or change things.

```python
class ThinCrust(Pizza):
    pass  # Literally no changes - it's identical to Pizza
```

```python
skinny = ThinCrust("medium", ["basil", "mozzarella"])
print(skinny.describe())     # medium pizza with basil, mozzarella
print(skinny.bake_time())    # 15
```

`ThinCrust` does nothing of its own, but it works perfectly. It got *everything* from `Pizza`. The `pass` keyword just means "nothing to add here."

> **Don't Panic:** Inheritance is just one class borrowing from another. That's it. If you understood functions - how one function can call another - you can understand this. A child class just *starts with* everything its parent has.

## Overriding Methods - Doing It YOUR Way

When a child class defines a method with the same name as the parent, it **overrides** (replaces) the parent's version:

```python
class Pizza:
    def bake_time(self):
        return 15

class DeepDish(Pizza):
    def bake_time(self):
        return 25  # Overrides the parent's bake_time
```

When you call `deep_dish.bake_time()`, Python checks the child first. If it finds the method there, it uses it. If not, it goes up to the parent. It's like asking a teenager a question - they'll give their own answer if they have one, otherwise they'll go ask their parents.

## `super()` - Calling Mom for Help

Sometimes you don't want to completely replace the parent's method. You want to *extend* it - do everything the parent does, plus a little extra. That's where `super()` comes in.

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()

    def _calculate_price(self):
        base = {"small": 8.99, "medium": 11.99, "large": 14.99}
        return base.get(self.size, 11.99) + len(self.toppings) * 1.50

class StuffedCrust(Pizza):
    def __init__(self, size, toppings, cheese_type="mozzarella"):
        super().__init__(size, toppings)  # Call Pizza's __init__
        self.cheese_type = cheese_type    # Add our own attribute
        self.price += 3.00               # Stuffed crust costs extra

    def describe(self):
        base = super().describe() if hasattr(Pizza, 'describe') else ""
        return f"{self.size} stuffed crust ({self.cheese_type}) with {', '.join(self.toppings)}"
```

`super()` means "call the parent class's version of this method." So `super().__init__(size, toppings)` runs `Pizza.__init__`, setting up `size`, `toppings`, and `price`. Then `StuffedCrust` adds its own `cheese_type` and adjusts the price.

Think of `super()` as calling your mom for help. "Hey Mom, do the usual setup. I'll handle the rest."

```python
fancy = StuffedCrust("large", ["pepperoni", "mushrooms"], "cheddar")
print(fancy.size)         # large (from Pizza)
print(fancy.cheese_type)  # cheddar (StuffedCrust's own)
print(fancy.price)        # 20.99 (Pizza's price + $3)
```

## A More Practical Example

Let's step outside the pizza shop for a moment and look at something you'd actually build:

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        return f"{self.username} has been deactivated"

    def display(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.username} ({self.email}) - {status}"


class AdminUser(User):
    def __init__(self, username, email, access_level="full"):
        super().__init__(username, email)
        self.access_level = access_level
        self.admin_actions = []

    def ban_user(self, user):
        user.deactivate()
        self.admin_actions.append(f"Banned {user.username}")
        return f"{user.username} has been banned by {self.username}"

    def display(self):
        base = super().display()
        return f"{base} [ADMIN: {self.access_level}]"


class PremiumUser(User):
    def __init__(self, username, email, subscription="monthly"):
        super().__init__(username, email)
        self.subscription = subscription

    def display(self):
        base = super().display()
        return f"{base} [Premium: {self.subscription}]"
```

```python
alice = User("alice", "alice@email.com")
admin = AdminUser("admin_bob", "bob@email.com")
premium = PremiumUser("charlie", "charlie@email.com", "yearly")

print(alice.display())
# alice (alice@email.com) - Active

print(admin.display())
# admin_bob (bob@email.com) - Active [ADMIN: full]

print(admin.ban_user(alice))
# alice has been banned by admin_bob

print(alice.display())
# alice (alice@email.com) - Inactive

print(premium.display())
# charlie (charlie@email.com) - Active [Premium: yearly]
```

Three user types, shared login logic, each with their own special powers. That's inheritance doing what it does best.

## `isinstance()` - Checking the Family Tree

Sometimes you need to check what type an object is. Maybe you want to verify someone is an admin before letting them ban people:

```python
print(isinstance(admin, AdminUser))  # True
print(isinstance(admin, User))       # True (AdminUser IS a User)
print(isinstance(alice, AdminUser))  # False (regular User, not Admin)
```

Notice that `admin` is both an `AdminUser` AND a `User`. That's because inheritance creates an "is a" relationship. An `AdminUser` *is a* `User` with extra powers.

```python
def perform_admin_action(user, target):
    if isinstance(user, AdminUser):
        return user.ban_user(target)
    return "Permission denied. Nice try though."

print(perform_admin_action(admin, alice))   # alice has been banned by admin_bob
print(perform_admin_action(premium, alice))  # Permission denied. Nice try though.
```

## Multiple Inheritance - A Brief Warning

Python lets a class inherit from *multiple* parents:

```python
class FlyingCar(Car, Airplane):
    pass
```

This is legal Python. A `FlyingCar` gets everything from both `Car` and `Airplane`. Sounds cool, right?

It is. Until `Car` and `Airplane` both have a `fuel_level` attribute and a `start_engine()` method that work differently. Then Python has to figure out which one to use, and things get confusing fast.

> **Pro Tip:** Multiple inheritance is like dual-wielding swords. Looks amazing in movies. In practice, you'll probably stab yourself. Stick with single inheritance until you have a really good reason not to. When you see it in the wild, it's usually with **mixins** - small, focused classes that add one specific feature. That's the safe way to do it.

We won't dive deeper into multiple inheritance here. Just know it exists, and that most Python developers use it sparingly and carefully.

## Your Turn

Build a vehicle hierarchy:

1. Create a parent class `Vehicle` with:
   - Attributes: `make`, `model`, `year`, `fuel_level` (starts at 100)
   - Method `drive(km)` that reduces fuel (1 unit per 10 km) and returns a message
   - Method `describe()` that returns a formatted string

2. Create `ElectricVehicle(Vehicle)` that:
   - Adds a `battery_capacity` attribute
   - Overrides `drive()` to use less fuel (1 unit per 15 km, because EVs are efficient)
   - Adds a `charge()` method that sets fuel_level back to 100

3. Create `Truck(Vehicle)` that:
   - Adds a `payload_capacity` attribute
   - Overrides `drive()` to use more fuel (1 unit per 5 km, because trucks are thirsty)
   - Adds a `load(weight)` method

4. Create instances of all three, drive them around, and print their states.

**Bonus:** Add a `HybridVehicle` that inherits from `Vehicle` and has both a `fuel_level` and `battery_level`.

## TL;DR

- **Inheritance** lets a child class get all the methods and attributes of a parent class for free
- Syntax: `class Child(Parent):` - that's it, the parentheses do all the work
- Children can **override** methods to change behavior
- `super()` calls the parent's version of a method - use it when you want to extend, not replace
- `isinstance(obj, ClassName)` checks if an object belongs to a class (or its parents)
- **Multiple inheritance** exists but use it carefully - stick with single inheritance for now
- Inheritance = "write the common stuff once, specialize as needed." Less copy-paste, fewer bugs, happier developer
