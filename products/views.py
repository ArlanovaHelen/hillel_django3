from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from products.models.product import Product

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world")

def count_product(request):
    count = Product.objects.count()
    return HttpResponse(f'ProductCount {count}')

def count_product_json(request):
    all_products = Product.objects.all()
    for product in all_products:
        products_json = {'name': product.name, 'price': product.price, 'description': product.description}
    return JsonResponse(products_json)

