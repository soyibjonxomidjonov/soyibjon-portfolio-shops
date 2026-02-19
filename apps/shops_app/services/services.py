from apps.shops_app.models import Product


def get_basket(request):
    basket = request.session.get('basket', {})

    cart_items = []
    total_price = 0

    for p_id, quantity in basket.items():
        try:
            product = Product.objects.get(id=p_id)
            item_total = product.price * quantity
            total_price += item_total
            cart_items.append(
                {
                    'product': product,
                    'quantity': quantity,
                    'item_total': item_total
                })
        except Product.DoesNotExist:
            continue

    return {'cart_items': cart_items, 'total_price': total_price}