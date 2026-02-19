from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.shops_app.forms import ProductForm, ShopForm
from apps.shops_app.services.decorators import login_decorator
from apps.shops_app.models import Shop




@login_decorator
def product_add(request):
    owner_shops = Shop.objects.filter(owner=request.my_user)
    if not owner_shops.exists():
        return redirect('../dashboard/shop/create/')
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.my_user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = ProductForm(user=request.my_user)

    return render(request, "forms/product.html", {'form': form, 'owner_shops': owner_shops})



@login_decorator
def shop_add(request):
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.owner = request.my_user
            shop.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = ShopForm()

    return render(request, "forms/product.html", {'form': form})
