from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.conf import settings
from cartapp.models import Orders

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'payment.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['key'] = settings.RAVE_PUBLIC_KEY
    #     return context


def success(request):
    if request.is_ajax():
        arry = request.POST.get("arry")
        total = request.POST.get("total")
        print(arry + total)
        # Orders.create()
        
    return render(request, 'success.html')
