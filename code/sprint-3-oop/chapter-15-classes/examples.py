"""
Chapter 15: Classes & Objects - Welcome to OOP!
================================================

Think of a CLASS as a blueprint, and an OBJECT as the thing you build from it.

Imagine you're opening a pizza shop. The MENU describes what a pizza is
(size, toppings, crust type) — that's the CLASS.
Each actual pizza you make for a customer — that's an OBJECT (or "instance").

One menu, infinite pizzas. That's OOP in a nutshell.
"""

# ============================================================
# 1. Your First Class — The Pizza Shop Analogy
# ============================================================

class Pizza:
    """A blueprint for making pizzas. Gordon Ramsay would be proud. Maybe."""

    # Class attribute — shared by ALL pizzas (like a shop-wide rule)
    restaurant = "Py-zza Palace"

    def __init__(self, size, crust, toppings):
        """
        __init__ is the CONSTRUCTOR — it runs automatically when you
        create a new pizza. Think of it as the pizza oven turning on.

        'self' refers to the specific pizza being made right now.
        It's like saying "THIS pizza's size" vs "THAT pizza's size."
        """
        # Instance attributes — unique to each pizza
        self.size = size            # "small", "medium", "large"
        self.crust = crust          # "thin", "thick", "stuffed"
        self.toppings = toppings    # list of toppings
        self.slices_left = 8        # every pizza starts with 8 slices
        self.is_ready = False

    def bake(self):
        """Bake the pizza. No raw dough allowed."""
        self.is_ready = True
        print(f"🍕 Your {self.size} {self.crust}-crust pizza is ready!")

    def eat_slice(self):
        """Eat a slice. Because that's what pizzas are for."""
        if not self.is_ready:
            print("Hold on! The pizza isn't baked yet. Patience, young padawan.")
            return

        if self.slices_left > 0:
            self.slices_left -= 1
            print(f"Nom nom! {self.slices_left} slices remaining.")
        else:
            print("No slices left! Time to order another one. 😢")

    def describe(self):
        """Describe this masterpiece."""
        topping_list = ", ".join(self.toppings) if self.toppings else "just cheese"
        print(f"A {self.size} {self.crust}-crust pizza with {topping_list}")
        print(f"From: {self.restaurant}")  # accessing the class attribute


# Let's make some pizzas! (Creating OBJECTS from the CLASS)
print("=" * 50)
print("THE PIZZA SHOP")
print("=" * 50)

# Each of these is an OBJECT — a unique instance of the Pizza class
my_pizza = Pizza("large", "thin", ["pepperoni", "mushrooms"])
your_pizza = Pizza("medium", "stuffed", ["pineapple"])  # controversial choice

my_pizza.describe()
print()
your_pizza.describe()

print()
my_pizza.bake()
my_pizza.eat_slice()
my_pizza.eat_slice()

print()
# Trying to eat an unbaked pizza:
your_pizza.eat_slice()


# ============================================================
# 2. Understanding 'self' — It's Not as Scary as It Looks
# ============================================================
print("\n" + "=" * 50)
print("UNDERSTANDING 'self'")
print("=" * 50)

class SuperHero:
    """
    'self' is just Python's way of saying "the object calling this method."

    When you write:  batman.introduce()
    Python secretly does:  SuperHero.introduce(batman)

    So 'self' IS batman. Or spider_man. Or whoever called the method.
    It's the object referring to itself — like pointing at yourself in a mirror.
    """

    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness
        self.energy = 100

    def introduce(self):
        print(f"I am {self.name}! My power: {self.power}")

    def fight_villain(self):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} fights evil! Energy: {self.energy}%")
        else:
            print(f"{self.name} needs a nap. Even heroes rest.")

    def eat_snack(self, snack):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} eats {snack}. Energy: {self.energy}%")


batman = SuperHero("Batman", "Being rich & cool gadgets", "No superpowers")
spider_man = SuperHero("Spider-Man", "Spidey senses", "Homework deadlines")

batman.introduce()
spider_man.introduce()

print()
# Batman has a busy night
batman.fight_villain()
batman.fight_villain()
batman.fight_villain()
batman.fight_villain()
batman.eat_snack("a protein bar")
batman.fight_villain()


# ============================================================
# 3. Class Attributes vs Instance Attributes
# ============================================================
print("\n" + "=" * 50)
print("CLASS vs INSTANCE ATTRIBUTES")
print("=" * 50)

class Student:
    """
    Class attributes: shared by ALL students (like school rules)
    Instance attributes: unique to each student (like their name)
    """

    # Class attribute — same for everyone
    school = "Hogwarts School of Python & Wizardry"
    total_students = 0  # tracks how many students exist

    def __init__(self, name, house):
        # Instance attributes — unique per student
        self.name = name
        self.house = house
        self.points = 0

        # Update the class attribute (all students share this counter)
        Student.total_students += 1

    def earn_points(self, amount):
        self.points += amount
        print(f"✨ {self.name} earns {amount} points for {self.house}!")
        print(f"   Total points: {self.points}")

    def info(self):
        print(f"{self.name} | House: {self.house} | Points: {self.points}")
        print(f"   School: {self.school}")


# All students go to the same school (class attribute)
harry = Student("Harry", "Gryffindor")
hermione = Student("Hermione", "Gryffindor")
draco = Student("Draco", "Slytherin")

harry.info()
hermione.info()
draco.info()

print(f"\nTotal students enrolled: {Student.total_students}")

# Each student earns their own points (instance attribute)
hermione.earn_points(50)
harry.earn_points(30)
draco.earn_points(10)


# ============================================================
# 4. Multiple Objects — They're Independent!
# ============================================================
print("\n" + "=" * 50)
print("MULTIPLE OBJECTS ARE INDEPENDENT")
print("=" * 50)

class BankAccount:
    """Each account is its own world. Changing one doesn't affect others."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            print("Nice try. You can't deposit negative money. 😏")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! {self.owner} has ${self.balance:.2f}")
        elif amount <= 0:
            print("You can't withdraw nothing. That's just standing at the ATM.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


# Two completely separate accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 50)

alice_account.deposit(500)     # Alice gets richer
bob_account.withdraw(30)       # Bob spends some

# Alice's transactions don't affect Bob
alice_account.check_balance()  # $1500.00
bob_account.check_balance()    # $20.00

# Bob tries to live large
bob_account.withdraw(100)      # Nope!


# ============================================================
# 5. Quick Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 15 RECAP")
print("=" * 50)
print("""
OOP Cheat Sheet:
-----------------------------------------------------------------
CLASS       = Blueprint / Template / Cookie cutter
OBJECT      = Instance / Actual thing / The cookie
__init__    = Constructor (runs when object is created)
self        = "This specific object" (the object calling the method)

Class Attr  = Shared by ALL objects  (Student.school)
Instance Attr = Unique to EACH object (self.name)

Methods     = Functions that belong to a class
              (they always take 'self' as the first parameter)
-----------------------------------------------------------------

Why OOP?
  - Organizes code into logical chunks
  - Reusable — make as many objects as you want from one class
  - Models real-world things naturally
  - Makes complex programs manageable

Coming up: Chapter 16 — Inheritance (classes having babies! ...sort of)
""")
