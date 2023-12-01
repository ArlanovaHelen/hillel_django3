from django.db import models
from products.models.order_product import OrderProduct

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', through=OrderProduct)