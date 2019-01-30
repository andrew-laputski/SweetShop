from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Category

# Create your views here.

def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()  # для выпадающего dropdown
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'order/created.html', {'order': order,
                                                          'categories': categories})
    else:
        form = OrderCreateForm
    return render(request, 'order/create.html', {'cart': cart,
                                                 'form': form,
                                                 'categories': categories})