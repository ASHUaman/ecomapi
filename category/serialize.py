from .models import category

from rest_framework import serializers
from .models import category
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = category
        fields = ('name','desc') 