import json
from contact import contact_from_dict


def add_contact(contacts, contact):
    contacts.append(contact)
    return contacts


def list_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.")
        return
    for contact in contacts:
        contact.display()


def search_contact(contacts, name):
    # list comprehension: filter contacts by name (case-insensitive)
    matches = [c for c in contacts if c.name.lower() == name.lower()]
    return matches[0] if matches else None


def delete_contact(contacts, name):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            return True
    return False


def save_contacts(contacts, filepath):
    # list comprehension: convert every object to a plain dict before saving
    data = [c.to_dict() for c in contacts]
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def load_contacts(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    return [contact_from_dict(d) for d in data]
