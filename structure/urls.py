from django.contrib import admin
from django.urls import path, include
from .views import home , about

app_name = 'structure'

urlpatterns = [
    path('',home, name= 'home'),
    path('about/',about, name= 'about'),
]
