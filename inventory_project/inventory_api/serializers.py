from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity']
        
        
    def validate_price(self, value):
        """Validate price is positive."""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
    
    def validate_quantity(self, value):
        """Validate quantity is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
    
    def get_extra_kwargs(self):
        """
        Add extra kwargs based on action (create vs update)
        """
        extra_kwargs = super().get_extra_kwargs()
        
        # Get the current request method
        request = self.context.get('request', None)
        
        if request and request.method in ['PUT', 'PATCH']:
            # For update operations, make product_id read-only
            extra_kwargs.setdefault('product_id', {})
            extra_kwargs['product_id']['read_only'] = True
            
        return extra_kwargs
    
    