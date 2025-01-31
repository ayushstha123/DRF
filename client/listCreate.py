import requests
from getpass import getpass #secure password 

# list_create_endpoint="http://localhost:8000/api/products/"
# response=requests.get(list_create_endpoint)
# print(response.json()) 

auth_endpoint="http://localhost:8000/api/auth/"
password=getpass()
auth_response=requests.post(auth_endpoint,json={'username':'ayush','password':password})

print(auth_response.json()) 

#when the user has a token 
if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        "Authorization":f"Token {token}"
    }
    list_create_endpoint="http://localhost:8000/api/products/"
    response=requests.get(list_create_endpoint)
    print(response.json())