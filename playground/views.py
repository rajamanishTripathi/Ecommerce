from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product,OrderItem


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
    # queryset = Product.objects.filter(inventory=F('unit_price')) 
    # queryset = Product.objects.order_by('title')  ASC
    # queryset = Product.objects.order_by('-title')  DESC
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    #  product = Product.objects.earliest('unit_price') asc
    # product = Product.objects.latest('unit_price')[0] desc
    # product = Product.objects.values('id','title','collection__title')
    #  instead of product instances we get dictonary object 
    # product = Product.objects.values_list('id','title','collection__title')
    #  instead of product instances we get tuple object 


    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    return render(request, 'hello.html', {'name': 'Mosh','product':list(queryset)})