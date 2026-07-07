from __future__ import annotations

from datetime import datetime

from elmely.config.location import (
    DEFAULT_LATITUDE,
    DEFAULT_LONGITUDE,
)
from elmely.core.http_client import HttpClient
from elmely.core.logger import log
from elmely.models.forecast_hour import ForecastHour
from elmely.models.weather import Weather


class WeatherService:
    """
    Henter værdata fra Open-Meteo.

    Resultatet caches frem til refresh() kalles.
    """

    API_URL = "https://api.open-meteo.com/v1/forecast"

    @staticmethod
    def _kmh_to_ms(speed: float) -> float:
        """
        Konverterer km/t til m/s.
        """

        return round(speed / 3.6, 1)

    def __init__(self):

        self.client = HttpClient()

        self._cached_weather: Weather | None = None

    def refresh(self):
        """
        Tøm cache slik at neste kall henter nye data.
        """

        self._cached_weather = None

    def get_weather(self) -> Weather:
        """
        Returnerer gjeldende vær og de neste 12 timene.
        """

        if self._cached_weather is not None:

            log.info("Using cached weather")

            return self._cached_weather

        log.info("Requesting weather from Open-Meteo")

        data = self.client.get_json(

            self.API_URL,

            params={

                "latitude": DEFAULT_LATITUDE,
                "longitude": DEFAULT_LONGITUDE,

                "current": ",".join(
                    (
                        "temperature_2m",
                        "weather_code",
                        "is_day",
                        "wind_speed_10m",
                        "wind_direction_10m",
                    )
                ),

                "hourly": ",".join(
                    (
                        "temperature_2m",
                        "weather_code",
                        "precipitation_probability",
                        "uv_index",
                        "wind_speed_10m",
                        "wind_direction_10m",
                    )
                ),

                "timezone": "auto",

            },

        )

        weather = Weather()

        weather.updated_at = datetime.now()

        current = data.get("current", {})

        weather.temperature = float(
            current.get(
                "temperature_2m",
                0.0,
            )
        )

        weather.weather_code = int(
            current.get(
                "weather_code",
                0,
            )
        )

        weather.is_day = bool(
            current.get(
                "is_day",
                1,
            )
        )

        weather.wind_speed = self._kmh_to_ms(
            float(
                current.get(
                    "wind_speed_10m",
                    0.0,
                )
            )
        )

        weather.wind_direction = float(
            current.get(
                "wind_direction_10m",
                0.0,
            )
        )

        hourly = data.get("hourly", {})

        times = hourly.get("time", [])

        temperatures = hourly.get(
            "temperature_2m",
            [],
        )

        weather_codes = hourly.get(
            "weather_code",
            [],
        )

        precipitation = hourly.get(
            "precipitation_probability",
            [],
        )

        uv_index = hourly.get(
            "uv_index",
            [],
        )

        wind_speed = hourly.get(
            "wind_speed_10m",
            [],
        )

        wind_direction = hourly.get(
            "wind_direction_10m",
            [],
        )

        now = weather.updated_at.replace(
            minute=0,
            second=0,
            microsecond=0,
        )
        current_hour = now.strftime(
            "%Y-%m-%dT%H:00"
        )

        started = False

        for index, timestamp in enumerate(times):

            #
            # Open-Meteo kan returnere tid både med og uten
            # tidssone. Vi sammenligner derfor kun dato og time.
            #

            forecast_hour = timestamp[:13] + ":00"

            if not started:

                if forecast_hour != current_hour:

                    continue

                started = True

            forecast = ForecastHour(

                timestamp=datetime.fromisoformat(
                    timestamp
                ),

                temperature=float(

                    temperatures[index]

                    if index < len(temperatures)

                    else 0.0

                ),

                weather_code=int(

                    weather_codes[index]

                    if index < len(weather_codes)

                    else 0

                ),

                precipitation_probability=int(

                    precipitation[index]

                    if index < len(precipitation)

                    else 0

                ),

                uv_index=float(

                    uv_index[index]

                    if index < len(uv_index)

                    else 0.0

                ),

                wind_speed=self._kmh_to_ms(

                    float(

                        wind_speed[index]

                        if index < len(wind_speed)

                        else 0.0

                    )

                ),

                wind_direction=float(

                    wind_direction[index]

                    if index < len(wind_direction)

                    else 0.0

                ),

            )

            weather.forecast.append(forecast)

            if len(weather.forecast) >= 12:

                break

        log.info(
            f"Created {len(weather.forecast)} forecast hours"
        )

        #
        # Bruk første prognosetime som kilde til UV-indeks og
        # nedbørssannsynlighet dersom den gjelder inneværende time.
        #

        if weather.forecast:

            first = weather.forecast[0]

            if first.timestamp.strftime(
                "%Y-%m-%dT%H:00"
            ) == current_hour:

                weather.precipitation_probability = (
                    first.precipitation_probability
                )

                weather.uv_index = first.uv_index

        self._cached_weather = weather

        log.info(

            "Weather updated: "

            f"{weather.temperature:.1f}°C, "

            f"{len(weather.forecast)} forecast hours"

        )

        return weather

        #
        # Dersom første prognosetime gjelder inneværende time,
        # bruker vi UV-indeks og nedbørssannsynlighet derfra.
        #

        if weather.forecast:

            first = weather.forecast[0]

            if first.timestamp.strftime(
                "%Y-%m-%dT%H:00"
            ) == current_hour:

                weather.precipitation_probability = (
                    first.precipitation_probability
                )

                weather.uv_index = first.uv_index

        log.info(

            f"Created weather object "
            f"({len(weather.forecast)} forecast hours)"

        )

        self._cached_weather = weather

        return weather