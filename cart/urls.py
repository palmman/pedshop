from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('add/<int:id>', views.add_cart, name='add_cart'),
    path('remove/<int:id>', views.remove_cart, name='remove_cart'),
]