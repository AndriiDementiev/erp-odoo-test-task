# 👨‍🦰 Odoo Persons Module

A minimal yet functional Odoo 16 module for managing persons, featuring backend CRUD and a public website page.

---

## 🌐 Overview

Manage person records via the Odoo backend and display the latest five entries on a public `/persons` webpage.

---

## ✨ Features

- ✅ Person model with computed `full_name` and `age`
- ✅ Backend form and tree views
- ✅ Public `/persons` page with responsive layout
- ✅ Multi-company support
- ✅ Dockerized with `.env` configuration
- ✅ Clean, maintainable code with `ruff`-friendly formatting
- ✅ CI for auto launching `ruff` on commit before pushing on develop branch
- ✅ Poetry for dependencies
---

## 🧱 Tech Stack

- Python 3.10+
- Odoo 16.0
- PostgreSQL 15
- Docker Compose
- QWeb templates
- Minimal JS/CSS static files

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AndriiDementiev/erp-odoo-test-task.git
cd erp-odoo-test-task
```

### 2. Create and configure .env

```bash
cp .env.sample .env
```

### 🔧 Adjust environment variables in .env if needed:

```
POSTGRES_DB=postgres
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
ODOO_ADMIN_PASS=admin
ODOO_DB_HOST=db
ODOO_DB_PORT=5432
```

### 3. Run the containers

```bash
docker-compose up --build -d
```

### 4. Access the system

```bash
http://localhost:8069
```

## 📝 Steps:

1. Create a new database (e.g. test_db)
2. Use the admin password from your .env file
3. Open the Apps menu
4. Click Update Apps List (enable Developer Mode if needed)
5. Search for Persons
6. Click Install

## 🚀 Usage
Backend (Admin Panel)

```bash
http://localhost:8069/web
```
Go to Persons → All Persons
Click Create
Fill in:
    ✅ First Name
    ✅ Last Name
🎂 Birthday (optional)
⚧️ Sex (optional)
Save

### Public Page

Displays 5 latest persons
```bash
http://localhost:8069/persons
```

Shows name, age, sex, and company
Responsive card layout (CSS via static//css/persons.css)

## 📁 Module Structure

```
addons/persons/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   └── persons.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └──── css/
│          └── persons.css
│   └──── js/
│           └── persons.js
├── views/
│   ├── person_action.xml
│   ├── person_form_template.xml
│   ├── person_views.xml
│   ├── website_templates.xml
│   └── menu.xml
```

### 🧪 Development & Debugging

Logs
```bash
docker-compose logs -f odoo
```

Odoo shell
```bash
docker-compose exec odoo odoo shell
```

Restart services
```bash
docker-compose restart
```

Debug mode
```bash
docker-compose exec odoo odoo --dev=all
```
