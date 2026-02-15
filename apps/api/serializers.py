from rest_framework import serializers
from apps.shops_app.models import Product, Order, Shop, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'image', 'description', 'price', 'stock', 'unity', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'phone_number', 'shop', 'address','items_json' ,'total_price',
                  'created_at', 'status']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'owner', 'name', 'description', 'address', 'bot_token', 'chat_id', 'slug', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'created_at']
        ref_name = "MyCustomUserSerializer"

