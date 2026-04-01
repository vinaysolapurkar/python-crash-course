"""
Chapter 17 Exercise: Money Class with Magic Methods
=====================================================

Build a Money class that makes financial calculations feel natural.

Requirements:

1. Money class with:
   - amount (float) and currency (string, default "USD")

2. Magic methods to implement:
   - __str__   → "$50.00 USD" (nice display)
   - __repr__  → "Money(50.00, 'USD')" (developer view)
   - __add__   → Money(10) + Money(20) = Money(30)
   - __sub__   → Money(50) - Money(20) = Money(30)
   - __eq__    → Money(10) == Money(10) is True
   - __lt__    → Money(10) < Money(20) is True
   - __le__    → Money(10) <= Money(10) is True
   - __bool__  → bool(Money(0)) is False, bool(Money(10)) is True

3. Rules:
   - Adding/subtracting different currencies should raise ValueError
   - Negative amounts should be allowed (debt is real!)
   - Amount should be rounded to 2 decimal places

Bonus:
   - __mul__   → Money(10) * 3 = Money(30) (multiply by a number)
   - Handle adding Money + int/float (treat as same currency)

Starter code below:
"""


class Money:
    """
    A money class that handles arithmetic like a pro.
    Because money math should be as easy as 1 + 1 = 2.
    """

    # Currency symbols for display
    SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "INR": "₹"}

    def __init__(self, amount, currency="USD"):
        # TODO: Store amount (rounded to 2 decimals) and currency (uppercase)
        pass

    def __str__(self):
        """Human-friendly display: '$50.00 USD'"""
        # TODO: Use the SYMBOLS dict for the currency symbol
        # Hint: self.SYMBOLS.get(self.currency, "") for the symbol
        pass

    def __repr__(self):
        """Developer display: Money(50.00, 'USD')"""
        # TODO: Return a string that looks like code to recreate this object
        pass

    def __add__(self, other):
        """Money + Money = Money (same currency only!)"""
        # TODO: Check if other is Money, check currencies match
        # TODO: Return new Money with combined amounts
        # Hint: raise ValueError if currencies don't match
        pass

    def __sub__(self, other):
        """Money - Money = Money"""
        # TODO: Similar to __add__ but subtract
        pass

    def __eq__(self, other):
        """Money == Money (same amount AND currency)"""
        # TODO: Compare amount and currency
        pass

    def __lt__(self, other):
        """Money < Money (must be same currency!)"""
        # TODO: Compare amounts, check currencies match
        pass

    def __le__(self, other):
        """Money <= Money"""
        # TODO: Use __lt__ and __eq__
        pass

    def __bool__(self):
        """bool(Money(0)) should be False"""
        # TODO: Return True if amount is not zero
        pass

    def __mul__(self, multiplier):
        """Money * number = Money (for tips, taxes, etc.)"""
        # TODO: Multiply amount by a number
        pass


# ----- Test your Money class below! -----

# TODO: Create some money objects
# wallet = Money(50)
# piggy_bank = Money(23.50)
# euros = Money(100, "EUR")

# TODO: Test string representations
# print(wallet)        # $50.00 USD
# print(repr(wallet))  # Money(50.00, 'USD')

# TODO: Test arithmetic
# total = wallet + piggy_bank
# print(f"Total: {total}")

# TODO: Test comparison
# print(f"wallet > piggy_bank? {wallet > piggy_bank}")  # uses __lt__ reversed

# TODO: Test error handling
# try:
#     wallet + euros  # should raise ValueError!
# except ValueError as e:
#     print(f"Error: {e}")

# TODO: Test bool
# print(f"bool(Money(0)): {bool(Money(0))}")
# print(f"bool(Money(10)): {bool(Money(10))}")
