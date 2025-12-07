import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_rainfall(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "rain",
        "daily": ["rain_sum", "precipitation_hours"],
        "timezone": "auto",
    }

    try:
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "hourly_rain": data.get("hourly", {}).get("rain", []),
            "daily_rain_sum": data.get("daily", {}).get("rain_sum", []),
            "precipitation_hours": data.get("daily", {}).get("precipitation_hours", [])
        }
    except Exception as e:
        return {"error": str(e)}
