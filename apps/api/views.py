from django_filters import rest_framework as django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from apps.api.permissions import IsOwnerOrReadOnly
from apps.api.serializers import OrderSerializer, ProductSerializer, ShopSerializer, UserSerializer
from apps.shops_app.models import Order, Product, Shop, User
from apps.api.filters import ProductFilter, OrderFilter, ShopFilter, UserFilter


# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 3


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = OrderFilter
    search_fields = ['first_name', 'phone_number', 'address']
    pagination_class = CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'price']
    pagination_class = CustomPagination

class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ShopFilter
    search_fields = ['name', 'description', 'address']
    pagination_class = CustomPagination

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = UserFilter
    search_fields = ['first_name', 'username', 'gmail']
    pagination_class = CustomPagination