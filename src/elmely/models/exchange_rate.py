from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ExchangeRate:
    """
    Valutakurs mellom to valutaer.
    """

    timestamp: datetime

    from_currency: str

    to_currency: str

    rate: float