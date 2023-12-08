# Example api request 
import requests
import json

# The API endpoint
url = "api.url"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()



print(response_json)

