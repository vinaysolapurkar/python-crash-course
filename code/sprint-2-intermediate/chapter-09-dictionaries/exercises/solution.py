"""
Chapter 9 Exercise SOLUTION: Contact Book
==========================================
A fully working contact book with partial name search!
Run this to see the complete app in action.
"""

# Our contact storage -- name -> phone number
contacts = {}


def show_menu():
    """Display the menu options -- fancier than a restaurant menu."""
    print("\n" + "=" * 35)
    print("       CONTACT BOOK v1.0")
    print("=" * 35)
    print("  1. View all contacts")
    print("  2. Add a contact")
    print("  3. Search for a contact")
    print("  4. Delete a contact")
    print("  5. Quit")
    print("=" * 35)


def view_all(contacts):
    """Display all contacts in a nice formatted table."""
    if not contacts:
        print("\n  No contacts yet! Add some friends (or enemies).")
        return

    print(f"\n  You have {len(contacts)} contact(s):")
    print("  " + "-" * 35)
    # Sort contacts alphabetically by name for a clean display
    for name in sorted(contacts.keys()):
        phone = contacts[name]
        print(f"  {name:<20} {phone}")
    print("  " + "-" * 35)


def add_contact(contacts):
    """Add a new contact -- or update if they already exist."""
    name = input("\n  Enter contact name: ").strip()
    if not name:
        print("  Name can't be empty! Even Voldemort has a name.")
        return

    # Check if contact already exists
    if name in contacts:
        print(f"  '{name}' already exists with number: {contacts[name]}")
        overwrite = input("  Update their number? (y/n): ").strip().lower()
        if overwrite != "y":
            print("  No changes made.")
            return

    phone = input("  Enter phone number: ").strip()
    if not phone:
        print("  Phone number can't be empty!")
        return

    contacts[name] = phone
    print(f"  Added: {name} -> {phone}")


def search_contact(contacts):
    """Search contacts by partial name match -- like Google, but for friends."""
    if not contacts:
        print("\n  No contacts to search! The book is empty.")
        return

    search_term = input("\n  Enter name to search: ").strip().lower()
    if not search_term:
        print("  Please enter something to search for!")
        return

    # Find all contacts whose name CONTAINS the search term (case-insensitive)
    results = {
        name: phone
        for name, phone in contacts.items()
        if search_term in name.lower()
    }

    if results:
        print(f"\n  Found {len(results)} match(es):")
        print("  " + "-" * 35)
        for name, phone in results.items():
            print(f"  {name:<20} {phone}")
        print("  " + "-" * 35)
    else:
        print(f"  No contacts found matching '{search_term}'.")
        print("  Maybe try a shorter search term?")


def delete_contact(contacts):
    """Delete a contact by exact name."""
    if not contacts:
        print("\n  No contacts to delete! Already a clean slate.")
        return

    name = input("\n  Enter exact name to delete: ").strip()

    if name in contacts:
        phone = contacts.pop(name)
        print(f"  Deleted: {name} ({phone}) -- gone like Thanos snapped them.")
    else:
        print(f"  '{name}' not found in contacts.")
        # Helpful: show similar names
        similar = [n for n in contacts if name.lower() in n.lower()]
        if similar:
            print(f"  Did you mean one of these? {', '.join(similar)}")


# =============================================================================
# MAIN PROGRAM LOOP
# =============================================================================
def main():
    """Run the contact book app."""
    print("\n  Welcome to Contact Book v1.0!")
    print("  Your digital Rolodex (ask your parents what that is).")

    # Pre-load some sample contacts so it's not lonely in here
    contacts["Tony Stark"] = "555-IRON"
    contacts["Peter Parker"] = "555-WEBS"
    contacts["Bruce Wayne"] = "555-BATS"
    contacts["Diana Prince"] = "555-WNDR"
    contacts["Clark Kent"] = "555-SUPE"

    while True:
        show_menu()
        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            view_all(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\n  Goodbye! Remember: with great contacts comes")
            print("  great responsibility. See you next time!")
            break
        else:
            print("  Invalid choice! Pick a number 1-5, not a Konami code.")


# Run the app!
if __name__ == "__main__":
    main()
