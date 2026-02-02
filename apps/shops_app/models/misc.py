from django.db import models
from .shop import Shop

class Order(models.Model):
    first_name = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=False)
    items_json = models.JSONField(default=list)
    total_price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='yangi', db_index=True)

    def __str__(self):
        return self.first_name