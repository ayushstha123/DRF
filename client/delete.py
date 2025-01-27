import requests

endpoint="http://localhost:8000/api/products/4/delete/"

delete_response=requests.delete(endpoint)
print(delete_response)