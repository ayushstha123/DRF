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