from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from elmely.core.logger import log
from elmely.models.price import Price
from elmely.models.total_price import TotalPrice


class TariffService:

    def __init__(self):

        self.config_path = (
            Path(__file__).resolve().parents[1]
            / "config"
            / "providers"
            / "bornholm.json"
        )

        self._config = None

    @property
    def config(self):

        if self._config is None:
            self.load()

        return self._config

    def load(self):

        log.info(
            f"Loading tariff configuration: {self.config_path.name}"
        )

        with open(
            self.config_path,
            encoding="utf-8",
        ) as file:

            self._config = json.load(file)

        log.info("Tariff configuration loaded successfully")

        return self._config

    def reload(self):

        self._config = None

        return self.load()

    #
    # Provider
    #

    def provider_name(self):

        return self.config["provider"]["name"]

    def price_area(self):

        return self.config["provider"]["price_area"]

    #
    # Satser
    #

    def vat_rate(self):

        return self.config["vat"]["rate"]

    def spot_markup(self):

        return self.config["spot"]["markup"]

    def electricity_tax(self):

        return self.config["electricity_tax"]["rate"]

    def supplier_subscription(self):

        return self.config["subscriptions"]["supplier_monthly"]

    def network_subscription(self):

        return self.config["subscriptions"]["network_monthly"]

    def energinet_subscription(self):

        return self.config["subscriptions"]["energinet_monthly"]

    #
    # Tariffvalg
    #

    def is_summer(self, timestamp: datetime) -> bool:

        month = timestamp.month

        return 4 <= month <= 9

    def tariff_period(self, timestamp: datetime) -> str:

        hour = timestamp.hour

        periods = self.config["time_periods"]

        for name, ranges in periods.items():

            for period in ranges:

                if period["from"] <= hour < period["to"]:

                    return name

        raise ValueError(
            f"No tariff period found for hour {hour}"
        )

    def network_charge(self, timestamp: datetime) -> float:

        season = (
            "summer"
            if self.is_summer(timestamp)
            else "winter"
        )

        period = self.tariff_period(timestamp)

        return self.config["network_tariffs"][season][period]

    #
    # Beregning
    #

    def calculate_total_price(
        self,
        price: Price,
    ) -> TotalPrice:

        spot = price.spot_price_dkk

        spot_markup = self.spot_markup()

        network_charge = self.network_charge(
            price.start
        )

        electricity_tax = self.electricity_tax()

        subtotal = (
            spot
            + spot_markup
            + network_charge
            + electricity_tax
        )

        vat = subtotal * self.vat_rate()

        total = subtotal + vat

        return TotalPrice(

            timestamp=price.start,

            spot=spot,

            spot_markup=spot_markup,

            network_charge=network_charge,

            electricity_tax=electricity_tax,

            vat=vat,

            total=total,

        )