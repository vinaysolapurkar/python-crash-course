"""
Chapter 16: Inheritance — Classes Having Babies (Sort Of)
==========================================================

Inheritance lets you create a new class based on an existing one.
The new class INHERITS all attributes and methods from the parent,
and can add its own or override the parent's behavior.

Think of it like genetics:
  - Parent class (base class) = Your parents' DNA
  - Child class (derived class) = You! (same DNA + your own quirks)

Or like a phone:
  - SmartPhone inherits from Phone (calling, texting)
  - But SmartPhone adds apps, camera, the ability to waste hours on TikTok
"""

# ============================================================
# 1. Basic Inheritance — Parent & Child Classes
# ============================================================
print("=" * 50)
print("1. BASIC INHERITANCE")
print("=" * 50)


class Animal:
    """The parent (base) class. All animals share these basics."""

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        self.energy = 100

    def speak(self):
        print(f"{self.name} says: {self.sound}!")

    def eat(self, food):
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} eats {food}. Energy: {self.energy}%")

    def sleep(self):
        self.energy = min(100, self.energy + 50)
        print(f"{self.name} takes a nap. 💤 Energy: {self.energy}%")

    def info(self):
        print(f"{self.name} ({self.species}) — Energy: {self.energy}%")


class Dog(Animal):
    """
    Dog INHERITS from Animal.
    It gets ALL of Animal's methods and attributes for free!
    Plus, we can add dog-specific stuff.
    """

    def __init__(self, name, breed):
        # super() calls the PARENT's __init__
        # So we don't have to repeat all that code!
        super().__init__(name, species="Dog", sound="Woof")
        self.breed = breed      # dog-specific attribute
        self.tricks = []        # dog-specific attribute

    def fetch(self, item):
        """Dogs can fetch. Cats... not so much."""
        if self.energy >= 10:
            self.energy -= 10
            print(f"🎾 {self.name} fetches the {item}! Good boy! Energy: {self.energy}%")
        else:
            print(f"{self.name} is too tired to fetch. Needs a nap!")

    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned: {trick}!")


class Cat(Animal):
    """Cats inherit from Animal but add their own... personality."""

    def __init__(self, name, indoor=True):
        super().__init__(name, species="Cat", sound="Meow")
        self.indoor = indoor
        self.mood = "indifferent"  # very cat-like default

    def knock_stuff_off_table(self):
        """A cat's favorite hobby."""
        print(f"{self.name} knocks your coffee off the table. No remorse. 😼")
        self.mood = "satisfied"

    def ignore_owner(self):
        """Cats are experts at this."""
        print(f"{self.name} looks at you, then deliberately looks away.")


# Both Dog and Cat get Animal's methods for FREE
buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers", indoor=True)

buddy.speak()       # inherited from Animal
buddy.eat("kibble") # inherited from Animal
buddy.fetch("ball") # dog-specific

print()
whiskers.speak()                    # inherited from Animal
whiskers.knock_stuff_off_table()    # cat-specific
whiskers.ignore_owner()             # cat-specific


# ============================================================
# 2. Method Overriding — "I do it MY way!"
# ============================================================
print("\n" + "=" * 50)
print("2. METHOD OVERRIDING")
print("=" * 50)


class Vehicle:
    """Base vehicle class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def start(self):
        print(f"The {self.year} {self.make} {self.model} starts up. Vroom!")

    def describe(self):
        print(f"{self.year} {self.make} {self.model}")


class ElectricCar(Vehicle):
    """Electric cars override some vehicle behaviors."""

    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size  # in kWh
        self.charge_level = 100

    def start(self):
        """
        OVERRIDE the parent's start() method.
        Electric cars don't go "Vroom" — they whisper.
        """
        print(f"The {self.year} {self.make} {self.model} silently glides to life. 🔋")
        print(f"Battery: {self.charge_level}% ({self.battery_size} kWh)")

    def describe(self):
        """Override describe to include battery info."""
        # Call parent's describe first, then add our own info
        super().describe()
        print(f"  Battery: {self.battery_size} kWh | Charge: {self.charge_level}%")


# Same method name, different behavior!
gas_car = Vehicle("Toyota", "Camry", 2023)
electric = ElectricCar("Tesla", "Model 3", 2024, battery_size=82)

gas_car.start()
print()
electric.start()  # overridden — different output!

print()
gas_car.describe()
print()
electric.describe()  # calls super().describe() + adds battery info


# ============================================================
# 3. super() — Calling the Parent's Methods
# ============================================================
print("\n" + "=" * 50)
print("3. super() IN ACTION")
print("=" * 50)


class Employee:
    """Base employee class."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.role = "Employee"

    def work(self):
        print(f"{self.name} is working hard. ⚒️")

    def get_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a ${amount:,} raise! New salary: ${self.salary:,}")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.role}. Salary: ${self.salary:,}")


class Developer(Employee):
    """Developers are employees who also write code (and drink coffee)."""

    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # let the parent handle name & salary
        self.language = language
        self.role = "Developer"
        self.coffees_today = 0

    def work(self):
        """Developers 'work' by coding and drinking coffee."""
        super().work()  # call the parent's work method first
        self.coffees_today += 1
        print(f"  ...writing {self.language} code. ☕ Coffee #{self.coffees_today}")

    def debug(self):
        """A developer-specific method."""
        print(f"{self.name}: 'It works on MY machine!' 🤷")


class Manager(Employee):
    """Managers manage a team of employees."""

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
        self.role = "Manager"

    def work(self):
        super().work()
        print(f"  ...managing a team of {self.team_size} people. 📋")

    def schedule_meeting(self):
        print(f"{self.name} scheduled another meeting. Everyone groans.")


dev = Developer("Alice", 95000, "Python")
mgr = Manager("Bob", 110000, 8)

dev.introduce()
dev.work()
dev.work()
dev.debug()

print()
mgr.introduce()
mgr.work()
mgr.schedule_meeting()

# Both can get raises — inherited from Employee
print()
dev.get_raise(5000)
mgr.get_raise(10000)


# ============================================================
# 4. isinstance() — "What type are you?"
# ============================================================
print("\n" + "=" * 50)
print("4. isinstance() — TYPE CHECKING")
print("=" * 50)

# isinstance() checks if an object is an instance of a class
# It also checks parent classes!

print(f"Is buddy a Dog?    {isinstance(buddy, Dog)}")        # True
print(f"Is buddy an Animal? {isinstance(buddy, Animal)}")    # True! (Dog inherits Animal)
print(f"Is buddy a Cat?    {isinstance(buddy, Cat)}")        # False

print(f"Is dev an Employee?  {isinstance(dev, Employee)}")    # True
print(f"Is dev a Developer?  {isinstance(dev, Developer)}")   # True
print(f"Is dev a Manager?    {isinstance(dev, Manager)}")     # False

# Practical use: handling mixed collections
print("\nAnimal Roll Call:")
animals = [
    Dog("Rex", "German Shepherd"),
    Cat("Luna"),
    Dog("Max", "Poodle"),
    Cat("Shadow", indoor=False),
]

for animal in animals:
    if isinstance(animal, Dog):
        animal.speak()
        animal.fetch("stick")
    elif isinstance(animal, Cat):
        animal.speak()
        animal.knock_stuff_off_table()
    print()


# ============================================================
# 5. Multiple Inheritance — Handle with Care!
# ============================================================
print("=" * 50)
print("5. MULTIPLE INHERITANCE (Use Sparingly!)")
print("=" * 50)


class Flyable:
    """A mixin class — adds flying ability."""
    def fly(self):
        print(f"{self.name} takes to the skies! 🦅")


class Swimmable:
    """A mixin class — adds swimming ability."""
    def swim(self):
        print(f"{self.name} dives into the water! 🏊")


class Duck(Animal, Flyable, Swimmable):
    """
    A duck can do it all — walk, fly, AND swim.
    Multiple inheritance lets us combine capabilities.

    BUT BE CAREFUL: Multiple inheritance can get confusing fast.
    Prefer COMPOSITION (Chapter 18) for complex cases.
    """

    def __init__(self, name):
        super().__init__(name, species="Duck", sound="Quack")


donald = Duck("Donald")
donald.speak()   # from Animal
donald.fly()     # from Flyable
donald.swim()    # from Swimmable
donald.eat("breadcrumbs")  # from Animal

# Check the Method Resolution Order (MRO)
# This is how Python decides which method to call when there's ambiguity
print(f"\nDuck MRO: {[cls.__name__ for cls in Duck.__mro__]}")


# ============================================================
# 6. Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 16 RECAP")
print("=" * 50)
print("""
Inheritance Cheat Sheet:
-----------------------------------------------------------------
PARENT CLASS     = Base class, the template to inherit from
CHILD CLASS      = Derived class, inherits from parent

class Child(Parent):   # Child inherits everything from Parent

super()          = Call the parent's method
                   super().__init__()  — call parent's constructor
                   super().method()    — call parent's method

OVERRIDE         = Redefine a parent's method in the child class
                   Same name, different behavior

isinstance(obj, Class) = Check if obj is an instance of Class
                         (also checks parent classes!)

MULTIPLE INHERITANCE = class Duck(Animal, Flyable, Swimmable)
                       Use sparingly! Can get messy.
-----------------------------------------------------------------

When to use inheritance:
  - "IS A" relationship → Dog IS AN Animal ✅
  - Shared behavior between related classes ✅
  - Specializing a general concept ✅

When NOT to use inheritance:
  - "HAS A" relationship → Car HAS AN Engine (use composition instead!)
  - Unrelated classes that happen to share a method
  - Deep inheritance chains (keep it shallow!)

Next: Chapter 17 — Magic Methods (making your classes Pythonic!)
""")
