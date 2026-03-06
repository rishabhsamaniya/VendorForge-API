# VendorForge-API

A **Multi-Vendor E-Commerce Backend API** built with **Django REST Framework**.

This project demonstrates production-level backend architecture including authentication, role-based permissions, product management, filtering, and category systems.

---

# 🚀 Features

### Authentication

* JWT Authentication
* Access & Refresh Tokens
* Custom JWT Claims
* Secure Password Hashing

### User Roles

* Admin
* Vendor
* Customer

### Product Management

* Vendor-only product creation
* Owner-based product update & delete
* Category-based products

### API Features

* Advanced Filtering
* Search
* Ordering
* Pagination

---

# 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* SQLite (Development)

---

# 📂 Project Structure

```
VendorForge-API
│
├── users
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── permissions.py
│
├── products
│   ├── models.py
│   ├── serializers.py
│   ├── filters.py
│   └── views.py
│
├── ecommerce_api
│   └── settings.py
│
├── manage.py
└── requirements.txt
```

---

# 🔐 Authentication

JWT authentication is implemented using:

```
djangorestframework-simplejwt
```

Example login endpoint:

```
POST /api/token/
```

---

# 📦 API Endpoints

### Authentication

```
POST /api/register/
POST /api/token/
```

### Vendor Test

```
GET /api/vendor-test/
```

### Categories

```
GET  /api/products/categories/
POST /api/products/categories/
```

### Products

```
POST   /api/products/create/
GET    /api/products/list/
PUT    /api/products/<id>/
DELETE /api/products/<id>/
```

---

# 🔎 Filtering Examples

```
/api/products/list/?category=1
/api/products/list/?min_price=50000
/api/products/list/?search=iphone
```

---

# ⚙ Installation

Clone the repository:

```
git clone https://github.com/yourusername/VendorForge-API.git
```

Go into project folder:

```
cd VendorForge-API
```

Create virtual environment:

```
python -m venv env
```

Activate environment:

Mac/Linux

```
source env/bin/activate
```

Windows

```
env\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Run server:

```
python manage.py runserver
```

---

# 🎯 Future Improvements

* Product image upload
* Cart system
* Order management
* Payment integration
* Docker support

---

# 👨‍💻 Author

**NeoRish**

GitHub:
https://github.com/rishabhsamaniya
