from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('api/signup/', views.SignUp.as_view(), name='signup'),
    path('api/login/', views.Login.as_view(), name='login'),
]