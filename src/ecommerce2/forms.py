from django import forms
from django.db import models
from django.forms.models import modelformset_factory

from products.models import Product


class SellerProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
            "categories",
            "title",
        ]