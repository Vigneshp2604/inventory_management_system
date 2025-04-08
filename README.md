# 🏭 Inventory Management System

A powerful, feature-rich Inventory Management System with dual functionality - a Python command-line interface and a full Django REST API backend. Manage your inventory with ease, track products, generate reports, and interact with a modern API.

## ✨ Features

- **Product Management**: Add, remove, update, and search for products effortlessly
- **Reporting**: Generate comprehensive inventory reports on demand
- **Interface**: Use REST API based on your needs
- **Data Persistence**: Automatic saving of data in JSON or database format
- **Admin Dashboard**: Complete Django admin interface for inventory management
- **Robust API**: Well-designed REST API with full CRUD operations
- **Error Handling**: Comprehensive error handling for all operations

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Django REST Framework

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Django database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate inventory_api
   ```

4. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure

```
inventory-management-system/
├── inventory_system.py       # Core classes and data conversion functionality
├── inventory.json            # Data storage file (created automatically)
│
├── inventory_project/        # Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
│
├── inventory_api/            # Django app folder
│   ├── __init__.py
│   ├── admin.py              # Admin interface configuration
│   ├── apps.py
│   ├── migrations/
│   ├── models.py             # Product model definition
│   ├── serializers.py        # REST framework serializers
│   ├── urls.py               # API endpoints
│   └── views.py              # API views
│
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database (created automatically)
├── README.md                 # Documentation
└── requirements.txt          # Project dependencies
```

## 🔧 Usage

### Django REST API

Launch the server and access the API:

```bash
python manage.py runserver
```

Access the API at [http://localhost:8000/api/](http://localhost:8000/api/) and the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Data Conversion

To convert Django model data to JSON:

```bash
python inventory_system.py
```

## 📡 API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/api/products/` | GET | List all products | - |
| `/api/products/` | POST | Create a new product | JSON body with product details |
| `/api/products/<id>/` | GET | Retrieve product details | - |
| `/api/products/<id>/` | PUT | Update a product | JSON body with updated fields |
| `/api/products/<id>/` | DELETE | Remove a product | - |
| `/api/products/search/` | GET | Search for products | `q`: Search term |
| `/api/report/` | GET | Generate inventory report | - |

## 📝 API Examples

### Get All Products
```http
GET /api/products/
```

### Search for Products
```http
GET /api/products/search/?q=PROD014
```

### Add a Product
```http
POST /api/products/
Content-Type: application/json

{
  "product_id": "PROD014",
  "name": "Laptop",
  "price": 999.99,
  "quantity": 10
}
```

### Update a Product
```http
PUT /api/products/PROD014/
Content-Type: application/json

{
  "price": 899.99,
  "quantity": 15
}
```

### Delete a Product
```http
DELETE /api/products/PROD014/
```

## 💾 Data Persistence

- CLI mode: Data is stored in `inventory.json` with automatic saving
- API mode: Data is stored in a SQLite database (`db.sqlite3`) by default
- Database can be configured to use PostgreSQL, MySQL, or other databases in `settings.py`

## ⚠️ Error Handling

The system includes comprehensive error handling for:

- Duplicate product IDs
- Non-existent products
- Invalid operations (removing or updating products that don't exist)
- Data validation for prices, quantities, and formats
- API request errors with appropriate status codes


## 📞 Contact

Project Link: [https://github.com/vigneshviji2604/inventory_management_system]
