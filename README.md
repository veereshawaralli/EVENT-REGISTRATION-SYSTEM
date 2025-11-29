# Event Registration System (Django)

A complete, minimal Django-based Event Registration System with role-based access, event creation, participant registration, CSV export, and an admin control panel.  
This project is designed for college/organization event management and academic project submission.

---

## 📌 Project Overview

The Event Registration System allows:

- **Participants** → View events, register, see their registrations  
- **Organizers** → Create/Manage events, export participants  
- **Admin** → Full control using Django Admin panel  

Built using **Django**, **SQLite**, **Bootstrap**, and standard web technologies.

---

## 🎯 Features

### 👤 User Roles
- **Participant** – registers for events  
- **Organizer** – creates & manages events  
- **Admin** – full control via `/admin/`

### 🗂 System Features
- User signup with role selection  
- Auto profile creation using Django Signals  
- Event create/update/delete (Organizer)  
- Event listing & detail page  
- Registration window check (start–end dates)  
- Prevent duplicate registrations  
- Optional maximum capacity  
- Organizer dashboard  
- CSV export of participants  
- Django admin integration  
- Basic unit tests  
- Sample fixture JSON  

---

## 🛠 Tech Stack

| Component | Used |
|----------|------|
| Backend | Django 4.x |
| Database | SQLite (default) |
| Frontend | HTML, CSS, Bootstrap 5 |
| Language | Python 3.x |

---

## 📁 Project Structure

```
event_reg_project/
│── manage.py
│── requirements.txt
│── README.md
│
├── event_reg_project/        
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── events/                  
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── signals.py
│   ├── admin.py
│   ├── tests.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   └── events/
│       ├── index.html
│       ├── event_detail.html
│       ├── signup.html
│       ├── participant_dashboard.html
│       ├── organizer_dashboard.html
│       └── event_form.html
│
├── static/
│   └── css/styles.css
│
└── fixtures/
    └── sample_fixture.json
```

---

## ⚙️ Getting Started (Local Setup)

### ✔ 1. Navigate to Project Folder
Make sure you enter the folder that contains `manage.py`.

### ✔ 2. Create Virtual Environment

**PowerShell:**
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope CurrentUser Unrestricted
.env\Scripts\Activate.ps1
```

**CMD:**
```cmd
python -m venv venv
venv\Scripts\Activate.bat
```

### ✔ 3. Install Dependencies
```
pip install -r requirements.txt
```

### ✔ 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### ✔ 5. Create Superuser
```
python manage.py createsuperuser
```

### ✔ 6. Run Server
```
python manage.py runserver
```

Visit in browser:
```
http://127.0.0.1:8000/events/
```

---

## 🔍 Usage Guide

### 👤 Participant Flow
- Sign up → choose **Participant**
- Browse events (`/events/`)
- View event details
- Register
- View "My Registrations"

### 📝 Organizer Flow
- Sign up → choose **Organizer**
- Go to Organizer Dashboard
- Create/Edit events
- Track registration count
- Export CSV

### 🛡 Admin Flow
Visit:
```
/admin/
```

---

## 🧪 Running Tests
```
python manage.py test
```

---

## 🧷 Fixtures
Load using:
```
python manage.py loaddata fixtures/sample_fixture.json
```

---

## 🚀 Deployment Notes
- Set `DEBUG = False` for production
- Add allowed hosts
- Replace SECRET_KEY
- Use collectstatic for production
- Recommended DB: PostgreSQL

---

## 🧩 Common Issues & Fixes

### ❌ no such table: events_event
Run:
```
python manage.py migrate
```

### ❌ Activate.ps1 cannot be loaded
```
Set-ExecutionPolicy -Scope CurrentUser Unrestricted
```

### ❌ python: can't open manage.py
Use:
```
cd path/to/project
```

---

## 🏆 Future Improvements
- Event photos
- QR-based attendance
- API integration (DRF)
- Payment gateway for ticketed events

---

## 🤝 Support
If you want:
- PDF version  
- PPT  
- Report documentation  

Just ask!
