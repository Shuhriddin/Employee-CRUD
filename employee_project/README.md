# Django Employee Register CRUD App

A simple Django web application for managing employee records using CRUD operations (Create, Read, Update, Delete). The app uses Bootstrap 5 for styling and Django Forms with Crispy Forms for cleaner UI.

## Features

- Add new employees with full name, code, mobile number, and position.
- Update existing employee records.
- Delete employees.
- View list of all employees.
- Clean and responsive UI using Bootstrap 5.
- Admin dashboard support via Jazzmin.

## Technologies Used

- Python 3.11+
- Django 4.x
- SQLite3 (default)
- Bootstrap 5 (via CDN)
- Font Awesome
- Crispy Forms
- Jazzmin (optional for admin UI)

## Getting Started

### Prerequisites

Make sure you have Python installed:

```bash
python --version
```

1. Clone the repository:
   git clone https://github.com/yourusername/employee-register-crud.git
   cd employee-register-crud

2. Create a virtual environment and activate it:
   python -m venv .venv
   source .venv/bin/activate # On Windows: .venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Create a superuser (optional for admin panel):
   python manage.py createsuperuser

6. Run the server:
   python manage.py runserver

7. Open in browser:
   http://127.0.0.1:8000/employee/

employee_project/
├── employee_register/ # Main app
│ ├── migrations/
│ ├── templates/
│ └── forms.py, models.py, views.py, urls.py
├── employee_project/ # Project settings
├── manage.py
