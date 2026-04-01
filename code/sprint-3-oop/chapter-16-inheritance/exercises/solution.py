"""
Chapter 16 Exercise SOLUTION: Vehicle Hierarchy
=================================================
From gas guzzlers to electric dreams — OOP on wheels!
"""


class Vehicle:
    """Base vehicle class — the ancestor of all things that go vroom (or hum)."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = 100    # percentage
        self.mileage = 0         # total miles driven

    def drive(self, miles):
        """Drive the vehicle. Uses ~1 fuel per 3 miles."""
        fuel_needed = miles / 3
        if fuel_needed > self.fuel_level:
            max_miles = int(self.fuel_level * 3)
            print(f"Not enough fuel! Can only drive {max_miles} miles.")
            print("Time to fuel up! ⛽")
            return

        self.fuel_level -= fuel_needed
        self.mileage += miles
        print(f"🚗 Drove {miles} miles! Fuel: {self.fuel_level:.0f}% | "
              f"Total mileage: {self.mileage}")

    def fuel_up(self):
        """Fill the tank back to 100."""
        self.fuel_level = 100
        print(f"⛽ {self.make} {self.model} fueled up! Tank is full.")

    def describe(self):
        """Print vehicle info."""
        print(f"\n{'=' * 40}")
        print(f"  {self.year} {self.make} {self.model}")
        print(f"  Fuel:    {self.fuel_level:.0f}%")
        print(f"  Mileage: {self.mileage} miles")


class Car(Vehicle):
    """A car is a vehicle with doors (and hopefully air conditioning)."""

    def __init__(self, make, model, year, num_doors=4):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def describe(self):
        """Override to include door count."""
        super().describe()
        print(f"  Doors:   {self.num_doors}")
        print(f"  Type:    Car")
        print(f"{'=' * 40}")


class ElectricCar(Car):
    """An electric car — the future is now, old man."""

    def __init__(self, make, model, year, battery_size=75, num_doors=4):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size   # kWh
        self.battery_charge = 100          # percentage
        # Electric cars don't use fuel
        self.fuel_level = None  # N/A — we run on electrons!

    def drive(self, miles):
        """Override: uses battery instead of fuel. More efficient!"""
        charge_needed = miles / 4  # EVs are more efficient
        if charge_needed > self.battery_charge:
            max_miles = int(self.battery_charge * 4)
            print(f"Not enough charge! Can only drive {max_miles} miles.")
            print("Find a charging station! 🔌")
            return

        self.battery_charge -= charge_needed
        self.mileage += miles
        print(f"⚡ Silently glided {miles} miles! Battery: {self.battery_charge:.0f}% | "
              f"Total mileage: {self.mileage}")

    def charge(self):
        """Charge the battery to 100%."""
        self.battery_charge = 100
        print(f"🔋 {self.make} {self.model} fully charged! Ready to roll.")

    def fuel_up(self):
        """Electric cars don't use gas!"""
        print(f"This is an electric car! Use .charge() instead of .fuel_up()")
        print(f"No gas station needed — just find an outlet! 🔌")

    def describe(self):
        """Override to show battery info instead of fuel."""
        print(f"\n{'=' * 40}")
        print(f"  {self.year} {self.make} {self.model}")
        print(f"  Battery: {self.battery_size} kWh")
        print(f"  Charge:  {self.battery_charge:.0f}%")
        print(f"  Mileage: {self.mileage} miles")
        print(f"  Doors:   {self.num_doors}")
        print(f"  Type:    Electric Car ⚡")
        print(f"{'=' * 40}")


class Motorcycle(Vehicle):
    """Two wheels, one life. Born to ride. 🏍️"""

    STYLES = ["sport", "cruiser", "touring", "dirt", "cafe racer"]

    def __init__(self, make, model, year, style="sport"):
        super().__init__(make, model, year)
        if style.lower() not in Motorcycle.STYLES:
            print(f"Unknown style '{style}'. Defaulting to 'sport'.")
            style = "sport"
        self.style = style.lower()

    def drive(self, miles):
        """Override: motorcycles are more fuel efficient."""
        fuel_needed = miles / 5  # bikes sip fuel
        if fuel_needed > self.fuel_level:
            max_miles = int(self.fuel_level * 5)
            print(f"Not enough fuel! Can only ride {max_miles} miles.")
            return

        self.fuel_level -= fuel_needed
        self.mileage += miles
        print(f"🏍️ Rode {miles} miles! Fuel: {self.fuel_level:.0f}% | "
              f"Total mileage: {self.mileage}")

    def wheelie(self):
        """Pop a wheelie! Because we live on the edge."""
        if self.fuel_level < 5:
            print("Can't wheelie on an empty tank. Safety first... ish.")
        else:
            self.fuel_level -= 5
            print(f"🏍️ {self.make} {self.model} pops a SICK wheelie! 🤘")
            print("  (Don't try this in real life, kids)")

    def describe(self):
        """Override to include style."""
        super().describe()
        print(f"  Style:   {self.style}")
        print(f"  Type:    Motorcycle 🏍️")
        print(f"{'=' * 40}")


# ============================================================
# Test Drive!
# ============================================================
print("🏁 VEHICLE HIERARCHY TEST DRIVE 🏁")
print("=" * 50)

# Create vehicles
camry = Car("Toyota", "Camry", 2023, num_doors=4)
tesla = ElectricCar("Tesla", "Model 3", 2024, battery_size=82)
harley = Motorcycle("Harley-Davidson", "Iron 883", 2023, style="cruiser")

# Describe all vehicles
camry.describe()
tesla.describe()
harley.describe()

# Drive them around
print("\n--- Road Trip! ---")
camry.drive(100)
tesla.drive(100)
harley.drive(100)

# More driving to drain fuel/battery
print("\n--- Keep going... ---")
camry.drive(150)
tesla.drive(200)
harley.drive(250)

# Refuel/recharge
print("\n--- Pit Stop ---")
camry.fuel_up()
tesla.charge()
tesla.fuel_up()  # oops! wrong method for EV
harley.fuel_up()

# Motorcycle-specific fun
print("\n--- Show Off Time ---")
harley.wheelie()

# Type checking with isinstance()
print("\n--- isinstance() Checks ---")
print(f"Is tesla a Car?         {isinstance(tesla, Car)}")          # True
print(f"Is tesla a Vehicle?     {isinstance(tesla, Vehicle)}")      # True
print(f"Is tesla an ElectricCar? {isinstance(tesla, ElectricCar)}") # True
print(f"Is harley a Car?        {isinstance(harley, Car)}")         # False
print(f"Is harley a Vehicle?    {isinstance(harley, Vehicle)}")     # True
print(f"Is camry a Motorcycle?  {isinstance(camry, Motorcycle)}")   # False

# Final status
print("\n--- Final Status ---")
camry.describe()
tesla.describe()
harley.describe()
