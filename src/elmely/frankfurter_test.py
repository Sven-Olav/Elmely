import requests

print("Start")

r = requests.get(
    "https://api.frankfurter.app/latest",
    timeout=15,
)

print(r.status_code)

print(r.text)