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
    

def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)

ids = []
def shopcart(request):
    if request.is_ajax:
        
        id = request.POST.get('id', False)
        ids.append(id)
        
        print(id)
        print(ids)
        # full_str = convert_list_to_string(ids, ' or')
        full_str = ''.join([str(elem) for elem in ids])
        print(full_str)
        # print(Product.objects.filter(id=)
        # print("df")
        # name = request.POST['name']
        # print(name)
        # numbers = request.POST['number']
        # print(numbers)

    products = Product.objects.all()
    # orders = Order.objects.filter(ordered=False,)
    # carts =  Cart.objects.filter(user=request.user)
    # total_orders = Order.objects.filter(ordered=False, user=request.user)
    # if total_orders.exists():
    #     total_orders = total_orders[0].total  
    # else:
    #     total_orders = 0
    # context = {'carts': carts, 'orders': orders, 'total_orders':total_orders,}
    return render(request, 'shop-cart.html', {'products':products})


def samajax(request):
    print("df")
    name = request.POST['name']
    print(name)
    numbers = request.POST['number']
    print(numbers[0][1])



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
