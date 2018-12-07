from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.base_view, name='base'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_list, name='category_list'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_list, name='product_list'),
    url(r'^cart/$', views.cart_view, name='cart_view'),
    url(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', views.add_to_cart_view, name='add_to_cart'),
    url(r'^remove_from_cart/(?P<product_slug>[-\w]+)/$', views.remove_from_cart_view, name='remove_from_cart'),
    url(r'^change_item_qty/$', views.change_item_qty, name='change_item_qty')
]
