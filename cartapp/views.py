from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from fashionapp.models import Product
from .models import Cart, Order, Orders
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.


# Add to Cart View

def add_to_cart(request, slug):
    quantity = Product.objects.filter(slug=slug)[0].quantity
    Product.objects.filter(slug=slug).update(quantity=quantity+1)
    print(quantity)
    item = get_object_or_404(Product, slug=slug)
    price = item.price
    print(price)
    # if item.
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        t_total = float(order_qs[0].total) + price
        order = order_qs[0]
        # order_item.price += price
        order_item.save()
        # Order.objects.filter(user=request.user, ordered=False).update(total=t_total)
            
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            # order_item.price += price
            order_item.save()
            order_qs[0].total += price
            
            print(order.total)
            Order.objects.filter(user=request.user, ordered=False).update(total=t_total)
            # order_item.price += price
            order_item.save()
            # print(order_qs[0].total)
            messages.info(request, "This item quantity was updated.")
            data = {
                'message': "This item quantity was updated.",
                'price_total': order_qs[0].total,
                'cart_total': Cart.objects.filter(user=request.user, ).count() 
            }
            return JsonResponse(data)
        else:
            Order.objects.filter(user=request.user, ordered=False).update(total=t_total)
            order.orderitems.add(order_item)
            # order_item.price += price
            order_item.save()
            order_qs[0].total = t_total
            # print(order_qs[0].total)
            messages.info(request, "This item was added to your cart.")
            data = {
                'message': "This item quantity was updated.",
                'price_total': order_qs[0].total,
                'cart_total': Cart.objects.filter(user=request.user, ).count()
            }
            return JsonResponse(data)
    else:
        
        # order_item.price += price
        # order_item.price.save()
        order = Order.objects.create(user=request.user, total=price)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        data = {
            'message': "This item was added to your cart.",
            'price_total': Order.objects.filter(user=request.user, ordered=False)[0].total,
            'cart_total': Cart.objects.filter(user=request.user, ).count()
        }
        return JsonResponse(data)


# Remove item from cart

def remove_from_cart(request, slug):
    quantity = Product.objects.filter(slug=slug)[0].quantity
    Product.objects.filter(slug=slug).update(quantity=quantity-1)
    item = get_object_or_404(Product, slug=slug)
    price = float(item.price)
    # print(price)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            # # order_qs[0].total -= price
            # total = (order_qs[0].total) - price
            # # print(total)
            new_total = order_qs[0].total-price
            print(new_total)
            Order.objects.filter(user=request.user, ordered=False).update(total=order_qs[0].total-price)
            # Order.objects.filter(user=request.user, ordered=False).update(total=total)
            messages.info(request, "This item was removed from your cart.")
            data = {
                'message': "This item was added to your orders.",
                'price_total': new_total
            }
            return JsonResponse(data)
        else:
            new_total = order_qs[0].total-price
            print(new_total)
            Order.objects.filter(user=request.user, ordered=False).update(total=order_qs[0].total-price)

            # total = (order_qs[0].total) - price
            # Order.objects.filter(user=request.user, ordered=False).update(total=total)
            messages.info(request, "This item was not in your cart")
            data = {
                'message': "This item was added to your orders.",
                'price_total': new_total
            }
            return JsonResponse(data)
    else:
        messages.info(request, "You do not have an active order")
        data = {
            'message': "This item was added to your orders.",
            'cart_total': Order.objects.filter(user=request.user, ordered=False)
        }
        return JsonResponse(data)


# Count cart instances

def count_cart(request):
    cart_qs = Cart.objects.filter(user=request.user, ordered=False).count()
    cart = cart_qs
    data = {
            'message': "This item was added to your orders.",
            'cart_total': cart
        }
    return JsonResponse(data)


# Delete items from cart

def delete_from_cart(request, slug):
    q = request.POST['qname']
    print(q)
    q = int(q)
    quantity = Product.objects.filter(slug=slug)[0].quantity
    Product.objects.filter(slug=slug).update(quantity=quantity-q)
    item = get_object_or_404(Product, slug=slug)
    price = float(item.price)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print(order_qs[0].total)
    
    if cart_qs.exists():
        cart = cart_qs[0]
        r_total = cart.quantity * price
        cart.delete()
        
        order_qs = Order.objects.filter(user=request.user, ordered=False).update(total=order_qs[0].total-r_total)
        
        
        data = {
            'cart_total': Cart.objects.filter(user=request.user, item=item).count(),
            'price_total': Order.objects.filter(user=request.user, ordered=False)[0].total,
        }
        return JsonResponse(data)
        # Checking the cart quantity
        # if cart.quantity > 0:
        #     cart.quantity -= cart.quantity
        #     cart.save()
        #     cart_qs.exists()
        #     cart = cart_qs[0]
        #     if cart.quantity == 0:
        #         cart_qs.delete()
        #     cart_cqs = Cart.objects.filter(user=request.user, ).count()
        #     cart = cart_cqs
        #     data = {
        #         'cart_total': cart
        #     }
        #     return JsonResponse(data)
            # print(cart.quantity)
    #     else:
    #         cart_qs.delete()
    # order_qs = Order.objects.filter(
    #     user=request.user,
    #     ordered=False
    # )
    # if order_qs.exists():
    #     order = order_qs[0]
    #     # check if the order item is in the order
    #     if order.orderitems.filter(item__slug=item.slug).exists():
    #         order_item = Cart.objects.filter(
    #             item=item,
    #             user=request.user,
    #         )[0]
    #         order.orderitems.remove(order_item)
    #         messages.info(request, "This item was removed from your cart.")
    #         data = {
    #             'message': "This item was added to your orders."
    #         }
    #         return JsonResponse(data)
    #     else:
    #         messages.info(request, "This item was not in your cart")
    #         data = {
    #             'message': "This item was added to your orders."
    #         }
    #         return JsonResponse(data)
    # else:
    #     messages.info(request, "You do not have an active order")
    #     data = {
    #             'message': "This item was added to your orders."
    #         }
    #     return JsonResponse(data)


def orders(request):
    orders = request.POST['order']
    total = request.POST['total']
    print(orders)
    Orders.objects.create(
        items=orders,
        user="sammy",
        total=total,
        delivered=True)
    data = {
        'message': 'ok',
    }
    return JsonResponse(data)

# items = models.TextField()
#     user = models.CharField(max_length=255)
#     total = models.FloatField()
#     delivered = models.BooleanField(default=False)
