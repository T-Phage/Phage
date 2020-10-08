from django.urls import path
from .import views
from . views import *

app_name = 'adminapp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('', Dashboard.as_view(), name='dashboard'),
    path('products/', Products.as_view(), name='products'),
    path('orders__table/', views.OrderTable, name='order_table'),
    path('profile/', views.profile, name='profile'),
    path('add_product/', views.add_product, name='add_product'),
    path('order/detail/<str:pk>/?', views.order_detail, name='order_detail'),
]
