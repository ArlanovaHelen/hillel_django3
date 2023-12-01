from django.contrib import admin

# Register your models here.
from products.models.product import Product
from products.models.category import Category
from products.models.tag import Tag
from products.models.order import Order
from products.models.order_product import OrderProduct
from products.models.store import Store
from products.models.store_inventory import StoreInventory

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Store)
admin.site.register(StoreInventory)
