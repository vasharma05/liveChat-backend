from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CompanyDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=256)
    company_email = models.EmailField()
    company_address = models.CharField(max_length=256)
    company_city = models.CharField(max_length=256)
    company_state = models.CharField(max_length=256)
    profile_pic = models.ImageField(default='', upload_to='profile_pic/')

    def __str__(self):
        return self.company_name