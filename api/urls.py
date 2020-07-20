from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('categories', api.CategoryViewSet, 'category')
router.register('subcategories', api.SubCategoryViewSet, 'subcategory'),
router.register('products', api.ProductViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
]
