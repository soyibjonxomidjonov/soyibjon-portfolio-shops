from contextlib import closing
from django.db import connection

def dictfetchall(cursor):
    columns =[col[0] for col in cursor.description]
    return[
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns =[col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_shops(owner_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_shop WHERE owner_id = %s""", [owner_id])
        shops = dictfetchall(cursor)
        return shops


def get_products(shop_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_product WHERE shop_id = %s""", [shop_id])
        products = dictfetchall(cursor)
        return products


def get_orders(shop_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_order WHERE shop_id = %s""", [shop_id])
        orders = dictfetchall(cursor)
        return orders




def get_shop(shop_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_shop WHERE id = %s""", [shop_id])
        shop = dictfetchone(cursor)
        return shop


def get_product(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_product WHERE id = %s""", [product_id])
        product = dictfetchone(cursor)
        return product


def get_order(order_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM shops_app_order WHERE id = %s""", [order_id])
        order = dictfetchone(cursor)
        return order
















