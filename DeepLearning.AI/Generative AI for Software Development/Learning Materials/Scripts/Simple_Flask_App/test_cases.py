import requests

base_url = "http://127.0.0.1:8000"

test_cases = [
    ("GET normal name", "GET", "/api/greet/Ali"),
    ("GET another name", "GET", "/api/greet/John"),
    ("GET with number", "GET", "/api/greet/123"),
    ("GET missing name", "GET", "/api/greet/"),
]

for description, method, path in test_cases:
    url = base_url + path
    if method == "GET":
        response = requests.get(url)
    else:
        response = requests.request(method, url)

    print(description)
    print("Status:", response.status_code)
    print("Body:", response.text)
    print("-" * 40)

# Wrong method example
response = requests.post(base_url + "/api/greet/Ali")
print("POST wrong method")
print("Status:", response.status_code)
print("Body:", response.text)