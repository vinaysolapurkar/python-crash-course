# ============================================================
# SOLUTION: Grocery List Manager
# ============================================================
# Finally, a program that won't let you forget the milk.
# (Your phone's Notes app is shaking right now.)
# ============================================================

grocery_list = []

print("=" * 40)
print("       GROCERY LIST MANAGER")
print("  (Never forget the milk again)")
print("=" * 40)

while True:
    # Show menu with item count (bonus)
    count = len(grocery_list)
    count_text = f" ({count} item{'s' if count != 1 else ''})" if count > 0 else ""
    print(f"\n[A]dd  [R]emove  [V]iew  [Q]uit{count_text}")
    choice = input("> ").strip().lower()

    if choice == "a":
        # --- ADD ITEM ---
        item = input("Item to add: ").strip().title()

        if not item:
            print("You didn't type anything. The grocery gods are displeased.")
        elif item in grocery_list:
            # Bonus: prevent duplicates
            print(f'"{item}" is already on your list. One is enough!')
        else:
            grocery_list.append(item)
            print(f'Added "{item}" to your list!')

    elif choice == "r":
        # --- REMOVE ITEM ---
        if not grocery_list:
            print("Your list is empty! Nothing to remove.")
            print("(You can't remove what doesn't exist. That's philosophy.)")
        else:
            # Show numbered list
            print("\n--- Your Grocery List ---")
            for i, item in enumerate(grocery_list, 1):
                print(f"  {i}. {item}")
            print("-" * 25)

            remove_input = input("Enter item name or number to remove: ").strip()

            # Try to remove by number first
            if remove_input.isdigit():
                index = int(remove_input) - 1
                if 0 <= index < len(grocery_list):
                    removed = grocery_list.pop(index)
                    print(f'Removed "{removed}" from your list.')
                else:
                    print(f"No item at number {remove_input}. Check the list!")
            else:
                # Try to remove by name
                item_name = remove_input.title()
                if item_name in grocery_list:
                    grocery_list.remove(item_name)
                    print(f'Removed "{item_name}" from your list.')
                else:
                    print(f'"{item_name}" not found. Did you spell it right?')

    elif choice == "v":
        # --- VIEW LIST ---
        if not grocery_list:
            print("\nYour list is empty! Time to add some goodies.")
        else:
            # Bonus: show sorted view
            sorted_list = sorted(grocery_list)
            print("\n--- Your Grocery List ---")
            for i, item in enumerate(sorted_list, 1):
                print(f"  {i}. {item}")
            print(f"--- {len(grocery_list)} item{'s' if len(grocery_list) != 1 else ''} ---")

    elif choice == "q":
        # --- QUIT ---
        if grocery_list:
            print(f"\nYour final list ({len(grocery_list)} items):")
            for item in sorted(grocery_list):
                print(f"  - {item}")
        print("\nHappy shopping! Don't forget the snacks.")
        break

    else:
        print(f'"{choice}" is not an option. Try A, R, V, or Q.')
        print("(Reading is fundamental, as they say.)")
