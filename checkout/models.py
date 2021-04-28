from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.


class ShipppingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zipcode = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + self.firstName

    class Meta:
        verbose_name_plural = 'ShipppingAddress'
