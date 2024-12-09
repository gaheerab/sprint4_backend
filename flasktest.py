import requests
# an api endpoint most commonly returns JSON data
response = requests.get('http://127.0.0.1:5001/api/data')
print(response.text)