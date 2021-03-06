from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50 ,default= 'Anonymous')
    email = models.EmailField(max_length=100 , unique=True)

    username = None                                                         #remove username as login parameter
    USERNAME_FIELD = 'email'                                                #email is our default login parameter

    REQUIRED_FIELDS =[]

    phone = models.CharField(max_length=10, blank=True , null=True)

    session_token = models.CharField(max_length= 10, default = 0)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    


