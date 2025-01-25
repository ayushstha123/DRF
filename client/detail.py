import requests

endpoint="http://localhost:8000/api/products/1/"

get_requests=requests.get(endpoint)
print(get_requests.json())