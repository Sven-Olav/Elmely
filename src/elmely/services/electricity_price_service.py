from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime, timedelta

from elmely.core.http_client import HttpClient
from elmely.core.logger import log
from elmely.models.price import Price


class ElectricityPriceService:

    API_URL = (
        "https://api.energidataservice.dk/dataset/"
        "DayAheadPrices"
    )

    def __init__(self):

        self.client = HttpClient()

        self._cached_prices: list[Price] | None = None

    def _get_live_prices(
        self,
        price_area: str = "DK2",
    ) -> list[Price]:

        #
        # Bruk cache hvis vi allerede har hentet data
        #

        if self._cached_prices is not None:

            log.info(
                f"Using cached prices ({len(self._cached_prices)})"
            )

            return self._cached_prices

        log.info(
            f"Requesting live prices for {price_area}"
        )

        data = self.client.get_json(

            self.API_URL,

            params={
                "start": "now-P1D",
                "end": "now+P2D",
                "filter": f'{{"PriceArea":["{price_area}"]}}',
                "sort": "TimeDK",
            },

        )

        records = data.get("records", [])

        log.info(
            f"Received {len(records)} quarter-hour prices"
        )

        hourly_groups = defaultdict(list)

        for record in records:

            try:

                timestamp = datetime.fromisoformat(
                    record["TimeDK"]
                )

                hour = timestamp.replace(
                    minute=0,
                    second=0,
                    microsecond=0,
                )

                price = (
                    float(record["DayAheadPriceDKK"])
                    / 1000.0
                )

                hourly_groups[hour].append(price)

            except Exception as ex:

                log.warning(
                    f"Skipping record: {ex}"
                )

        prices: list[Price] = []

        for hour in sorted(hourly_groups.keys()):

            values = hourly_groups[hour]

            if not values:
                continue

            average = sum(values) / len(values)

            prices.append(

                Price(

                    start=hour,

                    end=hour + timedelta(hours=1),

                    spot_price_dkk=average,

                )

            )

        log.info(
            f"Created {len(prices)} hourly prices"
        )

        #
        # Lagre i cache
        #

        self._cached_prices = prices

        return prices

    def refresh(self):

        """
        Tøm cache slik at neste kall henter nye data.
        """

        self._cached_prices = None

    def get_all_prices(self) -> list[Price]:

        return self._get_live_prices()

    def get_today_prices(self) -> list[Price]:

        today = date.today()

        return [

            price

            for price in self._get_live_prices()

            if price.start.date() == today

        ]

    def get_tomorrow_prices(self) -> list[Price]:

        tomorrow = date.today() + timedelta(days=1)

        return [

            price

            for price in self._get_live_prices()

            if price.start.date() == tomorrow

        ]