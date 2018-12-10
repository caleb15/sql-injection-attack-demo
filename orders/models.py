from django.db import models
from django.conf import settings


class Item(models.Model):
    name = models.CharField(
        max_length=100
    )

    price = models.FloatField()

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    item = models.ForeignKey(
        'orders.Item',
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.item} ({self.quantity})'

