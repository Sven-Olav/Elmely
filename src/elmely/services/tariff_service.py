from __future__ import annotations

import json
from pathlib import Path

from elmely.core.logger import log
from elmely.models.price import Price
from elmely.models.total_price import TotalPrice


class TariffService:

    def __init__(self):

        self.config_path = (
            Path(__file__)
            .resolve()
            .parents[1]
            / "config"
            / "providers"
            / "bornholm.json"
        )

        self._config = None

    @property
    def config(self) -> dict:

        if self._config is None:
            self.load()

        return self._config

    def load(self) -> dict:
        """
        Leser tariff-konfigurasjonen.
        """

        log.info(
            f"Loading tariff configuration: {self.config_path.name}"
        )

        with open(
            self.config_path,
            encoding="utf-8",
        ) as file:

            self._config = json.load(file)

        log.info(
            "Tariff configuration loaded successfully"
        )

        return self._config

    def reload(self):

        self._config = None

        return self.load()

    #
    # Provider
    #

    def provider_name(self) -> str:

        return self.config["provider"]["name"]

    def price_area(self) -> str:

        return self.config["provider"]["price_area"]

    #
    # Satser
    #

    def vat_rate(self) -> float:

        return self.config["vat"]["rate"]

    def spot_markup(self) -> float:

        return self.config["spot"]["markup"]

    def supplier_subscription(self) -> float:

        return self.config["subscriptions"]["supplier_monthly"]

    def energinet_subscription(self) -> float:

        return self.config["subscriptions"]["energinet_monthly"]

    #
    # Beregning
    #

    def calculate_total_price(
        self,
        price: Price,
    ) -> TotalPrice:
        """
        Beregner total strømpris.

        Foreløpig:
        - Spotpris
        - Spottillegg
        - Nettkostnad (0,0)
        - Elavgift (0,0)
        - MVA
        """

        spot = price.spot_price_dkk

        spot_markup = self.spot_markup()

        network_charge = 0.0

        electricity_tax = 0.0

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