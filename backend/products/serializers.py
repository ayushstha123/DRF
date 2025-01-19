from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','content','price','sales_price','get_discount',] # 💀 => ,