from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image= serializers.ImageField( max_length=None ,allow_null=True ,allow_empty_file=False, required=False )
    class Meta:
        model = product
        fields = ['id','name','desc', 'price', 'image','category']