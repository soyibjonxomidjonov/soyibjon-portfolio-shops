from django.db import models
from .shop import Shop



UNIT_CHOICES = [
    ('kg', 'Kilogramm'),
    ('dona', 'Dona/Shtat'),
    ('litr', 'Litr'),
    ('metr', 'Metr'),
]

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(default=0)
    unity = models.CharField(max_length=10, choices=UNIT_CHOICES, default='dona')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name