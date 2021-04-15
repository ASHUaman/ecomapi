from django.db import models
from category.models import category
# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    stocks = models.CharField(max_length=10)
    is_active = models.BooleanField(default= True , blank = True)
    image = models.ImageField(upload_to= 'images/', blank= True ,null = True)
    category = models.ForeignKey(category , on_delete = models.SET_NULL , blank= True ,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
