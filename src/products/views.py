from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.

from .models import Product, Variation

class VariationListView(ListView):
    model = Variation
    queryset = Variation.objects.all

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print context
        return context

    # collect user input then search through product list
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title_icontains=query) |
                Q(description_icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()

            except:
                pass

        return qs


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print context
        return context

    # collect user input then search through product list
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title_icontains=query) |
                Q(description_icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()

            except:
                pass

        return qs


class ProductDetailView(DetailView):
    model = Product


def product_detail_view_func(request, id):
    product_instance = Product.objects.get(id=id)
    template = "products/product_detail.html"
    context = {
        "object": product_instance
    }
    return render(request, template, context)
