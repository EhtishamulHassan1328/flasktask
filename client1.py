import requests

# URL of the Flask application endpoint for getting user information
url = 'http://127.0.0.1:5000/getusersinfo'

# Data to be sent in the POST request
data = {'api_key': 'ehtisham', 'session_id': 'c76652c6-9caa-45d7-86c6-e5b5d1172911'}

# Make a POST request to the Flask application
response = requests.post(url, data=data)

# Print the response text
print(response.text)
