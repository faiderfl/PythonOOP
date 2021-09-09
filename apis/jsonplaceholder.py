import requests
import json

#Get - Get object
url_api='https://jsonplaceholder.typicode.com/todos/'
response= requests.get(url_api+'1')
response_json= response.json()
print(response_json)
print(response.status_code)

#Post - Insert a new object
json_post={
    "userId": 2,
    "title": "Buy milk",
    "completed": False
}
headers =  {"Content-Type":"application/json"}
response_post= requests.post(url_api, data=json.dumps(json_post), headers=headers)
print(response_post.status_code)

#Put - Update an existing object
json_put={'userId': 1, 'id': 1,"title": "Wash car", 'completed': False}
response_put= requests.put(url_api+'1',data=json.dumps(json_put), headers=headers)
print(response_put.status_code)
print(response_put.json())


#Patch -Update existing attribute
json_patch={'userId': 1, 'id': 1,"title": "Wash car2", 'completed': False}
response_patch= requests.patch(url_api+'1',data=json.dumps(json_patch), headers=headers)
print(response_patch.status_code)
print(response_patch.json())