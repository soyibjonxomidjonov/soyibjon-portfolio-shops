from django.contrib import admin
from apps.shops_app.models import Product, User, Order, Shop
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Shop)
