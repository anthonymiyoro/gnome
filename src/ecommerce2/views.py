from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.conf.urls import url
from products.models import Product
from .forms import SellerProductForm
from django.core.urlresolvers import reverse
# from products.models import product


def about(request):
    return render(request, "about.html", {})


def new_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product = SellerProductForm(instance=product)
    if request.method == "POST":
        form = SellerProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('ProductDetailView', pk=product.pk)
    return render_to_response(request, 'seller.html', {'form': form})
    # else:

    #


    # images = ProductImage.objects.all()

