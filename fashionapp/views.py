from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Product
from cartapp.models import Cart, Order


# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'index.html'
    # paginate_by = 1


class ShopCart(ListView):
    # model = Order
    model = Cart
    template_name = 'shop-cart.html'


def shopcart(request):
    orders = Order.objects.filter(ordered=False,)
    carts =  Cart.objects.filter(user=request.user)
    total_orders = Order.objects.filter(ordered=False, user=request.user)
    if total_orders.exists():
        total_orders = total_orders[0].total  
    else:
        total_orders = 0
    context = {'carts': carts, 'orders': orders, 'total_orders':total_orders,}
    return render(request, 'shop-cart.html', context)


def contact(request):
    return render(request, 'contact.html')


def shop(request):
    return render(request, 'shop.html')


def checkout(request):
    orders = Order.objects.filter(ordered=False, user=request.user)
    carts =  Cart.objects.filter(user=request.user)
    total_orders = Order.objects.get(ordered=False, user=request.user)
    context = {'orders': orders, 'carts': carts, 'total_orders':total_orders,}
    return render(request, 'checkout.html', context)


def save_ordered(request):
    Order.objects.filter(ordered=False, user=request.user).update(ordered=True)
    Cart.objects.filter(user=request.user, ordered=True).update(ordered=True)
    Cart.objects.filter(user=request.user, ordered=True).delete()
    return redirect('fashionapp:index')
    
# from django.shortcuts import render
#
#
# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
#
#
# def shopcart(request):
#     return render(request, 'shop-cart.html')
#
#
# def shop(request):
#     return render(request, 'shop.html')
#
#
# def contact(request):
#     return render(request, 'contact.html')
#
#
# def checkout(request):
#     return render(request, 'checkout.html')
