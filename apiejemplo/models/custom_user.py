from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    tipo = models.CharField(max_length=20, null=True, blank=True)
    carnet = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username
