from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    """API view to list all products or create a new product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def post(self, request, *args, **kwargs):
        """Handle POST request for creating a new product."""
        # Check if product_id is in request data
        if 'product_id' not in request.data:
            return Response(
                {"error": "Missing required field: product_id"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if product with given ID already exists
        product_id = request.data['product_id']
        if Product.objects.filter(product_id=product_id).exists():
            return Response(
                {"error": f"Product with ID '{product_id}' already exists"},
                status=status.HTTP_409_CONFLICT
            )
        
        return super().post(request, *args, **kwargs)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        """Handle PUT request for updating a product."""
        instance = self.get_object()
        
        # Check if at least one field to update is provided
        update_fields = set(request.data.keys()) & {'name', 'price', 'quantity'}
        if not update_fields:
            return Response(
                {"error": "No updates specified"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Partial update to only change specified fields
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)

class ProductSearchView(generics.ListAPIView):
    """API view to search for products."""
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        """Return queryset based on search query."""
        query = self.request.query_params.get('q', '')
        if query:
            return Product.objects.filter(
                Q(product_id__icontains=query) | Q(name__icontains=query)
            )
        return Product.objects.none()

class InventoryReportView(APIView):
    """API view to generate inventory report."""
    def get(self, request):
        """Handle GET request for inventory report."""
        products = Product.objects.all()
        
        # Format product details
        report_data = []
        for product in products:
            report_data.append(
                f"ID: {product.product_id}, "
                f"Name: {product.name}, "
                f"Price: ${float(product.price):.2f}, "
                f"Quantity: {product.quantity}"
            )
        
        return Response({
            'success': True,
            'total_products': products.count(),
            'data': report_data
        })
