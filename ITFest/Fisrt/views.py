from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from tutorial.quickstart.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User, Product, Order, OrderItem, Customer, Category
from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = UserAPIListPagination
    # authentication_classes = [TokenAuthentication]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['created_at']


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(['POST'])
def add_to_cart(request, pk):
    if not hasattr(request.user, 'customer') or not request.user.customer:
        return Response({'error': 'Customer profile not found'}, status=400)

    if not request.user.customer:
        return Response({'error': 'Customer not found for this user'}, status=status.HTTP_400_BAD_REQUEST)

    product = get_object_or_404(Product, id=pk)
    order, created = Order.objects.get_or_create(customer=request.user.customer, is_active=True)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return Response({'message': 'Product added to cart successfully!'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    product_data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'image_url': product.image.url if product.image else None
        }
        for product in products
    ]
    return Response(product_data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove_from_cart(request, product_id):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        return Response({'error': 'Customer profile not found!'}, status=status.HTTP_400_BAD_REQUEST)

    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.filter(customer=customer, is_active=True).first()
    if order:
        order_item = OrderItem.objects.filter(order=order, product=product).first()
        if order_item:
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            return Response({'message': 'Product removed from cart successfully!'}, status=status.HTTP_200_OK)
    return Response({'error': 'Product not found in cart!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_cart(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        return Response({'error': 'Customer profile not found!'}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.filter(customer=customer, is_active=True).first()
    if order:
        items = order.orderitem_set.all()
        cart_items = [{'product': item.product.name, 'quantity': item.quantity} for item in items]
        return Response({'cart': cart_items}, status=status.HTTP_200_OK)
    return Response({'cart': []}, status=status.HTTP_200_OK)
