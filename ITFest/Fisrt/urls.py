from django.urls import path
from .views import UserViewSet, CategoryView, OrderView, CustomerDetailAPIView, ProductListCreateAPIView, \
    ProductDetailAPIView

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('cat/', CategoryView.as_view({'get': 'list'}), name='category'),
    path('order/', OrderView.as_view({'get': 'list'}), name='order'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('product_create/', ProductListCreateAPIView.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
