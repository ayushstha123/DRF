from rest_framework import generics

from .models import Product
from .serializers import ProductSerializers

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    #lookup_field='pk
    # product.objects.get(pk=1)