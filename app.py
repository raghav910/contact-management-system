from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path

from contact import Contact, WorkContact
from manager import (
    add_contact,
    list_contacts,
    search_contact,
    delete_contact,
    save_contacts,
    load_contacts,
)

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

DATA_FILE = Path(__file__).with_name("contacts.json")


def get_contacts():
    return load_contacts(str(DATA_FILE))


def persist(contacts):
    save_contacts(contacts, str(DATA_FILE))


@app.get("/")
def index():
    contacts = get_contacts()
    query = request.args.get("q", "").strip()
    if query:
        contacts = [c for c in contacts if query.lower() in c.name.lower()
                    or query.lower() in c.phone.lower()
                    or (isinstance(c, WorkContact) and query.lower() in c.company.lower())]
    return render_template("index.html", contacts=contacts, query=query,
                           total=len(get_contacts()))


@app.post("/contacts/add")
def add():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    company = request.form.get("company", "").strip()
    kind = request.form.get("kind", "personal")

    if not name or not phone:
        flash("Name and phone number are required.", "error")
        return redirect(url_for("index"))

    contacts = get_contacts()
    if kind == "work":
        if not company:
            flash("Please enter a company for a work contact.", "error")
            return redirect(url_for("index"))
        contact = WorkContact(name, phone, company)
    else:
        contact = Contact(name, phone)

    add_contact(contacts, contact)
    persist(contacts)
    flash(f"{name} was added successfully.", "success")
    return redirect(url_for("index"))


@app.post("/contacts/<int:contact_index>/delete")
def remove(contact_index):
    contacts = get_contacts()
    if 0 <= contact_index < len(contacts):
        deleted_name = contacts[contact_index].name
        contacts.pop(contact_index)
        persist(contacts)
        flash(f"{deleted_name} was deleted.", "success")
    else:
        flash("Contact not found.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
