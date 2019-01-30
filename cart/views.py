from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from cart.forms import CartAddProductForm
from shop.models import Product, Category
from .cart import Cart
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
             quantity=cd['quantity'],
             update_quantity=cd['update'])
    return HttpResponseRedirect(reverse('cart_view'))

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponseRedirect('/cart/')

def cart_view(request):
    cart = Cart(request)
    categories = Category.objects.all()  # для выпадающего dropdown
    return render(request, 'cart/cart_view.html', {'cart': cart,
                                                   'categories':categories})