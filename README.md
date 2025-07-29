# 📝 Django Notes App

A full-featured Notes application built using Django. This project includes both **Function-Based Views (FBV)** and **Class-Based Views (CBV)** for educational comparison and better understanding.

---

## 🚀 Features

- User Registration & Login
- Create, Edit, Delete Personal Notes
- Admin can view all users’ notes
- Authenticated views for each user
- Secure configuration using `.env`
- CBV and FBV versions side-by-side
- Django Admin Panel
- Search and filter notes (Admin panel)

---

## 📁 Project Structure
```plaintext
notes-app/
│
├── env/                     # Virtual environment (not pushed to GitHub)
├── .env                    # Environment variables
├── .gitignore              # Ignore env/, .env, pycache, etc.
├── manage.py               # Django project manager
├── README.md               # Project instructions
├── requirements.txt        # Installed Python dependencies
│
├── notes/                  # Main project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── notesapp/               # Notes app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # For CBV
│   ├── urls1.py            # For FBV
│   ├── views.py            # Class-based views
│   └── view1.py            # Function-based views
│
└── templates/              # HTML templates
    ├── base.html
    ├── home.html
    ├── login.html
    ├── signup.html
    ├── note_create.html
    ├── note_detail.html
    ├── note_list.html
    └── note_update.html
```

## 🛠️ Setup Instructions

Follow these steps to run the project locally:

1. Clone the Repository
```bash
    git clone https://github.com/sumitgit1912/Notes-App.git
    cd notes-app
```

2. Create and Activate Virtual Environment
```bash
    python -m venv env
    source env/bin/activate     # On Windows: env\Scripts\activate
```

3. Install Dependencies
```bash
    pip install -r requirements.txt
```

4. Create .env File
Create a .env file in the root directory based on .env.example:
    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_NAME=your_db
    DATABASE_USER=your_user
    DATABASE_PASSWORD=your_password
    DATABASE_HOST=localhost
    DATABASE_PORT=3306

    You can also use SQLite by default if you're not using MySQL.


5. Apply Migrations
```bash
    python manage.py makemigrations
    python manage.py migrate
```

6. Run the Server
```bash
    python manage.py runserver
```
visit http://127.0.0.1:8000/ to use the app.


### 🌐 Switching Between CBV and FBV
By default, the app uses Class-Based Views (CBV) through `notesapp/urls.py`.
To switch to Function-Based Views (FBV):
1. Open the project’s main `urls.py` file (located in the base project directory).
2. Find the line:
   ```python
   path('', include('notesapp.urls')),
   ```
3. Change it to:
    ```
    path('', include('notesapp.urls1')),
    ```

## 📦 Dependencies
See requirements.txt. Key packages:

    Django

    python-decouple

    django-crispy-forms

    mysqlclient (or use SQLite)


## 🛡️ Security
    Environment variables loaded via .env

    .env is in .gitignore and not tracked

    Production-ready settings supported (DEBUG=False, ALLOWED_HOSTS, etc.)

## 🚀 Live Demo

🔗 [Click here to view the live app](https://notes-app-zpdm.onrender.com)

## 🔐 Test Credentials

### 👤 Test User Login
- **Username:** testuser  
- **Password:** Test@123

## 🧪 Want to Try It Yourself?

You can also sign up as a new user using the **Sign Up** button on the login page and create your own notes.

---




