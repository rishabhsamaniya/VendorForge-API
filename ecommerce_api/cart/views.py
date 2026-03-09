from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .models import Cart, CartItem
from products.models import Product

# Create your views here.

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = Product.objects.get(id=product_id)
        
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product

        )

        if not created:
            cart_item.quantity += int(quantity)

        cart_item.save()

        return Response({"message": "Product Added To Cart"})
    

class ViewCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        cart, created = Cart.objects.get_or_create(user=request.user)

        serializer = CartSerializer(cart)

        return Response(serializer.data)