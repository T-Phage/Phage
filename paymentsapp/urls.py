from django.urls import path
from .views import *
from . import views

app_name = 'paymentsapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='payment'),
    path('success/', views.success, name='success'),
    path('success/page/', views.success_page, name='success_page'),
    path('add_quantity/', views.addquantity, name='add_quantity'),
]
