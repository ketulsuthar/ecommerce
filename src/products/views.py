from django.views import ListView
from django.shortcuts import render

# Create your views here.
from .models import  Product

class ProductListView(ListView):
    queryset = Product.objects.all()