import requests
from datetime import date

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def get_daily_rainfall(latitude, longitude):
    """
    Fetch today's rainfall (mm) for given coordinates from Open-Meteo API.
    """
    if latitude is None or longitude is None:
        return None

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_sum",
        "timezone": "Africa/Nairobi"
    }

    try:
        response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        daily = data.get("daily", {})
        dates = daily.get("time", [])
        rainfall = daily.get("precipitation_sum", [])

        today = str(date.today())

        if today in dates:
            return rainfall[dates.index(today)]

        return None

    except requests.RequestException:
        return None
