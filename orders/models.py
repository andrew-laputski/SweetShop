from django.db import models
from shop.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=18)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    buying_type = models.CharField(max_length=10, choices=(('Самовывоз', 'Самовывоз'),
                                                           ('Доставка', 'Доставка')),
                                   default='Самовывоз')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = models.TextField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Заказ № {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity