from django.contrib import admin
from .models import Cart, CartItem
from django.utils.html import format_html

# Register your models here.



admin.site.register(Cart)

admin.site.register(CartItem)