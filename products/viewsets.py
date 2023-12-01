from rest_framework.viewsets import ModelViewSet
from products.models.product import Product
from products.models.category import Category
from products.models.tag import Tag
from products.serialisers import ProductSerializer, ProductViewSerializer, CategoryWithProductsSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.all().select_related('category').prefetch_related('tags')
    def get_serializer_class(self):
        if self.request.method=='GET':
            return ProductViewSerializer
        else:
            return ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().prefetch_related('products')
    serializer_class = CategoryWithProductsSerializer