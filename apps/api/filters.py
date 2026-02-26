from django_filters import rest_framework as django_filters  #pip install django-filter
from apps.shops_app.models import Shop, Order, Product, User


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    shop = django_filters.NumberFilter(field_name="shop__id")
    class Meta:
        model = Product
        fields = ['shop', 'min_price', 'max_price', 'name']


class ShopFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    owner = django_filters.NumberFilter(field_name="owner__id")
    slug = django_filters.CharFilter(field_name="slug", lookup_expr='icontains')
    class Meta:
        model = Shop
        fields = ['name', 'owner', 'slug']

class OrderFilter(django_filters.FilterSet):
    shop = django_filters.CharFilter(field_name="shop__name", lookup_expr='icontains')
    status = django_filters.CharFilter(field_name="status", lookup_expr='icontains')
    shop_id = django_filters.NumberFilter(field_name="shop__id")


    class Meta:
        model = Order
        fields = ['shop', 'shop_id', 'status']

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="username", lookup_expr='icontains')
    gmail = django_filters.CharFilter(field_name="gmail", lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['name', 'gmail']