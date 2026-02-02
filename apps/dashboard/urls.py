from django.urls import path
from .views import *

urlpatterns = [
    # Main page settings urls
    path('', dashboard_main, name='dashboard_home'),
    path('<int:shop_id>/', dashboard_main, name='dashboard_id'),


#     Shops page settings urls
    path('shops/', dashboard_shops, name='shops'),
    path('shops/create', dashboard_shop_create, name='shop_create'),
    path('shops/delete/<int:shop_id>', dashboard_shop_delete, name='shop_delete'),
    path('shops/edit/<int:shop_id>', dashboard_shop_edit, name='shop_edit'),
    path('shops/<int:shop_id>/', dashboard_shop, name='shops_id'),

#     Products page settings urls
    path('products/', dashboard_products, name='products'),
    path('products/<int:shop_id>/', dashboard_products, name='products_shop'),
    path('product/<int:shop_id>/<int:product_id>/', dashboard_product, name='product_id'),

#     Orders page settings urls
    path('orders/', dashboard_orders, name='orders'),
    path('orders/<int:shop_id>/', dashboard_orders, name='orders_shop'),
    path('order/<int:shop_id>/<int:order_id>/', dashboard_order, name='order_id'),
]
