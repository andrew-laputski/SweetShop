from _decimal import Decimal
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from shop.models import Category, Product, CartItem, Cart

# Create your views here.
def base_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'shop/base.html', {'categories': categories,
                                              'products': products,
                                              'cart':cart})

def category_list(request, category_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    category = Category.objects.get(slug=category_slug)
    products_of_category = category.product_set.all()
    categories = Category.objects.all()  # для выпадающего dropdown
    return render(request, 'shop/category_list.html', {'category':category,
                                                       'products_of_category':products_of_category,
                                                       'categories':categories,
                                                       'cart':cart})

def product_list(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all() # для выпадающего dropdown
    return render(request, 'shop/product_list.html', {'product':product,
                                                      'categories':categories,
                                                      'cart':cart})

def cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    return render(request, 'shop/cart_view.html', {'cart':cart,
                                                   'categories':categories})

def add_to_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)

    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return HttpResponseRedirect(reverse('cart_view'))

def remove_from_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return HttpResponseRedirect(reverse('cart_view'))

#def change_item_qty(request):
#    try:
#        cart_id = request.session['cart_id']
#        cart = Cart.objects.get(id=cart_id)
#        request.session['total'] = cart.items.count()
#    except:
#        cart = Cart()
#        cart.save()
#        cart_id = cart.id
#        request.session['cart_id'] = cart_id
#        cart = Cart.objects.get(id=cart_id)
#    qty = request.GET.get('qty')
#    item_id = request.GET.get('item_id')
#    cart_item = CartItem.objects.get(id=int(item_id))
#    cart_item.qty = int(qty)
#    cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
#    cart_item.save()
#    new_cart_total = 0.00
#    for item in cart.items.all():
#        new_cart_total += float(item.item_total)
#    cart.cart_total = new_cart_total
#    cart.save()
#    return HttpResponseRedirect(reverse('cart_view'))

def change_item_qty(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	qty = request.GET.get('qty')
	item_id = request.GET.get('item_id')
	cart.change_qty(qty, item_id)
	cart_item = CartItem.objects.get(id=int(item_id))
	return HttpResponseRedirect(reverse('cart_view'))
