import requests
from getpass import getpass

# Authentication endpoint
auth_endpoint = "http://localhost:8000/api/auth/"
username=input("Username: ")
password = getpass("Password: ")
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})

# Check if authentication is successful
if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    print("Token received:", token)
    
    # Authorization header
    headers = {
        "Authorization": f"Token {token}"
    }
    
    # Fetch product list
    list_create_endpoint = "http://localhost:8000/api/products/"
    response = requests.get(list_create_endpoint, headers=headers)  # Include the headers in the request
    
    if response.status_code == 200:
        print(response.json())
    else:
        print("Failed to fetch products:", response.status_code, response.json())
else:
    print("Authentication failed:", auth_response.status_code, auth_response.json())
