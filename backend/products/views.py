from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers
#import decorators
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
class ProductListAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers


list_product_create_view=ProductListAPIView.as_view()

class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title

        serializer.save(content=content)

        #send a signal

product_create_view=ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    #lookup_field='pk
    # product.objects.get(pk=1)

@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method
          
    if method=="GET":
        if pk is not None:
            #detail view
            obj=get_object_or_404(Product,pk=pk) #yelay chai product db bata tyo specific primary key vako object lai khojcha if not found it returns a 404 not found response
            data=ProductSerializers(obj,many=False).data

            return Response(data)
        #list view
        queryset=Product.objects.all() # Fetch all products from the database
        data=ProductSerializers(queryset,many=True).data # Serialize the queryset many true garnu ko karan chai dherai data awoochan yewotai db bata ani serializer lai tha hunna so it returns an error 
        return Response(data) # Return the serialized data as an API response
    if method=="POST":
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response({"invalid":"not good data"},status=400)
    
            

