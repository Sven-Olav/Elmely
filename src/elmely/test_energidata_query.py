import requests
from pprint import pprint

url = "https://api.energidataservice.dk/dataset/DayAheadPrices"

params = {
    "start": "now-P1D",
    "end": "now+P2D",
    "filter": '{"PriceArea":["DK2"]}',
    "sort": "TimeDK desc",
    "limit": 10,
}

r = requests.get(url, params=params, timeout=20)

print("Status:", r.status_code)
print("URL:")
print(r.url)
print()

data = r.json()

print("Antall records:", len(data.get("records", [])))
print()

for rec in data.get("records", []):
    pprint(rec)
    print("-" * 60)