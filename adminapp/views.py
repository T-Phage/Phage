from django.views.generic import ListView
from django.shortcuts import render, redirect
from fashionapp.models import Product
from cartapp.models import Order, Orders
from django.db.models import Sum
from .forms import ProductForm

# Create your views here.
def dashboard(request):
    items  = Product.objects.all()
    print(items)
    orders_delivered = Orders.objects.filter(delivered=True).count()
    orders_not_delivered = Orders.objects.filter(delivered=False).count()
    earnings = Orders.objects.aggregate(Sum('total'))["total__sum"]
    print(earnings)
    context = {'orders_delivered':orders_delivered, 'orders_not_delivered':orders_not_delivered,
               'earnings':earnings, 'items':items}
    return render(request, 'admin_index.html', context)


class Products(ListView):
    model = Product
    # paginate_by = 50
    template_name = 'productstable.html'
    ordering = ['-stock']


# class OrderTable(ListView):
#     model = Orders
#     template_name = 'ordertable.html'
    

def OrderTable(request):
    orders = Orders.objects.all()
    context = {'orders':orders}
    return render(request, 'ordertable.html', context)
    

def profile(request):
    return render(request, 'adminprofile.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        form.save()
        return redirect('adminapp:add_product')
    form = ProductForm()
    context = {'form':form}
    return render(request, 'addproduct.html', context)


def order_detail(request, pk):
    order = Orders.objects.get(id=pk)
    print(order.ordered_by)
    orders = Orders.objects.filter(id=order.id)
    context ={'orders': orders}    
    return render(request, 'order_detail.html', context)