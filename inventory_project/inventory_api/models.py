from django.db import models

# Create your models here.
"""Model representing a product in the inventory system."""
class Product(models.Model):
    
    product_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.product_id} - {self.name}"
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': float(self.price),
            'quantity': self.quantity
        }