from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Property(models.Model):
    class Status(models.TextChoices):
        FINISHED = 'finished', _('Finished')
        CLOSED = 'closed', _('Closed')
        DEVELOPING = 'developing', _('Developing')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DEVELOPING,
    )

    class PropertyType(models.TextChoices):
        HOUSE = 'house', _('House')
        BUILDING = 'building', _('Building')
        CELLAR = 'cellar', _('Cellar')
    property_type = models.CharField(
        max_length=10,
        choices=PropertyType.choices,
        default=PropertyType.BUILDING,
    )
    name = models.CharField(max_length=200)
    amount_brick = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Price(models.Model):
    value = models.PositiveIntegerField()
    property = models.ForeignKey('Property', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property.name} - {self.value}"


class Brick(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)


class Basket(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.customer.username}"


class Item(models.Model):
    amount_brick = models.PositiveIntegerField()
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
