from rest_framework import serializers
from .models import CustomUser  # Import your model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'