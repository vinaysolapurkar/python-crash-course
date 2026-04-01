"""
Chapter 13 Exercise SOLUTION: Crash-Proof Tip Calculator
=========================================================
A tip calculator that can survive ANYTHING the user throws at it.
Type "banana" as a bill amount? No problem.
Try to split by zero people? We've got you covered.
This calculator is tougher than a Nokia 3310.
"""


def get_float(prompt, min_val=None, max_val=None):
    """
    Safely get a float from the user. Keeps asking until valid.

    Parameters:
        prompt (str): The question to ask
        min_val (float): Minimum allowed value (optional)
        max_val (float): Maximum allowed value (optional)

    Returns:
        float: A valid number, or None if user types 'quit'
    """
    while True:
        user_input = input(prompt).strip()

        # Let the user escape at any time
        if user_input.lower() == "quit":
            return None

        # Try to convert to float
        try:
            value = float(user_input)
        except ValueError:
            print(f"  '{user_input}' is not a number! Try again.")
            print("  (Or type 'quit' to exit)")
            continue

        # Range checking
        if min_val is not None and value < min_val:
            print(f"  Must be at least {min_val}. Got {value}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Must be at most {max_val}. Got {value}.")
            continue

        return value


def get_int(prompt, min_val=None, max_val=None):
    """
    Safely get an integer from the user. No decimals allowed!

    Returns:
        int: A valid integer, or None if user types 'quit'
    """
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "quit":
            return None

        try:
            value = int(user_input)
        except ValueError:
            # Maybe they typed a float like 2.5?
            try:
                float_val = float(user_input)
                print(f"  {float_val} isn't a whole number! No splitting people in half.")
            except ValueError:
                print(f"  '{user_input}' is not a number! Try again.")
            continue

        if min_val is not None and value < min_val:
            print(f"  Must be at least {min_val}. Got {value}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Must be at most {max_val}. Got {value}.")
            continue

        return value


def calculate_tip(bill, tip_percent, num_people):
    """
    Calculate the tip, total, and per-person amount.

    Returns:
        tuple: (tip_amount, total, per_person)
    """
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / num_people
    return tip_amount, total, per_person


def display_results(bill, tip_percent, tip_amount, total, per_person, num_people):
    """Display the calculation results in a fancy receipt format."""
    print("\n" + "=" * 35)
    print("        YOUR TIP RECEIPT")
    print("=" * 35)
    print(f"  Bill amount:     ${bill:>10.2f}")
    print(f"  Tip ({tip_percent:.0f}%):       ${tip_amount:>10.2f}")
    print(f"  " + "-" * 31)
    print(f"  Total:           ${total:>10.2f}")
    if num_people > 1:
        print(f"  Split {num_people} ways:     ${per_person:>10.2f} each")
    print("=" * 35)

    # Fun tip commentary
    if tip_percent == 0:
        print("  (No tip? The waiter is giving you the stink eye.)")
    elif tip_percent < 15:
        print("  (Decent tip. The waiter nods approvingly.)")
    elif tip_percent < 20:
        print("  (Good tip! The waiter smiles.)")
    elif tip_percent < 30:
        print("  (Great tip! The waiter does a little dance.)")
    else:
        print("  (Legendary tip! The waiter is naming their child after you.)")


def main():
    """Run the crash-proof tip calculator."""
    print("=" * 40)
    print("   CRASH-PROOF TIP CALCULATOR")
    print("   'Unbreakable, like a Nokia 3310'")
    print("=" * 40)
    print("Type 'quit' at any prompt to exit.\n")

    while True:
        # Get bill amount
        bill = get_float(
            "  Enter the bill amount: $",
            min_val=0.01,
            max_val=1_000_000  # If your bill is over $1M, you have other problems
        )
        if bill is None:
            break

        # Get tip percentage
        tip_percent = get_float(
            "  Enter tip percentage (0-100): ",
            min_val=0,
            max_val=100
        )
        if tip_percent is None:
            break

        # Get number of people
        num_people = get_int(
            "  How many people splitting? ",
            min_val=1,
            max_val=100  # If 100+ people, use a different tool!
        )
        if num_people is None:
            break

        # Calculate!
        try:
            tip_amount, total, per_person = calculate_tip(bill, tip_percent, num_people)
            display_results(bill, tip_percent, tip_amount, total, per_person, num_people)
        except Exception as e:
            # This should never happen with our validated inputs,
            # but belt AND suspenders, as they say.
            print(f"\n  Unexpected error: {e}")
            print("  Something went very wrong. Please try again!")

        # Ask to go again
        print()
        again = input("  Calculate another tip? (y/n): ").strip().lower()
        if again != "y":
            break
        print()  # Breathing room for the next calculation

    print("\n  Thanks for using the Crash-Proof Tip Calculator!")
    print("  Remember: always tip your servers. They deal with a lot.")
    print("  Goodbye!\n")


if __name__ == "__main__":
    main()
