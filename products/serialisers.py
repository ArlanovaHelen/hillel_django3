from rest_framework import serializers
from products.models.product import Product
from products.models.category import Category
from products.models.tag import Tag

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        category = CategorySerializer()
        fields = ('id', 'name', 'price', 'description', 'category', 'tags')

class ProductViewSerializer(ProductSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()



class CategoryWithProductsSerializer(CategorySerializer):
    products = ProductSerializer(many=True)
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ('products',)

