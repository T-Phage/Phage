from django.urls import path
from .import views
from . views import *

app_name = 'adminapp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', Products.as_view(), name='products'),
    path('orders__table/', views.OrderTable, name='order_table'),
    path('profile/', views.profile, name='profile'),
    path('add_product/', views.add_product, name='add_product')
]
