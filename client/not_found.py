import requests
endpoint="http://localhost:8000/api/products/123123/"

get_not_found_response=requests.get(endpoint)

print(get_not_found_response.json())