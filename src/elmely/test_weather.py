from elmely.services.weather_service import WeatherService

service = WeatherService()

weather = service.get_weather()

print(weather)
print(weather.temperature)
print(weather.weather_code)
print(weather.is_day)
print(len(weather.forecast))