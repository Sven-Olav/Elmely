from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ForecastHour:
    """
    Værprognose for én time.
    """

    #
    # Tid
    #

    timestamp: datetime

    #
    # Vær
    #

    temperature: float = 0.0
    weather_code: int = 0

    wind_speed: float = 0.0
    wind_direction: float = 0.0

    precipitation_probability: int = 0
    uv_index: float = 0.0