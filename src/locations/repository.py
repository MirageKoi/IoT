from utils.repository import PeeWeeRepository

from .models import Location


class LocationRepository(PeeWeeRepository):
    model = Location
