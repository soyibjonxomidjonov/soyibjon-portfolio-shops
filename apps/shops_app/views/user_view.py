from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.shops_app.forms import OrderForm
from apps.shops_app.models import Shop, Product
from apps.shops_app.services.services import get_basket
from apps.shops_app import signals

def view_shop_page(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    products = shop.products.all()
    cart_data = get_basket(request)
    ctx = {
        "shop": shop,
        "products": products,
    }
    ctx.update(cart_data)
    return render(request, 'user/user_main.html', ctx)


def view_product_page(request, shop_slug, product_id):
    shop = get_object_or_404(Shop, slug=shop_slug)
    product = Product.objects.get(id=product_id, shop=shop)
    cart_data = get_basket(request)
    ctx = {
        "shop": shop,
        "product": product
    }
    ctx.update(cart_data)
    return render(request, 'user/user_product.html', ctx)



def order_save_page(request, shop_slug):
    basket = get_basket(request)
    now_shop = get_object_or_404(Shop, slug=shop_slug)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(commit=False)
            order.shop = now_shop

            if not basket['cart_items']:
                return redirect('shop', shop_slug=shop_slug)

            save_items = []

            for item in basket['cart_items']:
                save_items.append({
                    'product_name': item['product'].name,
                    'price': float(item['product'].price),
                    'quantity': item['quantity'],
                    "unity": item['product'].unity,
                    'item_total': float(item['item_total']),
                })

            order.items_json = save_items
            order.total_price = basket['total_price']
            order.save()
            request.session['basket'] = {}
            messages.success(request, f"Buyurtmangiz {now_shop.name.title()} do'koni tomonidan qabul qilindi!")
            return redirect('shop', shop_slug=shop_slug)
        else:
            print(form.errors)
    else:
        form = OrderForm()

    ctx = {
        'form': form,
        'shop': now_shop,
        'cart_items': basket['cart_items'],
        'total_price': basket['total_price'],
    }

    return render(request, 'user/user_order.html', ctx)


































