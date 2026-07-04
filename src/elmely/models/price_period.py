from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class PricePeriod:
    """
    En sammenhengende periode med beregnet gjennomsnittspris.
    """

    start: datetime

    end: datetime

    hours: int

    average_price: float