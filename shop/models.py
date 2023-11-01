from django.db import models
from django.contrib.auth.models import AbstractUser

class Order(models.Model):
    date = models.DateField()
    contacts = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)