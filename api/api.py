from ecom.models import Category,SubCategory,Product
from .serializers import CategorySerializer,SubCategorySerialsizer,ProductSerializer
from rest_framework import viewsets, permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SubCategorySerialsizer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer