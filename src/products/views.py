#from django.views import ListView
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from .models import  Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,"products/list.html",context)