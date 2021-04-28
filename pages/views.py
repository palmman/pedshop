from django.shortcuts import render, get_object_or_404
from pages.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def home(request):
    top_pro = Product.objects.order_by('-create_date')

    data = {
        'top_pro' : top_pro,
    }
    return render(request, 'pages/home.html', data)

def shop(request, pages_slug=None):

    categorise = None
    shop_all = None

    if pages_slug != None:
        categorise = get_object_or_404(Product, slug=pages_slug)
        shop_all = Product.objects.filter(category=categorise)
    else:
        shop_all = Product.objects.order_by('-create_date')
        catagories = Product.objects.all()
        paginator = Paginator(shop_all, 6)
        page = request.GET.get('page')
        page_shop = paginator.get_page(page)

    data = {
        'shop_all' : page_shop,
        'catagory' : catagories,
    }
    
    return render(request, 'pages/shop.html', data)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def product(request, id):

    singel_product = get_object_or_404(Product, pk=id)

    data = {
        'singel_product' : singel_product,
    }
    return render(request, 'pages/product.html', data)

