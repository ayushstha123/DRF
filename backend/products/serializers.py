from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    this_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        # fields=['title','content','price','sales_price','get_discount',] # 💀 => ,
        fields=['title','content','price','sales_price','this_discount',] # 💀 => ,

    def get_this_discount(self, obj):
        if not hasattr(obj,'id'):  #Does the object have an ID?
            return None
        if not isinstance(obj,Product): #Is the object a Product?
            return None
        return obj.get_discount()

#WRITE ABOUT SERIALIZERS 
