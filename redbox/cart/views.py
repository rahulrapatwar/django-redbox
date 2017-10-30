from django.shortcuts import render,get_object_or_404
from .models import Cart
from shop.models import Game,Movie

# Create your views here.
def cart(request):
    items = Cart.objects.all()
    cart_items = []

    for item in items:
        if item.product == 'movie':
            movie = get_object_or_404(Movie,pk=item.product_id)
            cart_items.append(movie)
    return render(request,'cart/cart.html',{'cart_items':cart_items})

def confirmation(request):
    return render(request,'cart/cart.html',{'confirmation':'confirmation'})
