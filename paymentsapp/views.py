from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from cartapp.models import Orders
from paymentsapp.models import PayerDetails
from adminapp.forms import PayerDetailsForm
from fashionapp.models import Product
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class HomePageView(TemplateView):
    template_name = 'payment.html'


def success(request):
    if request.is_ajax:
        detailform=PayerDetailsForm(request.POST)
        print(detailform.is_valid())
        print(detailform.errors)
        
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        othername = request.POST.get('username')
        password = request.POST.get('password')
        
        phone = request.POST.get('phone')
        postcode = request.POST.get('postcode')
        address = request.POST.get('address')
        region = request.POST.get('region')
        country = request.POST.get('country')
        city = request.POST.get('city')
        account = request.POST.get('account')
        print(account)
        print(firstname)
        print(lastname)
        print(email)
        print(username)
        
        note = request.POST.get('note')
        paid = request.POST.get('paid')
        transaction_id = request.POST.get('transaction_id')
        tx_ref = request.POST.get('tx_ref')
        items = request.POST.get("items")
        total = request.POST.get("total")
        
        
        print(detailform.is_valid())
        print(detailform.errors)

        print(items)
        print(total)
        
        if account == "yes":
            user_q = User.objects.filter(first_name=firstname, email=email, username=username)
            # payer_qs = PayerDetails.objects.filter(firstname=firstname, lastname=lastname, email=email)
            # print(user_q)
            if user_q.exists():
                print(user_q)
                # data = {'message': 'User alredy exists'}
                # return JsonResponse(data)
            else:
                User.objects.create(first_name=firstname, last_name=lastname, email=email, password=password, username=username)
                
                query = User.objects.filter(first_name=firstname, last_name=lastname, email=email, password=password, username=username)
                print(query)
                PayerDetails.objects.create(country=country, region=region, address=address, postcode=postcode, phone=phone,
                                            payer=query, othername=othername, city=city)
                # data = {'message': 'User created'}
                # return JsonResponse(data)
        elif account == "no":
            user_q = User.objects.filter(first_name=firstname, email=email, username=username)
            payer_q = PayerDetails.objects.filter(firstname=firstname, othername=othername, lastname=lastname, email=email)
            print(payer_q)
            if payer_q.exists():
                print('Payer exixts')
                # data = {'message': 'User alredy exists'}
                
                # return JsonResponse(data)
            else:
                form = PayerDetailsForm(request.POST)
                form.save()
                # data = {'message': 'details saved'}
                # return JsonResponse(data)
                
        qs = PayerDetails.objects.filter(firstname=firstname, email=email)
        print(qs)
        if qs.exists():
            print('not none')
            user = PayerDetails.objects.filter(firstname=firstname, email=email, username=username)[0]
            Orders.objects.create(ordered_by=user, items=items, total=total, amount_paid=paid, transaction_id=transaction_id,
                                  tx_ref=tx_ref, note=note)
            print('saved already existed')
            data={'message': 'success', }
            return JsonResponse(data)
        else:
            print('is none')
            print(detailform.is_valid())
            detailform.save()
            
            user = PayerDetails.objects.filter(firstname=firstname, email=email, username=username)[0]
            print(user)
            Orders.objects.create(ordered_by=user, items=items, total=total, amount_paid=paid, transaction_id=transaction_id,
                                tx_ref=tx_ref, note=note)
            print('saved not existed')
            data={'message': 'success', }
            return JsonResponse(data)


def success_page(request):
    return render(request, 'success.html')
    
def addquantity(request):
    q_value = request.POST.get('q_value')
    item = request.POST.get('item')
    
    products = Product.objects.filter(name=item)
    # Product.objects.filter(name=item)[0].quantity
    Product.objects.filter(name=item).update(quantity=int(Product.objects.filter(name=item)[0].quantity) + int(q_value))
    Product.objects.filter(name=item).update(stock=int(Product.objects.filter(name=item)[0].stock) - int(q_value))
    
    print(q_value)
    print(item)
    print(products[0].name)
    data = {'message': f"{q_value} {item} {products[0].name} {Product.objects.filter(name=item)[0].quantity} {Product.objects.filter(name=item)[0].stock}"}
    return JsonResponse(data)
