from django.views.generic import ListView
from django.shortcuts import render, redirect
from fashionapp.models import Product
from cartapp.models import Order, Orders
from django.db.models import Sum
from .forms import ProductForm
from django.views.generic import TemplateView, DetailView
from paymentsapp.models import PayerDetails
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    items  = Product.objects.all().order_by("-quantity")[:5]
    print(items)
    orders_delivered = Orders.objects.filter(delivered=True).count()
    orders_not_delivered = Orders.objects.filter(delivered=False).count()
    earnings = Orders.objects.aggregate(Sum('total'))["total__sum"]
    print(earnings)
    context = {'orders_delivered':orders_delivered, 'orders_not_delivered':orders_not_delivered,
               'earnings':earnings, 'items':items}
    return render(request, 'admin_index.html', context)


# @login_required(login_url='login')
class Products(ListView):
    model = Product
    # paginate_by = 50
    template_name = 'productstable.html'
    ordering = ['-stock']


# class OrderTable(ListView):
#     model = Orders
#     template_name = 'ordertable.html'
    
@login_required(login_url='login')
def OrderTable(request):
    orders = Orders.objects.all()
    context = {'orders':orders}
    return render(request, 'ordertable.html', context)
    

@login_required(login_url='login')
def profile(request):
    user = PayerDetails.objects.get(payer=request.user.id)
    print(user)
    context = {'user':user}
    return render(request, 'adminprofile.html', context)


@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        form.save()
        return redirect('adminapp:add_product')
    form = ProductForm()
    context = {'form':form}
    return render(request, 'addproduct.html', context)


@login_required(login_url='login')
def order_detail(request, pk):
    order = Orders.objects.get(id=pk)
    print(order.ordered_by)
    orders = Orders.objects.filter(id=order.id)
    context ={'orders': orders}    
    return render(request, 'order_detail.html', context)