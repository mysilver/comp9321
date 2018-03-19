import requests
response = requests.get("http://localhost:5000/statistics", params=None)
print("statistics:", response.json())
