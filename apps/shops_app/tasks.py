import time
import requests
from django.conf import settings
from celery import shared_task
from .models.shop import Shop




@shared_task
def send_telegram_notification(order_id, products, customer, phone_number, address, total_price, created_at, status,
                               bot_token, chat_id):

    method = 'sendMessage'
    message_text = (
        f"📦 New order: {order_id}\n"
        f"📊 Status: {status}\n"
        f"💰 Total price: {total_price} so'm\n\n"
        f"👤 Client: {customer}\n"
        f"📞 Tel: {phone_number}\n"
        f"📍 Address: {address}\n\n"
        f"🛍 Products:\n{products}\n"
        f"📅 Created at: {created_at}"
    )
    try:
        response = requests.post(
            url=f"https://api.telegram.org/bot{bot_token}/{method}",
            data={
                "chat_id": chat_id,
                "text": message_text
            },
            timeout=10
        ).json()
        res_data = response
        print(f"Telegram javobi: {res_data}")  # Nima bo'layotganini ko'rish uchun
        if not res_data.get('ok'):
            print(f"Telegram yubormadi: {res_data.get('description')}")
    except Exception as e:
        print(f'Xatolik {e}')