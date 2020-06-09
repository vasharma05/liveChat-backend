from django.shortcuts import render

# rest framework
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

#serializers
from .serializers import UserSerializer, CompanySerializer
# models
from .models import CompanyDetail
from django.contrib.auth.models import User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

# class LoginView(APIView)