# ============================================================
# YOUR TURN: Build a Tip Calculator
# ============================================================
# You just had an amazing dinner. Now it's time to figure out
# how much to tip (and how to split it without losing friends).
#
# YOUR PROGRAM SHOULD:
# 1. Ask the user for the total bill amount
# 2. Ask for the tip percentage (e.g., 15, 18, 20)
# 3. Ask how many people are splitting the bill
# 4. Calculate:
#    - The tip amount
#    - The total (bill + tip)
#    - Each person's share
# 5. Display everything formatted to 2 decimal places
#
# EXAMPLE OUTPUT:
#    === TIP CALCULATOR ===
#    Enter the bill amount: $85.50
#    Tip percentage: 20
#    How many people are splitting? 3
#
#    --- RECEIPT ---
#    Bill:           $85.50
#    Tip (20%):      $17.10
#    Total:          $102.60
#    Split 3 ways:   $34.20 each
#    -------------------
#
# HINTS:
# - input() returns a string — convert with float() or int()
# - To calculate tip: bill * (tip_percent / 100)
# - Use :.2f in f-strings for 2 decimal places: f"${amount:.2f}"
# - round() can also help: round(number, 2)
#
# BONUS:
# - Handle the case where someone enters 0 people (can't divide by zero!)
# - Show a "suggested tips" table for 15%, 18%, and 20%
#
# Type your code below!
# ============================================================

