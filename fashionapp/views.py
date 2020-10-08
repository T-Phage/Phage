from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Product
from cartapp.models import Cart, Orders
from adminapp.forms import *
from paymentsapp.models import PayerDetails


# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'index.html'
    # paginate_by = 1


class ShopCart(ListView):
    # model = Order
    model = Cart
    template_name = 'shop-cart.html'
    

def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)

# ids = []
def shopcart(request):
    products = Product.objects.all()
    carts =  Cart.objects.all()
    print(request.user)
    context = {'carts': carts,}
    return render(request, 'shop-cart.html', context)


def contact(request):
    return render(request, 'contact.html')


def shop(request):
    return render(request, 'shop.html')


def checkout(request):
    detailform = PayerDetailsForm()
    carts =  Cart.objects.all()
    context = {'detailform':detailform, 'carts':carts, }
    return render(request, 'checkout.html', context)


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
