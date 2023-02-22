import requests

# Your API key
api_key = "API_KEY_HERE"

# The endpoint for the weather forecast API
url = f"http://api.openweathermap.org/data/2.5/forecast?q=London&appid={api_key}"

# Send a GET request to the API
response = requests.get(url)

# If the request was successful, print the JSON data returned by the API
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
