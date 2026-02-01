from django.urls import path
from .views import dashboard_main, dashboard_shops

urlpatterns = [
    # Main page settings urls
    path('', dashboard_main, name='dashboard_home'),
    path('<int:shop_id>/', dashboard_main, name='dashboard_id'),


#     Shops page settings urls
    path('shops/', dashboard_shops, name='shops'),
    path('shops/<int:shop_id>/', dashboard_shops, name='shops_id'),
]
