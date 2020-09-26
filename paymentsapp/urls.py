from django.urls import path
from .views import *
from . import views

app_name = 'paymentsapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='payment'),
    path('success/', views.success, name='success'),
]
