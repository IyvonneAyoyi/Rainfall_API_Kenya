from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Initialize the geolocator with a user agent
geolocator = Nominatim(user_agent="locations_app")

def geocode_location(location_name):
    """
    Given a location name (string), return (latitude, longitude).
    Returns (None, None) if geocoding fails or location not found.
    """
    if not location_name:
        return None, None

    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding error: {e}")  # Consider logging in production

    return None, None
