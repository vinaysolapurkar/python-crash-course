# ============================================================
# YOUR TURN: Grocery List Manager
# ============================================================
# Build an interactive grocery list manager with a menu system.
# The user should be able to add, remove, view, and quit.
#
# FEATURES:
# 1. Show a menu with options:
#    [A] Add item
#    [R] Remove item
#    [V] View list
#    [Q] Quit
#
# 2. Keep looping until the user types 'Q' or 'q'
#
# 3. For ADDING:
#    - Ask for the item name
#    - Add it to the list
#    - Print a confirmation
#
# 4. For REMOVING:
#    - Show the current list with numbers
#    - Ask which item to remove (by name or number)
#    - Handle the case where the item doesn't exist
#
# 5. For VIEWING:
#    - Show all items numbered (1, 2, 3...)
#    - If empty, say "Your list is empty!"
#
# EXAMPLE SESSION:
#    === GROCERY LIST MANAGER ===
#    [A]dd  [R]emove  [V]iew  [Q]uit
#    > a
#    Item to add: Milk
#    Added "Milk" to your list!
#
#    [A]dd  [R]emove  [V]iew  [Q]uit
#    > a
#    Item to add: Eggs
#    Added "Eggs" to your list!
#
#    [A]dd  [R]emove  [V]iew  [Q]uit
#    > v
#    --- Your Grocery List ---
#    1. Milk
#    2. Eggs
#    -------------------------
#
#    [A]dd  [R]emove  [V]iew  [Q]uit
#    > q
#    Happy shopping! Don't forget the snacks.
#
# HINTS:
# - Use a while True loop for the menu
# - Use .lower() on input for case-insensitive matching
# - For remove, check if the item is 'in' the list first
#
# BONUS:
# - Show the item count in the menu
# - Sort the list alphabetically when viewing
# - Prevent duplicate items from being added
#
# Type your code below!
# ============================================================

