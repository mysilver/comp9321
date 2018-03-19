import requests

john = {
    "name": "John",
    "grade": 95
}

result = requests.post("http://localhost:5000/students", json=john, headers={"Content-Type": "application/json"})
if not result.ok:
    print("status code", result.status_code)
    print(result.text)
    quit()
else:
    print(result.text)

susan = {
    "name": "Susan",
    "grade": 100
}

result = requests.post("http://localhost:5000/students", json=susan)
if not result.ok:
    print("status code", result.status_code)
    print(result.text)
    quit()
else:
    print(result.text)

result = requests.get("http://localhost:5000/statistics", params=None)
print("statistics : ", result.json())
