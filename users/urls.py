from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views

from django.contrib.auth.views import LoginView, LogoutView, login_required


app_name = 'users'

urlpatterns = [
    path('register/',views.register_view,name = 'register'),
    path('login/',LoginView.as_view(
                                    template_name='users/login.html',
                                    success_url= 'home/',
                                    ), name= 'login'),
    path('logout/',LogoutView.as_view(), name= 'logout'),
    path('profile/',views.UpdateProfileView.as_view(), name ='profile'),
]
