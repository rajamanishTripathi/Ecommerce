from django.shortcuts import render
from store.models import Product,Order,OrderItem,Customer,Collection
from django.db import transaction,connection

def say_hello(request):

    # queryset = Product.objects.raw('SELECT * FROM store_product')

    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM store_product')
    # cursor.close()

    # with connection.cursor() as cursor:
    #     cursor.execute()

    with connection.cursor() as cursor:
        cursor.callproc('get_customers',[1,2,'a'])

    return render(request, 'hello.html', {'name': 'Mosh','query' : queryset})