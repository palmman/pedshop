from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pages.models import Product
from cart.models import Cart, CartItem

# Create your views here.

def cart_display(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, id):
    product = Product.objects.get(pk=id)
    try:
        cart = Cart.objects.get(cart_id=cart_display(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_display(request))
        cart.save()

    try:
        cart_item=CartItem.objects.get(product=product, cart=cart)
        #if cart_item.quantity<cart_item.product.stock :
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()

    return redirect('shop')


def cart(request):
    total = 0
    counter = 0
    cart_items = None
    try:
        cart = Cart.objects.get(cart_id=cart_display(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total+=(item.product.price*item.quantity)
            counter+=item.quantity
    except Exception as e :
        pass
        
    return render(request, 'cart/cart.html', 
    dict(cart_items=cart_items, total=total, counter=counter))


def remove_cart(request, id):
    cart = Cart.objects.get(cart_id=cart_display(request))
    product = get_object_or_404(Product, pk=id)
    cart_Item = CartItem.objects.get(product=product, cart=cart)
    cart_Item.delete()
    return redirect('cart')

