from django.db import models
from .user import User
from django.utils.text import slugify


class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    bot_token = models.CharField(max_length=500, blank=True, null=True)
    chat_id = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.owner.username}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"