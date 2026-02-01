from django.shortcuts import render
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import *


@login_decorator
def dashboard_main(request, shop_id=None):
    shops = get_shops(request.my_user.id)
    ctx = {}
    if shop_id:
        ctx['products_count'] = len(get_products(shop_id))
        ctx['orders_count'] = len(get_orders(shop_id))

    ctx['shops'] = shops
    ctx['shops_count'] = len(shops)
    ctx['current_shop'] = next((s for s in shops if s['id'] == shop_id), None)
    return render(request, "dashboard/main/main.html", ctx)



@login_decorator
def dashboard_shops(request, shop_id=None):
    shops = get_shops(request.my_user.id)
    ctx = {}
    if shop_id:
        choose_shop = get_shop(shop_id)
        ctx['current_shop'] = choose_shop
    ctx['shops'] = shops
    return render(request, "dashboard/shops/list.html", ctx)