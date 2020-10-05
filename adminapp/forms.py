from django import forms 
from fashionapp.models import Product
from paymentsapp.models import PayerDetails
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'


class PayerDetailsForm(forms.ModelForm):
    
    class Meta:
        model = PayerDetails
        fields = '__all__' 
