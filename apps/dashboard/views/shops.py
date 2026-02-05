from django.shortcuts import render, redirect, get_object_or_404
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import get_shop, get_shops
from apps.shops_app.models import Shop
from apps.shops_app.forms import ShopForm



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
        'model': shop,
        'shop': shop
    }
    return render(request, 'dashboard/shops/form.html', ctx)



@login_decorator
def dashboard_shop_create(request):
    model = Shop()
    form = ShopForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        shop = form.save(commit=False)
        shop.owner = request.my_user
        shop.save()
        return redirect('shops')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/shops/form.html', ctx)


@login_decorator
def dashboard_shop_edit(request, shop_id):
    model = get_object_or_404(Shop, pk=shop_id, owner_id=request.my_user.id)
    form = ShopForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('shops')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/shops/form.html', ctx)

@login_decorator
def dashboard_shop_delete(request, shop_id):
    model = Shop.objects.get(pk=shop_id)
    model.delete()
    return redirect('shops')
















