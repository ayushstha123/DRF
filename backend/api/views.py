import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from products.models import Product
from django.forms.models import model_to_dict

#REST API 
from rest_framework.response import Response
from rest_framework.decorators import api_view

#import serializers from product
from products.serializers import ProductSerializers

# Create your views here.
# def api_home(request,*args,**kwargs):
    # print('GET:', request.GET)
    # print("POST:" , request.POST)
    # body=request.body
    # data={}
    # try:
    #     data=json.loads(body) #turns the string of json data into python dictionary
    # except:
    #     pass
    # print(data)
    # data['headers']=request.headers
    # return JsonResponse({"message":"hi there this is your Django api resposne made by ayush"})

    #Django Model Instance as API response
    # model_datas=Product.objects.all().order_by("?").first()
    # data={}
    # if model_datas:
        # data['id']=model_datas.id
        # data['title']=model_datas.title
        # data['content']=model_datas.content
        # data['price']=model_datas.price

    #     #if we are using model_to_dict we dont need the above code
    #     data=model_to_dict(model_datas,fields=['id','title'])
    #     converted_data_to_json=json.dumps(data) #dump string
    #     print(data)
    # # return JsonResponse(data)
    # return HttpResponse(converted_data_to_json,headers={"content-type":"application/json"})

#Rest rest framework
#For GET
# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#     """DRF API VIEW """ #this is called docstring
#     instance=Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         # data=model_to_dict(model_data,fields=['id','title','price'])
#         data=ProductSerializers(instance).data
#     return Response(data)

# For POST
@api_view(["POST"])
def api_home(request,*args,**kwargs):
    data=request.data
    """DRF API VIEW """ #this is called docstring
    serializer=ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        
        print(serializer.data)
        # instance=serializer.save()
        # print(instance)
        return Response(serializer.data)  
    return Response({"invalid":"not good data"})

