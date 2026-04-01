# Chapter 18: Encapsulation, Polymorphism & Design Principles

> **Sprint 3** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-18-design-principles/)**

Welcome to the chapter where you go from "I can write classes" to "I can *design systems*." This is the difference between knowing how to cook and being a chef. Between playing guitar chords and writing a song. Between stacking LEGO bricks and building the Millennium Falcon.

The concepts in this chapter have fancy names -- encapsulation, polymorphism, composition, SOLID. They sound like a university lecture. But they're actually just common-sense ideas with expensive vocabulary. And once you know them, you'll write code that's genuinely easier to change, test, and explain.

## What You'll Learn

- Encapsulation -- keeping your object's internals private
- Polymorphism -- same method name, different behavior
- Composition vs inheritance -- "has a" vs "is a"
- The SOLID principles -- simplified, no enterprise jargon

## Why Should I Care?

Two reasons. First, job interviews love these concepts. If someone asks "explain polymorphism," you want an answer, not a blank stare.

But more importantly: these principles prevent your code from turning into an unmaintainable mess. You know that codebase at work that nobody wants to touch? The one where changing one thing breaks three other things? It probably ignored every concept in this chapter. These ideas exist because developers learned the hard way what happens without them.

## Encapsulation -- Keep Your Internals Private

Encapsulation means "don't let the outside world mess with your object's guts." It's like a restaurant kitchen: you order food (public interface), but you don't walk into the kitchen and start adjusting the oven temperature (internal state).

Python doesn't have *true* private attributes like Java or C++. Instead, it uses **naming conventions**:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public -- anyone can see/change this
        self._account_id = id(self)  # Protected -- "please don't touch" (single underscore)
        self.__balance = balance     # Private -- "seriously don't touch" (double underscore)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.__balance:.2f}"
```

```python
account = BankAccount("Alice", 1000)

# Public -- works fine
print(account.owner)  # Alice

# Protected -- works but you SHOULDN'T
print(account._account_id)  # 140234567890 (works, but it's a hint to stay away)

# Private -- Python mangles the name to prevent access
# print(account.__balance)  # AttributeError!

# The RIGHT way to interact with balance:
account.deposit(500)
print(account.get_balance())  # 1500

account.withdraw(200)
print(account)  # Alice's account: $1300.00
```

Here's the cheat sheet:

| Convention | Example | Meaning |
|-----------|---------|---------|
| `self.name` | Public | Go ahead, use it freely |
| `self._name` | Protected | "Hey, this is internal. Use at your own risk." |
| `self.__name` | Private | Python actually renames it to prevent accidental access |

The double underscore triggers **name mangling** -- Python renames `__balance` to `_BankAccount__balance` behind the scenes. You *can* still access it if you really try, but it's Python's way of putting a "DO NOT ENTER" sign on the door.

> **Don't Panic:** Python's approach to privacy is sometimes called "we're all consenting adults here." It trusts you to respect the conventions rather than enforcing strict rules. A single underscore `_` is usually all you need. Double underscore `__` is for when you really want to prevent subclass name collisions. Don't overuse it.

**Practical rule:** Use single underscore `_` for internal methods and attributes. Use double underscore `__` rarely. Use public attributes when there's no reason to hide them. Python isn't Java -- you don't need getters and setters for everything.

## Polymorphism -- Same Name, Different Behavior

Here's the $50 word for a $5 concept.

> **Fun Fact:** "Polymorphism" comes from Greek, meaning "many forms." It's a fancy way of saying "different objects can respond to the same method name in their own way." That's it. That's the whole thing.

You've actually already seen this. When you call `len()` on a string, a list, or a dictionary, each one responds differently -- but the method name is the same. That's polymorphism.

Let's see it with our own classes. The classic example (sorry, we're using shapes -- it's the law):

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"{self.__class__.__name__}: area = {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

Now here's the magic:

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape.describe())

# Circle: area = 78.54
# Rectangle: area = 24.00
# Triangle: area = 12.00
```

One loop, three different classes, one method name. Each shape knows how to calculate its own area. The calling code doesn't care *which* shape it's dealing with -- it just calls `.area()` and gets the right answer.

That's polymorphism. You write code that works with the *interface* (all shapes have `.area()`), not the specific type. It makes your code flexible and extensible -- you can add a `Pentagon` class tomorrow without changing the loop.

### Polymorphism Without Inheritance

In Python, you don't even need inheritance for polymorphism. Thanks to **duck typing** ("if it walks like a duck and quacks like a duck..."), any object with the right method works:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Polly wants a cracker!"

# These classes share NO parent, but they all have speak()
animals = [Dog(), Cat(), Parrot()]

for animal in animals:
    print(animal.speak())
```

Python doesn't check if `animal` *is a* certain type. It just checks if `animal` *has* a `speak()` method. If it does, great. If it doesn't, you get an error. This is duck typing, and it's one of Python's superpowers.

## Composition vs Inheritance -- "Has A" vs "Is A"

This is one of the most important design decisions in OOP, and getting it wrong leads to tangled, fragile code.

**Inheritance** says: "A `Dog` **is an** `Animal`."
**Composition** says: "A `Car` **has an** `Engine`."

Here's the difference in code:

### Inheritance Approach

```python
class Car(Engine):  # A car IS an engine? That's weird...
    pass
```

### Composition Approach

```python
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        return f"{self.fuel_type} engine started ({self.horsepower} HP)"

    def stop(self):
        self.running = False
        return "Engine stopped"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Car HAS an engine

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
```

```python
v8 = Engine(450, "gasoline")
mustang = Car("Ford", "Mustang", v8)

print(mustang.start())
# Ford Mustang: gasoline engine started (450 HP)
```

The beauty here: you can swap engines without changing the `Car` class at all.

```python
electric_motor = Engine(300, "electric")
tesla = Car("Tesla", "Model 3", electric_motor)

print(tesla.start())
# Tesla Model 3: electric engine started (300 HP)
```

Same car class, different engine. That's the power of composition -- your objects are built from interchangeable parts.

### When to Use Which?

Here's a practical guide:

**Use inheritance when:**
- There's a clear "is a" relationship (a `Dog` IS an `Animal`)
- The child genuinely shares *all* the parent's behavior
- You want to reuse and extend existing code

**Use composition when:**
- There's a "has a" relationship (a `Car` HAS an `Engine`)
- You want to swap components at runtime
- The relationship doesn't fit a neat hierarchy
- You catch yourself creating deep inheritance chains (more than 2-3 levels deep)

**The famous advice:** "Favor composition over inheritance." This doesn't mean never use inheritance. It means when you're not sure, composition is usually the safer bet. Inheritance creates tight coupling -- change the parent, and all children change too. Composition is looser and more flexible.

## Let's Combine Everything

Here's a more realistic example that uses encapsulation, polymorphism, and composition together:

```python
class PaymentProcessor:
    """Base class for payment methods (polymorphism)."""
    def process(self, amount):
        raise NotImplementedError


class CreditCard(PaymentProcessor):
    def __init__(self, number, name):
        self._number = number  # Encapsulation: protected
        self.name = name

    def process(self, amount):
        last_four = self._number[-4:]
        return f"Charged ${amount:.2f} to card ending in {last_four}"


class PayPal(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def process(self, amount):
        return f"Charged ${amount:.2f} to PayPal ({self.email})"


class Order:
    """Uses composition -- an order HAS a payment processor."""
    def __init__(self, items, payment_method):
        self.items = items
        self._payment = payment_method  # Composition

    def total(self):
        return sum(price for _, price in self.items)

    def checkout(self):
        amount = self.total()
        result = self._payment.process(amount)  # Polymorphism!
        return f"Order total: ${amount:.2f}\n{result}"
```

```python
card = CreditCard("4111111111111234", "Alice")
paypal = PayPal("alice@email.com")

order1 = Order([("Widget", 9.99), ("Gadget", 24.99)], card)
order2 = Order([("Thingamajig", 14.99)], paypal)

print(order1.checkout())
# Order total: $34.98
# Charged $34.98 to card ending in 1234

print(order2.checkout())
# Order total: $14.99
# Charged $14.99 to PayPal (alice@email.com)
```

Same `Order` class, different payment methods. The order doesn't know or care whether it's dealing with a credit card, PayPal, or crypto. It just calls `.process()`. That's polymorphism and composition working together.

## SOLID Principles -- The Cliff Notes

SOLID is a set of five design principles that help you write maintainable code. They were originally described for enterprise Java, but the ideas apply everywhere. Here's each one in plain English, no corporate jargon.

**S -- Single Responsibility Principle.** Each class should do one thing. A `User` class manages user data. A `UserValidator` class validates user data. A `UserDatabase` class saves user data. Don't cram it all into one mega-class. If you're describing your class and you need to use the word "and," it probably does too much.

**O -- Open/Closed Principle.** Your code should be open for extension but closed for modification. Translation: you should be able to add new features without changing existing code. Our payment example nails this -- adding `BitcoinPayment` just means writing a new class. We never touch `Order`, `CreditCard`, or `PayPal`.

**L -- Liskov Substitution Principle.** If you have a function that expects a `Shape`, it should work with any subclass of `Shape` (Circle, Rectangle, Triangle) without breaking. Your child classes shouldn't violate the promises made by the parent. If `Shape.area()` returns a number, `Circle.area()` should too -- not a string, not `None`, not a list of cats.

**I -- Interface Segregation Principle.** Don't force a class to implement methods it doesn't need. If you have a `Worker` interface with `code()`, `test()`, and `make_coffee()`, your `Developer` class shouldn't be required to implement `make_coffee()`. (Although, let's be honest, most developers *do* make a lot of coffee.) Split big interfaces into smaller, focused ones.

**D -- Dependency Inversion Principle.** High-level code shouldn't depend on low-level details. Our `Order` class depends on the `PaymentProcessor` abstraction, not on `CreditCard` specifically. This means you can swap in a new payment method without the `Order` knowing or caring. Depend on abstractions, not concrete implementations.

> **Don't Panic:** These fancy words are just names for common-sense ideas. You've probably been doing some of these already without knowing it. When you wrote small, focused functions in Sprint 2? That's the Single Responsibility Principle. When your code worked with lists AND tuples because they both support iteration? That's the Liskov Substitution Principle. You were already thinking this way. Now you just have the vocabulary.

## Your Turn

Let's refactor the vehicle hierarchy from Chapter 16 using composition:

1. Create an `Engine` class with attributes: `fuel_type`, `horsepower`, `efficiency` (km per fuel unit)

2. Create a `Vehicle` class that HAS an engine (composition):
   - Attributes: `make`, `model`, `year`, `engine`, `fuel_level` (starts at 100)
   - Method `drive(km)` that uses `self.engine.efficiency` to calculate fuel consumption
   - Method `describe()` that includes engine info

3. Create different engine types:
   - `gasoline_engine = Engine("gasoline", 200, 10)` (10 km per fuel unit)
   - `electric_motor = Engine("electric", 300, 15)` (15 km per unit)
   - `diesel_engine = Engine("diesel", 250, 8)` (8 km per unit)

4. Create vehicles with swappable engines:

```python
sedan = Vehicle("Toyota", "Camry", 2024, gasoline_engine)
ev = Vehicle("Tesla", "Model 3", 2024, electric_motor)
truck = Vehicle("Ford", "F-150", 2024, diesel_engine)
```

5. Add a `Fleet` class that contains multiple vehicles and can report total fuel usage.

**Bonus:** Make the `Vehicle` class support `__str__`, `__lt__` (compare by year), and `__len__` (returns fuel_level, because why not).

## TL;DR

- **Encapsulation** means hiding internals: `_protected` (convention), `__private` (name-mangled)
- Python's privacy is by convention, not enforcement -- "we're all consenting adults"
- **Polymorphism** means same method name, different behavior. Call `.area()` on any shape, get the right answer
- Python's duck typing gives you polymorphism for free -- no inheritance required
- **Composition** ("has a") is often better than inheritance ("is a") -- it's more flexible and less fragile
- **SOLID** principles are common-sense rules for clean design. You don't need to memorize acronyms to write good code
- The goal of all these concepts: code that's easy to change, test, and explain to the next person
- These aren't academic abstractions -- they're the difference between a codebase people enjoy working on and one that makes them update their resume
