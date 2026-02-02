from django.shortcuts import render
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import get_shop, get_shops
from apps.shops_app.models import Shop



@login_decorator
def dashboard_shops(request):
    shops = get_shops(request.my_user.id)
    ctx = {
        'shops': shops
    }
    return render(request, "dashboard/shops/list.html", ctx)


@login_decorator
def dashboard_shop(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    ctx = {
        'shop': shop
    }
    return render(request, 'dashboard/shops/form.html', ctx)



# @login_decorator
























