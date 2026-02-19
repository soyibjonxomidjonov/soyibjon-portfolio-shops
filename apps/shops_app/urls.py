from django.urls import path
from apps.shops_app.views import user_view, basket_view
from apps.shops_app.views import main, login, form_view

urlpatterns = [
    path('', main.main_page, name='main_page'),

    # Login, logout and register urls
    path('login/', login.login, name='login'),
    path('logout/', login.logout_page, name="logout_page"),

    # Saved form urls
    path('register/', login.register, name='register'),
    path('product_add/', form_view.product_add, name='product_add'),
    path('shop_add/', form_view.shop_add, name='shop_add'),

    # Project User-view urls
    path('shop/<slug:shop_slug>/<int:product_id>/', user_view.view_product_page, name='shop_product'),
    path('shop/<slug:shop_slug>/order/', user_view.order_save_page, name='order_save_page'),
    path('shop/<slug:shop_slug>/', user_view.view_shop_page, name='shop'),

    # Basket + and - url
    path('shop/<slug:shop_slug>/add-to-basket/<int:product_id>/', basket_view.add_to_basket, name='add_to_basket'),
    path('shop/<slug:shop_slug>/remove/<int:product_id>/', basket_view.remove_basket, name='remove_basket'),
    path('shop/<slug:shop_slug>/delete/<int:product_id>/', basket_view.delete_product, name='delete_product'),
    path('shop/<slug:shop_slug>/clear/', basket_view.clear_basket, name='clear_basket'),

]













#V1
# urlpatterns = [
#     path('', main.main_page, name='main_page'),
#     path('register/', register.user_register, name='register_page'),
#     path('login/', register.login_page, name='login_page'),
#     path('biznes_add/', businessmen_menu.add_biznes, name='add_biznes'),
#     path('product_add/', businessmen_menu.add_product, name='product_add_page'),
# ]