from django.shortcuts import render

# rest framework
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
#serializers
from .serializers import UserSerializer, CompanySerializer
# models
from .models import CompanyDetail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class Login(APIView):

    permission_classes=[]
    
    def post(self, request, format=None):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is None:
            message = {}
            message['detail'] = 'Email or password is incorrect'
            return Response(message, status=400)
        else:
            message = {}
            token = Token.objects.get_or_create(user = user)
            message['token'] = token[0].key
            message['detail'] = CompanySerializer(user.companydetail).data
            return Response(message, status = 200)

        

class SignUp(APIView):
    # get_extra_actions = {}
    permission_classes = []

    def post(self, request, format=None):
        try:
            user = User.objects.create(first_name=request.data['name'],username = request.data['username'],email= request.data['email'], password = request.data['password'])
            data = dict({'message': 'success'})
        except:
            data = dict({'message': 'Username already exits'})
            return Response(data, status=status.HTTP_201_CREATED)

        token = Token.objects.create(user=user)

        CompanyDetail.objects.create(
            user = user,
            company_name = request.data['companyName'],
            company_email = request.data['companyEmail'],
            company_address = request.data['companyAddress'],
        )
        data = dict({
            'message': 'success',
            })
        return Response(data, status=status.HTTP_201_CREATED)
