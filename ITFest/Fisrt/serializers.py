from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from .models import User, Category, Product, Order, OrderItem, Customer


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'groups', 'mobile', 'date_joined', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'first_name': {'validators': [MaxLengthValidator(240)]},
            'last_name': {'validators': [MaxLengthValidator(240)]},

        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError({"password": "This field is required."})

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_full_name(self, obj):
        first_name = obj.first_name or ''
        last_name = obj.last_name or ''
        return f"{first_name} {last_name}".strip()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
