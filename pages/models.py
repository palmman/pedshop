from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class Product(models.Model):

    category_choice = (
        ('Shoes', 'Shoes'),
        ('Clothes', 'Clothes'),
        ('Watches', 'Watches'),
        ('Electronics', 'Electronics'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = RichTextField()
    product_photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    product_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    product_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    product_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    product_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    sku = models.IntegerField()
    category = models.CharField(choices=category_choice, max_length=50)
    brand = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField()

    
    def __str__(self):
        return self.product_name