from django.db import models
from pages.models import Product
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.id

    class Meta: 
        ordering = ('date_added',)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    

    def sub_total(self):
        return self.product.price*self.quantity
    
    def __str__(self):
        return self.product



