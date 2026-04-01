"""
Chapter 17 Exercise SOLUTION: Money Class with Magic Methods
=============================================================
Making cents (and dollars) of magic methods. 💰
"""


class Money:
    """
    A money class that handles arithmetic like a pro.
    Because money math should be as easy as 1 + 1 = 2.
    """

    # Currency symbols for pretty display
    SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "INR": "₹"}

    def __init__(self, amount, currency="USD"):
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def _check_compatible(self, other):
        """Helper: ensure the other object is Money with the same currency."""
        if not isinstance(other, Money):
            return False
        if self.currency != other.currency:
            raise ValueError(
                f"Cannot operate on {self.currency} and {other.currency}. "
                f"Currency exchange not supported (yet — maybe in Chapter 21 with APIs!)."
            )
        return True

    def __str__(self):
        """Human-friendly display: '$50.00 USD'"""
        symbol = self.SYMBOLS.get(self.currency, "")
        return f"{symbol}{self.amount:.2f} {self.currency}"

    def __repr__(self):
        """Developer display: Money(50.00, 'USD')"""
        return f"Money({self.amount:.2f}, '{self.currency}')"

    def __add__(self, other):
        """Money + Money = Money. Also handles Money + number."""
        if isinstance(other, (int, float)):
            # Treat raw numbers as same currency
            return Money(self.amount + other, self.currency)
        if self._check_compatible(other):
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def __radd__(self, other):
        """Handles: number + Money (reverse add)"""
        return self.__add__(other)

    def __sub__(self, other):
        """Money - Money = Money. Debt is a thing, so negatives are fine."""
        if isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        if self._check_compatible(other):
            return Money(self.amount - other.amount, self.currency)
        return NotImplemented

    def __mul__(self, multiplier):
        """Money * number = Money. Great for tips and taxes!"""
        if isinstance(multiplier, (int, float)):
            return Money(self.amount * multiplier, self.currency)
        return NotImplemented

    def __rmul__(self, multiplier):
        """Handles: number * Money"""
        return self.__mul__(multiplier)

    def __eq__(self, other):
        """Money == Money (same amount AND same currency)."""
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __lt__(self, other):
        """Money < Money (must be same currency)."""
        if self._check_compatible(other):
            return self.amount < other.amount
        return NotImplemented

    def __le__(self, other):
        """Money <= Money."""
        if self._check_compatible(other):
            return self.amount <= other.amount
        return NotImplemented

    def __gt__(self, other):
        """Money > Money."""
        if self._check_compatible(other):
            return self.amount > other.amount
        return NotImplemented

    def __ge__(self, other):
        """Money >= Money."""
        if self._check_compatible(other):
            return self.amount >= other.amount
        return NotImplemented

    def __bool__(self):
        """bool(Money(0)) is False, bool(Money(10)) is True."""
        return self.amount != 0

    def __neg__(self):
        """Unary minus: -Money(50) = Money(-50)"""
        return Money(-self.amount, self.currency)

    def __abs__(self):
        """abs(Money(-50)) = Money(50)"""
        return Money(abs(self.amount), self.currency)


# ============================================================
# Test Drive!
# ============================================================
print("💰 MONEY CLASS TEST DRIVE 💰")
print("=" * 50)

# Create money objects
wallet = Money(50)
piggy_bank = Money(23.50)
euros = Money(100, "EUR")
pounds = Money(75.99, "GBP")
yen = Money(5000, "JPY")
rupees = Money(2500, "INR")

# Test __str__ and __repr__
print("\n--- String Representations ---")
for m in [wallet, piggy_bank, euros, pounds, yen, rupees]:
    print(f"  str:  {m}")
    print(f"  repr: {repr(m)}")
    print()

# Test arithmetic
print("--- Arithmetic ---")
total = wallet + piggy_bank
print(f"{wallet} + {piggy_bank} = {total}")

change = wallet - Money(12.75)
print(f"{wallet} - $12.75 = {change}")

tip = Money(45.00) * 0.20
print(f"20% tip on $45.00 = {tip}")

# Money + number
print(f"{wallet} + 10 = {wallet + 10}")
print(f"5 * {piggy_bank} = {5 * piggy_bank}")

# Test comparisons
print("\n--- Comparisons ---")
a = Money(50)
b = Money(30)
c = Money(50)

print(f"{a} == {c}? {a == c}")     # True
print(f"{a} == {b}? {a == b}")     # False
print(f"{a} > {b}?  {a > b}")     # True
print(f"{b} < {a}?  {b < a}")     # True
print(f"{a} <= {c}? {a <= c}")    # True

# Test bool
print("\n--- Bool ---")
empty_wallet = Money(0)
full_wallet = Money(100)
print(f"bool({empty_wallet}): {bool(empty_wallet)}")  # False
print(f"bool({full_wallet}): {bool(full_wallet)}")    # True

# Using in if statements
if full_wallet:
    print("You've got money! Let's go shopping!")
if not empty_wallet:
    print("Wallet's empty. Time to check the couch cushions.")

# Test unary operators
print("\n--- Unary Operators ---")
debt = -Money(500)
print(f"Debt: {debt}")
print(f"Absolute value: {abs(debt)}")

# Test currency mismatch errors
print("\n--- Currency Mismatch Handling ---")
try:
    result = wallet + euros  # USD + EUR = Error!
except ValueError as e:
    print(f"Error caught: {e}")

try:
    wallet < pounds  # Can't compare different currencies
except ValueError as e:
    print(f"Error caught: {e}")

# Sorting works because we defined comparison methods!
print("\n--- Sorting (works because of __lt__!) ---")
prices = [Money(99.99), Money(12.50), Money(45.00), Money(7.99), Money(150.00)]
sorted_prices = sorted(prices)
print("Sorted prices:")
for p in sorted_prices:
    print(f"  {p}")

# Shopping cart example
print("\n--- Shopping Cart ---")
items = {
    "Python Book": Money(39.99),
    "Mechanical Keyboard": Money(89.99),
    "Coffee (lots)": Money(24.50),
    "Rubber Duck (debugging)": Money(4.99),
}

print("Shopping Cart:")
for item, price in items.items():
    print(f"  {item}: {price}")

subtotal = Money(0)
for price in items.values():
    subtotal = subtotal + price

tax = subtotal * 0.08
total = subtotal + tax

print(f"\n  Subtotal: {subtotal}")
print(f"  Tax (8%): {tax}")
print(f"  Total:    {total}")
print(f"\n  That rubber duck is the best investment on this list. Trust me. 🦆")
