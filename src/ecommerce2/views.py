from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.conf.urls import url
from .forms import SellerProductForm
from django.core.urlresolvers import reverse


def about(request):
    return render(request, "about.html", {})


def new_product(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ProductDetailView', pk=post.pk)
    else:
        post = PostForm(instance=post)

    # images = ProductImage.objects.all()

    return render_to_response(request, 'seller.html', {'form': form})
