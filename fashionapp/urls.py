from django.urls import path
from . views import *
from . import views
from cartapp.views import add_to_cart, remove_from_cart, delete_from_cart, count_cart


app_name = 'fashionapp'

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('cart/remove/<slug>', remove_from_cart, name='remove-cart'),
    path('cart/delete/<slug>', delete_from_cart, name='delete-cart'),
    path('shop-cart/', views.shopcart, name='shopcart'),  # path('cart/', ShopCart.as_view(), name='shopcart'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('fetch_count/', count_cart, name='count-cart'),
    # path('checkout/ordered/', views.save_ordered),
    # path('samajax/', views.samajax),
    # path('save_orders/', orders),
    # path('success/', views.success, name='success'),
]


