# ============================================================
# YOUR TURN: Movie Rating Classifier
# ============================================================
# Build a program that recommends movie ratings based on age,
# with a special "parent mode" that bumps you up one tier.
#
# THE RATING SYSTEM:
#   Age 0-6   → "G"     (Animated wonderland)
#   Age 7-12  → "PG"    (Mild peril, nothing scarring)
#   Age 13-16 → "PG-13" (Teenagers being teenagers)
#   Age 17+   → "R"     (Welcome to the real world)
#
# PARENT BONUS:
#   If a parent is present (has_parent = True), bump up ONE tier:
#   - G  kid can watch PG
#   - PG kid can watch PG-13
#   - PG-13 kid can watch R
#   - R stays R (you're already at the top)
#
# YOUR PROGRAM SHOULD:
# 1. Ask for the viewer's age
# 2. Ask if a parent is present (yes/no)
# 3. Determine the base rating for their age
# 4. Apply the parent bump if applicable
# 5. Display the result with a fun message
#
# EXAMPLE OUTPUT:
#    Enter your age: 10
#    Is a parent with you? (yes/no): yes
#
#    Base rating: PG
#    Parent bonus: UPGRADED to PG-13!
#    You can watch PG-13 movies. Enjoy mild superhero violence!
#
# HINTS:
# - Convert yes/no input: has_parent = input(...).lower().strip() == "yes"
# - Use if/elif/else for the age brackets
# - Consider using a list of ratings and finding the index
#   OR just use another if/elif chain for the bump
#
# BONUS:
# - Suggest a movie for each rating tier
# - Handle invalid ages (negative numbers, unreasonably high)
#
# Type your code below!
# ============================================================

