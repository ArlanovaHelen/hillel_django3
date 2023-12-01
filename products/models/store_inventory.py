from django.db import models
#from products.models.product import Product
#from products.models.store import Store

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError('Price cannot be negative.')

class StoreInventory(models.Model):
    store = models.ForeignKey('products.Store', on_delete=models.CASCADE, related_name='store_inventory')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='store_inventory')
    quantity = models.FloatField(validators=[non_negative_validator], null=True)
    county_of_origin = models.CharField(max_length=220, null=True)

    def __str__(self):
        return f'{self.product.name} x {self.store.name}'