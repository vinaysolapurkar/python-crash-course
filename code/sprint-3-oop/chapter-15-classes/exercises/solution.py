"""
Chapter 15 Exercise SOLUTION: Build a Dog Class
=================================================
Every dog has its day — and today is that day in Python!
"""


class Dog:
    """Man's best friend, now in Python form."""

    # Class attribute — shared by all dogs
    total_dogs = 0

    # Breeds we'll consider "small" for bark purposes
    SMALL_BREEDS = ["chihuahua", "pomeranian", "yorkshire terrier",
                    "dachshund", "shih tzu", "pug", "maltese"]

    def __init__(self, name, breed, age):
        """Initialize a new dog. Who's a good boy/girl?"""
        self.name = name
        self.breed = breed
        self.age = age
        self.tricks = []        # every dog starts with no tricks (yet!)
        self.energy = 100       # bonus: energy level

        Dog.total_dogs += 1
        print(f"🐕 Welcome to the world, {self.name}!")

    def bark(self):
        """
        Make the dog bark!
        Small breeds yip, big breeds WOOF, puppies do tiny barks.
        """
        if self.age < 1:
            # Puppies are adorable
            print(f"{self.name}: *tiny squeaky bark* arf! arf!")
        elif self.breed.lower() in Dog.SMALL_BREEDS:
            # Small dogs have BIG attitudes
            print(f"{self.name}: YIP YIP YIP! *spins in circles* YIP!")
        else:
            # Big dogs bring the thunder
            print(f"{self.name}: WOOF! WOOF WOOF! *deep intimidating bark*")

    def birthday(self):
        """It's the dog's birthday! 🎂"""
        self.age += 1
        human_age_approx = self.age * 7  # the classic (if inaccurate) formula
        print(f"🎂 Happy Birthday, {self.name}! Now {self.age} years old!")
        print(f"   (That's roughly {human_age_approx} in 'dog years')")

    def describe(self):
        """Print a summary of this good boy/girl."""
        print(f"\n{'=' * 35}")
        print(f"  Name:   {self.name}")
        print(f"  Breed:  {self.breed}")
        print(f"  Age:    {self.age} year(s)")
        print(f"  Tricks: {len(self.tricks)} learned")
        print(f"  Energy: {'🟢' * (self.energy // 20)}{'⚪' * (5 - self.energy // 20)}")
        print(f"{'=' * 35}")

    def sit(self):
        """Tell the dog to sit. Results may vary based on breed."""
        if self.breed.lower() == "chihuahua":
            # Chihuahuas answer to no one
            print(f"{self.name} stares at you defiantly. Sitting is for amateurs.")
        elif self.energy < 20:
            print(f"{self.name} is already lying down. Too tired to sit formally.")
        else:
            print(f"{self.name} sits like a perfect angel. Good dog! 🦮")

    def learn_trick(self, trick):
        """Teach the dog a new trick!"""
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} already knows '{trick}'! Try something new!")
        else:
            self.tricks.append(trick)
            print(f"🎓 {self.name} learned '{trick}'! What a smart pupper!")

    def show_tricks(self):
        """Show off all learned tricks."""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
            print("But that's okay — they're still a good dog!")
        else:
            print(f"\n{self.name}'s Trick Repertoire:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"  {i}. {trick}")
            print(f"Total tricks: {len(self.tricks)} — Impressive!")

    def play(self):
        """Play with the dog! Uses some energy."""
        if self.energy >= 20:
            self.energy -= 20
            print(f"🎾 {self.name} plays fetch! Energy: {self.energy}%")
        else:
            print(f"{self.name} yawns... needs a nap first. 😴")

    def nap(self):
        """Let the dog take a nap to restore energy."""
        self.energy = min(100, self.energy + 50)
        print(f"💤 {self.name} takes a nap... Energy restored to {self.energy}%")


# ============================================================
# Testing our Dog class!
# ============================================================
print("🐾 DOG CLASS DEMO 🐾")
print("=" * 50)

# Create some dogs
rex = Dog("Rex", "German Shepherd", 5)
bella = Dog("Bella", "Chihuahua", 3)
puppy = Dog("Biscuit", "Golden Retriever", 0)

# Describe them all
rex.describe()
bella.describe()
puppy.describe()

# Different barks for different dogs
print("\n--- Bark Contest! ---")
rex.bark()      # Big dog bark
bella.bark()    # Small dog yip
puppy.bark()    # Puppy bark

# Birthday time!
print("\n--- Birthday Party! ---")
puppy.birthday()   # Biscuit turns 1!

# Sit!
print("\n--- Obedience Test ---")
rex.sit()       # Good boy
bella.sit()     # Chihuahua attitude

# Learn tricks
print("\n--- Trick School ---")
rex.learn_trick("shake")
rex.learn_trick("roll over")
rex.learn_trick("play dead")
rex.learn_trick("shake")  # already knows this!
rex.show_tricks()

bella.show_tricks()  # no tricks yet (she's independent)

# Play time!
print("\n--- Play Time! ---")
rex.play()
rex.play()
rex.play()
rex.play()
rex.play()   # getting tired!
rex.play()   # too tired!
rex.nap()    # ahh, refreshed

# Total dogs
print(f"\n🐕 Total dogs created: {Dog.total_dogs}")
