from django.db import models

from main_app.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=100
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="product")
