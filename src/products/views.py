#from django.views import ListView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import  Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,  *args, **kwargs):
        request = self.request
        return  Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self,  *args, **kwargs):
        request = self.request
        return  Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,"products/list.html",context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request =self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product,slug=slug,active=True)
        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not found.")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404

        return instance

class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request =self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.object.get(pk=pk, featured=True) #id
    #instance = get_object_or_404(Product, pk=pk, featured=True)

    # try:
    #     instance = Product.object.get(pk=pk)
    # except Product.DoesNotExist:
    #     print("No product here")
    #     raise Http404("Product does not exist")
    # except:
    #     print("huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # print(instance)
    # qs = Product.object.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    context = {
        'object' : instance
    }
    return render(request,"products/detail.html", context)