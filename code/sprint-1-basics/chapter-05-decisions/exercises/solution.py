# ============================================================
# SOLUTION: Movie Rating Classifier
# ============================================================
# Because nobody wants to explain an R-rated movie to a 6-year-old.
# ============================================================

print("=" * 40)
print("      MOVIE RATING CLASSIFIER")
print("  (Your ticket to cinematic adventure)")
print("=" * 40)

# Get input
age_input = input("\nEnter your age: ").strip()

# Validate age (bonus)
if not age_input.isdigit():
    print("That's not a valid age. Are you a time traveler?")
elif int(age_input) > 150:
    print("150+? Impressive. But we'll need to see some ID, Gandalf.")
else:
    age = int(age_input)
    has_parent = input("Is a parent with you? (yes/no): ").lower().strip() == "yes"

    # Rating tiers and their suggested movies (bonus)
    ratings = ["G", "PG", "PG-13", "R"]
    suggestions = {
        "G":     "Try 'Finding Nemo' — a fish dad with serious anxiety.",
        "PG":    "Try 'The Incredibles' — a family of superheroes. Relatable?",
        "PG-13": "Try 'Spider-Man: Across the Spider-Verse' — absolute masterpiece.",
        "R":     "Try 'The Matrix' — take the red pill. Trust me."
    }

    # Determine base rating
    if age <= 6:
        base_index = 0       # G
    elif age <= 12:
        base_index = 1       # PG
    elif age <= 16:
        base_index = 2       # PG-13
    else:
        base_index = 3       # R

    base_rating = ratings[base_index]

    # Apply parent bump
    if has_parent and base_index < 3:
        final_index = base_index + 1
        final_rating = ratings[final_index]
        bump_message = f"Parent bonus: UPGRADED from {base_rating} to {final_rating}!"
    else:
        final_rating = base_rating
        if has_parent and base_index == 3:
            bump_message = "Parent bonus: You're already at R. Can't go higher (legally)."
        else:
            bump_message = "No parent bonus. Flying solo!"

    # Display results
    print("\n" + "-" * 40)
    print(f"  Age:          {age}")
    print(f"  Parent:       {'Yes' if has_parent else 'No'}")
    print(f"  Base rating:  {base_rating}")
    print(f"  {bump_message}")
    print(f"  Final rating: {final_rating}")
    print("-" * 40)

    # Fun message based on final rating
    if final_rating == "G":
        print("\n  Animated adventures await! Grab your juice box.")
    elif final_rating == "PG":
        print("\n  Mild thrills ahead! Nothing a nightlight can't fix.")
    elif final_rating == "PG-13":
        print("\n  Teenage drama and superhero action. Buckle up!")
    else:
        print("\n  Welcome to the big leagues. Popcorn is mandatory.")

    # Movie suggestion (bonus)
    print(f"\n  {suggestions[final_rating]}")
    print("\n  Enjoy the movie! (Silence your phone. Seriously.)")
