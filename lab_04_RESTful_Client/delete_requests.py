import requests

john = {
    "name": "John",
    "grade": 95
}
URL = 'http://localhost:5000/students/' + john["name"]
result = requests.delete(URL, headers={"Content-Type": "application/json"})
if not result.ok:
    print("status code", result.status_code)
    print(result.text)
    quit()
else:
    print(result.text)
