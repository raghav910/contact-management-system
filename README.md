# Contactly — Contact Management System

A responsive Flask frontend for a Python contact manager. It supports personal and work contacts, search, delete, and JSON-file persistence through your existing `contact.py` and `manager.py` modules.

## Project structure

```text
contact-management-system/
├── app.py
├── contact.py
├── manager.py
├── contacts.json          # created when you save contacts
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Setup

1. Keep your existing `contact.py` and `manager.py` in the same folder as `app.py`.
2. Install Flask:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the web app:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in your browser.

## Notes

- Data is stored in `contacts.json` beside `app.py`.
- This app uses the `Contact`, `WorkContact`, and manager functions from your existing Python modules.
- The delete form uses the contact's displayed index. If you later add sorting or pagination, switch to stable contact IDs.
- `debug=True` is suitable for local development only; disable it before deployment.
