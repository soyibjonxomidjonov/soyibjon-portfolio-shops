from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from apps.shops_app.forms import ProductForm
from apps.shops_app.services.decorators import login_decorator
from apps.dashboard.services import get_products, get_product, get_shops, get_shop
from apps.shops_app.models import Product, Shop


@login_decorator
def dashboard_products(request, shop_id=None):
    shops = get_shops(request.my_user.id)
    ctx = {}
    if shop_id:
        choose_shop_products = Product.objects.filter(shop_id=shop_id)
        current_shop = get_object_or_404(Shop, id=shop_id)
        ctx['current_shop'] = current_shop
        ctx['current_shop_products'] = choose_shop_products
    ctx['shops'] = shops
    ctx['shop_id'] = shop_id
    return render(request, "dashboard/products/list.html", ctx)

@login_decorator
def dashboard_product(request, product_id):
    ctx = {}
    choose_product = Product.objects.get(pk=product_id)
    ctx['product'] = choose_product
    ctx['shop'] = get_shop(choose_product.shop_id)
    return render(request, 'dashboard/products/form.html', ctx)


@login_decorator
def dashboard_product_create(request):
    owner_shops = Shop.objects.filter(owner=request.my_user)
    if not owner_shops.exists():
        return HttpResponse("Sizda do'kon mavjud emas. Iltimos, avval do'kon yarating.")
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.my_user)
        if form.is_valid():
            form.save()
            return redirect('products')

    else:
        form = ProductForm(user=request.my_user)
    ctx = {
        'form': form,
        'owner_shops': owner_shops
    }

    return render(request, 'dashboard/products/create.html', ctx)

# @login_decorator
# def product_add(request):
#     owner_shops = Shop.objects.filter(owner=request.my_user)
#     if not owner_shops.exists():
#         return HttpResponse("Sizda do'kon mavjud emas. Iltimos, avval do'kon yarating.")
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES, user=request.my_user)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             print(form.errors)
#     else:
#         form = ProductForm(user=request.my_user)
#
#     return render(request, "forms/product.html", {'form': form, 'owner_shops': owner_shops})


@login_decorator
def dashboard_product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    shop = get_object_or_404(Shop, pk=product.shop_id)

    if request.method == 'POST':
        # Oddiy request.POST bilan formani yaratamiz
        form = ProductForm(request.POST, request.FILES, instance=product)

        # MANA BU MUHIM: Formadan shop maydonini olib tashlaymiz
        # Shunda Django "shop qani?" yoki "bu shop ro'yxatda yo'q" deb so'ramaydi
        if 'shop' in form.fields:
            del form.fields['shop']

        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.shop = shop  # Shopni qo'lda biriktiramiz
            updated_product.save()
            return redirect('products_shop', shop_id=shop.id)
        else:
            print("Form xatolari:", form.errors)
    else:
        form = ProductForm(instance=product)

    ctx = {
        "product": product,
        "form": form,
        'shop': shop,
    }
    return render(request, 'dashboard/products/form.html', ctx)


@login_decorator
def dashboard_product_delete(request, product_id):
    model = get_object_or_404(Product, pk=product_id)
    shop_id = model.shop_id
    model.delete()
    return redirect('products_shop', shop_id=shop_id)