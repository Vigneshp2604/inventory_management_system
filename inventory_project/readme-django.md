# Inventory Management System

A Python-based Inventory Management System with both interface and Django REST API functionality.

## Features

- Add, remove, update, and search for products
- Generate and display inventory reports
- CLI with data persistence through JSON
- Django REST API with database backend
- Admin interface for managing inventory

### Project Structure

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
├── README.md                 # This file
├── requirements.txt          # project dependencies (required)

#### Requirements

- Python 3.6 or higher
- Django 3.2 or higher
- Django REST Framework

##### Installation

1. Unzip the project files to a directory of your choice
2. Install required dependencies: 

```````````bash````````````````
pip install -r requirements.txt
```````````````````````````````

3. Set up the Django database:

````````````````bash``````````````````
python manage.py makemigrations

python manage.py migrate inventory_api
``````````````````````````````````````

4. Create a superuser for the admin interface:

`````````bash`````````````````````
python manage.py createsuperuser
``````````````````````````````````

### Command Line Interface

To start the command-line interface with Django REST framework:

1. Django REST API

To start the Django development server:

````````bash```````````````
python manage.py runserver
```````````````````````````

The server runs on http://localhost:8000 by default. 

2. API Endpoints

|    Endpoint             | Method |          Description      | Parameters                     |
|-------------------------|--------|---------------------------|--------------------------------|
| `/api/products/`        | GET    | Get all products          | -                              |
| `/api/products/`        | POST   | Add a new product         | JSON body with product details |
| `/api/products/<id>/`   | GET    | Get product by ID         | -                              |
| `/api/products/<id>/`   | PUT    | Update a product          | JSON body with updated fields  |
| `/api/products/<id>/`   | DELETE | Delete a product          | -                              |
| `/api/products/search/` | GET    | Search for products       | `q`: Search term               |
| `/api/report/`          | GET    | Generate inventory report | -                              |

3. Example REST API Usage

Get all products:
```````````````````````````````````
GET /api/products/
```````````````````````````````````

Search for products:
```````````````````````````````````
GET /api/products/search/?q=PROD014
```````````````````````````````````

Add a product:
```````````````````````````````````
POST /api/products/
Content-Type: application/json

{
  "product_id": "PROD014",
  "name": "Laptop",
  "price": 999.99,
  "quantity": 10
}
```````````````````````````````````

Update a product:
```````````````````````````````````
PUT /api/products/PROD014/
Content-Type: application/json

{
  "price": 899.99,
  "quantity": 15
}
```````````````````````````````````

Delete a product:
``````````````````````````````````
DELETE /api/products/PROD014/
``````````````````````````````````

4. For Conversion of django model data into JSON data.

`````````bash``````````````
python inventory_system.py
```````````````````````````
## Data Persistence:

-The system automatically saves data to `inventory.json` when changes are made.
-The Django API uses a SQLite database by default, but can be configured to use other databases in `settings.py`.

## Error Handling:

The system includes error handling for:
- Duplicate product IDs
- Non-existent products- Attempting to remove or update a product that does not exist
- Invalid data formats
- Negative prices or quantities
