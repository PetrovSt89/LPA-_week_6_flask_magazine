import requests

from typing import NamedTuple

from webapp.config import api_key, city


def parse_from_openweather(city:str) -> dict|bool:
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city,
              "units": "metric",
              "appid": api_key}
    try:
        result = requests.get(url=weather_url, params=params).json()
        try:
            return result
        except TypeError:
            return False
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def parse_temp(weather_data:dict) -> tuple[float,float]|bool:
    if 'main' in weather_data and 'temp' in weather_data['main']:
        temp = weather_data['main']['temp']
        if 'feels_like' in weather_data['main']:
            feels_like = weather_data['main']['feels_like']
        return temp, feels_like
    return False


weather = parse_from_openweather(city)
if weather:
    temp, feels_like = parse_temp(weather_data=weather)


class Weather(NamedTuple):
    city: str
    temp: float
    feels_like: float


weather_class = Weather(city=city, temp=temp, feels_like=feels_like)


if __name__ == "__main__":
    # temp, feels_like = parse_temp(weather_data=parse_from_openweather(city))
    print(weather_class)