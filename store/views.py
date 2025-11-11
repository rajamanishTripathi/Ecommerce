from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from django.db.models import Count
from .serializers import ProductSerializer,CollectionSerializer,Collection


class ProductList(ListCreateAPIView):
    # implementing below if no logic  required
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    # implementing below if more logic  required
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'
    def delete(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        if product.orderitem_set.count() > 0:
            return Response({'error':'product cannot be deleted as it is associated with order item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    print(queryset)
    serializer_class = CollectionSerializer
    

class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(products_count = Count('products'))
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection,pk=pk)
        if collection.products.count > 0:
            return Response({'error': 'Collection cannot be deleted because this collections includes one or more products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    