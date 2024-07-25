from .api import LocationAPI
from .repository import LocationRepository
from .service import LocationService


def init_location_api() -> LocationAPI:
    return LocationAPI(LocationService(LocationRepository()))
