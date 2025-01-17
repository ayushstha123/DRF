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



