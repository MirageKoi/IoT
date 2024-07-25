from .api import DeviceAPI
from .repository import DeviceRepository
from .service import DeviceService


def init_device_api():
    return DeviceAPI(DeviceService(DeviceRepository()))
