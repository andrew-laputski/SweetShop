from django.shortcuts import render
from cart.forms import CartAddProductForm
from shop.models import Category, Product

# Create your views here.
def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/base.html', {'categories': categories,
                                              'products': products,
                                              'cart_product_form': cart_product_form})

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products_of_category = category.product_set.all()
    categories = Category.objects.all()  # для выпадающего dropdown
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/category_list.html', {'category':category,
                                                       'products_of_category':products_of_category,
                                                       'categories':categories,
                                                       'cart_product_form': cart_product_form})

def product_list(request, product_slug, id):
    product = Product.objects.get(slug=product_slug, id=id)
    categories = Category.objects.all() # для выпадающего dropdown
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_list.html', {'product':product,
                                                      'categories':categories,
                                                      'cart_product_form':cart_product_form})

