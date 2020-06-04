from django.urls import path, include
from rest_framework import routers
from api import api
from . import views

app_name = "ecom"

router = routers.DefaultRouter()
router.register('api/categories', api.CategoryViewSet, 'category')
router.register('api/subcategories', api.SubCategoryViewSet, 'subcategory'),
router.register('api/products', api.ProductViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
    path('home', views.index, name='index')
]
