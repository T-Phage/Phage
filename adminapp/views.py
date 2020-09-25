from django.views.generic import ListView
from django.shortcuts import render
from fashionapp.models import Product
from cartapp.models import Order, Orders
from django.db.models import Sum

# Create your views here.
def dashboard(request):
    products = Product.objects.all()
    orders_delivered = Orders.objects.filter(delivered=True).count()
    orders_not_delivered = Orders.objects.filter(delivered=False).count()
    earnings = Orders.objects.aggregate(Sum('total'))["total__sum"]
    print(earnings)
    context = {'products':products, 'orders_delivered':orders_delivered, 'orders_not_delivered':orders_not_delivered,
               'earnings':earnings}
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