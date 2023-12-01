from django.db import models
from products.models.store_inventory import StoreInventory
class Store(models.Model):
    name = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    opening_hours = models.CharField(max_length=220)
    products = models.ManyToManyField('products.Product', through = StoreInventory)
    delivery = models.BooleanField(null=True)

    def __str__(self):
        return self.name