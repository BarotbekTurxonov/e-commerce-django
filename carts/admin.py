from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']

@admin.register(CartItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']

