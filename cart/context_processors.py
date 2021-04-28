from .models import *
from .views import *

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id=cart_display(request))
            cart_item = CartItem.objects.all().filter(cart=cart[:1])
            for item in cart_item:
                item_count += item.quantity

        except Cart.DoesNotExist :
            item_count = 0
    return dict(item_count=item_count)