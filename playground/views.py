from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # queryset = Product.objects.filter(unit_price__range =(1,20))
    # queryset = Product.objects.filter(title__icontains ='coffee')
    # queryset = Product.objects.filter(inventory__lt =10,unit_price__lt = 10) AND operation
    # queryset = Product.objects.filter(inventory__lt =10).filter(unit_price__lt = 20) AND operations
    # queryset = Product.objects.filter(Q(inventory__lt =10) | Q(unit_price__lt = 20))  OR opertions
    # queryset = Product.objects.filter(Q(inventory__lt =10) & Q(unit_price__lt = 20))  AND opertion
    #  queryset = Product.objects.filter(Q(inventory__lt =10) | ~Q(unit_price__lt = 20))  OR opertions with NOT operator
    # Product : inventory = unit_price
    queryset = Product.objects.filter(inventory=F('unit_price')) 

    return render(request, 'hello.html', {'name': 'Mosh','product':list(queryset)})