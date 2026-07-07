from __future__ import annotations

from dataclasses import dataclass, field

from elmely.models.forecast_hour import ForecastHour


@dataclass(slots=True)
class Weather:
    """
    Samlet værinformasjon for dashboardet.
    """

    #
    # Nåværende vær
    #

    is_day: bool = True
    updated_at: datetime | None = None
    
    temperature: float = 0.0
    weather_code: int = 0

    wind_speed: float = 0.0
    wind_direction: float = 0.0

    precipitation_probability: int = 0
    uv_index: float = 0.0

    #
    # Timeprognose
    #

    forecast: list[ForecastHour] = field(default_factory=list)