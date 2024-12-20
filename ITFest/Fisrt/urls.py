from django.urls import path
from .views import UserViewSet, CategoryView, OrderView, CustomerDetailAPIView, ProductListCreateAPIView, \
    ProductDetailAPIView, view_cart, add_to_cart, remove_from_cart, get_products

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('cat/', CategoryView.as_view({'get': 'list'}), name='category'),
    path('order/', OrderView.as_view({'get': 'list'}), name='order'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('product_create/', ProductListCreateAPIView.as_view(), name='product-create'),
    path('products/', get_products, name='get_products'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_from_cart, name='cart-remove'),
    path('cart/view/', view_cart, name='cart-view'),

]
