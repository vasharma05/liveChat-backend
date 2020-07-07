from django.shortcuts import render

# rest framework
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
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
            message['error'] = 'Email or password is incorrect'
            return Response(message, status=203)
        else:
            message = {}
            token = Token.objects.get_or_create(user = user)
            message['token'] = token[0].key
            message['userDetails'] = CompanySerializer(user.companydetail,  context={'request': request}).data
            return Response(message, status = 200)

        

class SignUp(APIView):
    # get_extra_actions = {}
    permission_classes = []

    def post(self, request, format=None):
        print(request.data)
        try:
            user = User.objects.create(first_name=request.data['name'],username = request.data['username'],email= request.data['email'], password = request.data['password'])
        except:
            data = dict({'error': 'Username already exits'})
            return Response(data, status = 203)

        token = Token.objects.create(user=user)
        company = CompanySerializer(CompanyDetail.objects.create(
            user = user
            # company_name = request.data['companyName'],
            # company_email = request.data['companyEmail'],
            # company_address = request.data['companyAddress'],
            # profile_pic = request.data['profile_pic']
        ))
        data = dict({
            'message': 'success',
            'token': token.key,
            'userDetails' : company.data
            })
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def changePassword(request, format=None):
    try:
        try:
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save
            return Response({'detail': 'success'}, status=200)
        except:
            return Response({'detail':'Incorrect username'}, status=200)
    except:
        return Response({'detail':'Something went wrong'}, status=500)