from __future__ import annotations

from datetime import date, datetime

from elmely.core.http_client import HttpClient
from elmely.core.logger import log
from elmely.models.exchange_rate import ExchangeRate


class ExchangeRateService:

    BASE_URL = "https://api.frankfurter.app/latest"

    def __init__(self):

        self.http = HttpClient()

        self._cached_rate: ExchangeRate | None = None

    def get_rate(
        self,
        from_currency: str = "DKK",
        to_currency: str = "NOK",
    ) -> ExchangeRate:

        #
        # Bruk cache dersom dagens kurs allerede er hentet
        #

        if (
            self._cached_rate is not None
            and self._cached_rate.timestamp.date() == date.today()
            and self._cached_rate.from_currency == from_currency
            and self._cached_rate.to_currency == to_currency
        ):

            log.info(
                f"Using cached exchange rate "
                f"{from_currency}->{to_currency}"
            )

            return self._cached_rate

        log.info(
            f"Requesting exchange rate "
            f"{from_currency}->{to_currency}"
        )

        data = self.http.get_json(

            self.BASE_URL,

            params={

                "from": from_currency,

                "to": to_currency,

            },

        )

        exchange_rate = ExchangeRate(

            timestamp=datetime.now(),

            from_currency=from_currency,

            to_currency=to_currency,

            rate=float(
                data["rates"][to_currency]
            ),

        )

        self._cached_rate = exchange_rate

        log.info(

            f"Exchange rate: "

            f"1 {from_currency} = "

            f"{exchange_rate.rate:.4f} {to_currency}"

        )

        return exchange_rate

    def refresh(

        self,

        from_currency: str = "DKK",

        to_currency: str = "NOK",

    ) -> ExchangeRate:

        self._cached_rate = None

        return self.get_rate(

            from_currency,

            to_currency,

        )
    
    def convert(
        self,
        amount: float,
        from_currency: str = "DKK",
        to_currency: str = "NOK",
    ) -> float:

        rate = self.get_rate(
            from_currency,
            to_currency,
        )

        return amount * rate.rate