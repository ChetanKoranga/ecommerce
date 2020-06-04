from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from . import views

# app_name = "authentication"

urlpatterns = [
    # path("", include())
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
