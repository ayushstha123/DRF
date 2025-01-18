import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def api_home(request,*args,**kwargs):
    print('GET:', request.GET)
    print("POST:" , request.POST)
    body=request.body
    data={}
    try:
        data=json.loads(body) #turns the string of json data into python dictionary
    except:
        pass
    print(data)
    data['headers']=request.headers
    return JsonResponse({"message":"hi there this is your Django api resposne made by ayush"})
