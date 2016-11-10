from django.shortcuts import render
from django.conf.urls import url
from .forms import SellerProductForm


def about(request):
    return render(request, "about.html", {})


def new_product(request):
    form = SellerProductForm()
    return render(request, 'templates/seller.html', {'form': form})
