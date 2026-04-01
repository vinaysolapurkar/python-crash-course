"""
Chapter 18 Exercise SOLUTION: Refactor Vehicles with Composition
================================================================
Same Vehicle class, different power sources — that's the beauty of composition!
"""


class Engine:
    """A gasoline/diesel engine. Old school but reliable."""

    def __init__(self, horsepower, fuel_type="gasoline"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.fuel_level = 100
        self.running = False

    def start(self):
        """Start the engine. VROOM!"""
        self.running = True
        print(f"  🔥 {self.horsepower}hp {self.fuel_type} engine roars to life!")

    def stop(self):
        self.running = False
        print(f"  Engine stopped.")

    def consume(self, amount):
        """Use fuel for driving. Returns True if enough fuel."""
        if self.fuel_level >= amount:
            self.fuel_level -= amount
            return True
        else:
            print(f"  Not enough fuel! (have {self.fuel_level:.0f}%, need {amount:.0f}%)")
            return False

    def replenish(self):
        """Fill the tank."""
        self.fuel_level = 100
        print(f"  ⛽ Tank filled! Fuel: 100%")

    def status(self):
        """Return a status string."""
        state = "running" if self.running else "off"
        return f"{self.horsepower}hp {self.fuel_type} ({state}) | Fuel: {self.fuel_level:.0f}%"


class Battery:
    """An electric battery. Silent, clean, and full of electrons."""

    def __init__(self, capacity_kwh=75):
        self.capacity_kwh = capacity_kwh
        self.charge_level = 100
        self.running = False

    def start(self):
        """Start the electric motor. Barely a whisper."""
        self.running = True
        print(f"  ⚡ {self.capacity_kwh}kWh electric motor hums to life (silently)!")

    def stop(self):
        self.running = False
        print(f"  Electric motor stopped.")

    def consume(self, amount):
        """Use battery charge. Returns True if enough charge."""
        if self.charge_level >= amount:
            self.charge_level -= amount
            return True
        else:
            print(f"  Not enough charge! (have {self.charge_level:.0f}%, need {amount:.0f}%)")
            return False

    def replenish(self):
        """Charge to 100%."""
        self.charge_level = 100
        print(f"  🔋 Fully charged! Charge: 100%")

    def status(self):
        """Return a status string."""
        state = "running" if self.running else "off"
        return f"{self.capacity_kwh}kWh battery ({state}) | Charge: {self.charge_level:.0f}%"


class HybridPowerSource:
    """
    BONUS: Hybrid power — uses battery first, then switches to gas.
    This COMPOSES an Engine and Battery together. Composition inception!
    """

    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        self.running = False
        self.using_electric = True  # start on electric

    def start(self):
        self.running = True
        if self.battery.charge_level > 0:
            self.battery.start()
            self.using_electric = True
            print(f"  Starting in electric mode.")
        else:
            self.engine.start()
            self.using_electric = False
            print(f"  Starting in gas mode.")

    def stop(self):
        self.running = False
        if self.using_electric:
            self.battery.stop()
        else:
            self.engine.stop()

    def consume(self, amount):
        """Try battery first, then fall back to engine."""
        if self.using_electric and self.battery.charge_level > 0:
            if self.battery.consume(amount):
                return True
            # Battery ran out, switch to gas
            print(f"  Switching to gas mode...")
            self.using_electric = False

        if not self.using_electric:
            return self.engine.consume(amount)
        return False

    def replenish(self):
        """Refuel AND recharge — best of both worlds."""
        self.engine.replenish()
        self.battery.replenish()
        self.using_electric = True
        print(f"  Hybrid: refueled AND recharged!")

    def status(self):
        mode = "electric" if self.using_electric else "gas"
        return (f"HYBRID ({mode} mode) | "
                f"Battery: {self.battery.charge_level:.0f}% | "
                f"Fuel: {self.engine.fuel_level:.0f}%")


class GPS:
    """Navigation component."""

    def __init__(self):
        self.destination = None

    def navigate(self, destination):
        self.destination = destination
        print(f"  📍 GPS: Navigating to {destination}")

    def status(self):
        if self.destination:
            return f"Navigating to {self.destination}"
        return "Idle"


class SoundSystem:
    """Entertainment component."""

    def __init__(self, brand="Generic"):
        self.brand = brand

    def play(self, song):
        print(f"  🎵 {self.brand}: Now playing '{song}'")


class Vehicle:
    """
    A vehicle COMPOSED of parts.
    Same class works for gas, electric, AND hybrid!
    The Vehicle doesn't know or care what type of power source it has.
    It just calls .consume(), .replenish(), .start() — polymorphism!
    """

    def __init__(self, make, model, year, power_source, gps=None, sound=None):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

        # Composition: Vehicle HAS these components
        self.power_source = power_source
        self.gps = gps or GPS()
        self.sound = sound or SoundSystem()

    def start(self):
        """Start the vehicle (delegates to power source)."""
        print(f"\n{self.year} {self.make} {self.model} starting:")
        self.power_source.start()

    def drive(self, miles):
        """Drive some miles. Delegates energy use to power source."""
        if not self.power_source.running:
            print("Start the vehicle first!")
            return

        # Energy consumption: roughly 1 unit per 3 miles
        energy_needed = miles / 3
        if self.power_source.consume(energy_needed):
            self.mileage += miles
            print(f"  Drove {miles} miles! Total: {self.mileage} miles")
        else:
            print(f"  Can't drive {miles} miles. Need to refuel/recharge!")

    def drive_to(self, destination, miles):
        """Drive to a destination with GPS."""
        self.gps.navigate(destination)
        self.drive(miles)

    def refuel_or_recharge(self):
        """One method that works regardless of power source type!"""
        print(f"\n{self.make} {self.model} pit stop:")
        self.power_source.replenish()

    def road_trip(self, destination, miles, song):
        """The full road trip experience."""
        self.start()
        self.gps.navigate(destination)
        self.sound.play(song)
        self.drive(miles)

    def describe(self):
        """Show vehicle info and component status."""
        print(f"\n{'=' * 45}")
        print(f"  {self.year} {self.make} {self.model}")
        print(f"  Mileage: {self.mileage} miles")
        print(f"  Power:   {self.power_source.status()}")
        print(f"  GPS:     {self.gps.status()}")
        print(f"  Sound:   {self.sound.brand}")
        print(f"{'=' * 45}")


# ============================================================
# Test Drive!
# ============================================================
print("🏁 COMPOSITION VEHICLE TEST 🏁")
print("=" * 50)

# --- Gas Car ---
print("\n--- Gas Car ---")
civic = Vehicle(
    "Honda", "Civic", 2024,
    power_source=Engine(180, "gasoline"),
    sound=SoundSystem("Pioneer"),
)
civic.start()
civic.drive(60)
civic.drive(120)
civic.describe()

# --- Electric Car (same Vehicle class!) ---
print("\n--- Electric Car ---")
tesla = Vehicle(
    "Tesla", "Model 3", 2024,
    power_source=Battery(82),
    sound=SoundSystem("Tesla Premium"),
)
tesla.start()
tesla.drive(80)
tesla.drive(150)
tesla.describe()

# --- Hybrid Car (same Vehicle class again!) ---
print("\n--- Hybrid Car ---")
prius = Vehicle(
    "Toyota", "Prius", 2024,
    power_source=HybridPowerSource(
        engine=Engine(120, "gasoline"),
        battery=Battery(8),  # small battery for hybrid
    ),
    sound=SoundSystem("JBL"),
)
prius.start()
prius.drive(20)   # uses battery
prius.drive(100)  # battery runs out, switches to gas
prius.describe()

# Refuel/recharge — same method for all vehicles!
print("\n--- Pit Stop for Everyone ---")
civic.refuel_or_recharge()
tesla.refuel_or_recharge()
prius.refuel_or_recharge()

# Road trip!
print("\n--- Road Trip! ---")
tesla.road_trip("San Francisco", 50, "Hotel California - Eagles")

# Show that swapping components is easy
print("\n--- Engine Swap (Easy with Composition!) ---")
print("Upgrading Civic's engine...")
civic.power_source = Engine(300, "turbocharged")
civic.describe()
civic.start()
civic.drive(50)

print("""
\n--- Why This Is Better ---

With INHERITANCE, we needed separate classes:
  Vehicle → Car → ElectricCar → HybridCar
  Each with duplicated/overridden drive(), fuel_up(), etc.

With COMPOSITION, we have:
  ONE Vehicle class + swappable components (Engine, Battery, Hybrid)
  Adding a hydrogen fuel cell? Just make a new power source class!
  No Vehicle code needs to change. Open/Closed principle in action!
""")
