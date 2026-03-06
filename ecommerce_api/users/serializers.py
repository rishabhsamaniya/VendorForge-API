from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']

        )
        return user
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        tokens = self.get_tokens(instance)
        data['tokens'] = tokens
        return data
    
    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),

        }
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #custom claims
        token['username'] = user.username
        token['role'] = user.role

        return token
    
    