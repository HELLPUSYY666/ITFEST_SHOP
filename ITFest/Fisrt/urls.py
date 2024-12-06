from django.urls import path
from .views import UserViewSet, CategoryView, OrderView, CustomerDetailAPIView, ProductListCreateAPIView, \
    ProductDetailAPIView, view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('cat/', CategoryView.as_view({'get': 'list'}), name='category'),
    path('order/', OrderView.as_view({'get': 'list'}), name='order'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('product_create/', ProductListCreateAPIView.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='cart-add'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='cart-remove'),
    path('cart/view/', view_cart, name='cart-view'),

]
