import requests 

# endpoints="https://httpbin.org/anything"
endpoints="http://127.0.0.1:8000/api/"

#aplication programming interface
# get_response=requests.get(endpoints) #HTTP request

#FOR: GET
# get_response=requests.get(endpoints,params="123",json={"query":"hello ayush ji"})

#FOR: POST
get_response=requests.post(endpoints,params="123",json={"id":4,"content":"hello ayush ji"})


# print(get_response.text) #print raw text response
# print(get_response.json()['message']) #print raw text response

# print (get_response.status_code) #to print out the status code
# get_all_response=requests.get(endpoints)
print(get_response.json()) #print raw text response
