from django.shortcuts import render,redirect
from paymentsapp.models import PayerDetails
from adminapp.forms import PayerDetailsForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
# User = get_user_model()


# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        othername = request.POST['othername']
        country = request.POST['country']
        address = request.POST['address']
        username = request.POST['username']
        city = request.POST['city']
        region = request.POST['region']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        
        user = User.objects.filter(username=username)[0]
        print(user)
        PayerDetails.objects.create(payer=user, othername=othername, country=country,
                                    address=address, city=city, region=region, postcode=postcode,
                                    phone=phone)
        return redirect('fashionapp:login')
    else:
        form = PayerDetailsForm()
        context = {'form':form,}
        return render(request, 'register.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user1 = User.objects.filter(username=username)[0]
        print(user1.is_staff)
        # print(username)
        # print(password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print('logged in')
            
            if user.is_staff is True:
                return redirect('adminapp:dashboard')
            else:
                return redirect('fashionapp:index')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'An error occurred')
            print('error')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('fashionapp:login')


def validate(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)