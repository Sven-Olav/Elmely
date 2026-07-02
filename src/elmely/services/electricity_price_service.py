import json
from datetime import datetime
from pathlib import Path

from elmely.models.price import Price


class ElectricityPriceService:

    def __init__(self):

        self.data_file = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "sample_data"
            / "nordpool_today.json"
        )

    def get_today_prices(self) -> list[Price]:

        with open(self.data_file, encoding="utf-8") as file:

            raw = json.load(file)

        prices = []

        for item in raw:

            prices.append(

                Price(

                    start=datetime.fromisoformat(item["start"]),

                    end=datetime.fromisoformat(item["end"]),

                    spot_price_dkk=item["spot_price_dkk"]

                )

            )

        return prices