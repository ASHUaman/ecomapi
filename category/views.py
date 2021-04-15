from django.shortcuts import render
from rest_framework import viewsets
from .serialize import CategorySerializer
from .models import category
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all().order_by('name')
    serializer_class = CategorySerializer