from django.contrib import admin
from .models import Cart, Order, Orders

# Register your models here.
class CartAdmin(admin.ModelAdmin):
	list_display = ['user', 'item', 'quantity']
	
admin.site.register(Cart, CartAdmin)
admin.site.register(Order)
admin.site.register(Orders)