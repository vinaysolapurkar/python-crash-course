"""
Chapter 16 Exercise: Vehicle Hierarchy
=======================================

Build a vehicle inheritance hierarchy:

  Vehicle (base class)
    |
    +-- Car
    |     |
    |     +-- ElectricCar
    |
    +-- Motorcycle

Requirements:

1. Vehicle (parent class):
   - Attributes: make, model, year, fuel_level (starts at 100), mileage (starts at 0)
   - Methods:
     - drive(miles) — reduces fuel, increases mileage, prints status
     - fuel_up() — fills fuel back to 100
     - describe() — prints vehicle info

2. Car (inherits Vehicle):
   - Additional attribute: num_doors (default 4)
   - Override describe() to include door count

3. ElectricCar (inherits Car):
   - Replace fuel_level with battery_charge (starts at 100)
   - Override drive() — uses battery instead of fuel
   - Add charge() method instead of fuel_up()
   - Override describe() to show battery info

4. Motorcycle (inherits Vehicle):
   - Additional attribute: style ("sport", "cruiser", "touring")
   - Override drive() — motorcycles use less fuel per mile
   - Add wheelie() method (just for fun!)

Starter code below:
"""


class Vehicle:
    """Base vehicle class."""

    def __init__(self, make, model, year):
        # TODO: Set attributes (make, model, year, fuel_level=100, mileage=0)
        pass

    def drive(self, miles):
        """Drive the vehicle. Uses ~1 fuel per 3 miles."""
        # TODO: Check if enough fuel, reduce fuel, increase mileage
        # Hint: fuel_used = miles / 3
        pass

    def fuel_up(self):
        """Fill the tank back to 100."""
        # TODO: Set fuel_level to 100, print message
        pass

    def describe(self):
        """Print vehicle info."""
        # TODO: Print make, model, year, fuel, mileage
        pass


class Car(Vehicle):
    """A car is a vehicle with doors."""

    def __init__(self, make, model, year, num_doors=4):
        # TODO: Call super().__init__() and set num_doors
        pass

    def describe(self):
        """Override to include door count."""
        # TODO: Call super().describe() then print door info
        pass


class ElectricCar(Car):
    """An electric car — no gas, just electrons!"""

    def __init__(self, make, model, year, battery_size=75):
        # TODO: Call super().__init__() and set battery_size, battery_charge
        pass

    def drive(self, miles):
        """Override: uses battery instead of fuel."""
        # TODO: Check battery, reduce charge, increase mileage
        # Hint: charge_used = miles / 4
        pass

    def charge(self):
        """Charge the battery to 100%."""
        # TODO: Set battery_charge to 100
        pass

    def describe(self):
        """Override to show battery info instead of fuel."""
        # TODO: Print all info including battery
        pass


class Motorcycle(Vehicle):
    """Two wheels, one life. 🏍️"""

    def __init__(self, make, model, year, style="sport"):
        # TODO: Call super().__init__() and set style
        pass

    def drive(self, miles):
        """Override: motorcycles are more fuel efficient."""
        # TODO: Same as Vehicle but use less fuel (miles / 5)
        pass

    def wheelie(self):
        """Pop a wheelie! Because why not."""
        # TODO: Print a fun wheelie message
        pass

    def describe(self):
        """Override to include style."""
        # TODO: Call super().describe() and print style
        pass


# ----- Test your vehicle hierarchy! -----

# TODO: Create one of each vehicle type and test their methods

# car = Car(???)
# electric = ElectricCar(???)
# bike = Motorcycle(???)

# Test driving, refueling/charging, describe, etc.

# Bonus: Use isinstance() to check types
# print(isinstance(electric, Car))      # Should be True
# print(isinstance(electric, Vehicle))  # Should be True
# print(isinstance(bike, Car))          # Should be False
