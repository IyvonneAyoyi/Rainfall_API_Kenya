from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

# Proper descriptive user agent - for Nominatim usage policy
geolocator = Nominatim(user_agent="rainfall_api_kenya_v1", timeout=10)

def geocode_location(location_name, retries=1):
    """
    Given a location name (string), return (latitude, longitude).
    Retries once on timeout.
    Returns (None, None) if geocoding fails.
    """

    if not location_name:
        return None, None

    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude

    except GeocoderTimedOut:
        if retries > 0:
            time.sleep(2)   # wait 2 seconds then retry
            return geocode_location(location_name, retries=retries - 1)
        else:
            print("Geocoding failed after retry due to timeout.")

    except GeocoderServiceError as e:
        print(f"Geocoding service error: {e}")

    return None, None
