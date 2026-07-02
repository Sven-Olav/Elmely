import json
from pprint import pprint

import requests


URL = (
    "https://api.energidataservice.dk/dataset/"
    "DayAheadPrices"
)


params = {
    "limit": 3
}


response = requests.get(
    URL,
    params=params,
    timeout=20,
)

print("Status:", response.status_code)
print()

print("URL:")
print(response.url)
print()

data = response.json()

print("Top-level keys:")
print(data.keys())
print()

print("First record:")
print()

pprint(data["records"][0])

print()

print("Full JSON saved to energidata_response.json")

with open(
    "energidata_response.json",
    "w",
    encoding="utf-8",
) as f:

    json.dump(
        data,
        f,
        indent=2,
        ensure_ascii=False,
    )