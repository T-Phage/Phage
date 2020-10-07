from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from fashionapp.models import Product
from .models import Cart, Order, Orders
from django.contrib import messages
from django.http import JsonResponse
from paymentsapp.models import PayerDetails


# Create your views here.


# Add to Cart View

def add_to_cart(request, slug):
    user = PayerDetails.objects.filter(payer=request.user.id)
    print(user[0])
        
    item = get_object_or_404(Product, slug=slug)
    print(item)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=user[0]
    )
    cart_qs = Cart.objects.filter(user=user[0], item=item)
    if cart_qs.filter(item=item).exists():
        order_item.quantity += 1
        order_item.save()
   
    data = {
        'message': "This item was added to cart.",
        'cart_total': Cart.objects.filter(item=item, user=user[0]).count() 
    }
    return JsonResponse(data)
    

# Remove item from cart

def remove_from_cart(request, slug):
    user = PayerDetails.objects.filter(payer=request.user.id)
    item = get_object_or_404(Product, slug=slug)

    cart_qs = Cart.objects.filter(user=user[0], item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    data = {
        'message': "This item was added to cart.",
        'cart_total': Cart.objects.filter(item=item, user=user[0]).count() 
    }
    return JsonResponse(data)
            

# Count cart instances

def count_cart(request):
    cart_qs = Cart.objects.filter(user=request.user.id).count()
    cart = cart_qs
    data = {
            'message': "This item was added to your orders.",
            'cart_total': cart,
        }
    return JsonResponse(data)


# Delete items from cart

def delete_from_cart(request, slug):
    user = PayerDetails.objects.filter(payer=request.user.id)
    item = get_object_or_404(Product, slug=slug)

    cart_qs = Cart.objects.filter(user=user[0], item=item)
    if cart_qs.exists():
        cart_qs.delete()
        
    data = {
        'cart_total': Cart.objects.filter(user=user[0], item=item).count(),
    }
    return JsonResponse(data)


# def orders(request):
#     orders = request.POST['order']
#     total = request.POST['total']
#     print(orders)
#     Orders.objects.create(
#         items=orders,
#         user="sammy",
#         total=total,
#         delivered=True)
#     data = {
#         'message': 'ok',
#     }
#     return JsonResponse(data)


    