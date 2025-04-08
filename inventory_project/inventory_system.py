"""
Script to sync data between inventory.json and Django database.
This can be used if you need to migrate data or operate in both systems.
"""
import json
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_project.settings')
django.setup()

from inventory_api.models import Product

def import_json_to_django():
    """Import data from inventory.json to Django database."""
    try:
        # Load data from JSON file
        with open('inventory.json', 'r') as f:
            data = json.load(f)
        
        products_imported = 0
        products_updated = 0
        
        # Create or update products in Django
        for product_id, product_data in data.items():
            product, created = Product.objects.update_or_create(
                product_id=product_data['product_id'],
                defaults={
                    'name': product_data['name'],
                    'price': product_data['price'],
                    'quantity': product_data['quantity']
                }
            )
            
            if created:
                products_imported += 1
            else:
                products_updated += 1
        
        print(f"Import complete: {products_imported} products imported, {products_updated} products updated")
        return True
    
    except FileNotFoundError:
        print("inventory.json file not found")
        return False
    except json.JSONDecodeError:
        print("Error parsing inventory.json file")
        return False
    except Exception as e:
        print(f"Error during import: {str(e)}")
        return False

def export_django_to_json():
    """Export data from Django database to inventory.json."""
    try:
        # Get all products from Django
        products = Product.objects.all()
        
        # Convert to dictionary format for JSON
        data = {}
        for product in products:
            data[product.product_id] = {
                'product_id': product.product_id,
                'name': product.name,
                'price': float(product.price),
                'quantity': product.quantity
            }
        
        # Save to JSON file
        with open('inventory.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Export complete: {len(data)} products exported to inventory.json")
        return True
    
    except Exception as e:
        print(f"Error during export: {str(e)}")
        return False

if __name__ == "__main__":
    while True:
        print("\n--- Inventory Data Integration ---")
        print("1. Import from inventory.json to Django database")
        print("2. Export from Django database to inventory.json")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            import_json_to_django()
        elif choice == '2':
            export_django_to_json()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")