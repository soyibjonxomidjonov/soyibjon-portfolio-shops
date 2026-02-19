from django.urls import path
from .views import *

urlpatterns = [
    # Main page settings urls
    path('', dashboard_main, name='dashboard_home'),
    path('<int:shop_id>/', dashboard_main, name='dashboard_id'),


#     Shops page settings urls
    path('shops/', dashboard_shops, name='shops'),
    path('shops/<int:shop_id>/', dashboard_shop, name='shops_id'),
    path('shop/create/', dashboard_shop_create, name='shop_create'),
    path('shop/delete/<int:shop_id>', dashboard_shop_delete, name='shop_delete'),
    path('shop/edit/<int:shop_id>', dashboard_shop_edit, name='shop_edit'),

#     Products page settings urls
    path('products/', dashboard_products, name='products'),
    path('products/<int:shop_id>/', dashboard_products, name='products_shop'),
    path('product/<int:product_id>/', dashboard_product, name='product_id'),
    path('product/create/', dashboard_product_create, name='product_create'),
    path('product/edit/<int:product_id>/', dashboard_product_edit, name='product_edit'),
    path('product/delete/<int:product_id>/', dashboard_product_delete, name='product_delete'),

    #     Orders page settings urls
    path('orders/', dashboard_orders, name='orders'),
    path('orders/<int:shop_id>/', dashboard_orders, name='orders_shop'),
    path('order/<int:shop_id>/<int:order_id>/', dashboard_order, name='order_id'),
    path('order/edit/<int:shop_id>/<int:order_id>/', dashboard_order_edit, name='order_edit'),
    path('order/delete/<int:order_id>/', dashboard_order_delete, name='order_delete'),

]
