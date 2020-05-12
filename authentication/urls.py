from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from . import views

urlpatterns = [
    # path("", include())
    path('', views.index, name='index'),
    path('register', views.register, name='register')
]
