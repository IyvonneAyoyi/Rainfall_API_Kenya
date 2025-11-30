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
        location = geolocator.geocode(location_name, exactly_one=True)
        if location:
            return location.latitude, location.longitude

    except GeocoderTimedOut:
        if retries > 0:
            time.sleep(2)
            return geocode_location(location_name, retries=retries - 1)

    except GeocoderServiceError as e:
        print(f"Geocoding service error: {e}")

    return None, None


def reverse_geocode_location(latitude, longitude, retries=1):
    """
    Given coordinates, return a human-readable location name.
    Retries once on timeout.
    Returns None if reverse geocoding fails.
    """
    if latitude is None or longitude is None:
        return None

    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location:
            return location.address

    except GeocoderTimedOut:
        if retries > 0:
            time.sleep(2)
            return reverse_geocode_location(latitude, longitude, retries=retries - 1)

    except GeocoderServiceError as e:
        print(f"Reverse geocoding error: {e}")

    return None
