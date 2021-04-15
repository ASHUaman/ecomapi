from django.shortcuts import render
from .serialize import ProductSerializer
from .models import product
from rest_framework import viewsets
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('id')
    serializer_class = ProductSerializer