import requests

url = 'http://127.0.0.1:5000/add_usersinfo'
data = {'api_key': 'ehtisham', 'name': 'John', 'age': '30', 'gender': 'male'}

response = requests.post(url, data=data)
print(response.text)
