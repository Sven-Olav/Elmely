from __future__ import annotations


#
# Open-Meteo weather codes:
# https://open-meteo.com/en/docs
#


def get_weather_icon(
    weather_code: int,
    is_day: bool = True,
) -> str:

    #
    # Clear sky
    #

    if weather_code == 0:

        return "☀" if is_day else "🌙"

    #
    # Mainly clear
    #

    if weather_code == 1:

        return "🌤" if is_day else "🌙"

    #
    # Partly cloudy
    #

    if weather_code == 2:

        return "⛅"

    #
    # Overcast
    #

    if weather_code == 3:

        return "☁"

    #
    # Fog
    #

    if weather_code in (45, 48):

        return "🌫"

    #
    # Drizzle
    #

    if weather_code in (51, 53, 55):

        return "🌦"

    #
    # Freezing drizzle
    #

    if weather_code in (56, 57):

        return "🌧"

    #
    # Rain
    #

    if weather_code in (61, 63, 65):

        return "🌧"

    #
    # Freezing rain
    #

    if weather_code in (66, 67):

        return "🌧"

    #
    # Snow
    #

    if weather_code in (71, 73, 75, 77):

        return "❄"

    #
    # Rain showers
    #

    if weather_code in (80, 81, 82):

        return "🌦"

    #
    # Snow showers
    #

    if weather_code in (85, 86):

        return "❄"

    #
    # Thunderstorm
    #

    if weather_code in (95, 96, 99):

        return "⛈"

    #
    # Unknown
    #

    return "❔"