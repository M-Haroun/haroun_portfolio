# 🚀 Django Portfolio Website

A full-featured personal portfolio web application built with Django.
It showcases projects, blog posts, and includes authentication, contact system, and admin dashboard.

---

## ✨ Features

* 📁 Projects management (CRUD)
* 📝 Blog system with pagination & slug URLs
* 🔐 Authentication (Login / Logout)
* 👤 Admin dashboard (Django Admin)
* 💬 Comment system (with approval)
* 📩 Contact form with email support
* 🖼 Media & static file handling
* 🧱 Clean and scalable project structure

---

## 🛠 Tech Stack

* Python
* Django
* HTML / CSS
* SQLite (Development)

---

## 📂 Project Structure

```
apps/
 ├── core
 ├── portfolio
 ├── blog
 ├── contact
 └── accounts
```

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/haroun_portfolio.git

# Go to project folder
cd haroun_portfolio

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## 🔐 Environment Variables

Create a `.env` file in the root:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🌍 Live Demo

Coming soon...

---

## 📸 Screenshots

Coming soon...
---

## 📌 Key Highlights

* Built using Class-Based Views (CBVs)
* Implements authentication & permissions
* Clean URL design with slugs
* Scalable Django app structure
* Production-ready setup

---

## 👨‍💻 Author

**Mahmoud Haroun**

---

## 📄 License

