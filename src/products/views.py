from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.

from .models import Product

class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print context
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def product_detail_view_func(request, id):
    product_instance = Product.objects.get(id=id)
    template = "products/product_detail.html"
    context = {
        "object": product_instance
    }
    return render(request, template, context)
