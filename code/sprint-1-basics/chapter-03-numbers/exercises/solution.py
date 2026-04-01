# ============================================================
# SOLUTION: Tip Calculator
# ============================================================
# Because splitting the bill shouldn't require a math degree.
# ============================================================

print("=" * 35)
print("       TIP CALCULATOR")
print("  (Saving friendships since 2026)")
print("=" * 35)

# Get input from the user
bill = float(input("\nEnter the bill amount: $"))
tip_percent = float(input("Tip percentage (e.g. 15, 18, 20): "))
num_people = int(input("How many people are splitting? "))

# Bonus: handle the divide-by-zero villain
if num_people <= 0:
    print("\nNice try, but you can't split a bill among 0 people.")
    print("Setting to 1 person. You're paying alone, champ.")
    num_people = 1

# Calculate the important stuff
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / num_people

# Display the receipt
print("\n" + "-" * 35)
print("           RECEIPT")
print("-" * 35)
print(f"  Bill:             ${bill:.2f}")
print(f"  Tip ({tip_percent:.0f}%):        ${tip_amount:.2f}")
print(f"  Total:            ${total:.2f}")
print(f"  Split {num_people} ways:      ${per_person:.2f} each")
print("-" * 35)

# Bonus: suggested tips table
print("\n  SUGGESTED TIPS:")
print("  " + "-" * 31)
for pct in [15, 18, 20, 25]:
    suggested_tip = bill * (pct / 100)
    suggested_total = bill + suggested_tip
    suggested_each = suggested_total / num_people
    print(f"  {pct}% tip: ${suggested_tip:.2f} "
          f"(total: ${suggested_total:.2f}, "
          f"each: ${suggested_each:.2f})")
print("  " + "-" * 31)

print("\nDon't forget to thank your server! They deal with a LOT.")
