from rest_framework import serializers
from .models import Product, Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.ReadOnlyField(source='category.name')
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ["vendor"]




