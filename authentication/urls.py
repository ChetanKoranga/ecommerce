from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from . import views

app_name = "authentication"

urlpatterns = [
    # path("", include())
    path('login', views.login, name='login'),
    path('logout', views.signout, name='logout'),
    path('register', views.register, name='register'),
    path('getcookie', views.setCookie, name='getcookie'),
    path('savesession', views.save_session_data, name="save-session"),
    path('accesssession', views.access_session_data, name='access-session'),
    path('deletesession', views.delete_session_data, name='delete-session')
]
