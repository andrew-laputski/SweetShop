from _decimal import Decimal

from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]# split разделили название картинки
    # на две части (до точки и после) и взяли аргумент после точки ([1])
    # сформировали название: slug + . + разделенное split-ом
    return "{0}/{1}".format(instance.slug, filename)# вернули строку из: slug / название
    # создали каталог (instance.slug) и создали картинку с filename

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=user_directory_path)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.title)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        cart_items = [item.product for item in cart.items.all()]
        if new_item.product not in cart_items:
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()

    def change_qty(self, qty, item_id):
        cart = self
        cart_item = CartItem.objects.get(id=int(item_id))
        cart_item.qty = int(qty)
        cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
        cart_item.save()
        new_cart_total = 0.00
        for item in cart.items.all():
            new_cart_total += float(item.item_total)
        cart.cart_total = new_cart_total
        cart.save()