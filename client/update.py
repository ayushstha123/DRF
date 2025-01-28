import requests

endpoint="http://localhost:8000/api/products/1/update/"

data={
    "title":"New IPHONE 16",
    "price":"23000",
}
update_response=requests.put(endpoint,json=data)
print(update_response.json())