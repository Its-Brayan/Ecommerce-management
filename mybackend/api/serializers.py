from rest_framework import serializers
from .models import *

from django.contrib.auth.hashers import make_password



class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterUser
        fields = '__all__'
class RegisterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= RegisterCategory
        fields = '__all__'
class RegisterBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterBrand
        fields = '__all__'
class AddProductSerializer(serializers.ModelSerializer):  
     product_category = serializers.CharField(source="product_category.category_name", read_only=True)
     product_brand = serializers.CharField(source="product_brand.brand_name", read_only=True)
     class Meta:
        model = Addproduct
        fields = '__all__'

    

