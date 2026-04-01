"""
Chapter 13 Exercise: Crash-Proof Tip Calculator
=================================================
Remember the tip calculator from Chapter 3?
Let's make it INDESTRUCTIBLE with error handling!

Your calculator should handle:
  - Non-numeric bill amounts ("banana" instead of 25.99)
  - Negative bill amounts
  - Non-numeric tip percentages
  - Tip percentages below 0% or above 100%
  - Non-numeric number of people
  - Zero or negative number of people (can't split by zero!)
  - User wanting to quit at any point

HINTS:
  - Create helper functions: get_float() and get_int()
  - These should loop until the user gives valid input
  - Use try/except ValueError for non-numeric input
  - Use if/else for range checking
  - Wrap the whole thing in a loop so they can calculate again
"""


def get_float(prompt, min_val=None, max_val=None):
    """
    Safely get a float from the user.
    Keeps asking until they give a valid number in range.

    Parameters:
        prompt (str): The question to ask
        min_val (float): Minimum allowed value (optional)
        max_val (float): Maximum allowed value (optional)

    Returns:
        float: A valid number from the user, or None if they type 'quit'
    """
    # TODO: Loop until valid input
    # TODO: Try to convert input to float
    # TODO: Catch ValueError and print a helpful message
    # TODO: Check min/max range
    # TODO: If user types 'quit', return None
    pass


def get_int(prompt, min_val=None, max_val=None):
    """
    Safely get an integer from the user.
    Same idea as get_float but for whole numbers.

    Returns:
        int: A valid integer, or None if they type 'quit'
    """
    # TODO: Similar to get_float, but use int() instead of float()
    pass


def calculate_tip(bill, tip_percent, num_people):
    """
    Calculate the tip and per-person amount.

    Returns:
        tuple: (tip_amount, total, per_person)
    """
    # TODO: Calculate tip amount, total bill, and per-person share
    # HINT: tip_amount = bill * (tip_percent / 100)
    pass


def main():
    """Run the crash-proof tip calculator."""
    print("=== CRASH-PROOF TIP CALCULATOR ===")
    print("Type 'quit' at any point to exit.\n")

    # TODO: Get the bill amount using get_float()
    # TODO: Get the tip percentage using get_float()
    # TODO: Get the number of people using get_int()
    # TODO: If any input is None (user quit), exit gracefully
    # TODO: Calculate and display results
    # TODO: Wrap in a loop so they can calculate again
    pass


if __name__ == "__main__":
    main()
