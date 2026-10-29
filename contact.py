class Contact:
     # A basic contact with a name and phone number.

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.name}: {self.phone}")

    def to_dict(self):
        return {"type": "contact", "name": self.name, "phone": self.phone}


class WorkContact(Contact):
    """A Contact with an extra 'company' field."""

    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display(self):
        print(f"{self.name}: {self.phone} ({self.company})")

    def to_dict(self):
        return {
            "type": "work",
            "name": self.name,
            "phone": self.phone,
            "company": self.company,
        }


def contact_from_dict(data):
    """Rebuild a Contact or WorkContact object from a saved dict."""
    if data.get("type") == "work":
        return WorkContact(data["name"], data["phone"], data["company"])
    return Contact(data["name"], data["phone"])
