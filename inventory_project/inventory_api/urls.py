from django.urls import path
from .views import (
    ProductListCreateView, 
    ProductDetailView, 
    ProductSearchView,
    InventoryReportView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/<str:pk>/', ProductDetailView.as_view(), name='product-detail'),  
    path('report/', InventoryReportView.as_view(), name='inventory-report'),
]
