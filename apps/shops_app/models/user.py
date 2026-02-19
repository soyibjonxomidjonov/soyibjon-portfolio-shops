from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    # first_name = models.CharField(max_length=30, null=True, blank=True)
    # email = models.EmailField(null=False, blank=False)
    # password = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name if self.first_name else self.username