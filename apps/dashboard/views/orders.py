from django.shortcuts import render, get_object_or_404, redirect
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
    ctx['shop_id'] = ctx['shop']['id']
    return render(request, 'dashboard/orders/form.html', ctx)


@login_decorator
def dashboard_order_delete(request, order_id):
    model = get_object_or_404(Order, pk=order_id)
    shop_id = model.shop_id
    model.delete()
    return redirect('orders_shop', shop_id=shop_id)


@login_decorator
def dashboard_order_edit(request, shop_id, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        # 1. HTML dan statusni olamiz
        new_status = request.POST.get('status')

        # 2. Ob'ektni yangilaymiz
        order.status = new_status
        order.save()

        # 3. Muvaffaqiyatli saqlangach, ro'yxatga qaytaramiz
        return redirect('orders_shop', shop_id=shop_id)

    # GET so'rovi uchun
    ctx = {
        'choose_order': order,
        'shop_id': shop_id,
    }
    return render(request, 'dashboard/orders/form.html', ctx)