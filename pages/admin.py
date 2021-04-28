from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 35px;" />' .format(object.product_photo.url))

        thumbnail.short_description = 'Photo'

    list_display = ('thumbnail','product_name', 'price', 'sku', 'category', 'brand')
    list_editable = ('price', 'category')
    list_display_links = ('product_name', 'thumbnail')
    search_fields = ('product_name', 'sku', 'category', 'brand')
    list_filter = ('category', 'brand')


admin.site.register(Product, ProductAdmin)