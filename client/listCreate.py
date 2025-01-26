import requests

list_create_endpoint="http://localhost:8000/api/products/"

response=requests.get(list_create_endpoint)
print(response.json())