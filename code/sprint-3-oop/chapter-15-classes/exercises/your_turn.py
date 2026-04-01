"""
Chapter 15 Exercise: Build a Dog Class
=======================================

Your mission: Create a Dog class that would make any dog lover proud.

Requirements:
  1. Create a Dog class with these attributes:
     - name (string) — the dog's name
     - breed (string) — what kind of pupper
     - age (int) — how old in dog years... I mean human years

  2. Add these methods:
     - bark() — prints a bark message (small dogs yip, big dogs WOOF!)
       Hint: maybe use breed to determine the bark style?
     - birthday() — increases age by 1 and prints a birthday message
     - describe() — prints a nice summary of the dog
     - sit() — prints a message about the dog sitting (or refusing to!)

  3. Create at least 3 different Dog objects and test all methods

Bonus:
  - Add a 'tricks' list attribute and a learn_trick(trick) method
  - Add a class attribute to count total dogs created
  - Make the bark sound different based on something (age? breed? mood?)

Starter code below — fill in the blanks!
"""


class Dog:
    """Man's best friend, now in Python form."""

    # TODO: Add a class attribute to count total dogs
    # total_dogs = ???

    def __init__(self, name, breed, age):
        """Initialize a new dog. Who's a good boy/girl?"""
        # TODO: Set instance attributes for name, breed, age
        # TODO: Initialize a tricks list (empty)
        # TODO: Increment the total_dogs counter
        pass

    def bark(self):
        """
        Make the dog bark!
        Bonus: Make small breeds yip and large breeds WOOF.
        """
        # TODO: Print a bark message using self.name
        pass

    def birthday(self):
        """It's the dog's birthday! 🎂"""
        # TODO: Increase age by 1
        # TODO: Print a birthday message with the new age
        pass

    def describe(self):
        """Print a summary of this good boy/girl."""
        # TODO: Print name, breed, and age in a nice format
        pass

    def sit(self):
        """Tell the dog to sit. Results may vary."""
        # TODO: Print a message about the dog sitting
        pass

    def learn_trick(self, trick):
        """Teach the dog a new trick!"""
        # TODO: Add the trick to self.tricks
        # TODO: Print a message about learning the trick
        pass

    def show_tricks(self):
        """Show off all learned tricks."""
        # TODO: Print all tricks, or a message if no tricks yet
        pass


# ----- Test your Dog class below! -----

# TODO: Create at least 3 dogs
# dog1 = Dog(???)
# dog2 = Dog(???)
# dog3 = Dog(???)

# TODO: Test all methods
# dog1.describe()
# dog1.bark()
# dog1.birthday()
# dog1.sit()
# dog1.learn_trick("roll over")
# dog1.show_tricks()

# TODO: Print total dogs created
# print(f"Total dogs: {Dog.total_dogs}")
