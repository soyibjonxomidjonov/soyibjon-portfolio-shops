from django_filters import rest_framework as django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.permissions import IsOwnerOrReadOnly
from apps.api.serializers import OrderSerializer, ProductSerializer, ShopSerializer, UserSerializer
from apps.shops_app.models import Order, Product, Shop, User
from apps.api.filters import ProductFilter, OrderFilter, ShopFilter, UserFilter
from rest_framework.response import Response


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
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'price']
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        shop = serializer.validated_data.get('shop')
        if shop.owner != self.request.user:
            raise ValidationError({"shop": "Bu do'kon sizga tegishli emas yoki mavjud emas."})
        serializer.save()
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(shop__owner=self.request.user.id)
        shop = self.request.query_params.get('shop')
        if shop:
            return Product.objects.filter(shop__id=shop)
        return Product.objects.none()

class ShopViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ShopSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ShopFilter
    search_fields = ['name', 'description', 'address']
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Shop.objects.filter(owner=self.request.user.id).order_by('-created_at')
        slug = self.request.query_params.get('slug')
        if slug:
            return Shop.objects.filter(slug=slug)
        return Shop.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

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

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def public_shop_by_slug(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
        serializer = ShopSerializer(shop, context={'request': request})
        return Response(serializer.data)
    except Shop.DoesNotExist:
        return Response({'detail': 'Not found'}, status=404)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def public_products_by_shop(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
        products = Product.objects.filter(shop=shop)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response({'results': serializer.data})
    except Shop.DoesNotExist:
        return Response({'results': []}, status=404)