# ============================================================
# SOLUTION: Multiplication Table Printer
# ============================================================
# Making multiplication tables fun since... well, since now.
# Your 3rd grade teacher would be so proud.
# ============================================================

print("=" * 40)
print("    MULTIPLICATION TABLE PRINTER")
print("  (Flashcards are so last century)")
print("=" * 40)

while True:
    print("\nOptions:")
    print("  - Enter a number for its table")
    print("  - Type 'all' for tables 1-12")
    print("  - Type 'q' to quit")

    user_input = input("\nYour choice: ").strip().lower()

    # Check for quit
    if user_input == "q":
        print("\nThanks for multiplying! Math is power.")
        print("Go forth and conquer arithmetic.")
        break

    # Bonus: show all tables
    if user_input == "all":
        print("\n=== ALL MULTIPLICATION TABLES (1-12) ===")
        # Print header row
        print("      ", end="")
        for col in range(1, 13):
            print(f"{col:>5}", end="")
        print()
        print("     " + "-" * 60)

        for row in range(1, 13):
            print(f"  {row:>2} |", end="")
            for col in range(1, 13):
                product = row * col
                # Bonus: highlight perfect squares
                if row == col:
                    print(f" [{product:>2}]", end="")
                else:
                    print(f"{product:>5}", end="")
            print()
        print("\n(Numbers in [brackets] are perfect squares!)")
        continue

    # Validate input is a number
    if not user_input.lstrip("-").isdigit():
        print("That's not a number. Try again, mathletics champion.")
        continue

    number = int(user_input)

    # Bonus: ask for range
    range_input = input("Table range? (press Enter for 1-12, or type max like '20'): ").strip()
    if range_input.isdigit() and int(range_input) > 0:
        max_range = int(range_input)
    else:
        max_range = 12

    # Print the table
    print(f"\n--- Multiplication Table for {number} ---")
    for i in range(1, max_range + 1):
        product = number * i
        # Bonus: mark perfect squares
        marker = " *" if number == i else ""
        print(f"  {number:>4}  x  {i:>3}  =  {product:>6}{marker}")

    print("-" * 36)

    if number == 0:
        print("Well, that was anticlimactic. All zeros.")
    elif number < 0:
        print("Negative tables! Living dangerously, I see.")
    else:
        print(f"Fun fact: {number} x {number} = {number ** 2} (a perfect square!)")
