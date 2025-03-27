# подключаем библиотеку для работы с запросами
import requests


def _get_weather_data(city: str) -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather"
    # формируем запрос
    params = {
        "q": city,
        "units": "metric",
        "lang": "ru",
        "appid": "79d1ca96933b0328e1c7e3e7a26cb347",
    }
    # отправляем запрос на сервер
    response = requests.get(url, params=params)
    # возвращаем в виде json
    return response.json()


def get_openweathermap_temp(city: str) -> str:
    weather_data = _get_weather_data(city)
    return round(weather_data["main"]["temp"])


def get_openweathermap_temp_feelds(city: str) -> str:
    # Получаем общие данные
    weather_data = _get_weather_data(city)
    # получаем данные о температуре и том, как она ощущается
    return round(weather_data["main"]["feels_like"])


if __name__ == "__main__":
    CITY = "Сочи"
    print("Сейчас в городе", CITY, get_openweathermap_temp(CITY), "°C")
    print("Ощущается как", CITY, get_openweathermap_temp_feelds(CITY), "°C")
