from django.shortcuts import render
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import get_products, get_product, get_shops, get_shop
from apps.shops_app.models import Product


@login_decorator
def dashboard_products(request, shop_id=None):
    shops = get_shops(request.my_user.id)
    ctx = {}
    if shop_id:
        choose_shop_products = Product.objects.filter(shop_id=shop_id)
        ctx['current_shop_products'] = choose_shop_products
    ctx['shops'] = shops
    ctx['shop_id'] = shop_id
    return render(request, "dashboard/products/list.html", ctx)

@login_decorator
def dashboard_product(request, shop_id, product_id):
    ctx = {}
    choose_product = Product.objects.get(pk=product_id)
    ctx['choose_product'] = choose_product
    ctx['shop'] = get_shop(shop_id)
    return render(request, 'dashboard/products/form.html', ctx)