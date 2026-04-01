"""
Chapter 9 Exercise: Contact Book
=================================
Build a menu-driven contact book app using dictionaries!

Your contact book should support:
  1. View all contacts
  2. Add a contact (name + phone number)
  3. Search for a contact by name
  4. Delete a contact
  5. Quit

Starter code is below -- fill in the functions!

HINTS:
  - Store contacts as a dict: {"name": "phone_number"}
  - Use input() to get user choices
  - Use a while loop for the menu
  - For search, think about partial name matching (e.g., "jo" finds "John")
"""

# Your contact book storage -- a simple dict
contacts = {}


def show_menu():
    """Display the menu options."""
    print("\n===== CONTACT BOOK =====")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Quit")
    print("========================")


def view_all(contacts):
    """Display all contacts in a nice format."""
    # TODO: If contacts is empty, print a message saying so
    # TODO: Otherwise, loop through and print each name + number
    # HINT: Use contacts.items() to get name and number
    pass


def add_contact(contacts):
    """Add a new contact to the book."""
    # TODO: Ask for name and phone number
    # TODO: Check if contact already exists -- warn the user
    # TODO: Add the contact to the dict
    # HINT: contacts[name] = phone
    pass


def search_contact(contacts):
    """Search for a contact by name (partial match)."""
    # TODO: Ask for a search term
    # TODO: Search through contacts for names that CONTAIN the search term
    # HINT: Use 'if search_term.lower() in name.lower()' for partial matching
    # TODO: Display matching contacts, or "No results" if none found
    pass


def delete_contact(contacts):
    """Delete a contact by name."""
    # TODO: Ask which contact to delete
    # TODO: Check if it exists before deleting
    # HINT: Use 'if name in contacts:' then 'del contacts[name]'
    pass


# =============================================================================
# MAIN PROGRAM LOOP
# =============================================================================
def main():
    """Run the contact book app."""
    print("Welcome to your Contact Book! Let's get organized.")

    # TODO: Start some sample contacts so it's not empty
    # HINT: contacts["Tony Stark"] = "555-IRON"

    while True:
        show_menu()
        choice = input("Pick an option (1-5): ").strip()

        if choice == "1":
            view_all(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye! Your contacts are safe... until you restart. :)")
            break
        else:
            print("Invalid choice! Please pick 1-5.")


# Run the app!
if __name__ == "__main__":
    main()
