from django.urls import path
from . import views

app_name = "ecom"

urlpatterns = [
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('blog-detail', views.blogdetail, name='blog-detail'),
]
