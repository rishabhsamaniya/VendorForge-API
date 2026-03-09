from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer
from users.permissions import IsVendor

# Create your views here.

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    




class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsVendor]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter


    search_filter = ['description']
    ordering_filter = ['price', 'created_at']

class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)

class UploadProductImageView(APIView):
    permission_classes = [IsVendor]

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        image = request.FILES.get('image')
        product_image = ProductImage.objects.create(
            product=product,
            image=image
        )

        serializer = ProductImageSerializer(product_image)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
