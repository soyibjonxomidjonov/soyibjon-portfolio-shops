from django.shortcuts import render
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import get_orders, get_shops, get_shop
from apps.shops_app.models import Order


@login_decorator
def dashboard_orders(request, shop_id=None):
    shops = get_shops(request.my_user.id)
    ctx = {}
    if shop_id:
        current_shop_orders = Order.objects.filter(shop_id=shop_id)
        ctx['current_shop_orders'] = current_shop_orders
    ctx['shops'] = shops
    ctx['shop_id'] = shop_id
    return render(request, "dashboard/orders/list.html", ctx)

@login_decorator
def dashboard_order(request, shop_id, order_id):
    ctx = {}
    choose_order = Order.objects.get(pk=order_id)

    ctx['choose_order'] = choose_order
    ctx['shop'] = get_shop(shop_id)
    return render(request, 'dashboard/orders/form.html', ctx)