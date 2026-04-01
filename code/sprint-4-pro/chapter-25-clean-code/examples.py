"""
Chapter 25: Type Hints & Clean Code — Writing Code That Others (and Future You) Can Read
==========================================================================================

"Code is read much more often than it is written."
    — Guido van Rossum (Python's creator)

This chapter covers:
  1. Type hints — tell Python (and humans) what types to expect
  2. PEP 8 — Python's style guide
  3. Naming conventions — good vs bad names
  4. Code smells — signs your code needs cleaning
  5. Black formatter — auto-format your code

Type hints don't ENFORCE types at runtime (Python is still dynamically typed).
They're like road signs — they GUIDE you but don't physically stop you.
But tools like mypy can CHECK them before you run your code!

Install mypy: pip install mypy
Check types: mypy examples.py
"""

# ============================================================
# 1. Basic Type Hints
# ============================================================
print("=" * 50)
print("1. BASIC TYPE HINTS")
print("=" * 50)

# WITHOUT type hints (mysterious — what types do these expect?):
def add_mystery(a, b):
    return a + b

# WITH type hints (crystal clear!):
def add_clear(a: int, b: int) -> int:
    """Add two integers. Returns an integer."""
    return a + b

# The syntax: parameter: Type and -> ReturnType
def greet(name: str, excited: bool = False) -> str:
    """Greet someone. Optionally with excitement!"""
    if excited:
        return f"HI {name.upper()}!!!"
    return f"Hello, {name}"

# Type hints on variables (optional but useful for clarity)
age: int = 25
name: str = "Alice"
is_student: bool = True
gpa: float = 3.85

print(f"greet('Alice') → {greet('Alice')}")
print(f"greet('Bob', excited=True) → {greet('Bob', excited=True)}")
print(f"add_clear(3, 5) → {add_clear(3, 5)}")

# Type hints DON'T prevent this (Python won't stop you):
result = add_clear("hello", " world")  # Works! But mypy would flag it.
print(f"add_clear('hello', ' world') → {result}  (mypy would complain!)")


# ============================================================
# 2. Collection Type Hints — Lists, Dicts, Tuples
# ============================================================
print("\n" + "=" * 50)
print("2. COLLECTION TYPE HINTS")
print("=" * 50)

# For Python 3.9+, you can use built-in types directly:
#   list[int], dict[str, int], tuple[str, int]
#
# For Python 3.7-3.8, import from typing:
#   from typing import List, Dict, Tuple

from typing import List, Dict, Tuple, Set


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def count_words(text: str) -> dict[str, int]:
    """Count word frequencies in text."""
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """Return the minimum and maximum values as a tuple."""
    return min(numbers), max(numbers)


def unique_tags(articles: list[dict[str, list[str]]]) -> set[str]:
    """Extract unique tags from a list of articles."""
    tags: set[str] = set()
    for article in articles:
        tags.update(article.get("tags", []))
    return tags


# Demo
scores = [85.5, 92.0, 78.5, 95.0, 88.0]
print(f"Average: {calculate_average(scores):.1f}")

word_counts = count_words("the cat sat on the mat the cat")
print(f"Word counts: {word_counts}")

low, high = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")


# ============================================================
# 3. Optional and Union Types
# ============================================================
print("\n" + "=" * 50)
print("3. OPTIONAL AND UNION TYPES")
print("=" * 50)

from typing import Optional, Union


def find_user(user_id: int) -> Optional[dict]:
    """
    Find a user by ID.
    Returns the user dict, or None if not found.

    Optional[dict] means: dict | None
    It's the same as Union[dict, None]
    """
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)  # returns None if not found


def format_value(value: Union[int, float, str]) -> str:
    """
    Format a value that could be different types.
    Union[int, float, str] means: could be any of these.

    Python 3.10+ syntax: int | float | str
    """
    if isinstance(value, (int, float)):
        return f"${value:,.2f}"
    return str(value)


# Demo
user = find_user(1)
print(f"Found user: {user}")

missing = find_user(999)
print(f"Missing user: {missing}")  # None

print(f"format_value(42) → {format_value(42)}")
print(f"format_value(3.14) → {format_value(3.14)}")
print(f"format_value('hello') → {format_value('hello')}")


# ============================================================
# 4. Type Hints with Classes
# ============================================================
print("\n" + "=" * 50)
print("4. TYPE HINTS WITH CLASSES")
print("=" * 50)


class ShoppingCart:
    """A shopping cart with type hints throughout."""

    def __init__(self) -> None:
        self.items: list[dict[str, Union[str, float]]] = []
        self.discount: float = 0.0

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add an item to the cart."""
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
        })

    def get_total(self) -> float:
        """Calculate the total price."""
        total = sum(
            float(item["price"]) * int(item["quantity"])
            for item in self.items
        )
        return total * (1 - self.discount)

    def apply_discount(self, percent: float) -> None:
        """Apply a percentage discount (0-100)."""
        if not 0 <= percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = percent / 100

    def get_summary(self) -> str:
        """Return a summary of the cart."""
        lines: list[str] = []
        for item in self.items:
            lines.append(
                f"  {item['name']}: ${float(item['price']):.2f} x {item['quantity']}"
            )
        lines.append(f"  Total: ${self.get_total():.2f}")
        if self.discount > 0:
            lines.append(f"  (Discount: {self.discount * 100:.0f}%)")
        return "\n".join(lines)


cart = ShoppingCart()
cart.add_item("Python Book", 39.99)
cart.add_item("Mechanical Keyboard", 89.99, quantity=1)
cart.add_item("Coffee", 4.99, quantity=5)
cart.apply_discount(10)
print(cart.get_summary())


# ============================================================
# 5. PEP 8 — Python's Style Guide Highlights
# ============================================================
print("\n" + "=" * 50)
print("5. PEP 8 STYLE GUIDE HIGHLIGHTS")
print("=" * 50)
print("""
PEP 8 is Python's official style guide. Here are the greatest hits:

NAMING:
  variables_and_functions  → snake_case (lowercase with underscores)
  ClassNames               → PascalCase (capitalize each word)
  CONSTANTS                → UPPER_SNAKE_CASE
  _protected_methods       → single leading underscore
  __private_methods        → double leading underscore
  __dunder_methods__       → double underscore both sides (magic methods)

SPACING:
  - 4 spaces per indent (never tabs!)
  - 2 blank lines between top-level functions/classes
  - 1 blank line between methods in a class
  - Spaces around operators: x = 1 + 2 (not x=1+2)
  - No space inside brackets: func(arg) (not func( arg ))

LINE LENGTH:
  - Max 79 characters (some teams use 88 or 100)
  - Use parentheses for line continuation:
    result = (first_value
              + second_value
              - third_value)

IMPORTS:
  - One import per line
  - Group: stdlib, then third-party, then local
  - import os        (not: import os, sys)
  - from os import path

COMPARISON:
  - Use 'is' for None:      if x is None:    (not: if x == None:)
  - Use 'is not':            if x is not None: (not: if not x is None:)
  - Don't compare booleans:  if flag:          (not: if flag == True:)
""")


# ============================================================
# 6. Good vs Bad Naming — Show, Don't Tell
# ============================================================
print("=" * 50)
print("6. GOOD VS BAD NAMING")
print("=" * 50)


# ---- BAD NAMES (what NOT to do) ----
def proc(d):
    """Process... something? With... some data? Who knows!"""
    r = []
    for i in d:
        if i > 0:
            r.append(i * 2)
    return r

# What does x, d, r, i mean? Nobody knows. Not even the person who wrote it
# at 3 AM will remember next week.


# ---- GOOD NAMES (self-documenting code) ----
def double_positive_numbers(numbers: list[float]) -> list[float]:
    """Double all positive numbers in the list."""
    doubled = []
    for number in numbers:
        if number > 0:
            doubled.append(number * 2)
    return doubled

# Now ANYONE can understand this code without comments!

# More examples:
# BAD:                      GOOD:
# d = {}                    user_scores = {}
# temp = get_data()         api_response = get_data()
# flag = True               is_authenticated = True
# lst = []                  pending_orders = []
# n = 42                    max_retry_count = 42
# def calc(a, b):           def calculate_tax(income, rate):
# def do_stuff():           def send_notification():
# class Mgr:                class AccountManager:

print(f"double_positive_numbers([-3, 0, 5, -1, 8]) = {double_positive_numbers([-3, 0, 5, -1, 8])}")
print("\nGood naming makes comments almost unnecessary!")


# ============================================================
# 7. Code Smells — Signs Your Code Needs Cleaning
# ============================================================
print("\n" + "=" * 50)
print("7. CODE SMELLS")
print("=" * 50)

print("""
"Code smell" = code that works but hints at deeper problems.
Like a weird smell in your fridge — technically the fridge works,
but something in there needs attention.

COMMON CODE SMELLS:

1. LONG FUNCTIONS (> 20-30 lines)
   Fix: Break into smaller functions, each doing one thing.

2. DEEP NESTING (if inside if inside if...)
   Fix: Use early returns, extract conditions into functions.

3. MAGIC NUMBERS
   Bad:  if score > 42:
   Good: PASSING_SCORE = 42
         if score > PASSING_SCORE:

4. REPEATED CODE (copy-paste)
   Fix: Extract into a function or loop.

5. GOD CLASSES (one class that does everything)
   Fix: Split into smaller, focused classes.

6. LONG PARAMETER LISTS (func(a, b, c, d, e, f, g))
   Fix: Use a dataclass or config object.

7. DEAD CODE (commented out blocks, unused imports)
   Fix: Delete it! Version control has your back.

8. UNCLEAR BOOLEAN EXPRESSIONS
   Bad:  if not (not is_valid or not has_access):
   Good: if is_valid and has_access:
""")


# ---- SMELL: Deep nesting ----
# BAD
def process_order_bad(order):
    if order:
        if order.get("items"):
            if order.get("customer"):
                if order["customer"].get("verified"):
                    return "Order processed!"
    return "Invalid order"

# GOOD — Use early returns to flatten the nesting
def process_order_good(order: Optional[dict]) -> str:
    if not order:
        return "Invalid order"
    if not order.get("items"):
        return "Invalid order"
    if not order.get("customer"):
        return "Invalid order"
    if not order["customer"].get("verified"):
        return "Invalid order"
    return "Order processed!"


# ---- SMELL: Magic numbers ----
# BAD
def calculate_shipping_bad(weight):
    if weight < 5:
        return weight * 2.50
    elif weight < 20:
        return weight * 4.00
    else:
        return weight * 6.50 + 15

# GOOD — Named constants explain the business logic
LIGHT_RATE: float = 2.50
MEDIUM_RATE: float = 4.00
HEAVY_RATE: float = 6.50
HEAVY_SURCHARGE: float = 15.00
LIGHT_LIMIT: float = 5.0
MEDIUM_LIMIT: float = 20.0

def calculate_shipping_good(weight: float) -> float:
    """Calculate shipping cost based on weight in pounds."""
    if weight < LIGHT_LIMIT:
        return weight * LIGHT_RATE
    elif weight < MEDIUM_LIMIT:
        return weight * MEDIUM_RATE
    else:
        return weight * HEAVY_RATE + HEAVY_SURCHARGE


# ============================================================
# 8. Black Formatter — Auto-Format Your Code
# ============================================================
print("=" * 50)
print("8. BLACK FORMATTER")
print("=" * 50)
print("""
Black is the "uncompromising" Python code formatter.
It formats your code so you never argue about style again.

Install:  pip install black
Use:      black my_file.py           (formats in place)
          black my_file.py --check   (check without changing)
          black my_file.py --diff    (show what would change)
          black .                    (format entire project!)

What Black does:
  - Consistent indentation
  - Proper spacing around operators
  - Line length: 88 characters (configurable)
  - Consistent string quotes (double quotes)
  - Trailing commas in multi-line structures

Before Black:
  result=my_function( 'arg1','arg2',key = value  )
  x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

After Black:
  result = my_function("arg1", "arg2", key=value)
  x = [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  ]

Tip: Set up Black to run automatically on save in your editor!
""")


# ============================================================
# 9. Putting It All Together — Clean Code Example
# ============================================================
print("=" * 50)
print("9. CLEAN CODE EXAMPLE")
print("=" * 50)

from dataclasses import dataclass
from typing import Optional


# Clean, well-typed, well-named code
@dataclass
class Product:
    """A product in our store."""
    name: str
    price: float
    category: str
    in_stock: bool = True


def apply_discount(price: float, discount_percent: float) -> float:
    """Apply a percentage discount to a price."""
    if not 0 <= discount_percent <= 100:
        raise ValueError(f"Invalid discount: {discount_percent}%")
    return round(price * (1 - discount_percent / 100), 2)


def find_cheapest(products: list[Product]) -> Optional[Product]:
    """Find the cheapest in-stock product, or None if no products."""
    in_stock = [p for p in products if p.in_stock]
    if not in_stock:
        return None
    return min(in_stock, key=lambda p: p.price)


def format_price(amount: float) -> str:
    """Format a price as a dollar string."""
    return f"${amount:,.2f}"


# Usage
products = [
    Product("Laptop", 999.99, "Electronics"),
    Product("Python Book", 39.99, "Books"),
    Product("Coffee Mug", 12.99, "Kitchen"),
    Product("Keyboard", 89.99, "Electronics"),
    Product("Vintage Vinyl", 24.99, "Music", in_stock=False),
]

cheapest = find_cheapest(products)
if cheapest:
    sale_price = apply_discount(cheapest.price, 20)
    print(f"Cheapest in-stock: {cheapest.name}")
    print(f"  Regular: {format_price(cheapest.price)}")
    print(f"  On sale: {format_price(sale_price)} (20% off!)")


# ============================================================
# Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 25 RECAP")
print("=" * 50)
print("""
Clean Code Cheat Sheet:
-----------------------------------------------------------------
TYPE HINTS:
  def func(name: str, age: int = 0) -> str:
  numbers: list[int] = [1, 2, 3]
  Optional[str] = str | None
  Union[int, str] = int | str

MYPY:
  pip install mypy
  mypy your_file.py    → static type checking

PEP 8 ESSENTIALS:
  snake_case           → variables, functions
  PascalCase           → classes
  UPPER_CASE           → constants
  4 spaces             → indentation
  79-88 chars          → line length

BLACK FORMATTER:
  pip install black
  black your_file.py   → auto-format

NAMING RULES:
  - Be descriptive (user_count, not n)
  - Be consistent (don't mix styles)
  - Functions should be verbs (calculate_tax, send_email)
  - Variables should be nouns (user_list, total_price)
  - Booleans should be questions (is_valid, has_access)

CODE SMELLS TO AVOID:
  - Long functions → break into smaller ones
  - Deep nesting → use early returns
  - Magic numbers → use named constants
  - Repeated code → extract into functions
  - God classes → split into focused classes
  - Dead code → delete it

GOLDEN RULE: Write code for the human who reads it next.
That human might be Future You, and they'll thank you.
-----------------------------------------------------------------
""")
