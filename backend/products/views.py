from rest_framework import generics,mixins
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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
list_product_update_view=ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
product_delete_view=ProductDeleteAPIView.as_view()

#function based api view 
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
    
            

#mixins and generics api view

#listModelMixin
# class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# product_mixin_view=ProductMixinView.as_view()

#retirveModelMixin
class ProductMixinView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'


    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.update(request,*args,**kwargs)
        return Response({"detail": "Not found."})

        
    def destroy(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.destroy(request, *args, **kwargs)
        return Response({"detail": "Not found."})
    
product_mixin_view=ProductMixinView.as_view()