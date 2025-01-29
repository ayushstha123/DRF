# Django Rest Framework

> ## Setting up the environment
1. Create the environment in python 
``` bash
python -m venv venv
```

2. Make a requirements.txt file using 
```bash 
python -m freeze > requirements.txt
```

3. Write in that file these code and install them using the command 
- django 
- djangorestframework
- pyyaml
- requests
- django-cors-headers

```bash 
pip install -r requirements.txt 
```

4. Create a backend folder and write in that folder these commands to create a new project
`
django-admin startproject cfeHome .
`

> ## Creating a Python Api Client
API stands for Application Programming Interface. It's a set of rules and protocols that allow different software programs to communicate with each other

***Rest api** is for the web that humans cant understand.Javascript object notation ~ python DICT

1. Create a basic.py file inside client
- So on first we imported a package named request and the request package mostly is used for making HTTP requests. It simplifies the process of sending and retrieving the data from the websites

- we created a variable named endpoint that has the website link.

- we used request.get(endpoints) to get the response of the website.


```bash 
import requests
endpoints="https://httpbin.org/anything"

#aplication programming interface
get_response=requests.get(endpoints,json={"query":"This is Ayush Shrestha"}) #HTTP request

print(get_response.text) #print raw text response
print(get_response.json()) #print raw text response
```

> ### Creating my first api view
1. Create a app called as api
```bash 
py manage.py startapp api
```

2. write a code in views.py inside the api folder that says
- request:
The first parameter is mandatory in Django view functions and represents the HTTP request object.

- *args:
***Captures any extra positional arguments passed to the view function when it's called. In most Django cases, this is rarely used, but Django includes it for flexibility.***

- **kwargs:
***Captures any extra keyword arguments passed to the view function. These often come into play when using URL patterns with parameters.***

- import JsonResponse from django.http
- create a function named as api_home with request as a parameter and return JsonResponse({"message":"Hi there"})

3. now import views in urls.py insdie api folder and write 
```bash 
urlpatterns=[path('',views.api_home)] 
```

4. now add the url of the api folder into the main folder like This
```bash 
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'))
]
```

5. change in the client folder inside basic.py
```bash 
print(get_response.json()['message'])
```


> ### Creating Get echo 
load() function decodes a JSON file and returns a Python object. The decoding conversion is based on the following table. The . loads() function, alternatively, takes a JSON string and returns a Python object.

- api > views.py

```bash 
import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def api_home(request,*args,**kwargs):
    body=request.body
    data={}
    try:
        data=json.loads(body) #turns the string of json data into python dictionary
    except:
        pass
    print(data)
    return JsonResponse({"message":"hi there this is your Django api resposne made by ayush"})
```

- client > basic.py
```bash
import requests 
endpoints="http://127.0.0.1:8000/api/"
get_response=requests.get(endpoints,params="123",json={"query":"hello ayush ji"})
```

output 
```bash
Django version 5.1.5, using settings 'cfeHome.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
{'query': 'hello ayush ji'}
[18/Jan/2025 22:57:31] "GET /api/?123 HTTP/1.1" 200 70
```

#### Difference between python DICT and JSON
| Dict    | JSON |
| -------- | ------- |
| A data structure in Python that stores key-value pairs.  | A lightweight data interchange format commonly used for data transmission.   |
| Keys are unique and can be any immutable data type (e.g., strings, numbers, tuples). | JSON objects also store key-value pairs.     |
| Values can be any valid Python object.    | Keys are always strings, and values can be strings, numbers, booleans, arrays (lists), or other JSON objects.    |


### Django Model Instance as Api Response
1. create a app called as products
2. create a model in products with title,content,price 
```bash
from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15, decimal_places=2,default=99.99)
```

3. adding in views.py of api
In the code snippet, you're taking a Django model instance (Product) and formatting it as an API response using JsonResponse. 

- Product.objects.all() retrieves all the product records from the database.
- .order_by("?") randomizes the order of the records.
- .first() fetches the first product from this randomized order.

```bash 
    #Django Model Instance as API response
    
    model_datas=Product.objects.all().order_by("?").first()
    data={}
    if model_datas:
        data['id']=model_datas.id
        data['title']=model_datas.title
        data['content']=model_datas.content
        data['price']=model_datas.price
```

### Django Model Instance to dictionary
- now to make the model instance to dicts we need to add in the views 
```bash 
from django.forms.models import model_to_dict

    #Django Model Instance as API response
    model_datas=Product.objects.all().order_by("?").first()
    data={}
    if model_datas:
        data=model_to_dict(model_datas,fields=['id','price'])
    return JsonResponse(data)
```

> ## RESTFRAMEWORK 
### VIEWS AND RESPONSE
**DECORATORS**: A decorator is essentially a function that takes another function as input, adds some functionality to it, and then returns the modified function. Decorators are implemented using higher-order functions (functions that accept or return other functions).

> Decorator: @api_view
+ The @api_view decorator is used to mark this function-based view as a DRF API view.
+ By default, it supports GET requests, but you can specify supported HTTP methods like this:
```bash 
@api_view(['GET', 'POST'])
```

- import response from rest_framework.response
- import api_view from rest_framework.decorators

### Django rest framework Model Serializers
**What is a Serializer in Django Rest Framework (DRF)?**
- In Django Rest Framework, a serializer is a tool used to convert complex data types (such as Django model instances or querysets) into JSON or other content types that can be easily rendered in an API response. Similarly, serializers can validate and deserialize incoming data (e.g., JSON) into Python objects that can be saved to a database.

**Purpose of Serializers**
- Serialization: Converts Python objects (like Django models) into formats like JSON to send as API responses.
- Deserialization: Converts incoming data (JSON or other formats) into Python objects and validates the data.
- Validation: Ensures the incoming data adheres to specific rules or formats before processing.

**Types of Serializers in DRF**
1. Serializer (Basic Serializer)
This is the simplest form of a serializer where fields are explicitly defined.
```bash
class BasicSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
```

2.  ModelSerializer
A ModelSerializer is a shortcut for creating serializers directly tied to Django models.
It automatically generates fields based on the model.

```bash 
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']  # Fields to include in serialization

```
.
---
**Why Define Methods Inside a Django Model?**
Defining methods (like @property or other functions) inside a Django model allows us to extend the functionality of the model beyond the default behavior provided by Django. These methods can be used to compute derived values, perform custom logic, or encapsulate reusable operations related to the model

***Why It's Inside the Model:***
- The sales_price calculation is directly tied to the Product model, so keeping it in the model keeps the logic centralized and reusable.
- It ensures that all operations related to a Product instance stay together, making the code easier to read and maintain.

**What It Does:**
- This method computes the sales price as 8% of the product's price (price field).
- By using the @property decorator:
You can access the method like an attribute **(e.g., product.sales_price instead of product.sales_price()).**
- It simplifies usage and avoids cluttering your code with method calls.

```bash
from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15, decimal_places=2,default=99.99)

    @property
    def sales_price(self):
        return "%.2f" %(float(self.price)*0.08)
    
    def get_discount(self):
        return "122"
```

***Djnago serializers rely on naming conventions such as this_discount***

jaba maile discount matra haleko thiye in the custom discount field it didnt work jaba maile this_discount haleko thiey in the custom field ani maile function ko name ni change garey to get_this_discount it worked.

```bash
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
```

### Ingest Data with Django RestFramework Views
```bash 
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
```

**Raise Exception**
In Python, raise is used to trigger an exception manually. When you call raise Exception, it interrupts the normal flow of the program and raises the specified error. This can be useful for signaling that something has gone wrong and should be handled appropriately.


**When to Use raise?**
1. Validation: To enforce rules or constraints (e.g., invalid user input).
2. Custom Exceptions: To provide meaningful error messages or define specific types of errors.
3. Error Handling: To escalate issues that cannot be resolved locally.
```bash
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
```

### DRF Generics Retrieve APIVIEW
***Django’s generic views... were developed as a shortcut for common usage patterns... They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.***

**Using Generic Views**
- The generic views provided by the REST framework are a convenient way to quickly build API views that map closely to your database models. They offer a range of benefits, including:

- Simplified development: Generic views save you time and effort by providing pre-built views for common usage patterns.
Improved maintainability: By reusing existing views and mixins, you can keep your code organized and easier to maintain.

**List of Generic Api View**
1. ListAPIView: For read-only endpoints to list a queryset.
2. CreateAPIView: For create-only endpoints.
3. RetrieveAPIView: For read-only endpoints to represent a single model instance.
4. UpdateAPIView: For update-only endpoints for a single model instance.
5. DestroyAPIView: For delete-only endpoints for a single model instance.
6. ListCreateAPIView: For read-write endpoints to represent a collection of model instances.
7. RetrieveUpdateAPIView: For read or update endpoints to represent a single model instance.
8. RetrieveDestroyAPIView: For read or delete endpoints to represent a single model instance.
9. RetrieveUpdateDestroyAPIView: For read-write-delete endpoints to represent a single model instance.


1. Generics Retrieve API View
`views.py`

```bash 
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
```

`urls.py`
```bash
from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view(),name="Product details")
]

```

**so what does int:pk do what what does it mean?**
**Purpose**: the purpose of doing int:pk is to capture numeric value from the url like localhost:8000/api/products/1/ , so in here int:pk grabs the 1. `pk` which means primary key in databases . int is to specify the captured data should be integer and pk means that the pk parameter will be passed to the views

### Create API View
**what is Create API Viwe**
```bash

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
```


### Making a function with APIVIEW that handles List,create,retrive like generics
`get_object_or_404` is a shortcut to retrieve an object from the database. If the object exists, it returns the object. If the object does not exist, it raises a 404 HTTP error (not found).

***Difference beween API VIEW and Generic***
**APIView**
- APIView is a base class provided by Django Rest Framework (DRF) for creating API views. It provides a basic implementation for handling HTTP requests and responses.

**Generic Class-Based Views**
- Generic class-based views, on the other hand, are a set of pre-built views that provide common functionality for performing CRUD (create, read, update, delete) operations on models.

**Key differences:**
- Customizability: APIView is a more customizable base class, allowing you to implement your own logic for handling HTTP requests and responses. Generic class-based views are more opinionated and provide a fixed implementation for common use cases.
- Code reuse: Generic class-based views promote code reuse by providing a standard way to handle common operations like listing, retrieving, creating, updating, and deleting objects.
- Complexity: Generic class-based views are often simpler to implement, as they handle the underlying logic for you. 
However, they may not be as flexible as APIView for complex or custom use cases.
---
views.py

`many=True` Tells the serializer to handle multiple objects(a queryset)
`Product.objects.all()` fetches all Product objects from the db

> Using API VIEW

`views.py`
```bash 
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
```

`urls.py`

```bash 
from django.urls import path
from . import views
urlpatterns = [
    path('',views.product_alt_view),
    path('<int:pk>/',views.product_alt_view)
]
```

### UPDATE AND DESTROY API VIEW
`delete view`
```bash 
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
product_delete_view=ProductDeleteAPIView.as_view()
```

`update views`
```bash 
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
list_product_update_view=ProductUpdateAPIView.as_view()
```

### Mixins and Generic API View
> what is mixins from the ai content
- Mixins are a programming concept used in various languages to enhance code reusability and functionality. They are classes or objects that provide specific behaviors or methods that can be incorporated into other classes without the need for traditional inheritance.

- Mixins are a concept in object-oriented programming that allows you to add functionality to a class without using inheritance. Instead of creating a subclass, you can create a mixin class that contains methods and properties, and then "mix" it into other classes. This enables code reuse and modularity without the complexity of deep inheritance hierarchies.

> Mixins From Docs
The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as `.get()` and `.post()`, directly. This allows for more flexible composition of behavior.

The mixin classes can be imported from `rest_framework.mixins`.

- **ListModelMixin**
The ListModelMixin adds a .list() method to a view, which handles GET requests to list all objects in a queryset. It serializes the queryset and returns the serialized data in the response.
- it has pagination and filteration support.

```bash 
class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

product_mixin_view=ProductMixinView.as_view()
```

**RetirveModelMixin**
Provides a `.retrieve(request, *args, **kwargs)` method, that implements returning an existing model instance in a response.

```bash 

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
```

### Session Authentication and Permissions
***Throttling is similar to permissions, in that it determines if a request should be authorized. Throttles indicate a temporary state, and are used to control the rate of requests that clients can make to an API.***
```bash 
from rest_framework import authentication,generics,mixins,permissions

class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)

product_create_view=ProductCreateAPIView.as_view()
```

### Custom Permissions
This code defines a custom permission class called IsStaffEditorPermission that extends Django REST Framework's (DRF) DjangoModelPermissions. The purpose of this class is to enforce custom permission logic for staff users, ensuring they have specific permissions (view, delete, change, add) for the Product model.

`has_permission()` Method:
1. This method is overridden to implement custom permission logic.
2. It determines whether the user has permission to access the view.

```bash
from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        # Get the current user
        user = request.user

        # Print all permissions assigned to the user (for debugging)
        print(user.get_all_permissions())

        # Check if the user is a staff member
        if request.user.is_staff:
            # Check if the user has specific permissions for the Product model
            if user.has_perm("product.view_product"):  # Can view products
                return True
            if user.has_perm("product.delete_product"):  # Can delete products
                return True
            if user.has_perm("product.change_product"):  # Can change products
                return True
            if user.has_perm("product.add_product"):  # Can add products
                return True
            # If the user is staff but doesn't have any of the required permissions, deny access
            return False
        # If the user is not a staff member, deny access
        return False
```

> DeepSeek Improved Code
```bash 

from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user

        # Allow superusers to bypass permission checks
        if user.is_superuser:
            return True

        # Check if the user is a staff member
        if user.is_staff:
            # Get the model from the view
            model = view.queryset.model
            app_label = model._meta.app_label
            model_name = model._meta.model_name

            # Check if the user has any of the required permissions
            if user.has_perm(f"{app_label}.view_{model_name}"):  # Can view
                return True
            if user.has_perm(f"{app_label}.delete_{model_name}"):  # Can delete
                return True
            if user.has_perm(f"{app_label}.change_{model_name}"):  # Can change
                return True
            if user.has_perm(f"{app_label}.add_{model_name}"):  # Can add
                return True

            # If the user is staff but doesn't have any of the required permissions, deny access
            return False

        # If the user is not a staff member, deny access
        return False
```