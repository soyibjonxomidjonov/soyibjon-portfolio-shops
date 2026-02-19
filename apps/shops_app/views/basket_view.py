from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from apps.shops_app.models import Shop



def add_to_basket(request, shop_slug, product_id):
    shop = get_object_or_404(Shop, slug=shop_slug)
    basket = request.session.get('basket', {})
    p_id = str(product_id)
    if p_id in basket:
        basket[p_id] += 1
    else:
        basket[p_id] = 1

    request.session['basket'] = basket
    request.session.modified = True

    return JsonResponse({'status': 'ok', 'cart_count': len(basket)})

def remove_basket(request, shop_slug, product_id):
    basket = request.session.get('basket', {})
    p_id = str(product_id)
    if p_id in basket:
        if basket[p_id] > 1:
            basket[p_id] -= 1
        else:
            del basket[p_id]
    request.session['basket'] = basket
    request.session.modified = True
    return JsonResponse({'status': 'ok'})

def delete_product(request, shop_slug, product_id):
    basket = request.session.get('basket', {})
    p_id = str(product_id)
    if p_id in basket:
        del basket[p_id]
    request.session['basket'] = basket
    request.session.modified = True
    return JsonResponse({'status': 'ok'})

def clear_basket(request, shop_slug):
    if 'basket' in request.session:
        del request.session['basket']
    request.session.modified = True
    return redirect('shop', shop_slug=shop_slug)




