import requests

create_endpoint="http://localhost:8000/api/products/"

data={
    "title":"This field is done",
    "price":32.99,
    "content":"this is content"
}
get_create_response=requests.post(create_endpoint,json=data)
print(get_create_response.json())