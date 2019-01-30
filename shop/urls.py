from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.base_view, name='base'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_list, name='category_list'),
    url(r'^product/(?P<id>\d+)/(?P<product_slug>[-\w]+)/$', views.product_list, name='product_list'),
]
