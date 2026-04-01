# ============================================================
# YOUR TURN: Multiplication Table Printer
# ============================================================
# Build a program that prints a multiplication table for
# any number the user wants, with an option to keep going
# or quit.
#
# YOUR PROGRAM SHOULD:
# 1. Ask the user for a number (or 'q' to quit)
# 2. Print the multiplication table for that number (1 through 12)
# 3. Format it nicely (aligned columns)
# 4. Ask if they want another table or want to quit
#
# EXAMPLE OUTPUT:
#    === MULTIPLICATION TABLE PRINTER ===
#
#    Enter a number (or 'q' to quit): 7
#
#    --- Multiplication Table for 7 ---
#      7  x  1  =    7
#      7  x  2  =   14
#      7  x  3  =   21
#      7  x  4  =   28
#      7  x  5  =   35
#      7  x  6  =   42
#      7  x  7  =   49
#      7  x  8  =   56
#      7  x  9  =   63
#      7  x 10  =   70
#      7  x 11  =   77
#      7  x 12  =   84
#    --------------------------------
#
#    Enter a number (or 'q' to quit): q
#    Thanks for multiplying! Math is power.
#
# HINTS:
# - Use a while True loop for the main menu
# - Use a for loop with range(1, 13) for the table
# - Use f-strings with alignment: f"{number:>4}" for right-aligned
# - Check if input is 'q' before converting to int
#
# BONUS:
# - Let the user choose the range (e.g., 1 to 20 instead of 1 to 12)
# - Add a "show all tables 1-12" option
# - Highlight perfect squares (when n * n)
#
# Type your code below!
# ============================================================

