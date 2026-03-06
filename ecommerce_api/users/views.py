from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsVendor


# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Test Class 

class VendorOnlyView(APIView):
    permission_classes = [IsVendor]

    def get(self, request):
        return Response({"message": "Hello Vendor!"})