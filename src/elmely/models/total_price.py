from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class TotalPrice:
    """
    Resultatet av en totalprisberegning.

    Alle priser er oppgitt i DKK/kWh.
    """

    #
    # Tidsstempel
    #

    timestamp: datetime

    #
    # Prisbestanddeler
    #

    spot: float

    spot_markup: float

    network_charge: float

    electricity_tax: float

    vat: float

    #
    # Ferdig beregnet totalpris
    #

    total: float