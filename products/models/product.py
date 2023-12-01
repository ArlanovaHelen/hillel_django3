from django.db import models
from django.core.exceptions import ValidationError
from products.models.category import Category
from products.models.tag import Tag
from products.models.order_product import OrderProduct
from products.models.store import Store
from products.models.store_inventory import StoreInventory

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError('Price cannot be negative.')
class Product(models.Model):
    name = models.CharField(max_length=220)
    price = models.FloatField(validators=[non_negative_validator], null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    orders = models.ManyToManyField('products.Order', through=OrderProduct)
    stores = models.ManyToManyField('products.Store', through=StoreInventory)
    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return self.name