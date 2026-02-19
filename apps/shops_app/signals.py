from django.conf import settings
import requests
from .models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import send_telegram_notification


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        items = ''
        for item in instance.items_json:
            name = item.get('product_name', 'Nomalum')
            qty = item.get('quantity', 0)
            unit = item.get('unity', 'dona')  # Agar kg bo'lsa, kg chiqadi
            total = item.get('item_total', 0)

            items += f"🔹 {name}: {qty} {unit} — {total} so'm\n"
        tg_token = instance.shop.bot_token
        tg_id = instance.shop.chat_id
        send_telegram_notification.delay(
            order_id=instance.id,
            products=items,
            customer=instance.first_name,
            phone_number=instance.phone_number,
            address=instance.address,
            total_price=instance.total_price,
            created_at=str(instance.created_at),
            status=instance.status,
            bot_token=tg_token,
            chat_id=tg_id,
        )