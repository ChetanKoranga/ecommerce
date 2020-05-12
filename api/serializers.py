from rest_framework import serializers
from ecom.models import Category,SubCategory,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubCategorySerialsizer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"