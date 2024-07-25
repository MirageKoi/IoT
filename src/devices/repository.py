from utils.repository import PeeWeeRepository

from .models import Device


class DeviceRepository(PeeWeeRepository):
    model = Device
