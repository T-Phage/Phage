from django.contrib import admin
from .models import Category, Product
from django.contrib.auth.models import User
from paymentsapp.models import PayerDetails

# Register your models here.
# class  ProductAdmin(admin.ModelAdmin):
# 	"""
# 	docstring
# 	"""
# 	list_display = ['name', 'stock', 'quantity']
admin.site.register(Category)
admin.site.register(Product)
