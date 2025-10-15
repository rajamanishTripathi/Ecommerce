from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # queryset = Product.objects.filter(unit_price__range =(1,20))
    queryset = Product.objects.filter(title__icontains ='coffee')
    
    return render(request, 'hello.html', {'name': 'Mosh','product':queryset})