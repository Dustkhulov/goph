from rest_framework import serializers
from .models import *


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'