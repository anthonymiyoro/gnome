from django.contrib import admin

# Register your models here.

from .models import UserCheckout, UserAddress, Order
from products.models import Product

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["order_total", "shipping_total_price", "status"]
    class Meta:
        model = Order


admin.site.register(UserCheckout)


admin.site.register(UserAddress)

admin.site.register(Order, OrderModelAdmin)