from django.shortcuts import render
from store.models import Product,Order,OrderItem,Customer,Collection

def say_hello(request):
    # collection = Collection(pk=11)
    # collection.title = 'Game'
    # collection.featured_product = None
    # # or Product(id=1)
    # collection.save()

    #      ------------------OR-------------------
    # this get the data first and then update only required fields not all fields
    # by filtering a id first otherwise it will update all fiels
    Collection.objects.filter(pk=11).update(featured_product_id=None)


    return render(request, 'hello.html', {'name': 'Mosh'})