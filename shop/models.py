from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

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

    class Meta:
        ordering = ('title',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_list', args=[self.id, self.slug])
