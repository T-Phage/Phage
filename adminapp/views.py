from django.shortcuts import render
from fashionapp.models import Product
from cartapp.models import Order

# Create your views here.
def dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    context = {'products':products, 'orders':orders}
    return render(request, 'admin_index.html', context)
