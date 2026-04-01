"""
Chapter 18 Exercise: Refactor Vehicles with Composition
========================================================

In Chapter 16, we built a vehicle hierarchy with inheritance:
  Vehicle → Car → ElectricCar

Now refactor it to use COMPOSITION instead!

The idea: Instead of ElectricCar INHERITING fuel behavior and overriding it,
we give vehicles COMPONENTS that handle propulsion.

Requirements:

1. Create an Engine class:
   - Attributes: horsepower, fuel_type, fuel_level (starts at 100)
   - Methods: start(), use_fuel(amount), refuel(), status()

2. Create a Battery class:
   - Attributes: capacity_kwh, charge_level (starts at 100)
   - Methods: start(), use_charge(amount), recharge(), status()

3. Refactor the Vehicle class to use composition:
   - Vehicle HAS a power_source (Engine or Battery)
   - Vehicle HAS optional features (GPS, sound system, etc.)
   - drive() delegates to the power source
   - The Vehicle doesn't care if it's gas or electric!

4. Test it: Create a gas car and electric car using the SAME Vehicle class,
   just with different power sources.

Bonus:
   - Create a HybridPowerSource that has BOTH an Engine and Battery
   - The hybrid uses battery first, then switches to gas

Starter code below:
"""


class Engine:
    """A gasoline/diesel engine. Old school but reliable."""

    def __init__(self, horsepower, fuel_type="gasoline"):
        # TODO: Set attributes
        pass

    def start(self):
        """Start the engine."""
        # TODO: Print a starting message
        pass

    def use_fuel(self, amount):
        """Use fuel for driving. Returns True if enough fuel."""
        # TODO: Check fuel, reduce it, return True/False
        pass

    def refuel(self):
        """Fill the tank."""
        # TODO: Set fuel_level to 100
        pass

    def status(self):
        """Return a status string."""
        # TODO: Return something like "180hp gasoline | Fuel: 85%"
        pass


class Battery:
    """An electric battery. Silent and clean."""

    def __init__(self, capacity_kwh=75):
        # TODO: Set attributes
        pass

    def start(self):
        """Start the electric motor."""
        # TODO: Print a starting message
        pass

    def use_charge(self, amount):
        """Use battery charge. Returns True if enough charge."""
        # TODO: Check charge, reduce it, return True/False
        pass

    def recharge(self):
        """Charge to 100%."""
        # TODO: Set charge_level to 100
        pass

    def status(self):
        """Return a status string."""
        # TODO: Return something like "75kWh battery | Charge: 90%"
        pass


class Vehicle:
    """
    A vehicle COMPOSED of parts.
    The same class works for gas AND electric cars!
    """

    def __init__(self, make, model, year, power_source):
        # TODO: Set attributes, including the power_source component
        pass

    def start(self):
        """Delegate to the power source."""
        # TODO: Call power_source.start()
        pass

    def drive(self, miles):
        """Drive some miles. Delegate fuel/charge usage to power source."""
        # TODO: Calculate energy needed and delegate to power source
        # Hint: Use hasattr() to check if it's use_fuel or use_charge
        pass

    def refuel_or_recharge(self):
        """Refuel or recharge based on power source type."""
        # TODO: Check what type of power source and call appropriate method
        pass

    def describe(self):
        """Show vehicle info."""
        # TODO: Print make, model, year, and power source status
        pass


# ----- Test your composition! -----

# TODO: Create a gas car
# gas_engine = Engine(180, "gasoline")
# civic = Vehicle("Honda", "Civic", 2024, gas_engine)

# TODO: Create an electric car (same Vehicle class, different power source!)
# battery = Battery(82)
# tesla = Vehicle("Tesla", "Model 3", 2024, battery)

# TODO: Test both — they should work the same way!
# civic.start()
# civic.drive(100)
# civic.describe()

# tesla.start()
# tesla.drive(100)
# tesla.describe()

# BONUS: Create a HybridPowerSource class and test it!
