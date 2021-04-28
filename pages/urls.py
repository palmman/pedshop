from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:id>', views.product, name='product'),
    path('category/<slug:pages_slug>/', views.shop, name='products_by_category'),
]
