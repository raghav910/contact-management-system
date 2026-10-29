from contact import Contact, WorkContact
from manager import (
    add_contact,
    list_contacts,
    search_contact,
    delete_contact,
    save_contacts,
    load_contacts,
)

DATA_FILE = "contacts.json"


def menu():
    contacts = load_contacts(DATA_FILE)

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. Add work contact")
        print("3. List contacts")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Save & Quit")
        choice = input("> ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            add_contact(contacts, Contact(name, phone))
            print("Added.")

        elif choice == "2":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            company = input("Company: ").strip()
            add_contact(contacts, WorkContact(name, phone, company))
            print("Added.")

        elif choice == "3":
            list_contacts(contacts)

        elif choice == "4":
            name = input("Name to search: ").strip()
            found = search_contact(contacts, name)
            if found:
                found.display()
            else:
                print("Not found.")

        elif choice == "5":
            name = input("Name to delete: ").strip()
            if delete_contact(contacts, name):
                print("Deleted.")
            else:
                print("Not found.")

        elif choice == "6":
            save_contacts(contacts, DATA_FILE)
            print(f"Saved {len(contacts)} contact(s) to {DATA_FILE}. Bye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
