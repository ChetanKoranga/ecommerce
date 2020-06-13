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
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('blog-detail', views.blogdetail, name='blog-detail')
]
