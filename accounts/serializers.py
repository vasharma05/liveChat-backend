from django.contrib.auth.models import User
from .models import CompanyDetail
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    profile_pic = serializers.ImageField(required=False)
    class Meta:
        model = CompanyDetail
        fields = ['user', 'company_name', 'company_email', 'profile_pic', 'company_address']