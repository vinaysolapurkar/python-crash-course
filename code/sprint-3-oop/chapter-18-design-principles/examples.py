"""
Chapter 18: Design Principles — Writing Code That Doesn't Haunt You Later
===========================================================================

"Any fool can write code that a computer can understand.
 Good programmers write code that humans can understand." — Martin Fowler

This chapter covers:
  1. Access control (public, protected, private)
  2. Polymorphism ("same interface, different behavior")
  3. Composition vs Inheritance ("has a" vs "is a")
  4. SOLID principles (simplified, no PhD required)
"""

# ============================================================
# 1. Public, Protected, Private — The Underscore Convention
# ============================================================
print("=" * 50)
print("1. ACCESS CONTROL — UNDERSCORES")
print("=" * 50)


class BankAccount:
    """
    Python doesn't have TRUE private attributes like Java or C++.
    Instead, we use naming conventions to signal intent:

    public      → self.balance        (anyone can access)
    _protected  → self._account_type  (internal use, but accessible)
    __private   → self.__pin          (name-mangled — hard to access from outside)

    It's the "honor system" — Python trusts you to be an adult.
    """

    def __init__(self, owner, balance, pin):
        self.owner = owner            # Public: access freely
        self._account_type = "savings"  # Protected: "hey, don't touch this"
        self.__pin = pin              # Private: name-mangled for protection

    def check_balance(self):
        """Public method — part of the intended interface."""
        return f"{self.owner}'s balance: ${self.balance}"

    def _calculate_interest(self):
        """
        Protected method (single underscore).
        Meant for internal use or subclasses. Not part of the public API.
        """
        return self.owner  # simplified

    def __verify_pin(self, entered_pin):
        """
        Private method (double underscore).
        Name-mangled to _BankAccount__verify_pin.
        Really hard to call from outside (on purpose).
        """
        return entered_pin == self.__pin

    def withdraw(self, amount, pin):
        """Public method that uses the private __verify_pin internally."""
        if self.__verify_pin(pin):
            print(f"PIN verified. Withdrawing ${amount}.")
        else:
            print("Wrong PIN! Nice try, hacker. 😏")


account = BankAccount("Alice", 1000, "1234")

# Public — works fine
print(f"Owner: {account.owner}")

# Protected — works but says "please don't"
print(f"Account type: {account._account_type}")  # works, but frowned upon

# Private — name-mangled!
try:
    print(account.__pin)  # AttributeError!
except AttributeError:
    print("Can't access __pin directly! (That's the point)")

# You CAN access it via name mangling (but DON'T in real code):
print(f"Name-mangled access: {account._BankAccount__pin}")  # works but is evil

print()
account.withdraw(100, "1234")  # correct PIN
account.withdraw(100, "0000")  # wrong PIN


# ============================================================
# 2. Polymorphism — "Same Message, Different Response"
# ============================================================
print("\n" + "=" * 50)
print("2. POLYMORPHISM — SHAPE EXAMPLE")
print("=" * 50)

import math


class Shape:
    """
    Base class for shapes.
    All shapes can calculate area and describe themselves.
    The INTERFACE is the same — the IMPLEMENTATION varies.

    It's like asking different musicians to "play a song":
    - A guitarist strums chords
    - A pianist hits keys
    - A drummer... drums
    Same request, different execution. That's polymorphism!
    """

    def area(self):
        raise NotImplementedError("Subclasses must implement area()!")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()!")

    def describe(self):
        print(f"{self.__class__.__name__}: "
              f"Area = {self.area():.2f}, "
              f"Perimeter = {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # side lengths
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula — fancy math from ancient Greece
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# The magic: we can treat ALL shapes the same way!
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
    Circle(10),
    Rectangle(8, 3),
]

# Same method call, different results — that's polymorphism!
for shape in shapes:
    shape.describe()

# This works because they all share the same INTERFACE (area, perimeter)
# but each has its own IMPLEMENTATION

# Calculate total area of all shapes
total_area = sum(shape.area() for shape in shapes)
print(f"\nTotal area of all shapes: {total_area:.2f}")


# ============================================================
# 3. Composition vs Inheritance — "Has A" vs "Is A"
# ============================================================
print("\n" + "=" * 50)
print("3. COMPOSITION vs INHERITANCE")
print("=" * 50)

# ---- BAD: Using inheritance where composition makes more sense ----
# A Car IS NOT an Engine. A Car HAS an Engine.
# Don't inherit from Engine — compose with it!

# ---- GOOD: Composition ----

class Engine:
    """An engine that a vehicle HAS (composition target)."""

    def __init__(self, horsepower, fuel_type="gasoline"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        print(f"  Engine ({self.horsepower}hp, {self.fuel_type}) started!")

    def stop(self):
        self.running = False
        print(f"  Engine stopped.")

    def __str__(self):
        status = "running" if self.running else "off"
        return f"{self.horsepower}hp {self.fuel_type} engine ({status})"


class GPS:
    """A GPS system that a vehicle HAS."""

    def __init__(self):
        self.destination = None

    def navigate(self, destination):
        self.destination = destination
        print(f"  GPS: Navigating to {destination}. Turn left in 500 feet.")

    def __str__(self):
        return f"GPS ({'navigating to ' + self.destination if self.destination else 'idle'})"


class SoundSystem:
    """A sound system that a vehicle HAS."""

    def __init__(self, brand="Generic"):
        self.brand = brand
        self.playing = None

    def play(self, song):
        self.playing = song
        print(f"  {self.brand} Sound System: Now playing '{song}' 🎵")


class Car:
    """
    A Car is COMPOSED of parts.
    It HAS an engine, GPS, and sound system.

    This is COMPOSITION — building complex objects from simpler ones.
    Like LEGO: snap pieces together instead of inheriting a mega-block.
    """

    def __init__(self, make, model, engine, gps=None, sound=None):
        self.make = make
        self.model = model
        # Composition: Car HAS these components
        self.engine = engine
        self.gps = gps or GPS()
        self.sound = sound or SoundSystem()

    def start(self):
        print(f"{self.make} {self.model} starting up:")
        self.engine.start()

    def drive_to(self, destination):
        if not self.engine.running:
            print("Start the car first!")
            return
        self.gps.navigate(destination)

    def road_trip(self, destination, song):
        """The ultimate road trip experience."""
        self.start()
        self.drive_to(destination)
        self.sound.play(song)

    def describe(self):
        print(f"\n{self.make} {self.model}")
        print(f"  Engine: {self.engine}")
        print(f"  GPS:    {self.gps}")
        print(f"  Sound:  {self.sound.brand}")


# Build a car by COMPOSING parts
my_car = Car(
    "Honda", "Civic",
    engine=Engine(180, "gasoline"),
    sound=SoundSystem("Bose"),
)

my_car.describe()
print()
my_car.road_trip("The Beach", "Walking on Sunshine")

# Easy to swap components! That's the power of composition.
print("\n--- Swapping the engine (easy with composition!) ---")
my_car.engine = Engine(250, "hybrid")
my_car.describe()


# ============================================================
# 4. SOLID Principles — The Beginner-Friendly Version
# ============================================================
print("\n" + "=" * 50)
print("4. SOLID PRINCIPLES (SIMPLIFIED)")
print("=" * 50)
print("""
SOLID is a set of 5 design principles. Here's the "explain like
I'm five" version:

S - Single Responsibility Principle
    "A class should do ONE thing well."
    Bad:  UserManager that handles login AND sends emails AND generates reports
    Good: User, EmailService, ReportGenerator (each does one job)

O - Open/Closed Principle
    "Open for extension, closed for modification."
    Instead of modifying existing code to add features,
    EXTEND it (inheritance, composition, plugins).
    Our Shape example does this! Add a new shape without changing Shape.

L - Liskov Substitution Principle
    "If it looks like a duck, quacks like a duck — it should work like a duck."
    A child class should be usable wherever its parent class is expected.
    Circle should work anywhere Shape works. No surprises!

I - Interface Segregation Principle
    "Don't force classes to implement stuff they don't need."
    Bad:  Worker class with both code() and manage() — not all workers do both!
    Good: Coder interface and Manager interface, use what you need.

D - Dependency Inversion Principle
    "Depend on abstractions, not specifics."
    Our Car doesn't care HOW the engine works internally.
    It just calls engine.start(). We could swap in any engine!
""")

# ---- S: Single Responsibility ----
print("--- S: Single Responsibility in Action ---\n")


# BAD: One class doing everything
class GodObjectBAD:
    """This class does EVERYTHING. That's bad. Don't be this class."""
    def save_user(self): ...
    def send_email(self): ...
    def generate_pdf(self): ...
    def calculate_tax(self): ...
    # 500 more methods... 😱


# GOOD: Each class has ONE job
class UserRepository:
    """I only handle user data storage. That's my ONE job."""
    def save(self, user):
        print(f"  Saving user: {user}")

    def find(self, user_id):
        print(f"  Finding user: {user_id}")
        return {"id": user_id, "name": "Alice"}


class EmailService:
    """I only send emails. That's my ONE job."""
    def send(self, to, subject, body):
        print(f"  Sending email to {to}: '{subject}'")


class NotificationSystem:
    """I coordinate — but delegate the actual work to specialists."""

    def __init__(self):
        self.user_repo = UserRepository()
        self.email_service = EmailService()

    def notify_user(self, user_id, message):
        user = self.user_repo.find(user_id)
        self.email_service.send(user["name"], "Notification", message)


notifier = NotificationSystem()
notifier.notify_user(42, "Your order has shipped!")


# ---- O: Open/Closed in Action ----
print("\n--- O: Open/Closed in Action ---\n")


class NotificationChannel:
    """Base class — new channels extend this, don't modify it."""
    def send(self, message):
        raise NotImplementedError


class EmailChannel(NotificationChannel):
    def send(self, message):
        print(f"  Email: {message}")


class SMSChannel(NotificationChannel):
    def send(self, message):
        print(f"  SMS: {message}")


class PushChannel(NotificationChannel):
    def send(self, message):
        print(f"  Push notification: {message}")


# Adding Slack? Just add a new class! No existing code modified.
class SlackChannel(NotificationChannel):
    def send(self, message):
        print(f"  Slack: {message}")


# Works with ANY channel — that's the open/closed principle!
channels = [EmailChannel(), SMSChannel(), PushChannel(), SlackChannel()]
for channel in channels:
    channel.send("Your code is ready for review!")


# ============================================================
# 5. Putting It All Together
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 18 RECAP")
print("=" * 50)
print("""
Design Principles Cheat Sheet:
-----------------------------------------------------------------
UNDERSCORES:
  public       → self.name         (free for all)
  _protected   → self._internal    ("please don't touch")
  __private    → self.__secret     (name-mangled for protection)

POLYMORPHISM:
  Same method name, different behavior per class.
  shape.area() works for Circle, Rectangle, Triangle — each computes differently.

COMPOSITION > INHERITANCE (usually):
  "Has A" → use composition  (Car HAS an Engine)
  "Is A"  → use inheritance  (Dog IS an Animal)
  When in doubt, prefer composition. It's more flexible.

SOLID:
  S → One class, one job
  O → Extend, don't modify
  L → Children should work like parents
  I → Don't force unnecessary methods
  D → Depend on abstractions

Golden Rules:
  - Keep classes small and focused
  - Prefer composition over deep inheritance
  - Use polymorphism to avoid if/elif chains
  - Write code for the next person (it might be Future You)
-----------------------------------------------------------------
""")
