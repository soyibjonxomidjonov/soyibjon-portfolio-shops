from django_filters import rest_framework as django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.permissions import IsOwnerOrReadOnly
from apps.api.serializers import OrderSerializer, ProductSerializer, ShopSerializer, UserSerializer
from apps.shops_app.models import Order, Product, Shop, User
from apps.api.filters import ProductFilter, OrderFilter, ShopFilter, UserFilter


# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 3


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = OrderFilter
    search_fields = ['first_name', 'phone_number', 'address']
    pagination_class = CustomPagination
    def get_queryset(self):
        return Order.objects.filter(shop__owner=self.request.user.id)


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'price']
    pagination_class = CustomPagination
    def get_queryset(self):
        return Product.objects.filter(shop__owner=self.request.user.id)
    def perform_create(self, serializer):
        shop = serializer.validated_data.get('shop')
        if shop.owner != self.request.user:
            raise ValidationError({"shop": "Bu do'kon sizga tegishli emas yoki mavjud emas."})
        serializer.save()

class ShopViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ShopSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ShopFilter
    search_fields = ['name', 'description', 'address']
    pagination_class = CustomPagination
    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user.id).order_by('-created_at')
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = UserFilter
    search_fields = ['first_name', 'username', 'gmail']
    pagination_class = CustomPagination
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)