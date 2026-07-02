from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.core.http_client import HttpClient


URL = "https://httpbin.org/json"


def main():

    client = HttpClient()

    data = client.get_json(URL)

    print(data)


if __name__ == "__main__":
    main()