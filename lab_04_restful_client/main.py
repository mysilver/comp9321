import requests

john = {
    "name": "John",
    "grade": 95
}

result = requests.post("http://localhost:5000/student", json=john, headers={"Content-Type": "application/json"})
if not result.ok:
    print("status code", result.status_code)
    print(result.json())
    quit()
else:
    print(result.json())

susan = {
    "name": "Susan",
    "grade": 100
}

result = requests.post("http://localhost:5000/student", json=susan)
if not result.ok:
    print("status code", result.status_code)
    print(result.json())
    quit()
else:
    print(result.json())

result = requests.get("http://localhost:5000/statistics", params=None)
print("statistics : ", result.json())
