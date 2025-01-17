import requests

endpoints="https://httpbin.org/anything"

#aplication programming interface
get_response=requests.get(endpoints,json={"query":"This is Ayush Shrestha"}) #HTTP request

print(get_response.text) #print raw text response
print(get_response.json()) #print raw text response

