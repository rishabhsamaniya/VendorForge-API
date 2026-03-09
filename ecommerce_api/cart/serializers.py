from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer



class CartItemSerializer(serializers.ModelSerializer):

    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'product_detail']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']