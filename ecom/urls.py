from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ecom"

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('blog-detail', views.blogdetail, name='blog-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
