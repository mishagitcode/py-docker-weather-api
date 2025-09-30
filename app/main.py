import os
import requests
from dotenv import load_dotenv


def get_weather(city: str = "Paris") -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("No API_KEY found in .env")
        return

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    print(f"Performing request to Weather API for the city {city}...")

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    data = response.json()

    location = data.get("location", {})
    current = data.get("current", {})

    city_name = location.get("name", "Unknown")
    country = location.get("country", "Unknown")
    localtime = location.get("localtime", "Unknown")

    temp_c = current.get("temp_c", "N/A")
    condition = current.get("condition", {}).get("text", "N/A")

    print(f"{city_name}/{country} {localtime} "
          f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
