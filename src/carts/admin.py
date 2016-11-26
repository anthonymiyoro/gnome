from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem
from products.models import Product


class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline,
    ]
    list_filter = ["items"]

    class Meta:
        model = Cart, Product


class ProductAdmin2(admin.ModelAdmin):
    list_filter = ["title"]

    class Meta:
        model = Product

admin.site.register(Cart, CartAdmin)
