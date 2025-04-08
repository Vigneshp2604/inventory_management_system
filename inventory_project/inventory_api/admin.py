from django.contrib import admin

# Register your models here.
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product model."""
    list_display = ('product_id', 'name', 'price', 'quantity')
    search_fields = ('product_id', 'name')
    list_filter = ('price', 'quantity')

