from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    this_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        # fields=['title','content','price','sales_price','get_discount',] # 💀 => ,
        fields=['title','content','price','sales_price','this_discount',] # 💀 => ,

    def get_this_discount(self, obj):
        return obj.get_discount()