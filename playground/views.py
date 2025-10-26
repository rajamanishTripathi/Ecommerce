from django.shortcuts import render
from store.models import Product,Order,OrderItem,Customer,Collection

def say_hello(request):
    collection = Collection()
    collection.title = 'Video Game'
    collection.featured_product = Product(pk=1) 
    # or Product(id=1)
    collection.save()

    #      ------------------OR-------------------
    # collection = Collection.objects.create(title='a',featured_product_id=1)


    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})